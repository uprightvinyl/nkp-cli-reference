# `nkp upgrade cluster`

```text
Cluster one of [eks, metal, nutanix]

Usage:
  nkp upgrade cluster [command]

Available Commands:
  eks         Upgrade a Kubernetes cluster's version to 1.36.0 in EKS
  metal       Upgrade a NKP Metal cluster
  nutanix     Upgrade a Kubernetes cluster's version to 1.36.2 in Nutanix

Flags:
  -h, --help   Help for cluster

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp upgrade cluster [command] --help" for more information about a command.
```

## Subcommands

### `nkp upgrade cluster eks`

```text
Upgrade a Kubernetes cluster's version to 1.36.0 in EKS

Usage:
  nkp upgrade cluster eks [flags]

Flags:
  -c, --cluster-name name               Name used to prefix the cluster and all the created resources.
      --dry-run                         Only print the objects that would be created, without creating them.
  -h, --help                            Help for eks
      --kubeconfig string               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string                If present, the namespace scope for this CLI request. (default "default")
  -o, --output string                   Output format. One of: (json, yaml, name).
      --output-directory string         Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields             If true, keep the managedFields when printing objects in JSON or YAML format.
      --skip-preflight-checks strings   Skip preflight checks. Use "all" to skip all checks, a comma-separated list of names to skip specific checks, or "" to run all checks, even if checks were previously skipped. (default [])
      --timeout duration                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 40m0s)
      --use-context string              Use a specific context in a kubeconfig file.
  -v, --verbose int                     Output verbosity
      --wait                            If true, wait for operations to complete before returning. (default true)
```

### `nkp upgrade cluster metal`

```text
Upgrade a Kubernetes cluster's version to 1.36.2 on bare metal.

Usage:
  nkp upgrade cluster metal [flags]

Flags:
  -c, --cluster-name name                Name used to prefix the cluster and all the created resources.
      --dry-run                          Only print the objects that would be created, without creating them.
  -h, --help                             Help for metal
      --kubeconfig string                Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-image-uri image-uri   Machine OS image URI uploaded to an OCI-compliant registry. The expected format is oci://<registry-url>/<registry-path>/<image-name>:<image-tag>. When unset, will be derived based on the Kubernetes versions using the registry mirror when one is configured.
      --kubernetes-version string        Kubernetes version. (default "1.36.2")
  -n, --namespace string                 If present, the namespace scope for this CLI request. (default "kommander-default-workspace")
  -o, --output string                    Output format. One of: (json, yaml, kyaml, name).
      --show-managed-fields              If true, keep the managedFields when printing objects in JSON or YAML format.
      --skip-preflight-checks strings    Skip preflight checks. Use "all" to skip all checks, a comma-separated list of names to skip specific checks, or "" to run all checks, even if checks were previously skipped. (default [])
      --timeout duration                 The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 1h0m0s)
  -v, --verbose int                      Output verbosity
      --wait                             If true, wait for operations to complete before returning. (default true)
```

### `nkp upgrade cluster nutanix`

```text
Upgrade a Kubernetes cluster's version to 1.36.2 in Nutanix

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
      --skip-preflight-checks strings     Skip preflight checks. Use "all" to skip all checks, a comma-separated list of names to skip specific checks, or "" to run all checks, even if checks were previously skipped. (default [])
      --timeout duration                  The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 40m0s)
      --use-context string                Use a specific context in a kubeconfig file.
  -v, --verbose int                       Output verbosity
      --vm-image string                   Name of OS image to use for all machines.
      --wait                              If true, wait for operations to complete before returning. (default true)
      --worker-vm-images stringToString   Names of OS images to use for worker pools. If set, all worker pool names and OS images must be provided. (e.g. --worker-vm-images wpool1=os-image1,wpool2=os-image2) (default [])
```
