# `nkp get`

```text
Get one of [appdeployments, chart, clusters, dashboard, kubeconfig, nodepools, workspaces]

Usage:
  nkp get [command]

Available Commands:
  appdeployments Get AppDeployments from a Workspace, Project, or all Workspaces and Projects
  chart          Obtain information about charts stored in the repository
  clusters       Get clusters from specified Workspace
  dashboard      Show the UI URL and credentials
  kubeconfig     Retrieve cluster kubeconfig and modify local kubeconfig file
  nodepools      Get nodepools for a given cluster
  workspaces     Get Workspaces

Flags:
  -h, --help   Help for get

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp get [command] --help" for more information about a command.
```

## Subcommands

- [`nkp get chart`](chart/nkp-get-chart.md)
- [`nkp get clusters`](clusters/nkp-get-clusters.md)
- [`nkp get dashboard`](dashboard/nkp-get-dashboard.md)
- [`nkp get kubeconfig`](kubeconfig/nkp-get-kubeconfig.md)
- [`nkp get nodepools`](nodepools/nkp-get-nodepools.md)
- [`nkp get workspaces`](workspaces/nkp-get-workspaces.md)
