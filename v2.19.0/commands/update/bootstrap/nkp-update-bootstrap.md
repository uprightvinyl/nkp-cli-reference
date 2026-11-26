# `nkp update bootstrap`

```text
Update bootstrap cluster

Usage:
  nkp update bootstrap [command]

Available Commands:
  credentials Update credentials in the cluster

Flags:
  -h, --help   Help for bootstrap

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp update bootstrap [command] --help" for more information about a command.
```

## Subcommands

### `nkp update bootstrap credentials`

```text
Update credentials in the cluster

Usage:
  nkp update bootstrap credentials [command]

Available Commands:
  aws         Update AWS credentials in the cluster and restart CAPA controllers
  gcp         Update GCP credentials in the cluster and restart CAPG controllers
  vsphere     Update VSphere credentials in the cluster and restart CAPV controllers

Flags:
  -h, --help   Help for credentials

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp update bootstrap credentials [command] --help" for more information about a command.
```

### `nkp update bootstrap credentials aws`

```text
Update AWS credentials in the cluster and restart CAPA controllers

Usage:
  nkp update bootstrap credentials aws [flags]

Flags:
      --context string      The name of the kubeconfig context to use
  -h, --help                Help for aws
      --kubeconfig string   Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --print-only          Print the credentials and exit the function. Without modifying cluster

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update bootstrap credentials gcp`

```text
Update GCP credentials in the cluster and restart CAPG controllers

Usage:
  nkp update bootstrap credentials gcp [flags]

Flags:
      --context string      The name of the kubeconfig context to use
  -h, --help                Help for gcp
      --kubeconfig string   Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --print-only          Print the credentials and exit the function. Without modifying cluster

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update bootstrap credentials vsphere`

```text
Update VSphere credentials in the cluster and restart CAPV controllers

Usage:
  nkp update bootstrap credentials vsphere [flags]

Flags:
      --context string      The name of the kubeconfig context to use
  -h, --help                Help for vsphere
      --kubeconfig string   Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --print-only          Print the credentials and exit the function. Without modifying cluster

Global Flags:
  -v, --verbose int   Output verbosity
```
