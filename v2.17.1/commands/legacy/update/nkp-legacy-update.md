# `nkp legacy update`

```text
Update one of [controlplane, nodepool]

Usage:
  nkp legacy update [command]

Available Commands:
  controlplane Update a Kubernetes cluster control plane, one of [eks]
  nodepool     Upate a Kubernetes cluster node pool, one of [eks]

Flags:
  -h, --help   Help for update

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy update [command] --help" for more information about a command.
```

## Subcommands

### `nkp legacy update nodepool`

```text
Upate a Kubernetes cluster node pool, one of [eks]

Usage:
  nkp legacy update nodepool [command]

Available Commands:
  eks         Update a Konvoy cluster node pool in EKS

Flags:
  -h, --help   Help for nodepool

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy update nodepool [command] --help" for more information about a command.
```

### `nkp legacy update nodepool eks`

```text
Update a Konvoy cluster node pool in EKS

Usage:
  nkp legacy update nodepool eks [flags]

Flags:
  -c, --cluster-name name           Name used to prefix the cluster and all the created resources.
  -h, --help                        Help for eks
      --instance-type string        Instance type to use for node pool machines
      --kubeconfig string           Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string   Kubernetes version
  -n, --namespace string            If present, the namespace scope for this CLI request. (default "default")
      --timeout duration            The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string          Use a specific context in a kubeconfig file.
      --wait                        If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```
