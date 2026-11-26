# `nkp create metadata`

```text
Create a infrastructure metadata, one of [nutanix]

Usage:
  nkp create metadata [command]

Available Commands:
  nutanix     Creates nutanix metadata

Flags:
  -h, --help          Help for metadata
  -v, --verbose int   Output verbosity

Use "nkp create metadata [command] --help" for more information about a command.
```

## Subcommands

### `nkp create metadata nutanix`

```text
Creates nutanix metadata

Usage:
  nkp create metadata nutanix [flags]

Flags:
      --additional-trust-bundle string   Additional CA trust bundle to use to validate the Prism Central server certificate.
      --dry-run                          Only print the objects that would be created, without creating them.
      --endpoint url                     Prism Central URL. Accepted formats: host, host:port, http[s]://host[:port]. Accepted host formats: IP, FQDN.
  -h, --help                             Help for nutanix
      --insecure                         If true, the Prism Central server certificate will not be validated.
      --kubeconfig string                Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
  -o, --output string                    Output format. One of: (json, yaml, name).
      --output-directory string          Used with --output=json|yaml. The directory where to output resources to files. The directory must already exist.
      --show-managed-fields              If true, keep the managedFields when printing objects in JSON or YAML format.

Global Flags:
  -v, --verbose int   Output verbosity
```
