# `nkp upgrade cluster`

```text
Upgrade a Kubernetes cluster's version to 1.34.3, one of [nutanix]

Usage:
  nkp upgrade cluster [command]

Available Commands:
  nutanix     Upgrade a Kubernetes cluster's version to 1.34.3 in Nutanix

Flags:
  -h, --help          Help for cluster
  -v, --verbose int   Output verbosity

Use "nkp upgrade cluster [command] --help" for more information about a command.
```

## Subcommands

### `nkp upgrade cluster nutanix`

```text
Upgrade a Kubernetes cluster's version to 1.34.3 in Nutanix

Usage:
  nkp upgrade cluster nutanix [flags]

Flags:
  -c, --cluster-name name                 Name used to prefix the cluster and all the created resources.
      --control-plane-vm-image string     Name of OS image to use for control plane machines.
      --dry-run                           Only print the objects that would be created, without creating them.
  -h, --help                              Help for nutanix
      --kubeconfig string                 Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string                  If present, the namespace scope for this CLI request. (default "default")
  -o, --output string                     Output format. One of: (json, yaml, name).
      --output-directory string           Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields               If true, keep the managedFields when printing objects in JSON or YAML format.
      --timeout duration                  The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                Use a specific context in a kubeconfig file.
      --vm-image string                   Name of OS image to use for all machines.
      --wait                              If true, wait for operations to complete before returning. (default true)
      --worker-vm-images stringToString   Names of OS images to use for worker pools. If set, all worker pool names and OS images must be provided. (e.g. --worker-vm-images wpool1=os-image1,wpool2=os-image2) (default [])

Global Flags:
  -v, --verbose int   Output verbosity
```
