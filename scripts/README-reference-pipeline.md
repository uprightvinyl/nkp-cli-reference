# NKP Reference Pipeline

Default command (recommended):

```bash
bash scripts/generate_reference.sh
```

This command:

1. Detects installed `nkp` version.
2. Quickly exits if both outputs already exist for that version.
3. Builds structured markdown in `<version>/` directly from `nkp --help`.
4. Exports DOCX in `exports/`.

## Install

```bash
python3 -m pip install -r scripts/requirements-docx.txt
```

Use a different template:

```bash
bash scripts/generate_reference.sh "templates/General Document TEMPLATE.docx"
```

If the template file is missing, generation continues and creates a DOCX
using default Word styling.

Force regeneration even if outputs exist:

```bash
bash scripts/generate_reference.sh --force
```

You can combine force + template:

```bash
bash scripts/generate_reference.sh --force "templates/General Document TEMPLATE.docx"
```

## Version detection

The shell wrapper and `generate_markdown.py` share one `detect_version()`
implementation (the wrapper calls `python3 scripts/generate_markdown.py
--print-version`). The folder name is exactly the value from `nkp version`
(for example `v2.17.1`).

- If you pass `--version` and it differs from the live binary, generation
  **refuses** (avoids writing `v2.18.0/` from a 2.19 binary on `PATH`).
- Offline regeneration from recorded help dumps may set a different folder
  name only with both `--input-dir` and `--allow-version-mismatch`.
- An unparseable / missing `nkp version` fails loudly; an `unknown/` directory
  is never created.

Multi-version regen: put the target `nkp` on `PATH` (PATH swap / symlink), then
run the wrapper so the folder name always matches that binary.

## Additional Usage

Generate structured markdown only:

```bash
python3 scripts/generate_markdown.py
```

Print the detected live version (same helper the shell uses):

```bash
python3 scripts/generate_markdown.py --print-version
```

Offline flat dump with an explicit folder name when no matching binary is on
`PATH` (or when intentionally labeling differently):

```bash
python3 scripts/generate_markdown.py \
  --input-dir path/to/flat-help \
  --version v2.17.1 \
  --allow-version-mismatch
```

Export all versions:

```bash
python3 scripts/export_docx.py
```

Export one version:

```bash
python3 scripts/export_docx.py --version v2.17.1
```

Keep template body content (append generated content after template content):

```bash
python3 scripts/export_docx.py --template "templates/General Document TEMPLATE.docx" --keep-template-content
```
