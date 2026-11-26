#!/usr/bin/env python3
"""Generate structured, versioned NKP markdown docs from NKP help output."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
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


class VersionError(RuntimeError):
    """Raised when the NKP version cannot be resolved safely."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-dir",
        default="",
        help="Optional flat markdown input directory. If omitted, reads live nkp help.",
    )
    parser.add_argument("--output-root", default=".")
    parser.add_argument(
        "--version",
        default="",
        help=(
            "Version folder name. Must match live `nkp version` unless used with "
            "--input-dir and --allow-version-mismatch."
        ),
    )
    parser.add_argument(
        "--allow-version-mismatch",
        action="store_true",
        help=(
            "Allow --version to differ from live `nkp version` when regenerating "
            "from --input-dir (offline / recorded help dumps)."
        ),
    )
    parser.add_argument(
        "--print-version",
        action="store_true",
        help="Print the detected live nkp version and exit (shared with the shell wrapper).",
    )
    return parser.parse_args()


def parse_version_output(text: str) -> str | None:
    """Extract the nkp version string from `nkp version` stdout.

    Accepts lines such as ``nkp: v2.17.1`` or ``nkp:v2.17.1`` (optional spaces
    around the colon). Returns None when no usable version line is present.
    """
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("nkp:"):
            continue
        _, _, value = line.partition(":")
        value = value.strip()
        if value:
            return value
    return None


def detect_version() -> str:
    """Return the installed nkp version string.

    Raises VersionError instead of returning ``unknown``, so callers never create
    an ``unknown/`` output directory by accident.
    """
    try:
        proc = subprocess.run(
            ["nkp", "version"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as exc:
        raise VersionError("nkp is not installed or not on PATH") from exc

    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        suffix = f": {detail}" if detail else ""
        raise VersionError(
            f"`nkp version` failed with exit code {proc.returncode}{suffix}"
        )

    parsed = parse_version_output(proc.stdout or "")
    if parsed is None:
        raise VersionError(
            "could not parse version from `nkp version` output "
            "(expected a line like 'nkp: vX.Y.Z')"
        )
    return parsed


def resolve_version(
    requested: str,
    *,
    input_dir: str = "",
    allow_mismatch: bool = False,
    detected: str | None = None,
    detect_error: VersionError | None = None,
) -> str:
    """Choose the version folder name, refusing unsafe mismatches / unknown.

    Live crawls must use the detected binary version. ``--version`` may only
    differ when regenerating from ``--input-dir`` with ``--allow-version-mismatch``.
    """
    offline = bool(input_dir)

    if detected is None and detect_error is None:
        try:
            detected = detect_version()
        except VersionError as exc:
            detect_error = exc

    if detected is None:
        if offline and requested:
            # No live binary to compare against; use the explicit folder name.
            return requested
        if detect_error is not None:
            raise detect_error
        raise VersionError("could not detect nkp version")

    if not requested:
        return detected

    if requested == detected:
        return requested

    if allow_mismatch and offline:
        return requested

    if allow_mismatch and not offline:
        raise VersionError(
            f"--version {requested!r} does not match live `nkp version` "
            f"({detected!r}). --allow-version-mismatch only applies with "
            f"--input-dir (offline regeneration)."
        )

    raise VersionError(
        f"--version {requested!r} does not match live `nkp version` "
        f"({detected!r}). Omit --version to use the detected value, or use "
        f"--input-dir with --allow-version-mismatch for offline regeneration."
    )


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

        # Cobra pads descriptions to a column. Short names get two+ spaces;
        # long hyphenated names often get only a single space before the
        # description, so require one-or-more whitespace (not two-or-more).
        match = re.match(r"^\s{2,}([a-zA-Z0-9_-]+)(?:\s+|$)", line)
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


@dataclass(frozen=True)
class CompletenessIssue:
    path: Path
    message: str
    severity: str  # "error" | "warning"


_FIRST_FENCE = re.compile(r"```text\n(.*?)```", re.DOTALL)
_SUMMARY_ONE_OF = re.compile(r"\bone of \[([^\]]+)\]", re.IGNORECASE)
_PAGE_TITLE = re.compile(r"^# `(.+)`\s*$")


def extract_first_help_dump(page_md: str) -> str:
    """Return the page's own help fence (first ```text block), not embeds."""
    match = _FIRST_FENCE.search(page_md)
    return match.group(1) if match else ""


def page_command_from_md(page_md: str) -> str | None:
    for line in page_md.splitlines():
        if not line.strip():
            continue
        match = _PAGE_TITLE.match(line.strip())
        return match.group(1) if match else None
    return None


def extract_summary_names(help_text: str) -> list[str]:
    """Names listed in the one-line 'one of […]' summary before Usage/Available."""
    names: list[str] = []
    for line in help_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Usage:") or stripped == "Available Commands:":
            break
        match = _SUMMARY_ONE_OF.search(line)
        if not match:
            continue
        for part in match.group(1).split(","):
            token = re.sub(r"\s*\([^)]*\)\s*", "", part).strip()
            if token:
                names.append(token)
    return names


def covered_direct_children(
    page_md: str, page_command: str
) -> dict[str, str | None]:
    """Map direct child name → relative link href, or None when covered by ### embed."""
    covered: dict[str, str | None] = {}
    link_re = re.compile(
        rf"^- \[`{re.escape(page_command)} ([a-zA-Z0-9_-]+)`\]\(([^)]+)\)\s*$",
        re.MULTILINE,
    )
    for match in link_re.finditer(page_md):
        covered[match.group(1)] = match.group(2)

    # Exact one extra token so nested embeds do not satisfy a direct child.
    embed_re = re.compile(
        rf"^### `{re.escape(page_command)} ([a-zA-Z0-9_-]+)`\s*$",
        re.MULTILINE,
    )
    for match in embed_re.finditer(page_md):
        covered.setdefault(match.group(1), None)
    return covered


def check_page_completeness(page_path: Path) -> list[CompletenessIssue]:
    """Assert Available Commands on a page are linked or embedded (files exist)."""
    issues: list[CompletenessIssue] = []
    page_md = page_path.read_text(encoding="utf-8")
    page_command = page_command_from_md(page_md)
    if not page_command:
        return issues

    help_dump = extract_first_help_dump(page_md)
    available = extract_subcommands(help_dump)
    covered = covered_direct_children(page_md, page_command)

    for name in available:
        if name not in covered:
            issues.append(
                CompletenessIssue(
                    path=page_path,
                    message=(
                        f"Available Commands entry `{name}` has no linked child "
                        f"page or `###` embed under `{page_command}`"
                    ),
                    severity="error",
                )
            )
            continue
        href = covered[name]
        if href is None:
            continue
        target = (page_path.parent / href).resolve()
        if not target.is_file():
            issues.append(
                CompletenessIssue(
                    path=page_path,
                    message=(
                        f"linked child `{page_command} {name}` points to "
                        f"missing file `{href}`"
                    ),
                    severity="error",
                )
            )

    # Only compare summary inventories on parents that list Available Commands.
    # Leaf pages often say "for one of [ubuntu-22.04, …]" for args, not children.
    if "Available Commands:" in help_dump:
        available_set = set(available)
        for name in extract_summary_names(help_dump):
            if name not in available_set:
                issues.append(
                    CompletenessIssue(
                        path=page_path,
                        message=(
                            f"summary mentions `{name}` but it is absent from "
                            f"Available Commands (upstream help drift)"
                        ),
                        severity="warning",
                    )
                )

    return issues


def check_generated_docs(version_dir: Path) -> list[CompletenessIssue]:
    """Walk every generated markdown page under version_dir for completeness."""
    issues: list[CompletenessIssue] = []
    for path in sorted(version_dir.rglob("*.md")):
        if path.name == "README.md":
            continue
        issues.extend(check_page_completeness(path))
    return issues


def verify_completeness(version_dir: Path) -> None:
    """Print warnings; exit non-zero when Available Commands coverage has gaps."""
    issues = check_generated_docs(version_dir)
    warnings = [i for i in issues if i.severity == "warning"]
    errors = [i for i in issues if i.severity == "error"]

    for issue in warnings:
        rel = issue.path
        try:
            rel = issue.path.relative_to(version_dir)
        except ValueError:
            pass
        print(f"WARNING: {rel}: {issue.message}", file=sys.stderr)

    for issue in errors:
        rel = issue.path
        try:
            rel = issue.path.relative_to(version_dir)
        except ValueError:
            pass
        print(f"ERROR: {rel}: {issue.message}", file=sys.stderr)

    if errors:
        print(
            f"Completeness check failed: {len(errors)} gap(s) in {version_dir}",
            file=sys.stderr,
        )
        raise SystemExit(1)


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

    if args.print_version:
        try:
            print(detect_version())
        except VersionError as exc:
            print(f"error: {exc}", file=sys.stderr)
            raise SystemExit(1) from exc
        return

    try:
        version = resolve_version(
            args.version,
            input_dir=args.input_dir,
            allow_mismatch=args.allow_version_mismatch,
        )
    except VersionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    if version in ("", "unknown"):
        print(
            "error: refusing to create an 'unknown/' version directory; "
            "fix `nkp version` detection or pass an explicit --version",
            file=sys.stderr,
        )
        raise SystemExit(1)

    output_root = Path(args.output_root)

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
    verify_completeness(version_dir)
    write_root_index(output_root)

    print(f"Generated structured docs in: {version_dir}")


if __name__ == "__main__":
    main()
