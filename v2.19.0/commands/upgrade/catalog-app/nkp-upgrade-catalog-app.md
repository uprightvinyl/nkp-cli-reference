# `nkp upgrade catalog-app`

```text
Upgrade a Catalog Application to a newer version

Usage:
  nkp upgrade catalog-app CATALOGAPP_NAME --to-version VERSION [--workspace WORKSPACE | --project PROJECT] [flags]

Aliases:
  catalog-app, catalogapp

Flags:
      --allow-gitrepository-catalog-apps   Allow upgrade to proceed when deprecated GitRepository-based catalog apps are detected
      --config string                      Config file to use (default "/home/runner/.kommander/config")
      --context string                     The name of the kubeconfig context to use
      --core-app-timeout duration          Timeout to wait for upgrade of each kommander core application (default 20m0s)
  -h, --help                               Help for catalog-app
      --kubeconfig string                  Path to the kubeconfig file to use for CLI requests.
      --platform-apps-timeout duration     Timeout to wait for upgrade of the set of platform applications (default 1h0m0s)
      --project string                     Name of the Project to upgrade the Catalog App in
      --request-timeout string             The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
      --to-version string                  Version the Catalog App should be upgraded to
  -v, --verbose int                        Output verbosity
  -w, --workspace string                   Name of the Workspace to upgrade the Catalog App in
```
