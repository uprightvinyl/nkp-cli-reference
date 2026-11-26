# `nkp push`

```text
Push one of [bundle, image-archive]

Usage:
  nkp push [command]

Available Commands:
  bundle        Push from bundles into an existing OCI registry
  image-archive Push OCI/docker image archive tarballs into an existing OCI registry

Flags:
  -h, --help   Help for push

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp push [command] --help" for more information about a command.
```

## Subcommands

- [`nkp push bundle`](bundle/nkp-push-bundle.md)
- [`nkp push image-archive`](image-archive/nkp-push-image-archive.md)
