# `nkp update controlplane`

```text
Update a Kubernetes cluster control plane, one of [aks, aws, azure, gcp, nutanix, preprovisioned, vsphere]

Usage:
  nkp update controlplane [command]

Available Commands:
  aks            Update a Kubernetes cluster control plane in AKS
  aws            Update a Kubernetes cluster control plane in AWS
  azure          Update a Kubernetes cluster control plane in Azure
  gcp            Update a Kubernetes cluster control plane in GCP
  nutanix        Update a Kubernetes cluster control plane in Nutanix
  preprovisioned Update a Kubernetes cluster control plane in Preprovisioned
  vsphere        Update a Kubernetes cluster control plane in vSphere

Flags:
  -h, --help   Help for controlplane

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp update controlplane [command] --help" for more information about a command.
```

## Subcommands

### `nkp update controlplane aks`

```text
Update a Kubernetes cluster control plane in AKS

Usage:
  nkp update controlplane aks [flags]

Flags:
  -c, --cluster-name name           Name used to prefix the cluster and all the created resources.
  -h, --help                        Help for aks
      --kubeconfig string           Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string   Kubernetes version
  -n, --namespace string            If present, the namespace scope for this CLI request. (default "default")
      --timeout duration            The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string          Use a specific context in a kubeconfig file.
      --wait                        If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update controlplane aws`

```text
Update a Kubernetes cluster control plane in AWS

Usage:
  nkp update controlplane aws [flags]

Flags:
      --ami string                                      AMI ID to use for machines
      --ami-base-os string                              Base OS used in search of AMIs. Examples: 'ubuntu-22.04'
      --ami-format string                               Query string used in search of AMIs. Example: When --ami-base-os='rhel8.10', then the string 'prefix-{{.BaseOS}}-?{{.K8sVersion}}-*' matches any AMIs with the Name 'prefix-rhel8.10-1.35.2
      --ami-owner string                                ID of AWS account used in search of AMIs
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
  -h, --help                                            Help for aws
      --instance-type string                            Instance type to use for control plane machines
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string                       Kubernetes version
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                              Use a specific context in a kubeconfig file.
      --wait                                            If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update controlplane azure`

```text
Update a Kubernetes cluster control plane in Azure

Usage:
  nkp update controlplane azure [flags]

Flags:
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --compute-gallery-id string                       Compute Gallery ID of a custom image, e.g., '/subscriptions/<subscription id>/resourceGroups/<resource group name>/providers/Microsoft.Compute/galleries/<gallery name>/images/<image definition name>/versions/<version id>' (replacing placeholders with the values used when creating the image)
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
  -h, --help                                            Help for azure
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string                       Kubernetes version
      --machine-size string                             Worker machine size (ex. 'Standard_D2s_v3')
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --plan-offer string                               The offer for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --plan-publisher string                           The publisher for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --plan-sku string                                 The SKU for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                              Use a specific context in a kubeconfig file.
      --wait                                            If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update controlplane gcp`

```text
Update a Kubernetes cluster control plane in GCP

Usage:
  nkp update controlplane gcp [flags]

Flags:
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
  -h, --help                                            Help for gcp
      --image string                                    Full reference to an image to use for all nodes (set either this or --image-family) (ex. 'projects/my-project/global/images/konvoy-ubuntu-2204-1-99-99-1234567890')
      --image-family string                             Full reference to an image family to use for all nodes (set either this or --image) (ex. 'projects/my-project/global/images/family/nkp-ubuntu-2204-{{.K8sVersion}}')
      --instance-type string                            Control Plane machine instance type (ex. "n2-standard-4")
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string                       Kubernetes version
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                              Use a specific context in a kubeconfig file.
      --wait                                            If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update controlplane nutanix`

```text
Update a Kubernetes cluster control plane in Nutanix

Usage:
  nkp update controlplane nutanix [flags]

Flags:
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
  -h, --help                                            Help for nutanix
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                              Use a specific context in a kubeconfig file.
      --wait                                            If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update controlplane preprovisioned`

```text
Update a Kubernetes cluster control plane in Preprovisioned

Usage:
  nkp update controlplane preprovisioned [flags]

Flags:
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
  -h, --help                                            Help for preprovisioned
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string                       Kubernetes version
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                              Use a specific context in a kubeconfig file.
      --wait                                            If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp update controlplane vsphere`

```text
Update a Kubernetes cluster control plane in vSphere

Usage:
  nkp update controlplane vsphere [flags]

Flags:
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
      --cpus int                                        The number of virtual processors in a virtual machine.
      --disk-size int                                   The size of a virtual machine's disk, in GB.
  -h, --help                                            Help for vsphere
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string                       Kubernetes version
      --memory int                                      The size of a virtual machine's memory, in GB.
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --use-context string                              Use a specific context in a kubeconfig file.
      --vm-template string                              The virtual machine template to use for a virtual machine.
      --wait                                            If true, wait for operations to complete before returning. (default true)

Global Flags:
  -v, --verbose int   Output verbosity
```
