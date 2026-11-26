"""Unit tests for shared version detection and mismatch guards."""

from __future__ import annotations

import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_markdown import (  # noqa: E402
    VersionError,
    detect_version,
    main,
    parse_version_output,
    resolve_version,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCRIPT = ROOT / "scripts" / "generate_markdown.py"


class ParseVersionOutputTests(unittest.TestCase):
    def test_standard_space_after_colon(self) -> None:
        self.assertEqual(
            parse_version_output("nkp: v2.17.1\nkubernetes: v1.2.3\n"),
            "v2.17.1",
        )

    def test_no_space_after_colon(self) -> None:
        self.assertEqual(parse_version_output("nkp:v2.19.0\n"), "v2.19.0")

    def test_extra_spaces_around_colon_value(self) -> None:
        self.assertEqual(parse_version_output("  nkp:   v2.18.0  \n"), "v2.18.0")

    def test_ignores_non_nkp_lines(self) -> None:
        text = "client: v1\nserver: v2\nnkp: v2.17.1\n"
        self.assertEqual(parse_version_output(text), "v2.17.1")

    def test_empty_value_is_skipped(self) -> None:
        self.assertIsNone(parse_version_output("nkp:\n"))
        self.assertIsNone(parse_version_output("nkp:   \n"))

    def test_missing_nkp_line(self) -> None:
        self.assertIsNone(parse_version_output("version: 1.0\n"))

    def test_first_nkp_line_wins(self) -> None:
        text = "nkp: v2.17.1\nnkp: v9.9.9\n"
        self.assertEqual(parse_version_output(text), "v2.17.1")


class DetectVersionTests(unittest.TestCase):
    def test_success(self) -> None:
        proc = subprocess.CompletedProcess(
            args=["nkp", "version"],
            returncode=0,
            stdout="nkp: v2.17.1\n",
            stderr="",
        )
        with mock.patch("generate_markdown.subprocess.run", return_value=proc):
            self.assertEqual(detect_version(), "v2.17.1")

    def test_missing_binary(self) -> None:
        with mock.patch(
            "generate_markdown.subprocess.run",
            side_effect=FileNotFoundError("nkp"),
        ):
            with self.assertRaises(VersionError) as ctx:
                detect_version()
            self.assertIn("not installed", str(ctx.exception))

    def test_nonzero_exit(self) -> None:
        proc = subprocess.CompletedProcess(
            args=["nkp", "version"],
            returncode=2,
            stdout="",
            stderr="boom",
        )
        with mock.patch("generate_markdown.subprocess.run", return_value=proc):
            with self.assertRaises(VersionError) as ctx:
                detect_version()
            self.assertIn("exit code 2", str(ctx.exception))

    def test_unparseable_output(self) -> None:
        proc = subprocess.CompletedProcess(
            args=["nkp", "version"],
            returncode=0,
            stdout="something else\n",
            stderr="",
        )
        with mock.patch("generate_markdown.subprocess.run", return_value=proc):
            with self.assertRaises(VersionError) as ctx:
                detect_version()
            self.assertIn("could not parse", str(ctx.exception))


class ResolveVersionTests(unittest.TestCase):
    def test_defaults_to_detected(self) -> None:
        self.assertEqual(
            resolve_version("", detected="v2.17.1"),
            "v2.17.1",
        )

    def test_matching_requested(self) -> None:
        self.assertEqual(
            resolve_version("v2.17.1", detected="v2.17.1"),
            "v2.17.1",
        )

    def test_mismatch_refused_on_live_crawl(self) -> None:
        with self.assertRaises(VersionError) as ctx:
            resolve_version("v2.18.0", detected="v2.19.0")
        self.assertIn("does not match", str(ctx.exception))
        self.assertIn("v2.18.0", str(ctx.exception))
        self.assertIn("v2.19.0", str(ctx.exception))

    def test_allow_mismatch_without_input_dir_still_refuses(self) -> None:
        with self.assertRaises(VersionError) as ctx:
            resolve_version(
                "v2.18.0",
                detected="v2.19.0",
                allow_mismatch=True,
            )
        self.assertIn("only applies with --input-dir", str(ctx.exception))

    def test_allow_mismatch_with_input_dir(self) -> None:
        self.assertEqual(
            resolve_version(
                "v2.18.0",
                detected="v2.19.0",
                input_dir="/tmp/flat",
                allow_mismatch=True,
            ),
            "v2.18.0",
        )

    def test_offline_without_binary_uses_requested(self) -> None:
        self.assertEqual(
            resolve_version(
                "v2.17.1",
                input_dir="/tmp/flat",
                detect_error=VersionError("nkp missing"),
            ),
            "v2.17.1",
        )

    def test_offline_without_binary_or_version_fails(self) -> None:
        with self.assertRaises(VersionError):
            resolve_version(
                "",
                input_dir="/tmp/flat",
                detect_error=VersionError("nkp missing"),
            )

    def test_live_unknown_detection_fails_loudly(self) -> None:
        with self.assertRaises(VersionError) as ctx:
            resolve_version(
                "",
                detect_error=VersionError("could not parse version"),
            )
        self.assertIn("could not parse", str(ctx.exception))


class MainVersionCliTests(unittest.TestCase):
    def test_print_version_success(self) -> None:
        with mock.patch(
            "generate_markdown.detect_version", return_value="v2.17.1"
        ):
            with mock.patch.object(
                sys, "argv", ["generate_markdown.py", "--print-version"]
            ):
                with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
                    main()
        self.assertEqual(out.getvalue().strip(), "v2.17.1")

    def test_print_version_failure_exits(self) -> None:
        with mock.patch(
            "generate_markdown.detect_version",
            side_effect=VersionError("nkp missing"),
        ):
            with mock.patch.object(
                sys, "argv", ["generate_markdown.py", "--print-version"]
            ):
                with self.assertRaises(SystemExit) as ctx:
                    main()
        self.assertEqual(ctx.exception.code, 1)

    def test_mismatch_exits_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch(
                "generate_markdown.detect_version", return_value="v2.19.0"
            ):
                with mock.patch.object(
                    sys,
                    "argv",
                    [
                        "generate_markdown.py",
                        "--version",
                        "v2.18.0",
                        "--output-root",
                        tmp,
                    ],
                ):
                    with self.assertRaises(SystemExit) as ctx:
                        main()
            self.assertEqual(ctx.exception.code, 1)
            self.assertFalse((Path(tmp) / "v2.18.0").exists())
            self.assertFalse((Path(tmp) / "unknown").exists())

    def test_offline_allow_mismatch_writes_requested_folder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out_root = Path(tmp)
            with mock.patch(
                "generate_markdown.detect_version", return_value="v9.9.9"
            ):
                with mock.patch.object(
                    sys,
                    "argv",
                    [
                        "generate_markdown.py",
                        "--input-dir",
                        str(FIXTURES / "flat_complete"),
                        "--version",
                        "v0.0.1",
                        "--allow-version-mismatch",
                        "--output-root",
                        str(out_root),
                    ],
                ):
                    main()
            self.assertTrue((out_root / "v0.0.1" / "nkp.md").is_file())
            self.assertFalse((out_root / "v9.9.9").exists())

    def test_refuses_literal_unknown_version(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch(
                "generate_markdown.resolve_version", return_value="unknown"
            ):
                with mock.patch.object(
                    sys,
                    "argv",
                    [
                        "generate_markdown.py",
                        "--input-dir",
                        str(FIXTURES / "flat_complete"),
                        "--version",
                        "unknown",
                        "--allow-version-mismatch",
                        "--output-root",
                        tmp,
                    ],
                ):
                    with self.assertRaises(SystemExit) as ctx:
                        main()
            self.assertEqual(ctx.exception.code, 1)
            self.assertFalse((Path(tmp) / "unknown").exists())


class ShellWrapperUsesPythonDetectionTests(unittest.TestCase):
    def test_wrapper_invokes_print_version(self) -> None:
        wrapper = (ROOT / "scripts" / "generate_reference.sh").read_text(
            encoding="utf-8"
        )
        self.assertIn("--print-version", wrapper)
        self.assertIn('generate_markdown.py" --print-version', wrapper)
        # Must not parse `nkp version` with a local awk pipeline anymore.
        self.assertNotRegex(wrapper, r"nkp version.*\|.*awk")


if __name__ == "__main__":
    unittest.main()
