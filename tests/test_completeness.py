"""Unit and fixture tests for post-generate completeness checks."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_markdown import (  # noqa: E402
    assign_page_flags,
    build_tree,
    check_generated_docs,
    check_page_completeness,
    covered_direct_children,
    extract_first_help_dump,
    extract_summary_names,
    load_flat_docs,
    page_command_from_md,
    verify_completeness,
    write_pages,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
COMPLETENESS = FIXTURES / "completeness"


def _load_page(name: str) -> str:
    return (COMPLETENESS / name).read_text(encoding="utf-8")


class HelpDumpHelpersTests(unittest.TestCase):
    def test_extract_first_help_dump_ignores_embeds(self) -> None:
        dump = extract_first_help_dump(_load_page("page_complete_embeds.md"))
        self.assertIn("Available Commands:", dump)
        self.assertIn("preprovisioned", dump)
        self.assertNotIn("AKS help", dump)

    def test_page_command_from_md(self) -> None:
        self.assertEqual(
            page_command_from_md(_load_page("page_complete_links.md")),
            "nkp demo",
        )

    def test_extract_summary_names_strips_parentheticals(self) -> None:
        help_text = (
            "Update one of [bootstrap (cluster), controlplane, nodepool]\n"
            "\n"
            "Usage:\n"
            "  nkp update [command]\n"
        )
        self.assertEqual(
            extract_summary_names(help_text),
            ["bootstrap", "controlplane", "nodepool"],
        )

    def test_covered_direct_children_links_and_embeds(self) -> None:
        linked = covered_direct_children(
            _load_page("page_complete_links.md"), "nkp demo"
        )
        self.assertEqual(
            linked,
            {
                "alpha": "alpha/nkp-demo-alpha.md",
                "beta": "beta/nkp-demo-beta.md",
            },
        )
        embedded = covered_direct_children(
            _load_page("page_complete_embeds.md"), "nkp demo nest"
        )
        self.assertEqual(embedded, {"aks": None, "preprovisioned": None})


class CheckPageCompletenessTests(unittest.TestCase):
    def test_complete_embeds_pass(self) -> None:
        path = COMPLETENESS / "page_complete_embeds.md"
        self.assertEqual(check_page_completeness(path), [])

    def test_complete_links_pass_when_targets_exist(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "nkp-demo.md"
            page.write_text(_load_page("page_complete_links.md"), encoding="utf-8")
            (root / "alpha").mkdir()
            (root / "alpha" / "nkp-demo-alpha.md").write_text("# ok\n", encoding="utf-8")
            (root / "beta").mkdir()
            (root / "beta" / "nkp-demo-beta.md").write_text("# ok\n", encoding="utf-8")
            self.assertEqual(check_page_completeness(page), [])

    def test_missing_available_command_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "nkp-push.md"
            page.write_text(_load_page("page_missing_child.md"), encoding="utf-8")
            (root / "bundle").mkdir()
            (root / "bundle" / "nkp-push-bundle.md").write_text("# ok\n", encoding="utf-8")
            (root / "chart").mkdir()
            (root / "chart" / "nkp-push-chart.md").write_text("# ok\n", encoding="utf-8")

            issues = check_page_completeness(page)
            errors = [i for i in issues if i.severity == "error"]
            warnings = [i for i in issues if i.severity == "warning"]

            self.assertEqual(len(errors), 1)
            self.assertIn("chart-bundle", errors[0].message)
            # summary lists image-bundle which is also absent from Available Commands
            self.assertTrue(
                any("image-bundle" in w.message for w in warnings),
                msg=warnings,
            )

    def test_broken_link_is_error(self) -> None:
        path = COMPLETENESS / "page_broken_link.md"
        issues = check_page_completeness(path)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "error")
        self.assertIn("missing file", issues[0].message)

    def test_summary_drift_warns_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "nkp-create.md"
            page.write_text(_load_page("page_summary_drift.md"), encoding="utf-8")
            (root / "bundle").mkdir()
            (root / "bundle" / "nkp-create-bundle.md").write_text(
                "# ok\n", encoding="utf-8"
            )

            issues = check_page_completeness(page)
            self.assertTrue(issues)
            self.assertTrue(all(i.severity == "warning" for i in issues))
            drifted = {i.message.split("`")[1] for i in issues}
            self.assertEqual(drifted, {"catalog", "image-bundle"})


class VerifyCompletenessTests(unittest.TestCase):
    def test_verify_completeness_exits_on_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            version_dir = Path(tmp)
            shutil.copy(
                COMPLETENESS / "page_broken_link.md",
                version_dir / "nkp-tool.md",
            )
            with self.assertRaises(SystemExit) as ctx:
                verify_completeness(version_dir)
            self.assertEqual(ctx.exception.code, 1)

    def test_verify_completeness_passes_clean_tree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            version_dir = Path(tmp)
            page = version_dir / "nkp-demo-nest.md"
            page.write_text(
                _load_page("page_complete_embeds.md"), encoding="utf-8"
            )
            verify_completeness(version_dir)  # should not raise


class GenerateThenCheckTests(unittest.TestCase):
    def test_complete_flat_input_passes_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            version_dir = Path(tmp) / "v0.0.1"
            docs = load_flat_docs(FIXTURES / "flat_complete")
            root = build_tree(docs)
            assign_page_flags(root)
            version_dir.mkdir(parents=True)
            write_pages(root, version_dir)
            issues = check_generated_docs(version_dir)
            self.assertEqual(
                [i for i in issues if i.severity == "error"],
                [],
                msg=issues,
            )

    def test_incomplete_flat_input_fails_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            version_dir = Path(tmp) / "v0.0.1"
            docs = load_flat_docs(FIXTURES / "flat_incomplete")
            root = build_tree(docs)
            assign_page_flags(root)
            version_dir.mkdir(parents=True)
            write_pages(root, version_dir)
            with self.assertRaises(SystemExit) as ctx:
                verify_completeness(version_dir)
            self.assertEqual(ctx.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
