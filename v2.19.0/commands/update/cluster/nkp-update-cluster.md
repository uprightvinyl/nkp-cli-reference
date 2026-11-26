# `nkp update cluster`

```text
Update cluster resources

Usage:
  nkp update cluster [command]

Available Commands:
  nutanix-registry-credentials Set or rotate Nutanix DockerHub credentials on cluster(s).

Flags:
  -h, --help   Help for cluster

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp update cluster [command] --help" for more information about a command.
```

## Subcommands

### `nkp update cluster nutanix-registry-credentials`

```text
Set or rotate the Nutanix DockerHub credentials used to pull NKP images.

This command updates the Nutanix DockerHub credentials Secret
(<cluster-name>-dockerhub-nutanix-credentials).

Use --cluster-name to target a single cluster, --all to target every cluster in
the selected namespace, or --all-namespaces to set the credentials on the
management cluster and every workload cluster in the fleet.

Usage:
  nkp update cluster nutanix-registry-credentials [flags]

Flags:
      --all                                Set the credentials on every cluster in the selected namespace.
      --all-namespaces                     Set the credentials on the management cluster and every workload cluster in the fleet.
  -c, --cluster-name name                  Name used to prefix the cluster and all the created resources.
  -h, --help                               Help for nutanix-registry-credentials
      --kubeconfig string                  Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string                   If present, the namespace scope for this CLI request. (default "default")
      --nutanix-registry-password string   Personal access token (PAT) for the Nutanix DockerHub organization, used to pull NKP images.
      --nutanix-registry-username string   Username for the Nutanix DockerHub organization, used to pull NKP images.
      --use-context string                 Use a specific context in a kubeconfig file.

Global Flags:
  -v, --verbose int   Output verbosity
```
