# `nkp create cluster`

```text
Create a Kubernetes cluster, one of [aks, aws, azure, eks, gcp, nutanix, preprovisioned, vsphere]

Usage:
  nkp create cluster [command]

Available Commands:
  aks            Create a Konvoy cluster in AKS
  aws            Create a Konvoy cluster in AWS
  azure          Create a Konvoy cluster in Azure
  eks            Create a Konvoy cluster in EKS
  gcp            Create a Konvoy cluster in GCP
  nutanix        Create a Konvoy cluster in Nutanix
  preprovisioned Create a Konvoy cluster on pre-provisioned infrastructure
  vsphere        Create a Konvoy cluster in vSphere

Flags:
  -h, --help          Help for cluster
  -v, --verbose int   Output verbosity

Use "nkp create cluster [command] --help" for more information about a command.
```

## Subcommands

### `nkp create cluster aks`

```text
Create a Konvoy cluster in AKS

Usage:
  nkp create cluster aks [flags]

Flags:
      --additional-tags stringToString     Tags to apply to the provisioned infrastructure (default [])
  -c, --cluster-name name                  Name used to prefix the cluster and all the created resources.
      --dry-run                            Only print the objects that would be created, without creating them.
  -h, --help                               Help for aks
      --kubeconfig string                  Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-pod-network-cidr cidr   The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr       The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string          Kubernetes version. Run 'az aks get-versions -o table --location <location>' to see available versions. See https://docs.microsoft.com/en-us/azure/aks/supported-kubernetes-versions for more details. Must be a patch version for v1.34.x.
      --location string                    Azure location to deploy cluster to (default "westus")
  -n, --namespace string                   If present, the namespace scope for this CLI request. (default "default")
  -o, --output string                      Output format. One of: (json, yaml, name).
      --output-directory string            Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields                If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string         Path to the authorized SSH key for the user
      --ssh-username string                Name of the user to create on the instance (default "konvoy")
      --system-machine-size string         System node pool machine size (default "Standard_D4s_v3")
      --system-replicas int32              Number of system nodes (default 3)
      --timeout duration                   The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                               If true, wait for operations to complete before returning. (default true)
      --worker-availability-zone string    The availability zone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. 1). Not all locations, including the default 'westus', support setting this flag, see https://docs.microsoft.com/en-us/azure/availability-zones/az-overview.
      --worker-http-proxy string           HTTP proxy for nodes
      --worker-https-proxy string          HTTPS proxy for nodes
      --worker-machine-size string         Worker machine size (default "Standard_D8s_v3")
      --worker-no-proxy strings            No Proxy list for nodes (default [])
      --worker-replicas int32              Number of workers (default 4)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create cluster aws`

```text
Create a Konvoy cluster in AWS

Usage:
  nkp create cluster aws [flags]

Flags:
      --additional-security-group-ids strings           A comma separated list of existing security group IDs to use for machines in addition to those created automatically (default [])
      --additional-tags stringToString                  Tags to apply to the provisioned infrastructure (default [])
      --ami string                                      AMI ID to use for machines
      --ami-base-os string                              Base OS used in search of AMIs. Examples: 'ubuntu-22.04'
      --ami-format string                               Query string used in search of AMIs. Example: When --ami-base-os='rhel8.10', then the string 'prefix-{{.BaseOS}}-?{{.K8sVersion}}-*' matches any AMIs with the Name 'prefix-rhel8.10-1.34.3
      --ami-owner string                                ID of AWS account used in search of AMIs
      --aws-service-endpoints string                    Custom AWS service endpoints in a semi-colon separated format: ${SigningRegion1}:${ServiceID1}=${URL},${ServiceID2}=${URL};${SigningRegion2}...
      --bootstrap-cluster-image string                  Container image used to create the bootstrap cluster. Can be an image name or path to a file, e.g., ./nkp-v2.17.1/konvoy-bootstrap-image-v2.17.1.tar. If not provided, the default image will be used (default "docker.io/mesosphere/konvoy-bootstrap:v2.17.1")
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-http-proxy string                 HTTP proxy for control plane machines
      --control-plane-https-proxy string                HTTPS proxy for control plane machines
      --control-plane-iam-instance-profile string       Name of the IAM instance profile to assign to control plane machines. (default "control-plane.cluster-api-provider-aws.sigs.k8s.io")
      --control-plane-instance-type string              Control Plane machine instance type (default "m5.xlarge")
      --control-plane-no-proxy strings                  No Proxy list for control plane machines (default [])
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
      --control-plane-replicas int32                    Number of control plane nodes (default 3)
      --dry-run                                         Only print the objects that would be created, without creating them.
      --etcd-image-repository string                    The image repository to use for pulling the etcd image
      --etcd-version string                             The version of etcd to use.
      --extra-sans strings                              A comma separated list of additional Subject Alternative Names for the API Server signing cert (default [])
  -h, --help                                            Help for aws
      --http-proxy string                               HTTP proxy for CAPI controllers
      --https-proxy string                              HTTPS proxy for CAPI controllers
      --internal-load-balancer                          Make the control plane load balancer internal, i.e., reachable only within the VPC.
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply. This flag is ignored if used with the --self-managed flag.
      --kubernetes-image-repository string              The image repository to use for pulling kubernetes images
      --kubernetes-pod-network-cidr cidr                The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr                    The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string                       Kubernetes version (default "1.34.3")
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                                No Proxy list for CAPI controllers (default [])
      --os-hint flatcar                                 A hint which will allow the installer to generate appropriate configurations for a target OS. Presently, only the hint for flatcar is supported.
  -o, --output string                                   Output format. One of: (json, yaml, name).
      --output-directory string                         Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --region string                                   AWS region to deploy cluster to (default "us-west-2")
      --registry-mirror-cacert file                     Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string                 Password used to authenticate with the registry mirror
      --registry-mirror-url url                         URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string                 Username used to authenticate with the registry mirror
      --self-managed                                    When set to true, the required prerequisites are created before creating the cluster and the resulting cluster has all necessary components deployed onto itself, so it can manage its own cluster lifecycle. When set to false, a management cluster is used. (default false)
      --show-managed-fields                             If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string                      Path to the authorized SSH key for the user
      --ssh-username string                             Name of the user to create on the instance (default "konvoy")
      --subnet-ids strings                              A comma separated list of existing subnet IDs to use for the kube-apiserver ELB and all control-plane and worker nodes (default [])
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --vpc-id string                                   Existing VPC ID to use for the cluster
      --wait                                            If true, wait for operations to complete before returning. This flag is ignored and will always be 'true' if used with the --self-managed flag. (default true)
      --with-aws-bootstrap-credentials                  Set true to use AWS bootstrap credentials from your environment. When false, the instance profile of the EC2 instance where the CAPA controller is scheduled on will be used instead.
      --with-gcp-bootstrap-credentials                  Set true to use GCP bootstrap credentials from your environment. When false, the service account of the VM instance where the CAPG controller is scheduled on will be used instead.
      --worker-availability-zone string                 The AvailabilityZone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. us-west-2a)
      --worker-http-proxy string                        HTTP proxy for nodes
      --worker-https-proxy string                       HTTPS proxy for nodes
      --worker-iam-instance-profile string              Name of the IAM instance profile to assign to worker machines. (default "nodes.cluster-api-provider-aws.sigs.k8s.io")
      --worker-instance-type string                     Worker machine instance type (default "m5.2xlarge")
      --worker-no-proxy strings                         No Proxy list for nodes (default [])
      --worker-replicas int32                           Number of workers (default 4)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create cluster azure`

```text
Create a Konvoy cluster in Azure

Usage:
  nkp create cluster azure [flags]

Flags:
      --additional-tags stringToString                  Tags to apply to the provisioned infrastructure (default [])
      --aws-service-endpoints string                    Custom AWS service endpoints in a semi-colon separated format: ${SigningRegion1}:${ServiceID1}=${URL},${ServiceID2}=${URL};${SigningRegion2}...
      --bootstrap-cluster-image string                  Container image used to create the bootstrap cluster. Can be an image name or path to a file, e.g., ./nkp-v2.17.1/konvoy-bootstrap-image-v2.17.1.tar. If not provided, the default image will be used (default "docker.io/mesosphere/konvoy-bootstrap:v2.17.1")
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --compute-gallery-id string                       Compute Gallery ID of a custom image, e.g., '/subscriptions/<subscription id>/resourceGroups/<resource group name>/providers/Microsoft.Compute/galleries/<gallery name>/images/<image definition name>/versions/<version id>' (replacing placeholders with the values used when creating the image)
      --control-plane-http-proxy string                 HTTP proxy for control plane machines
      --control-plane-https-proxy string                HTTPS proxy for control plane machines
      --control-plane-machine-size string               Control Plane machine size (default "Standard_D4s_v3")
      --control-plane-no-proxy strings                  No Proxy list for control plane machines (default [])
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
      --control-plane-replicas int32                    Number of control plane nodes (default 3)
      --dry-run                                         Only print the objects that would be created, without creating them.
      --etcd-image-repository string                    The image repository to use for pulling the etcd image
      --etcd-version string                             The version of etcd to use.
      --extra-sans strings                              A comma separated list of additional Subject Alternative Names for the API Server signing cert (default [])
  -h, --help                                            Help for azure
      --http-proxy string                               HTTP proxy for CAPI controllers
      --https-proxy string                              HTTPS proxy for CAPI controllers
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply. This flag is ignored if used with the --self-managed flag.
      --kubernetes-image-repository string              The image repository to use for pulling kubernetes images
      --kubernetes-pod-network-cidr cidr                The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr                    The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string                       Kubernetes version (default "1.34.3")
      --location string                                 Azure location to deploy cluster to (default "westus")
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                                No Proxy list for CAPI controllers (default [])
  -o, --output string                                   Output format. One of: (json, yaml, name).
      --output-directory string                         Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --plan-offer string                               The offer for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --plan-publisher string                           The publisher for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --plan-sku string                                 The SKU for a Marketplace image or a custom image sourced from a Marketplace image requiring Plan information.
      --registry-mirror-cacert file                     Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string                 Password used to authenticate with the registry mirror
      --registry-mirror-url url                         URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string                 Username used to authenticate with the registry mirror
      --self-managed                                    When set to true, the required prerequisites are created before creating the cluster and the resulting cluster has all necessary components deployed onto itself, so it can manage its own cluster lifecycle. When set to false, a management cluster is used. (default false)
      --show-managed-fields                             If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string                      Path to the authorized SSH key for the user
      --ssh-username string                             Name of the user to create on the instance (default "konvoy")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                                            If true, wait for operations to complete before returning. This flag is ignored and will always be 'true' if used with the --self-managed flag. (default true)
      --with-aws-bootstrap-credentials                  Set true to use AWS bootstrap credentials from your environment. When false, the instance profile of the EC2 instance where the CAPA controller is scheduled on will be used instead.
      --with-gcp-bootstrap-credentials                  Set true to use GCP bootstrap credentials from your environment. When false, the service account of the VM instance where the CAPG controller is scheduled on will be used instead.
      --worker-availability-zone string                 The availability zone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. 1). Not all locations, including the default 'westus', support setting this flag, see https://docs.microsoft.com/en-us/azure/availability-zones/az-overview.
      --worker-http-proxy string                        HTTP proxy for nodes
      --worker-https-proxy string                       HTTPS proxy for nodes
      --worker-machine-size string                      Worker machine size (default "Standard_D8s_v3")
      --worker-no-proxy strings                         No Proxy list for nodes (default [])
      --worker-replicas int32                           Number of workers (default 4)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create cluster eks`

```text
Create a Konvoy cluster in EKS

Usage:
  nkp create cluster eks [flags]

Flags:
      --additional-security-group-ids strings   A comma separated list of existing security group IDs to use for machines in addition to those created automatically (default [])
      --additional-tags stringToString          Tags to apply to the provisioned infrastructure (default [])
  -c, --cluster-name name                       Name used to prefix the cluster and all the created resources.
      --dry-run                                 Only print the objects that would be created, without creating them.
  -h, --help                                    Help for eks
      --kubeconfig string                       Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-service-cidr cidr            The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string               Kubernetes version (default "1.34.0")
  -n, --namespace string                        If present, the namespace scope for this CLI request. (default "default")
  -o, --output string                           Output format. One of: (json, yaml, name).
      --output-directory string                 Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --region string                           AWS region to deploy cluster to (default "us-west-2")
      --registry-mirror-cacert file             Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string         Password used to authenticate with the registry mirror
      --registry-mirror-url url                 URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string         Username used to authenticate with the registry mirror
      --show-managed-fields                     If true, keep the managedFields when printing objects in JSON or YAML format.
      --subnet-ids strings                      A comma separated list of existing subnet IDs to use for the kube-apiserver ELB and all control-plane and worker nodes (default [])
      --timeout duration                        The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --vpc-id string                           Existing VPC ID to use for the cluster
      --wait                                    If true, wait for operations to complete before returning. (default true)
      --worker-availability-zone string         The AvailabilityZone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. us-west-2a)
      --worker-iam-instance-profile string      Name of the IAM instance profile to assign to worker machines. (default "nodes.cluster-api-provider-aws.sigs.k8s.io")
      --worker-instance-type string             Worker machine instance type (default "m5.2xlarge")
      --worker-placement-group string           AWS Placement group to deploy the worker machines to. The placement group must already exist.
      --worker-replicas int32                   Number of workers (default 4)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create cluster gcp`

```text
Create a Konvoy cluster in GCP

Usage:
  nkp create cluster gcp [flags]

Flags:
      --additional-tags stringToString                  Tags to apply to the provisioned infrastructure (default [])
      --associate-public-ip-address                     Associate a public IP for all machines. When set to false the specified network must have Cloud NAT configured to provide internet access. (default true)
      --aws-service-endpoints string                    Custom AWS service endpoints in a semi-colon separated format: ${SigningRegion1}:${ServiceID1}=${URL},${ServiceID2}=${URL};${SigningRegion2}...
      --bootstrap-cluster-image string                  Container image used to create the bootstrap cluster. Can be an image name or path to a file, e.g., ./nkp-v2.17.1/konvoy-bootstrap-image-v2.17.1.tar. If not provided, the default image will be used (default "docker.io/mesosphere/konvoy-bootstrap:v2.17.1")
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-http-proxy string                 HTTP proxy for control plane machines
      --control-plane-https-proxy string                HTTPS proxy for control plane machines
      --control-plane-instance-type string              Control Plane machine instance type (default "n2-standard-4")
      --control-plane-no-proxy strings                  No Proxy list for control plane machines (default [])
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
      --control-plane-replicas int32                    Number of control plane nodes (default 3)
      --control-plane-service-account-email string      Control Plane Service Account email address (default "default")
      --dry-run                                         Only print the objects that would be created, without creating them.
      --etcd-image-repository string                    The image repository to use for pulling the etcd image
      --etcd-version string                             The version of etcd to use.
      --extra-sans strings                              A comma separated list of additional Subject Alternative Names for the API Server signing cert (default [])
  -h, --help                                            Help for gcp
      --http-proxy string                               HTTP proxy for CAPI controllers
      --https-proxy string                              HTTPS proxy for CAPI controllers
      --image string                                    Full reference to an image to use for all nodes (set either this or --image-family) (ex. 'projects/my-project/global/images/konvoy-ubuntu-2204-1-99-99-1234567890')
      --image-family string                             Full reference to an image family to use for all nodes (set either this or --image) (ex. 'projects/my-project/global/images/family/nkp-ubuntu-2204-{{.K8sVersion}}')
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply. This flag is ignored if used with the --self-managed flag.
      --kubernetes-image-repository string              The image repository to use for pulling kubernetes images
      --kubernetes-pod-network-cidr cidr                The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr                    The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string                       Kubernetes version (default "1.34.3")
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --network string                                  The GCP network name to deploy the cluster to (default "default")
      --no-proxy strings                                No Proxy list for CAPI controllers (default [])
  -o, --output string                                   Output format. One of: (json, yaml, name).
      --output-directory string                         Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --project string                                  The GCP project name to deploy the cluster to
      --region string                                   GCP region to deploy cluster to (default "us-west1")
      --registry-mirror-cacert file                     Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string                 Password used to authenticate with the registry mirror
      --registry-mirror-url url                         URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string                 Username used to authenticate with the registry mirror
      --self-managed                                    When set to true, the required prerequisites are created before creating the cluster and the resulting cluster has all necessary components deployed onto itself, so it can manage its own cluster lifecycle. When set to false, a management cluster is used. (default false)
      --show-managed-fields                             If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string                      Path to the authorized SSH key for the user
      --ssh-username string                             Name of the user to create on the instance (default "konvoy")
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --wait                                            If true, wait for operations to complete before returning. This flag is ignored and will always be 'true' if used with the --self-managed flag. (default true)
      --with-aws-bootstrap-credentials                  Set true to use AWS bootstrap credentials from your environment. When false, the instance profile of the EC2 instance where the CAPA controller is scheduled on will be used instead.
      --with-gcp-bootstrap-credentials                  Set true to use GCP bootstrap credentials from your environment. When false, the service account of the VM instance where the CAPG controller is scheduled on will be used instead.
      --worker-http-proxy string                        HTTP proxy for nodes
      --worker-https-proxy string                       HTTPS proxy for nodes
      --worker-instance-type string                     Worker machine instance type (default "n2-standard-8")
      --worker-no-proxy strings                         No Proxy list for nodes (default [])
      --worker-replicas int32                           Number of workers (default 4)
      --worker-service-account-email string             Worker machine Service Account email address (default "default")
      --worker-zone string                              Zone in the region to deploy the worker nodes to, if not set a random one will be selected (ex. us-west1-a)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create cluster nutanix`

```text
Create a Konvoy cluster in Nutanix

Usage:
  nkp create cluster nutanix [flags]

Flags:
      --acme-email string                                  Email address the ACME server can use to contact you.
      --acme-server string                                 Address of the ACME service issuing the certificates (default: Let's encrypt). (default "https://acme-v02.api.letsencrypt.org/directory")
      --additional-trust-bundle string                     Additional CA trust bundle to use to validate the Prism Central server certificate.
      --airgapped                                          Enable airgapped mode.
      --aws-service-endpoints string                       Custom AWS service endpoints in a semi-colon separated format: ${SigningRegion1}:${ServiceID1}=${URL},${ServiceID2}=${URL};${SigningRegion2}...
      --bootstrap-cluster-image string                     Container image used to create the bootstrap cluster. Can be an image name or path to a file, e.g., ./nkp-v2.17.1/konvoy-bootstrap-image-v2.17.1.tar. If not provided, the default image will be used (default "docker.io/mesosphere/konvoy-bootstrap:v2.17.1")
      --bundle files                                       A comma separated list of bundle artifacts that will be pushed to an in-cluster registry. Supports glob pattern to match multiple artifacts (e.g. ./bundles/*.tar). Following artifacts must be provided: konvoy-image-bundle-v2.17.1.tar, kommander-image-bundle-v2.17.1.tar (default [])
      --cluster-hostname string                            Hostname that is used for accessing the cluster's ingresses.
  -c, --cluster-name name                                  Name used to prefix the cluster and all the created resources.
      --control-plane-cores-per-vcpu int32                 The number of cores per vCPU(equivalent to CPU cores) to use in a control plane machine (default 1)
      --control-plane-disk-size int32                      The size of the primary disk (in GiB) of a control plane machine (default 80)
      --control-plane-endpoint-ip ip                       The control plane endpoint ip. Must be a static IPv4 address from the Layer 2 network of the control plane machines.
      --control-plane-endpoint-port int32                  The control plane endpoint port. (default 6443)
      --control-plane-external-endpoint string             The external control plane endpoint. A host that resolves to the endpoint IP. The host may be a Floating IPv4 address that maps to the control plane endpoint IP, or an FQDN that resolves to the control plane endpoint IP.
      --control-plane-memory int32                         The size of memory (in GiB) of a control plane machine (default 16)
      --control-plane-pc-categories strings                Names of Prism Central categories to associate with control plane resources (VMs, VGs, etc). Example: key1=value1,key1=value2,key2=value2 (default [])
      --control-plane-pc-project string                    Name of Prism Central project to associate with control plane resources (VMs, VGs, etc).
      --control-plane-prism-element-cluster string         Name of the Prism Element cluster to use to create a control plane machine
      --control-plane-renew-certificates-before int32      Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
      --control-plane-replicas int32                       Number of control plane nodes (default 3)
      --control-plane-subnets strings                      Names of Prism Central subnets to use for control plane machines. Example: subnet1,subnet2,subnet3 (default [])
      --control-plane-vcpus int32                          The number of vCPUs(equivalent to CPU sockets) to use in a control plane machine (default 4)
      --control-plane-vm-image string                      Name of OS image to use for control plane machines.
      --csi-file-system string                             File system to use for CSI volumes. Allowed values ["ext4" "xfs"]. (default "ext4")
      --csi-flash-mode                                     If true, will enable flash mode for CSI volumes.
      --csi-hypervisor-attached-volumes                    If true, will enable the hypervisor attached feature for CSI volumes which allows disks to attach directly to the host without using iSCSI. (default true)
      --csi-reclaim-policy string                          Reclaim policy for CSI volumes. Allowed values ["Delete" "Retain"]. (default "Delete")
      --csi-storage-container string                       Name of the Prism Central storage container to associate with the storage class created on the cluster.
      --dry-run                                            Only print the objects that would be created, without creating them.
      --endpoint url                                       Prism Central URL. Accepted formats: host, host:port, http[s]://host[:port]. Accepted host formats: IP, FQDN.
      --extra-sans strings                                 A comma separated list of additional Subject Alternative Names for the API Server signing cert (default [])
      --fips                                               Enable FIPS mode. Note: The OS images used by the cluster must be prepared with FIPS mode enabled.
  -h, --help                                               Help for nutanix
      --http-proxy string                                  HTTP proxy for all nodes in the cluster
      --https-proxy string                                 HTTPS proxy for all nodes in the cluster
      --ingress-ca file                                    Path to file containing the certificate's CA bundle.
      --ingress-certificate file                           Path to file containing certificates for configuring Ingress.
      --ingress-private-key file                           Path to file containing the certificate's private key (PEM).
      --insecure                                           If true, the Prism Central server certificate will not be validated.
      --kubeconfig string                                  Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply. This flag is ignored if used with the --self-managed flag.
      --kubernetes-pod-network-cidr cidr                   The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr                       The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-service-load-balancer-ip-range string   A hyphen separated IP range to configure the Kubernetes Service Load Balancer provider with. Example: 10.0.0.0-10.0.0.10
      --kubernetes-version string                          Kubernetes version (default "1.34.3")
  -n, --namespace string                                   If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                                   No Proxy list for all nodes in the cluster (default [])
      --ntp-servers strings                                A comma-separated list of NTP servers to configure on all nodes. Each entry must be a fully qualified domain name (FQDN) or an IP address (IPv4 or IPv6). This list overrides any default NTP settings preconfigured in the machine image. (default [])
      --onboard-to-prism-central                           Makes the cluster visible in the Prism Central in the infrastructure tab. (default true)
  -o, --output string                                      Output format. One of: (json, yaml, name).
      --output-directory string                            Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --registry-cacert file                               Path to file containing the CA certificate used to verify the registry server certificate
      --registry-mirror-cacert file                        Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string                    Password used to authenticate with the registry mirror
      --registry-mirror-url url                            URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string                    Username used to authenticate with the registry mirror
      --registry-password string                           Password used to authenticate with the registry
      --registry-url url                                   URL of a container registry
      --registry-username string                           Username used to authenticate with the registry
      --self-managed                                       When set to true, the required prerequisites are created before creating the cluster and the resulting cluster has all necessary components deployed onto itself, so it can manage its own cluster lifecycle. When set to false, a management cluster is used. (default false)
      --show-managed-fields                                If true, keep the managedFields when printing objects in JSON or YAML format.
      --skip-preflight-checks strings                      Skip preflight checks. Provide "all" to skip all checks, or a comma-separated list of check names. (default [])
      --ssh-public-key-file string                         Path to the authorized SSH key for the user
      --ssh-username string                                Name of the user to create on the instance (default "konvoy")
      --timeout duration                                   The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --vm-image string                                    Name of OS image to use for all machines.
      --wait                                               If true, wait for operations to complete before returning. This flag is ignored and will always be 'true' if used with the --self-managed flag. (default true)
      --with-aws-bootstrap-credentials                     Set true to use AWS bootstrap credentials from your environment. When false, the instance profile of the EC2 instance where the CAPA controller is scheduled on will be used instead.
      --with-gcp-bootstrap-credentials                     Set true to use GCP bootstrap credentials from your environment. When false, the service account of the VM instance where the CAPG controller is scheduled on will be used instead.
      --worker-cores-per-vcpu int32                        The number of cores per vCPU(equivalent to CPU cores) to use in a worker machine (default 1)
      --worker-disk-size int32                             The size of the primary disk (in GiB) of a worker machine (default 80)
      --worker-memory int32                                The size of memory (in GiB) of a worker machine (default 32)
      --worker-pc-categories strings                       Names of Prism Central categories to associate with worker resources (VMs, VGs, etc). Example: key1=value1,key1=value2,key2=value2 (default [])
      --worker-pc-project string                           Name of Prism Central project to associate with worker resources (VMs, VGs, etc).
      --worker-prism-element-cluster string                Name of the Prism Element cluster to use to create a worker machine
      --worker-replicas int32                              Number of workers (default 4)
      --worker-subnets strings                             Names of Prism Central subnets to use for worker machines. Example: subnet1,subnet2,subnet3 (default [])
      --worker-vcpus int32                                 The number of vCPUs(equivalent to CPU sockets) to use in a worker machine (default 8)
      --worker-vm-image string                             Name of OS image to use for worker machines.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create cluster vsphere`

```text
Create a Konvoy cluster in vSphere

Usage:
  nkp create cluster vsphere [flags]

Flags:
      --aws-service-endpoints string                    Custom AWS service endpoints in a semi-colon separated format: ${SigningRegion1}:${ServiceID1}=${URL},${ServiceID2}=${URL};${SigningRegion2}...
      --bootstrap-cluster-image string                  Container image used to create the bootstrap cluster. Can be an image name or path to a file, e.g., ./nkp-v2.17.1/konvoy-bootstrap-image-v2.17.1.tar. If not provided, the default image will be used (default "docker.io/mesosphere/konvoy-bootstrap:v2.17.1")
  -c, --cluster-name name                               Name used to prefix the cluster and all the created resources.
      --control-plane-cpus int                          The number of virtual processors in a control plane machine (default 4)
      --control-plane-disk-size int                     The size of a control plane machine's disk, in GB (default 80)
      --control-plane-endpoint-host string              The control plane endpoint address. To use an external load balancer, set to its IP or hostname. To use the built-in virtual IP, set to a static IPv4 address in the Layer 2 network of the control plane machines. [Not for production use: To use a single-machine control plane, set to the IP or hostname of the machine.]
      --control-plane-endpoint-port int32               The control plane endpoint port. To use an external load balancer, set to its listening port. (default 6443)
      --control-plane-http-proxy string                 HTTP proxy for control plane machines
      --control-plane-https-proxy string                HTTPS proxy for control plane machines
      --control-plane-memory int                        The size of a control plane machine's memory, in GB (default 16)
      --control-plane-no-proxy strings                  No Proxy list for control plane machines (default [])
      --control-plane-renew-certificates-before int32   Enables automated control-plane certificates renewal. Provide the number of days between 7 and 360 when to trigger the certificate renewal. The renewal process will trigger new control-plane Machines to be created. A value of 0 disables the feature. (default 180)
      --control-plane-replicas int32                    Number of control plane nodes (default 3)
      --data-center string                              The vSphere datacenter to deploy the workload cluster on.
      --data-store string                               The vSphere datastore to deploy the workload cluster on.
      --dry-run                                         Only print the objects that would be created, without creating them.
      --etcd-image-repository string                    The image repository to use for pulling the etcd image
      --etcd-version string                             The version of etcd to use.
      --extra-sans strings                              A comma separated list of additional Subject Alternative Names for the API Server signing cert (default [])
      --folder string                                   The vSphere folder for your VMs. Set to "" to use the root vSphere folder.
  -h, --help                                            Help for vsphere
      --http-proxy string                               HTTP proxy for CAPI controllers
      --https-proxy string                              HTTPS proxy for CAPI controllers
      --kubeconfig string                               Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply. This flag is ignored if used with the --self-managed flag.
      --kubernetes-image-repository string              The image repository to use for pulling kubernetes images
      --kubernetes-pod-network-cidr cidr                The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr                    The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string                       Kubernetes version (default "1.34.3")
  -n, --namespace string                                If present, the namespace scope for this CLI request. (default "default")
      --network string                                  The vSphere network to deploy the workload cluster on.
      --no-proxy strings                                No Proxy list for CAPI controllers (default [])
      --os-hint flatcar                                 A hint which will allow the installer to generate appropriate configurations for a target OS. Presently, only the hint for flatcar is supported.
  -o, --output string                                   Output format. One of: (json, yaml, name).
      --output-directory string                         Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --registry-mirror-cacert file                     Path to file containing the CA certificate used to verify the registry mirror server certificate
      --registry-mirror-password string                 Password used to authenticate with the registry mirror
      --registry-mirror-url url                         URL of a container registry used as a mirror (required for air-gapped installations)
      --registry-mirror-username string                 Username used to authenticate with the registry mirror
      --resource-pool string                            The vSphere resource pool for the workload cluster's virtual machines.
      --self-managed                                    When set to true, the required prerequisites are created before creating the cluster and the resulting cluster has all necessary components deployed onto itself, so it can manage its own cluster lifecycle. When set to false, a management cluster is used. (default false)
      --server string                                   The vCenter server address. Accepted formats: host, host:port, http[s]://host[:port]. Accepted host formats: IPv4, IPv6, or DNS name.
      --show-managed-fields                             If true, keep the managedFields when printing objects in JSON or YAML format.
      --ssh-public-key-file string                      Path to the authorized SSH key for the user
      --ssh-username string                             Name of the user to create on the instance (default "konvoy")
      --storage-policy string                           This is the vSphere storage policy. Set it to "" if you don't want to use a storage policy.
      --timeout duration                                The length of time to wait before giving up. Zero means wait forever (e.g. 300s, 30m, 3h). (default 30m0s)
      --tls-thumb-print string                          sha1 thumbprint of the vcenter certificate: openssl x509 -sha1 -fingerprint -in ca.crt -noout
      --virtual-ip-interface string                     The network interface, e.g, 'eth0' or 'ens5', to use for the built-in virtual IP control plane endpoint. This interface must be available on every control plane machine. If the value is empty, the flag does nothing. If the value is not empty, the built-in virtual IP control plane endpoint is created, using values from --control-plane-endpoint-host and --control-plane-endpoint-port.
      --vm-template string                              The virtual machine template to use for the workload cluster's virtual machines.
      --wait                                            If true, wait for operations to complete before returning. This flag is ignored and will always be 'true' if used with the --self-managed flag. (default true)
      --with-aws-bootstrap-credentials                  Set true to use AWS bootstrap credentials from your environment. When false, the instance profile of the EC2 instance where the CAPA controller is scheduled on will be used instead.
      --with-gcp-bootstrap-credentials                  Set true to use GCP bootstrap credentials from your environment. When false, the service account of the VM instance where the CAPG controller is scheduled on will be used instead.
      --worker-cpus int                                 The number of virtual processors in a worker machine (default 8)
      --worker-disk-size int                            The size of a worker machine's disk, in GB (default 80)
      --worker-http-proxy string                        HTTP proxy for nodes
      --worker-https-proxy string                       HTTPS proxy for nodes
      --worker-memory int                               The size of a worker machine's memory, in GB (default 32)
      --worker-no-proxy strings                         No Proxy list for nodes (default [])
      --worker-replicas int32                           Number of workers (default 4)

Global Flags:
  -v, --verbose int   Output verbosity
```
