#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_PATH="$ROOT_DIR/templates/General Document TEMPLATE.docx"
FORCE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    -f|--force)
      FORCE=true
      shift
      ;;
    *)
      TEMPLATE_PATH="$1"
      shift
      ;;
  esac
done

if [[ ! -f "$TEMPLATE_PATH" ]]; then
  echo "Template not found: $TEMPLATE_PATH" >&2
  exit 1
fi

if ! command -v nkp >/dev/null 2>&1; then
  echo "nkp is not installed or not on PATH" >&2
  exit 1
fi

VERSION="$(nkp version 2>/dev/null | awk -F': ' '/^nkp:/{print $2; exit}')"
if [[ -z "$VERSION" ]]; then
  echo "Failed to detect nkp version" >&2
  exit 1
fi

VERSION_DIR="$ROOT_DIR/$VERSION"
DOCX_PATH="$ROOT_DIR/exports/NKP_CLI_Reference_${VERSION}.docx"

if [[ "$FORCE" != "true" && -d "$VERSION_DIR" && -f "$DOCX_PATH" ]]; then
  echo "Docs already exist for $VERSION. Nothing to do."
  exit 0
fi

if [[ "$FORCE" == "true" ]]; then
  echo "Force mode enabled: regenerating docs for $VERSION."
fi

echo "Building structured markdown for $VERSION..."
python3 "$ROOT_DIR/scripts/generate_markdown.py" \
  --output-root "$ROOT_DIR" \
  --version "$VERSION" >/dev/null

echo "Exporting DOCX for $VERSION..."
python3 "$ROOT_DIR/scripts/export_docx.py" \
  --root "$ROOT_DIR" \
  --version "$VERSION" \
  --template "$TEMPLATE_PATH" >/dev/null

echo "Done:"
echo "  Markdown: $VERSION_DIR"
echo "  DOCX:     $DOCX_PATH"
