#!/usr/bin/env python3
"""Generate structured, versioned NKP markdown docs from NKP help output."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class CommandNode:
    tokens: tuple[str, ...]
    content: str = ""
    children: list["CommandNode"] = field(default_factory=list)
    parent: "CommandNode | None" = None
    has_page: bool = False

    @property
    def depth(self) -> int:
        return len(self.tokens) - 1

    @property
    def command(self) -> str:
        return " ".join(self.tokens)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-dir",
        default="",
        help="Optional flat markdown input directory. If omitted, reads live nkp help.",
    )
    parser.add_argument("--output-root", default=".")
    parser.add_argument("--version", default="")
    return parser.parse_args()


def detect_version() -> str:
    try:
        proc = subprocess.run(
            ["nkp", "version"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return "unknown"

    if proc.returncode != 0:
        return "unknown"

    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("nkp:"):
            _, _, value = line.partition(":")
            return value.strip() or "unknown"
    return "unknown"


def render_help(cmd_tokens: tuple[str, ...]) -> str:
    proc = subprocess.run(
        [*cmd_tokens, "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    command = " ".join(cmd_tokens)
    return f"# `{command}`\n\n```text\n{output.rstrip()}\n```\n"


def extract_subcommands(help_text: str) -> list[str]:
    in_section = False
    subcommands: list[str] = []
    for line in help_text.splitlines():
        stripped = line.strip()
        if stripped == "Available Commands:":
            in_section = True
            continue
        if in_section and (
            stripped.startswith("Flags:")
            or stripped.startswith("Global Flags:")
            or stripped.startswith("Inherited Flags:")
            or stripped.startswith("Use ")
        ):
            in_section = False
            continue
        if not in_section:
            continue

        match = re.match(r"^\s{2,}([a-zA-Z0-9_-]+)\s{2,}", line)
        if match:
            subcommands.append(match.group(1))
    return subcommands


def collect_live_docs() -> dict[tuple[str, ...], str]:
    docs: dict[tuple[str, ...], str] = {}
    visited: set[tuple[str, ...]] = set()

    def walk(tokens: tuple[str, ...]) -> None:
        if tokens in visited:
            return
        visited.add(tokens)

        md = render_help(tokens)
        docs[tokens] = md

        help_text = body_without_title(md)
        for sub in extract_subcommands(help_text):
            walk((*tokens, sub))

    walk(("nkp",))
    return docs


def load_flat_docs(input_dir: Path) -> dict[tuple[str, ...], str]:
    docs: dict[tuple[str, ...], str] = {}
    for path in sorted(input_dir.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        first_line = text.splitlines()[0] if text.strip() else ""
        match = re.match(r"# `(.+)`$", first_line.strip())
        if not match:
            continue
        docs[tuple(match.group(1).split())] = text
    return docs


def build_tree(docs: dict[tuple[str, ...], str]) -> CommandNode:
    nodes: dict[tuple[str, ...], CommandNode] = {}

    for tokens in docs:
        for i in range(1, len(tokens) + 1):
            key = tokens[:i]
            if key not in nodes:
                nodes[key] = CommandNode(tokens=key)

    for tokens, content in docs.items():
        nodes[tokens].content = content

    for tokens, node in nodes.items():
        if len(tokens) == 1:
            continue
        parent_tokens = tokens[:-1]
        parent = nodes[parent_tokens]
        node.parent = parent
        parent.children.append(node)

    for node in nodes.values():
        node.children.sort(key=lambda n: n.tokens[-1])

    return nodes[("nkp",)]


def should_have_page(node: CommandNode) -> bool:
    # Root + top level + second level always get standalone pages.
    if node.depth <= 2:
        return True

    # For deeper levels, only split when the command itself fans out
    # and has siblings under the same parent.
    sibling_count = len(node.parent.children) if node.parent else 0
    return sibling_count > 1 and len(node.children) >= 3


def assign_page_flags(node: CommandNode) -> None:
    node.has_page = should_have_page(node)
    for child in node.children:
        assign_page_flags(child)


def page_path(version_dir: Path, node: CommandNode) -> Path:
    filename = f"{'-'.join(node.tokens)}.md"
    if node.depth == 0:
        return version_dir / filename
    rel = Path("commands")
    for token in node.tokens[1:]:
        rel = rel / token
    return version_dir / rel / filename


def body_without_title(content: str) -> str:
    lines = content.splitlines()
    if not lines:
        return ""
    if lines[0].startswith("# `"):
        lines = lines[1:]
    while lines and lines[0].strip() == "":
        lines = lines[1:]
    return "\n".join(lines).rstrip() + "\n"


def find_page_ancestor(node: CommandNode) -> CommandNode:
    cursor = node
    while cursor is not None and not cursor.has_page:
        cursor = cursor.parent
    if cursor is None:
        raise RuntimeError("No page-bearing ancestor found.")
    return cursor


def gather_embeds(root: CommandNode) -> dict[tuple[str, ...], list[CommandNode]]:
    embeds: dict[tuple[str, ...], list[CommandNode]] = defaultdict(list)

    def walk(node: CommandNode) -> None:
        if not node.has_page:
            target = find_page_ancestor(node.parent if node.parent else node)
            embeds[target.tokens].append(node)
        for child in node.children:
            walk(child)

    walk(root)
    for lst in embeds.values():
        lst.sort(key=lambda n: n.command)
    return embeds


def relative_md_link(from_page: Path, to_page: Path) -> str:
    return os.path.relpath(to_page, start=from_page.parent).replace("\\", "/")


def render_page(
    node: CommandNode,
    version_dir: Path,
    page_nodes: list[CommandNode],
    embeds: dict[tuple[str, ...], list[CommandNode]],
) -> str:
    current = page_path(version_dir, node)
    lines: list[str] = [f"# `{node.command}`", ""]
    if node.content:
        lines.append(body_without_title(node.content).rstrip())
        lines.append("")

    child_pages = [c for c in node.children if c.has_page]
    if child_pages:
        lines.append("## Subcommands")
        lines.append("")
        for child in child_pages:
            target = page_path(version_dir, child)
            link = relative_md_link(current, target)
            lines.append(f"- [`{child.command}`]({link})")
        lines.append("")

    embedded = embeds.get(node.tokens, [])
    if embedded:
        lines.append("## Subcommands")
        lines.append("")
        for inlined in embedded:
            if not inlined.content:
                continue
            lines.append(f"### `{inlined.command}`")
            lines.append("")
            lines.append(body_without_title(inlined.content).rstrip())
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_pages(root: CommandNode, version_dir: Path) -> None:
    all_nodes: list[CommandNode] = []

    def walk(node: CommandNode) -> None:
        all_nodes.append(node)
        for child in node.children:
            walk(child)

    walk(root)
    page_nodes = [n for n in all_nodes if n.has_page]
    embeds = gather_embeds(root)

    for node in page_nodes:
        path = page_path(version_dir, node)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            render_page(node, version_dir, page_nodes, embeds),
            encoding="utf-8",
        )


def write_root_index(output_root: Path) -> None:
    versions = sorted(
        [
            p.name
            for p in output_root.iterdir()
            if p.is_dir() and re.match(r"^v?\d+\.\d+\.\d+$", p.name)
        ]
    )
    lines = [
        "# NKP CLI Reference",
        "",
        "Structured, versioned command reference generated from NKP help output.",
        "",
        "## Versions",
        "",
    ]
    for version in versions:
        lines.append(f"- [`{version}`]({version}/nkp.md)")
    lines.append("")
    (output_root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    output_root = Path(args.output_root)
    version = args.version or detect_version()

    if args.input_dir:
        docs = load_flat_docs(Path(args.input_dir))
    else:
        docs = collect_live_docs()

    if ("nkp",) not in docs:
        raise RuntimeError("Could not find root `nkp` command documentation.")

    root = build_tree(docs)
    assign_page_flags(root)

    version_dir = output_root / version
    if version_dir.exists():
        shutil.rmtree(version_dir)
    version_dir.mkdir(parents=True, exist_ok=True)

    write_pages(root, version_dir)
    write_root_index(output_root)

    print(f"Generated structured docs in: {version_dir}")


if __name__ == "__main__":
    main()
