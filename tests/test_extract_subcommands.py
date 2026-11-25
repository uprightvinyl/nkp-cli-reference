"""Unit tests for extract_subcommands() crawl parsing."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_markdown import extract_subcommands  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _load(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


class ExtractSubcommandsTests(unittest.TestCase):
    def test_short_padded_names(self) -> None:
        names = extract_subcommands(_load("help_short_padded.txt"))
        self.assertEqual(names, ["bundle", "chart", "help"])

    def test_long_hyphenated_single_space(self) -> None:
        names = extract_subcommands(_load("help_long_hyphenated.txt"))
        self.assertEqual(
            names,
            [
                "appdeployments",
                "catalog-repository",
                "chart-bundle",
                "image-bundle",
                "default-workspace",
            ],
        )

    def test_mixed_short_and_long(self) -> None:
        names = extract_subcommands(_load("help_mixed.txt"))
        self.assertEqual(names, ["bundle", "chart", "chart-bundle", "help"])

    def test_empty_available_commands_section(self) -> None:
        self.assertEqual(extract_subcommands(_load("help_empty_section.txt")), [])

    def test_no_available_commands_section(self) -> None:
        self.assertEqual(extract_subcommands(_load("help_no_section.txt")), [])

    def test_name_only_no_description(self) -> None:
        self.assertEqual(extract_subcommands(_load("help_name_only.txt")), ["orphan"])

    def test_stops_at_flags_and_ignores_flag_lines(self) -> None:
        names = extract_subcommands(_load("help_mixed.txt"))
        self.assertEqual(names, ["bundle", "chart", "chart-bundle", "help"])
        for flag_token in ("-h", "--help", "--verbose", "Global"):
            self.assertNotIn(flag_token, names)

    def test_inline_string_long_name_regression(self) -> None:
        # Minimal reproduction of the v2.17.1 nkp generate / push gaps.
        help_text = """\
Available Commands:
  catalog-repository Generate the catalog repository layout and its contents
  chart-bundle Upload chart bundles to the repository

Flags:
  -h, --help          Help for generate
"""
        self.assertEqual(
            extract_subcommands(help_text),
            ["catalog-repository", "chart-bundle"],
        )


if __name__ == "__main__":
    unittest.main()
