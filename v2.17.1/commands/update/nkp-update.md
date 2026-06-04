# `nkp update`

```text
Update one of [bootstrap (cluster), controlplane, nodepool]

Usage:
  nkp update [command]

Available Commands:
  bootstrap    Update bootstrap cluster
  controlplane Update a Kubernetes cluster control plane, one of [aks, aws, azure, gcp, nutanix, preprovisioned, vsphere]
  nodepool     Upate a Kubernetes cluster node pool, one of [aws, azure, gcp, preprovisioned, vsphere]

Flags:
  -h, --help          Help for update
  -v, --verbose int   Output verbosity

Use "nkp update [command] --help" for more information about a command.
```

## Subcommands

- [`nkp update bootstrap`](bootstrap/nkp-update-bootstrap.md)
- [`nkp update nodepool`](nodepool/nkp-update-nodepool.md)
