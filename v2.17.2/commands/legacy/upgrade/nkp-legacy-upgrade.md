# `nkp legacy upgrade`

```text
Upgrade one of [addons]

Usage:
  nkp legacy upgrade [command]

Available Commands:
  addons      Upgrade the core Addons in a cluster, one of [eks]

Flags:
  -h, --help   Help for upgrade

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy upgrade [command] --help" for more information about a command.
```

## Subcommands

### `nkp legacy upgrade addons`

```text
Upgrade the core Addons in a cluster, one of [eks]

Usage:
  nkp legacy upgrade addons [command]

Available Commands:
  eks         Upgrade the core Addons in a EKS cluster

Flags:
  -h, --help   Help for addons

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy upgrade addons [command] --help" for more information about a command.
```

### `nkp legacy upgrade addons eks`

```text
Upgrade the core Addons in a EKS cluster

Usage:
  nkp legacy upgrade addons eks [flags]

Flags:
  -c, --cluster-name name         Name used to prefix the cluster and all the created resources.
      --dry-run                   Only print the objects that would be created, without creating them.
  -h, --help                      Help for eks
      --kubeconfig string         Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string          If present, the namespace scope for this CLI request. (default "default")
  -o, --output string             Output format. One of: (json, yaml, name).
      --output-directory string   Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields       If true, keep the managedFields when printing objects in JSON or YAML format.

Global Flags:
  -v, --verbose int   Output verbosity
```
