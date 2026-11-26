# `nkp experimental gitops`

```text
commands to interact with NKP's Gitops Host

Usage:
  nkp experimental gitops [command]

Available Commands:
  clone       clone a repo hosted on NKP Gitops system

Flags:
      --config string            Config file to use (default "/home/runner/.kommander/config")
      --context string           The name of the kubeconfig context to use
  -h, --help                     Help for gitops
      --kubeconfig string        Path to the kubeconfig file to use for CLI requests.
      --request-timeout string   The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int              Output verbosity

Use "nkp experimental gitops [command] --help" for more information about a command.
```

## Subcommands

### `nkp experimental gitops clone`

```text
clone a repo hosted on NKP Gitops system

Usage:
  nkp experimental gitops clone [flags]

Flags:
      --git-claim-user-name string        Name of the GitClaimUser (GitClaim will be deduced from GitClaimUser) (default "kommander")
      --git-claim-user-namespace string   Namespace of the GitClaimUser (GitClaim will be deduced from GitClaimUser) (default "kommander")
  -h, --help                              Help for clone
      --output-dir string                 Output path to clone the repo

Global Flags:
      --config string            Config file to use (default "/home/runner/.kommander/config")
      --context string           The name of the kubeconfig context to use
      --kubeconfig string        Path to the kubeconfig file to use for CLI requests.
      --request-timeout string   The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int              Output verbosity
```
