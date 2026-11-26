# `nkp experimental catalog`

```text
Experimental catalog commands (release, docgen)

Usage:
  nkp experimental catalog [command]

Available Commands:
  docgen      Generate Markdown CLI documentation from the command tree
  release     Build the release artifacts for a given catalog repository

Flags:
  -h, --help          Help for catalog
  -v, --verbose int   Output verbosity

Use "nkp experimental catalog [command] --help" for more information about a command.
```

## Subcommands

### `nkp experimental catalog docgen`

```text
Generates one Markdown file per command into the given directory (default: docs/content/cli) with Docusaurus frontmatter for the docs site.

Usage:
  nkp experimental catalog docgen [flags]

Flags:
  -h, --help         Help for docgen
      --out string   Output directory for generated Markdown files (default "docs/content/cli")

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp experimental catalog release`

```text
Build the release artifacts for a given catalog repository

Usage:
  nkp experimental catalog release [flags]

Flags:
  -h, --help                  Help for release
      --release-spec string   Path to the file with release specification (default ".release.yaml")
      --repo-dir string       Path to the catalog repository in which to build the release artifacts

Global Flags:
  -v, --verbose int   Output verbosity
```
