# `nkp upgrade platform-apps`

```text
Upgrade platform applications for a target NKPCluster

Usage:
  nkp upgrade platform-apps --cluster-name CLUSTER_NAME --version VERSION --workspace WORKSPACE [--dry-run] [flags]

Flags:
      --allow-gitrepository-catalog-apps   Allow upgrade to proceed when deprecated GitRepository-based catalog apps are detected
      --cluster-name string                Name of target NKPCluster
      --config string                      Config file to use (default "/home/runner/.kommander/config")
      --context string                     The name of the kubeconfig context to use
      --core-app-timeout duration          Timeout to wait for upgrade of each kommander core application (default 20m0s)
      --dry-run                            Do not upgrade, just list the operations that would be performed
  -h, --help                               Help for platform-apps
      --kubeconfig string                  Path to the kubeconfig file to use for CLI requests.
      --platform-apps-timeout duration     Timeout to wait for upgrade of the set of platform applications (default 1h0m0s)
      --request-timeout string             The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int                        Output verbosity
      --version string                     Target NKP platform version to upgrade to
      --workspace string                   Workspace containing the target NKPCluster
```
