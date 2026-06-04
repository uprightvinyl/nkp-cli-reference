# `nkp create nodepool`

```text
Create a nodepool, one of [aks, aws, azure, eks, gcp, nutanix, preprovisioned, vsphere]

Usage:
  nkp create nodepool [command]

Available Commands:
  aks            Create a nodepool in AKS.
  aws            Create a nodepool in AWS.
  azure          Create a nodepool in Azure.
  eks            Create a nodepool in EKS.
  gcp            Create a nodepool in GCP.
  nutanix        Create a nodepool in Nutanix.
  preprovisioned Create a nodepool in Preprovisioned.
  vsphere        Create a nodepool in vSphere.

Flags:
  -h, --help          Help for nodepool
  -v, --verbose int   Output verbosity

Use "nkp create nodepool [command] --help" for more information about a command.
```

## Subcommands

### `nkp create nodepool aks`

```text
Create a nodepool in AKS.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool aks NAME [flags]

Flags:
      --additional-tags stringToString   Tags to apply to the provisioned infrastructure (default [])
      --availability-zone string         The availability zone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. 1). Not all locations, including the default 'westus', support setting this flag, see https://docs.microsoft.com/en-us/azure/availability-zones/az-overview.
  -c, --cluster-name name                Name used to prefix the cluster and all the created resources.
      --dry-run                          Only print the objects that would be created, without creating them.
  -h, --help                             Help for aks
      --http-proxy string                HTTP proxy for nodes
      --https-proxy string               HTTPS proxy for nodes
      --kubeconfig string                Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string        Kubernetes version. Run 'az aks get-versions -o table --location <location>' to see available versions. See https://docs.microsoft.com/en-us/azure/aks/supported-kubernetes-versions for more details. Must be a patch version for v1.34.x.
      --machine-size string              Worker machine size (default "Standard_D8s_v3")
  -n, --namespace string                 If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                 No Proxy list for nodes (default [])
  -o, --output string                    Output format. One of: (json, yaml, name).
      --output-directory string          Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --replicas int32                   Number of replicas (default 1)
      --show-managed-fields              If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string       Path to the authorized SSH key for the user
      --ssh-username string              Name of the user to create on the instance (default "konvoy")
      --timeout duration                 The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                             If true, wait for operations to complete before returning.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create nodepool aws`

```text
Create a nodepool in AWS.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool aws NAME [flags]

Flags:
      --additional-security-group-ids strings   A comma separated list of existing security group IDs to use for machines in addition to those created automatically (default [])
      --additional-tags stringToString          Tags to apply to the provisioned infrastructure (default [])
      --ami string                              AMI ID to use for machines
      --ami-base-os string                      Base OS used in search of AMIs. Examples: 'ubuntu-22.04'
      --ami-format string                       Query string used in search of AMIs. Example: When --ami-base-os='rhel8.10', then the string 'prefix-{{.BaseOS}}-?{{.K8sVersion}}-*' matches any AMIs with the Name 'prefix-rhel8.10-1.34.3
      --ami-owner string                        ID of AWS account used in search of AMIs
      --availability-zone string                The AvailabilityZone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. us-west-2a)
  -c, --cluster-name name                       Name used to prefix the cluster and all the created resources.
      --dry-run                                 Only print the objects that would be created, without creating them.
  -h, --help                                    Help for aws
      --http-proxy string                       HTTP proxy for nodes
      --https-proxy string                      HTTPS proxy for nodes
      --iam-instance-profile string             Name of the IAM instance profile to assign to worker machines. (default "nodes.cluster-api-provider-aws.sigs.k8s.io")
      --instance-type string                    Worker machine instance type (default "m5.2xlarge")
      --kubeconfig string                       Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string               Kubernetes version (default "1.34.3")
  -n, --namespace string                        If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                        No Proxy list for nodes (default [])
      --os-hint flatcar                         A hint which will allow the installer to generate appropriate configurations for a target OS. Presently, only the hint for flatcar is supported.
  -o, --output string                           Output format. One of: (json, yaml, name).
      --output-directory string                 Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --registry-mirror-cacert file             Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string         Password used to authenticate with the registry mirror
      --registry-mirror-url url                 URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string         Username used to authenticate with the registry mirror
      --replicas int32                          Number of replicas (default 1)
      --show-managed-fields                     If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string              Path to the authorized SSH key for the user
      --ssh-username string                     Name of the user to create on the instance (default "konvoy")
      --timeout duration                        The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                                    If true, wait for operations to complete before returning.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create nodepool azure`

```text
Create a nodepool in Azure.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool azure NAME [flags]

Flags:
      --additional-tags stringToString    Tags to apply to the provisioned infrastructure (default [])
      --availability-zone string          The availability zone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. 1). Not all locations, including the default 'westus', support setting this flag, see https://docs.microsoft.com/en-us/azure/availability-zones/az-overview.
  -c, --cluster-name name                 Name used to prefix the cluster and all the created resources.
      --compute-gallery-id string         Compute Gallery ID of a custom image, e.g., '/subscriptions/<subscription id>/resourceGroups/<resource group name>/providers/Microsoft.Compute/galleries/<gallery name>/images/<image definition name>/versions/<version id>' (replacing placeholders with the values used when creating the image)
      --dry-run                           Only print the objects that would be created, without creating them.
  -h, --help                              Help for azure
      --http-proxy string                 HTTP proxy for nodes
      --https-proxy string                HTTPS proxy for nodes
      --kubeconfig string                 Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string         Kubernetes version (default "1.34.3")
      --machine-size string               Worker machine size (default "Standard_D8s_v3")
  -n, --namespace string                  If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                  No Proxy list for nodes (default [])
  -o, --output string                     Output format. One of: (json, yaml, name).
      --output-directory string           Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --plan-offer string                 The offer for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --plan-publisher string             The publisher for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --plan-sku string                   The SKU for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --registry-mirror-cacert file       Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string   Password used to authenticate with the registry mirror
      --registry-mirror-url url           URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string   Username used to authenticate with the registry mirror
      --replicas int32                    Number of replicas (default 1)
      --show-managed-fields               If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string        Path to the authorized SSH key for the user
      --ssh-username string               Name of the user to create on the instance (default "konvoy")
      --timeout duration                  The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                              If true, wait for operations to complete before returning.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create nodepool eks`

```text
Create a nodepool in EKS.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool eks NAME [flags]

Flags:
      --additional-security-group-ids strings   A comma separated list of existing security group IDs to use for machines in addition to those created automatically (default [])
      --additional-tags stringToString          Tags to apply to the provisioned infrastructure (default [])
      --availability-zone string                The AvailabilityZone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. us-west-2a)
  -c, --cluster-name name                       Name used to prefix the cluster and all the created resources.
      --dry-run                                 Only print the objects that would be created, without creating them.
  -h, --help                                    Help for eks
      --http-proxy string                       HTTP proxy for nodes
      --https-proxy string                      HTTPS proxy for nodes
      --iam-instance-profile string             Name of the IAM instance profile to assign to worker machines. (default "nodes.cluster-api-provider-aws.sigs.k8s.io")
      --instance-type string                    Worker machine instance type (default "m5.2xlarge")
      --kubeconfig string                       Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string               Kubernetes version (default "1.34.0")
  -n, --namespace string                        If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                        No Proxy list for nodes (default [])
  -o, --output string                           Output format. One of: (json, yaml, name).
      --output-directory string                 Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --placement-group string                  AWS Placement group to deploy the worker machines to. The placement group must already exist.
      --registry-mirror-cacert file             Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string         Password used to authenticate with the registry mirror
      --registry-mirror-url url                 URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string         Username used to authenticate with the registry mirror
      --replicas int32                          Number of replicas (default 1)
      --show-managed-fields                     If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string              Path to the authorized SSH key for the user
      --ssh-username string                     Name of the user to create on the instance (default "konvoy")
      --timeout duration                        The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                                    If true, wait for operations to complete before returning.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create nodepool gcp`

```text
Create a nodepool in GCP.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool gcp NAME [flags]

Flags:
      --additional-tags stringToString    Tags to apply to the provisioned infrastructure (default [])
      --associate-public-ip-address       Associate a public IP for all machines. When set to false the specified network must have Cloud NAT configured to provide internet access. (default true)
  -c, --cluster-name name                 Name used to prefix the cluster and all the created resources.
      --dry-run                           Only print the objects that would be created, without creating them.
  -h, --help                              Help for gcp
      --http-proxy string                 HTTP proxy for nodes
      --https-proxy string                HTTPS proxy for nodes
      --image string                      Full reference to an image to use for all nodes (set either this or --image-family) (ex. 'projects/my-project/global/images/konvoy-ubuntu-2204-1-99-99-1234567890')
      --image-family string               Full reference to an image family to use for all nodes (set either this or --image) (ex. 'projects/my-project/global/images/family/nkp-ubuntu-2204-{{.K8sVersion}}')
      --instance-type string              Worker machine instance type (default "n2-standard-8")
      --kubeconfig string                 Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string         Kubernetes version (default "1.34.3")
  -n, --namespace string                  If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                  No Proxy list for nodes (default [])
  -o, --output string                     Output format. One of: (json, yaml, name).
      --output-directory string           Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --registry-mirror-cacert file       Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string   Password used to authenticate with the registry mirror
      --registry-mirror-url url           URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string   Username used to authenticate with the registry mirror
      --replicas int32                    Number of replicas (default 1)
      --service-account-email string      Worker machine Service Account email address (default "default")
      --show-managed-fields               If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string        Path to the authorized SSH key for the user
      --ssh-username string               Name of the user to create on the instance (default "konvoy")
      --timeout duration                  The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                              If true, wait for operations to complete before returning.
      --zone string                       Zone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. us-west1-a)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create nodepool nutanix`

```text
Create a nodepool in Nutanix.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool nutanix NAME [flags]

Flags:
  -c, --cluster-name name              Name used to prefix the cluster and all the created resources.
      --cores-per-vcpu int32           The number of cores per vCPU(equivalent to CPU cores) to use in a worker machine (default 1)
      --disk-size int32                The size of the primary disk (in GiB) of a worker machine (default 80)
      --dry-run                        Only print the objects that would be created, without creating them.
      --gpu-count int32                Number of GPUs per VM in the nodepool. (default 1)
      --gpu-name string                Name of the GPU resource. Can be either vGPU profile or name of passthrough GPU.
  -h, --help                           Help for nutanix
      --kubeconfig string              Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string      Kubernetes version (default "1.34.3")
      --memory int32                   The size of memory (in GiB) of a worker machine (default 32)
  -n, --namespace string               If present, the namespace scope for this CLI request. (default "default")
  -o, --output string                  Output format. One of: (json, yaml, name).
      --output-directory string        Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --pc-categories strings          Names of Prism Central categories to associate with worker resources (VMs, VGs, etc). Example: key1=value1,key1=value2,key2=value2 (default [])
      --pc-project string              Name of Prism Central project to associate with worker resources (VMs, VGs, etc).
      --prism-element-cluster string   Name of the Prism Element cluster to use to create a worker machine
      --replicas int32                 Number of replicas (default 1)
      --show-managed-fields            If true, keep the managedFields when printing objects in JSON or YAML format.
      --subnets strings                Names of Prism Central subnets to use for worker machines. Example: subnet1,subnet2,subnet3 (default [])
      --timeout duration               The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --vcpus int32                    The number of vCPUs(equivalent to CPU sockets) to use in a worker machine (default 8)
      --vm-image string                Name of OS image to use for worker machines.
      --wait                           If true, wait for operations to complete before returning.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create nodepool vsphere`

```text
Create a nodepool in vSphere.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp create nodepool vsphere NAME [flags]

Flags:
      --additional-tags stringToString    Tags to apply to the provisioned infrastructure (default [])
  -c, --cluster-name name                 Name used to prefix the cluster and all the created resources.
      --cpus int                          The number of virtual processors in a worker machine (default 8)
      --data-center string                The vSphere datacenter to deploy the workload cluster on.
      --data-store string                 The vSphere datastore to deploy the workload cluster on.
      --disk-size int                     The size of a worker machine's disk, in GB (default 80)
      --dry-run                           Only print the objects that would be created, without creating them.
      --folder string                     The vSphere folder for your VMs. Set to "" to use the root vSphere folder.
  -h, --help                              Help for vsphere
      --http-proxy string                 HTTP proxy for nodes
      --https-proxy string                HTTPS proxy for nodes
      --kubeconfig string                 Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-version string         Kubernetes version (default "1.34.3")
      --memory int                        The size of a worker machine's memory, in GB (default 32)
  -n, --namespace string                  If present, the namespace scope for this CLI request. (default "default")
      --network string                    The vSphere network to deploy the workload cluster on.
      --no-proxy strings                  No Proxy list for nodes (default [])
      --os-hint flatcar                   A hint which will allow the installer to generate appropriate configurations for a target OS. Presently, only the hint for flatcar is supported.
  -o, --output string                     Output format. One of: (json, yaml, name).
      --output-directory string           Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --registry-mirror-cacert file       Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string   Password used to authenticate with the registry mirror
      --registry-mirror-url url           URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string   Username used to authenticate with the registry mirror
      --replicas int32                    Number of replicas (default 1)
      --resource-pool string              The vSphere resource pool for the workload cluster's virtual machines.
      --server string                     The vCenter server address. Accepted formats: host, host:port, http[s]://host[:port]. Accepted host formats: IPv4, IPv6, or DNS name.
      --show-managed-fields               If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string        Path to the authorized SSH key for the user
      --ssh-username string               Name of the user to create on the instance (default "konvoy")
      --storage-policy string             This is the vSphere storage policy. Set it to "" if you don't want to use a storage policy.
      --timeout duration                  The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --tls-thumb-print string            sha1 thumbprint of the vcenter certificate: openssl x509 -sha1 -fingerprint -in ca.crt -noout
      --vm-template string                The virtual machine template to use for the workload cluster's virtual machines.
      --wait                              If true, wait for operations to complete before returning.

Global Flags:
  -v, --verbose int   Output verbosity
```
