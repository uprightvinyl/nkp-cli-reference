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

## Additional Usage

Generate structured markdown only:

```bash
python3 scripts/generate_markdown.py
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
