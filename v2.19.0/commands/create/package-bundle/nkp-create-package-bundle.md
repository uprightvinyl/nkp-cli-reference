# `nkp create package-bundle`

```text
Create Operating System package bundle for one of [oracle-8.9, oracle-9.4, rhel-8.10, rhel-9.6, rhel-9.8, rocky-9.8, ubuntu-22.04, ubuntu-24.04]

Usage:
  nkp create package-bundle OSName [flags]

Flags:
      --artifacts-directory string   Path to a directory for storing OS package bundles. The directory must already exist.
      --container-image string       A container image to use for building the package bundles
      --fips                         Creats FIPS compliant packages
      --from-directory string        Build using the scripts and configuration files in this directory instead of the embedded defaults. Typically the files are first produced and customized via --output-directory. The directory must already exist. Mutually exclusive with --output-directory.
  -h, --help                         Help for package-bundle
      --kubernetes-version string    Kubernetes version used to build packages (default "1.36.2")
      --output-directory string      Extract the scripts and configuration files used for the build into this directory and exit without building. Review and customize the extracted files, then pass the same directory to --from-directory on a later run to build from your customized files. The directory must already exist. Mutually exclusive with --from-directory.
  -v, --verbose int                  Output verbosity
```
