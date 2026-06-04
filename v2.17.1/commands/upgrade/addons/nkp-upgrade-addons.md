# `nkp upgrade addons`

```text
Upgrade the core Addons in a cluster, one of [aws, azure, gcp, preprovisioned, vsphere]

Usage:
  nkp upgrade addons [command]

Available Commands:
  aws            Upgrade the core Addons in a AWS cluster
  azure          Upgrade the core Addons in a Azure cluster
  gcp            Upgrade the core Addons in a GCP cluster
  preprovisioned Upgrade the core Addons in a Preprovisioned cluster
  vsphere        Upgrade the core Addons in a vSphere cluster

Flags:
  -h, --help          Help for addons
  -v, --verbose int   Output verbosity

Use "nkp upgrade addons [command] --help" for more information about a command.
```

## Subcommands

### `nkp upgrade addons aws`

```text
Upgrade the core Addons in a AWS cluster

Usage:
  nkp upgrade addons aws [flags]

Flags:
  -c, --cluster-name name         Name used to prefix the cluster and all the created resources.
      --dry-run                   Only print the objects that would be created, without creating them.
  -h, --help                      Help for aws
      --kubeconfig string         Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string          If present, the namespace scope for this CLI request. (default "default")
  -o, --output string             Output format. One of: (json, yaml, name).
      --output-directory string   Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields       If true, keep the managedFields when printing objects in JSON or YAML format.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp upgrade addons azure`

```text
Upgrade the core Addons in a Azure cluster

Usage:
  nkp upgrade addons azure [flags]

Flags:
  -c, --cluster-name name         Name used to prefix the cluster and all the created resources.
      --dry-run                   Only print the objects that would be created, without creating them.
  -h, --help                      Help for azure
      --kubeconfig string         Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string          If present, the namespace scope for this CLI request. (default "default")
  -o, --output string             Output format. One of: (json, yaml, name).
      --output-directory string   Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields       If true, keep the managedFields when printing objects in JSON or YAML format.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp upgrade addons gcp`

```text
Upgrade the core Addons in a GCP cluster

Usage:
  nkp upgrade addons gcp [flags]

Flags:
  -c, --cluster-name name         Name used to prefix the cluster and all the created resources.
      --dry-run                   Only print the objects that would be created, without creating them.
  -h, --help                      Help for gcp
      --kubeconfig string         Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string          If present, the namespace scope for this CLI request. (default "default")
  -o, --output string             Output format. One of: (json, yaml, name).
      --output-directory string   Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields       If true, keep the managedFields when printing objects in JSON or YAML format.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp upgrade addons vsphere`

```text
Upgrade the core Addons in a vSphere cluster

Usage:
  nkp upgrade addons vsphere [flags]

Flags:
  -c, --cluster-name name         Name used to prefix the cluster and all the created resources.
      --dry-run                   Only print the objects that would be created, without creating them.
  -h, --help                      Help for vsphere
      --kubeconfig string         Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string          If present, the namespace scope for this CLI request. (default "default")
  -o, --output string             Output format. One of: (json, yaml, name).
      --output-directory string   Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields       If true, keep the managedFields when printing objects in JSON or YAML format.

Global Flags:
  -v, --verbose int   Output verbosity
```
