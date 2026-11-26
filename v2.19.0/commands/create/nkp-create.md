# `nkp create`

```text
Create one of [appdeployment, bootstrap, bootstrap-token, bundle, capi-components, catalog-app, catalog-bundle, cluster, image, metadata, nodepool, package-bundle, project, workspace]

Usage:
  nkp create [command]

Available Commands:
  appdeployment   Create an AppDeployment
  bootstrap       Create bootstrap cluster
  bootstrap-token Create a bootstrap token for the NKP host agent
  bundle          Create a bundle containing container images and/or Helm charts
  capi-components Create the CAPI components in the cluster
  catalog-app     Create a catalog application or collection in project or workspace namespace
  catalog-bundle  Bundle up the catalog application(s) including container images & any OCI artifacts
  cluster         Cluster one of [aks, aws, azure, eks, gcp, metal, nutanix, preprovisioned, vsphere]
  image           Create Operating System image for one of [aws, azure, gcp, nutanix, preprovisioned, vsphere]
  metadata        Create a infrastructure metadata, one of [nutanix]
  nodepool        Nodepool one of [aks, aws, azure, eks, gcp, metal, nutanix, preprovisioned, vsphere]
  package-bundle  Create Operating System package bundle for one of [oracle-8.9, oracle-9.4, rhel-8.10, rhel-9.6, rhel-9.8, rocky-9.8, ubuntu-22.04, ubuntu-24.04]
  project         Create a Project
  workspace       Create a Workspace

Flags:
  -h, --help   Help for create

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp create [command] --help" for more information about a command.
```

## Subcommands

- [`nkp create appdeployment`](appdeployment/nkp-create-appdeployment.md)
- [`nkp create bootstrap`](bootstrap/nkp-create-bootstrap.md)
- [`nkp create bootstrap-token`](bootstrap-token/nkp-create-bootstrap-token.md)
- [`nkp create bundle`](bundle/nkp-create-bundle.md)
- [`nkp create capi-components`](capi-components/nkp-create-capi-components.md)
- [`nkp create catalog-app`](catalog-app/nkp-create-catalog-app.md)
- [`nkp create catalog-bundle`](catalog-bundle/nkp-create-catalog-bundle.md)
- [`nkp create cluster`](cluster/nkp-create-cluster.md)
- [`nkp create image`](image/nkp-create-image.md)
- [`nkp create metadata`](metadata/nkp-create-metadata.md)
- [`nkp create nodepool`](nodepool/nkp-create-nodepool.md)
- [`nkp create package-bundle`](package-bundle/nkp-create-package-bundle.md)
- [`nkp create project`](project/nkp-create-project.md)
- [`nkp create workspace`](workspace/nkp-create-workspace.md)
