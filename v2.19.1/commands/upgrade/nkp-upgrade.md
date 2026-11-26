# `nkp upgrade`

```text
Upgrade one of [addons, catalog-app, cluster, kommander, platform-apps]

Usage:
  nkp upgrade [command]

Available Commands:
  addons          Upgrade the core Addons in a cluster, one of [aws, azure, gcp, preprovisioned, vsphere]
  catalog-app     Upgrade a Catalog Application to a newer version
  cluster         Cluster one of [eks, metal, nutanix]
  kommander       Upgrade the Kommander version of the targeted cluster
  platform-apps   Upgrade platform applications for a target NKPCluster

Flags:
  -h, --help   Help for upgrade

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp upgrade [command] --help" for more information about a command.
```

## Subcommands

- [`nkp upgrade addons`](addons/nkp-upgrade-addons.md)
- [`nkp upgrade catalog-app`](catalog-app/nkp-upgrade-catalog-app.md)
- [`nkp upgrade cluster`](cluster/nkp-upgrade-cluster.md)
- [`nkp upgrade kommander`](kommander/nkp-upgrade-kommander.md)
- [`nkp upgrade platform-apps`](platform-apps/nkp-upgrade-platform-apps.md)
