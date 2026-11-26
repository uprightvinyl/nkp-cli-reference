# `nkp push image-archive`

```text
Push OCI image layout tarballs (oci-archive) and docker-save tarballs (docker-archive) directly to an OCI registry. The archive format is auto-detected from the file contents.

Usage:
  nkp push image-archive [flags]

Flags:
  -h, --help                                   Help for image-archive
      --image-archive strings                  Tarball containing an image archive to push (OCI image layout or docker-save format, auto-detected). Can be specified multiple times or as a glob pattern. (default [])
      --image-tag string                       Destination image reference (repo:tag) to use when the archive contains a single image. Overrides any embedded tag; required if the archive has no embedded tag. Only valid when exactly one archive with one image is provided.
      --to-registry string                     Registry to push images to. TLS verification will be skipped when using an http:// registry.
      --to-registry-ca-cert-file string        CA certificate file used to verify TLS verification of registry to push images to
      --to-registry-insecure-skip-tls-verify   Skip TLS verification of registry to push images to (also use for non-TLS http registries)
      --to-registry-password string            Password to use to log in to destination registry
      --to-registry-username string            Username to use to log in to destination registry
  -v, --verbose int                            Output verbosity
```
