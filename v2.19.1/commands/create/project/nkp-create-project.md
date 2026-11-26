# `nkp create project`

```text
Create a Project

Usage:
  nkp create project PROJECT_NAME [flags]

Flags:
      --config string                Config file to use (default "/home/runner/.kommander/config")
      --context string               The name of the kubeconfig context to use
      --display-name string          Display name shown in the UI (defaults to PROJECT_NAME)
      --dry-run                      Export in YAML format to stdout
  -h, --help                         Help for project
      --kubeconfig string            Path to the kubeconfig file to use for CLI requests.
  -n, --namespace string             Optional namespace name to use for the project (immutable)
  -o, --output string                Output format. One of: yaml|json (default "yaml")
      --request-timeout string       The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.
  -v, --verbose int                  Output verbosity
  -w, --workspace string             Name of the Workspace the project belongs to
      --workspace-namespace string   Namespace backing the Workspace (where the Project CR is created). If empty, it will be looked up from the Workspace.
```
