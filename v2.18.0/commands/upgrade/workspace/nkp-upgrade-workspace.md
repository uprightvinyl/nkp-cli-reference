# `nkp upgrade workspace`

```text
Upgrade all platform applications in the given workspace and its projects to the same version as platform applications running on the management cluster

Usage:
  nkp upgrade workspace WORKSPACE_NAME [--dry-run] [flags]

Flags:
      --allow-gitrepository-catalog-apps   Allow upgrade to proceed when deprecated GitRepository-based catalog apps are detected
      --config string                      Config file to use (default "/home/runner/.kommander/config")
      --context string                     The name of the kubeconfig context to use
      --core-app-timeout duration          Timeout to wait for upgrade of each kommander core application (default 20m0s)
      --disable-appdeployments strings     List of AppDeployments to be disabled during upgrade (default [])
      --dry-run                            Do not upgrade, just list the operation that would be performed
  -h, --help                               Help for workspace
      --kubeconfig string                  Path to the kubeconfig file to use for CLI requests.
      --platform-apps-timeout duration     Timeout to wait for upgrade of the set of platform applications (default 1h0m0s)
      --request-timeout string             The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int                        Output verbosity
```
