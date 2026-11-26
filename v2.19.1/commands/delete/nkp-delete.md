# `nkp delete`

```text
Delete one of [bootstrap (cluster), capi-components, cluster, nodepool]

Usage:
  nkp delete [command]

Aliases:
  delete, destroy

Available Commands:
  bootstrap       Delete bootstrap cluster
  capi-components Delete the CAPI components from the cluster
  cluster         Delete a Kubernetes cluster
  nodepool        Delete a nodepool for a given cluster

Flags:
  -h, --help          Help for delete
  -v, --verbose int   Output verbosity

Use "nkp delete [command] --help" for more information about a command.
```

## Subcommands

- [`nkp delete bootstrap`](bootstrap/nkp-delete-bootstrap.md)
- [`nkp delete capi-components`](capi-components/nkp-delete-capi-components.md)
- [`nkp delete cluster`](cluster/nkp-delete-cluster.md)
- [`nkp delete nodepool`](nodepool/nkp-delete-nodepool.md)
