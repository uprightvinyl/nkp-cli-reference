# `nkp upgrade kommander`

```text
Upgrades all Kommander components and platform applications running on the targeted cluster. No attached clusters and applications running on them are affected by this action.

Usage:
  nkp upgrade kommander [flags]

Flags:
      --allow-gitrepository-catalog-apps           Allow upgrade to proceed when deprecated GitRepository-based catalog apps are detected
      --config string                              Config file to use (default "/home/runner/.kommander/config")
      --context string                             The name of the kubeconfig context to use
      --core-app-timeout duration                  Timeout to wait for upgrade of each kommander core application (default 20m0s)
      --disable-appdeployments strings             List of AppDeployments to be disabled during upgrade (default [])
  -h, --help                                       Help for kommander
      --kommander-applications-repository string   git repository with application definitions (default "v2.18.0")
      --kubeconfig string                          Path to the kubeconfig file to use for CLI requests.
      --platform-apps-timeout duration             Timeout to wait for upgrade of the set of platform applications (default 1h0m0s)
      --request-timeout string                     The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int                                Output verbosity
```
