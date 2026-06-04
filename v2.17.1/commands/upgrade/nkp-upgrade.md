# `nkp upgrade`

```text
Upgrade one of [addons, capi-components, catalogapp, cluster, kommander, workspace]

Usage:
  nkp upgrade [command]

Available Commands:
  addons          Upgrade the core Addons in a cluster, one of [aws, azure, gcp, preprovisioned, vsphere]
  capi-components Upgrade the CAPI components in the cluster
  catalogapp      Upgrade a Catalog Application to a newer version
  cluster         Upgrade a Kubernetes cluster's version to 1.34.3, one of [nutanix]
  kommander       Upgrade the Kommander version of the targeted cluster
  workspace       Upgrade all platform applications in the given workspace and its projects to the same version as platform applications running on the management cluster

Flags:
  -h, --help   Help for upgrade

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp upgrade [command] --help" for more information about a command.
```

## Subcommands

- [`nkp upgrade addons`](addons/nkp-upgrade-addons.md)
- [`nkp upgrade catalogapp`](catalogapp/nkp-upgrade-catalogapp.md)
- [`nkp upgrade cluster`](cluster/nkp-upgrade-cluster.md)
- [`nkp upgrade kommander`](kommander/nkp-upgrade-kommander.md)
- [`nkp upgrade workspace`](workspace/nkp-upgrade-workspace.md)
