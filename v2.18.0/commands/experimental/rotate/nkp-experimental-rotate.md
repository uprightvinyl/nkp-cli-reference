# `nkp experimental rotate`

```text
commands to rotate passwords

Usage:
  nkp experimental rotate [command]

Available Commands:
  dashboard-password rotate the dashboard password

Flags:
      --config string            Config file to use (default "/home/runner/.kommander/config")
      --context string           The name of the kubeconfig context to use
  -h, --help                     Help for rotate
      --kubeconfig string        Path to the kubeconfig file to use for CLI requests.
      --request-timeout string   The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int              Output verbosity

Use "nkp experimental rotate [command] --help" for more information about a command.
```

## Subcommands

### `nkp experimental rotate dashboard-password`

```text
rotate the dashboard password

Usage:
  nkp experimental rotate dashboard-password [flags]

Flags:
  -h, --help   Help for dashboard-password

Global Flags:
      --config string            Config file to use (default "/home/runner/.kommander/config")
      --context string           The name of the kubeconfig context to use
      --kubeconfig string        Path to the kubeconfig file to use for CLI requests.
      --request-timeout string   The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int              Output verbosity
```
