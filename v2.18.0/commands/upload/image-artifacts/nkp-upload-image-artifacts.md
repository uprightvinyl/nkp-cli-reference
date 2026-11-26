# `nkp upload image-artifacts`

```text
Upload artifacts to remote hosts

Usage:
  nkp upload image-artifacts [flags]

Flags:
      --artifacts-directory string      Path to a directory containing the artifacts needed to build the OS image. Useful in an air-gapped environment
      --bastion-host string             IP or hostname for bastion
      --bastion-port int                SSH port of the bastion host (default 22)
      --bastion-private-key-file file   Path to a PEM encoded private key file to use to authenticate with the bastion host
      --bastion-username string         The username to connect to the bastion host
      --bundle fileSlice                Path to a container image bundle tarball to load in the OS image. Multiple bundles can be provided with a comma separated list. File must be a '.tar' format. Useful in an air-gapped environment (default [])
      --debug                           Run packer in debug mode. user will be prompted after each step while building the image.
      --dry-run                         Do not create artifacts, or delete them after creating. Recommended for tests.
      --extra-build-name string         Additional name to add in the OS image name
      --fips                            Enable FIPS support
  -h, --help                            Help for image-artifacts
      --kubernetes-version string       Kubernetes version used to build packages (default "1.35.2")
      --nvidia-runfile file             path to NVIDIA runfile to to upload to remote hosts
      --overrides fileSlice             A comma separated list of override YAML files. (default [])
      --provider string                 An optional provider hint when installing provider specific utilities.
      --ssh-host strings                IP or hostname of the remote host(s). A comma separated list can be provided for multiple hosts. (default [])
      --ssh-password string             Password to use for SSH authentication (not recommended)
      --ssh-port int                    SSH port of the remote host (default 22)
      --ssh-private-key-file file       Path to a PEM encoded private key file to use to authenticate with the remote host
      --ssh-username string             The username to connect to the remote host
      --work-directory string           Path to a directory to use as a workspace to build the OS image. The directory must already exist.

Global Flags:
  -v, --verbose int   Output verbosity
```
