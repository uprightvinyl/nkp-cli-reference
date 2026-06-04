# `nkp create image`

```text
Create Operating System image for one of [aws, azure, gcp, nutanix, preprovisioned, vsphere]

Usage:
  nkp create image [command]

Available Commands:
  aws            Create Amazon Machine Image(AMI) for one of [flatcar, oracle-8.9, rhel-8.10, rhel-9.6, rocky-9.6, ubuntu-22.04, ubuntu-24.04]
  azure          Create Azure Image for one of [rhel-9.6, rocky-9, ubuntu-22.04, ubuntu-24.04]
  gcp            Create Google Cloud Platform Image for one of [ubuntu-22.04, ubuntu-24.04]
  nutanix        Create Nutanix Machine Image for one of [rhel-8.10, rhel-9.6, rocky-9.6, ubuntu-22.04, ubuntu-24.04]
  preprovisioned Configuring an existing remote host
  vsphere        Create Vsphere VM template for one of [flatcar, oracle-9.4, rhel-8.10, rhel-9.6, rocky-9.6, ubuntu-22.04, ubuntu-24.04]

Flags:
  -h, --help          Help for image
  -v, --verbose int   Output verbosity

Use "nkp create image [command] --help" for more information about a command.
```

## Subcommands

### `nkp create image aws`

```text
Create Amazon Machine Image(AMI) for one of [flatcar, oracle-8.9, rhel-8.10, rhel-9.6, rocky-9.6, ubuntu-22.04, ubuntu-24.04]

Usage:
  nkp create image aws OSName [flags]

Flags:
      --ami-regions strings          A list of regions to publish AMIs to (default [])
      --artifacts-directory string   Path to a directory containing the artifacts needed to build the OS image. Useful in an air-gapped environment
      --bundle fileSlice             Path to a container image bundle tarball to load in the OS image. Multiple bundles can be provided with a comma separated list. File must be a '.tar' format. Useful in an air-gapped environment (default [])
      --debug                        Run packer in debug mode. user will be prompted after each step while building the image.
      --dry-run                      Do not create artifacts, or delete them after creating. Recommended for tests.
      --extra-build-name string      Additional name to add in the OS image name
      --fips                         Enable FIPS support
      --gpu                          Enable GPU support
  -h, --help                         Help for aws
      --instance-type string         Instance type used to build the AMI. If not provided, a default instance type 't3.small' or 'g4dn.2xlarge (for GPU)' will be used.
      --kubernetes-version string    Kubernetes version used to build packages (default "1.34.3")
      --overrides fileSlice          A comma separated list of override YAML files. (default [])
      --region string                Region in which to build the AMI (default "us-west-2")
      --source-ami string            The ID of the AMI to use as the source; If not provided, a source AMI will be selected automatically
      --work-directory string        Path to a directory to use as a workspace to build the OS image. The directory must already exist.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create image azure`

```text
Create Azure Image for one of [rhel-9.6, rocky-9, ubuntu-22.04, ubuntu-24.04]

Usage:
  nkp create image azure OSName [flags]

Flags:
      --client-id string                  Client ID for the Azure service principal.
      --cloud-endpoint string             Azure cloud endpoint. Which can be one of [Public USGovernment China] (default "Public")
      --debug                             Run packer in debug mode. user will be prompted after each step while building the image.
      --dry-run                           Do not create artifacts, or delete them after creating. Recommended for tests.
      --extra-build-name string           Additional name to add in the OS image name
      --fips                              Enable FIPS support
      --gallery-image-locations strings   List of locations where to replicate the image to.If not provided, the value of the location flag will be used. (default [])
      --gallery-image-name string         Name of the Azure Shared Image Gallery image.If not provided, a default name based on the OS and Kubernetes version will be used.
      --gallery-image-offer string        The gallery image offer where the image will be stored. (default "nkp")
      --gallery-image-publisher string    The gallery image publisher to use for the image. (default "nkp")
      --gallery-name string               The gallery where the image will be stored. (default "nkp")
  -h, --help                              Help for azure
      --instance-type string              The Instance Type to use for the build VM. (default "Standard_D2s_v3")
      --kubernetes-version string         Kubernetes version used to build packages (default "1.34.3")
      --location string                   The location of the resource group. (default "westus")
      --overrides fileSlice               A comma separated list of override YAML files. (default [])
      --resource-group-name string        The resource group name to create image in. (default "nkp")
      --subscription-id string            Azure subscription ID to use for the virtual machine.
      --tenant-id string                  The tenant id to use for the build
      --work-directory string             Path to a directory to use as a workspace to build the OS image. The directory must already exist.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create image gcp`

```text
Create Google Cloud Platform Image for one of [ubuntu-22.04, ubuntu-24.04]

Usage:
  nkp create image gcp OSName [flags]

Flags:
      --debug                             Run packer in debug mode. user will be prompted after each step while building the image.
      --dry-run                           Do not create artifacts, or delete them after creating. Recommended for tests.
      --extra-build-name string           Additional name to add in the OS image name
  -h, --help                              Help for gcp
      --image-storage-locations strings   The locations where the image will be stored. (default [])
      --kubernetes-version string         Kubernetes version used to build packages (default "1.34.3")
      --network string                    The network to use when creating an image
      --overrides fileSlice               A comma separated list of override YAML files. (default [])
      --project-id string                 The project id to use when storing created image.
      --region string                     The region in which to launch the instance. (default "us-west1")
      --work-directory string             Path to a directory to use as a workspace to build the OS image. The directory must already exist.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create image nutanix`

```text
Create Nutanix Machine Image for one of [rhel-8.10, rhel-9.6, rocky-9.6, ubuntu-22.04, ubuntu-24.04]

Usage:
  nkp create image nutanix OSName [flags]

Flags:
      --artifacts-directory string      Path to a directory containing the artifacts needed to build the OS image. Useful in an air-gapped environment
      --bastion-host string             IP or hostname for bastion
      --bastion-port int                SSH port of the bastion host (default 22)
      --bastion-private-key-file file   Path to a PEM encoded private key file to use to authenticate with the bastion host
      --bastion-username string         The username to connect to the bastion host
      --bundle fileSlice                Path to a container image bundle tarball to load in the OS image. Multiple bundles can be provided with a comma separated list. File must be a '.tar' format. Useful in an air-gapped environment (default [])
      --cluster string                  Name of the Nutanix cluster.
      --debug                           Run packer in debug mode. user will be prompted after each step while building the image.
      --dry-run                         Do not create artifacts, or delete them after creating. Recommended for tests.
      --endpoint string                 Host URL or IP for the Nutanix Prism Central instance.
      --extra-build-name string         Additional name to add in the OS image name
      --fips                            Enable FIPS support
      --gpu-name string                 Assigns a GPU that is present on cluster-name on the temporary VM.
  -h, --help                            Help for nutanix
      --insecure                        Connect with Prism without verifying CA certificates.
      --kubernetes-version string       Kubernetes version used to build packages (default "1.34.3")
      --overrides fileSlice             A comma separated list of override YAML files. (default [])
      --port int                        Port for the Nutanix Prism Central instance. (default 9440)
      --source-image string             Base Image name or UUID used as a disk source. If the image name is not provided then upstream base image for the OS will be downloaded.
      --subnet string                   Nutanix subnet name or UUID to use with the virtual machine.
      --vgpu-runfile file               Local path to runfile for vGPU driver.
      --work-directory string           Path to a directory to use as a workspace to build the OS image. The directory must already exist.

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp create image vsphere`

```text
Create Vsphere VM template for one of [flatcar, oracle-9.4, rhel-8.10, rhel-9.6, rocky-9.6, ubuntu-22.04, ubuntu-24.04]

Usage:
  nkp create image vsphere OSName [flags]

Flags:
      --artifacts-directory string      Path to a directory containing the artifacts needed to build the OS image. Useful in an air-gapped environment
      --bastion-host string             IP or hostname for bastion
      --bastion-port int                SSH port of the bastion host (default 22)
      --bastion-private-key-file file   Path to a PEM encoded private key file to use to authenticate with the bastion host
      --bastion-username string         The username to connect to the bastion host
      --bundle fileSlice                Path to a container image bundle tarball to load in the OS image. Multiple bundles can be provided with a comma separated list. File must be a '.tar' format. Useful in an air-gapped environment (default [])
      --cluster string                  vSphere cluster name
      --data-center string              vSphere datacenter name
      --data-store string               vSphere datastore name
      --debug                           Run packer in debug mode. user will be prompted after each step while building the image.
      --dry-run                         Do not create artifacts, or delete them after creating. Recommended for tests.
      --extra-build-name string         Additional name to add in the OS image name
      --fips                            Enable FIPS support
      --folder string                   vSphere folder name
  -h, --help                            Help for vsphere
      --insecure                        Connect with vCenter without verifying CA certificates.Beneficial in scenarios where the certificate is self-signed. (not recommended for production use)
      --kubernetes-version string       Kubernetes version used to build packages (default "1.34.3")
      --network string                  vSphere network name
      --overrides fileSlice             A comma separated list of override YAML files. (default [])
      --resource-pool string            vSphere resource pool name
      --server string                   Host IP or FQDN of vCenter API server
      --template string                 Base template name to use for creating VM
      --work-directory string           Path to a directory to use as a workspace to build the OS image. The directory must already exist.

Global Flags:
  -v, --verbose int   Output verbosity
```
