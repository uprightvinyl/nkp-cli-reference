# `nkp push bundle`

```text
Push from bundles into an existing OCI registry

Usage:
  nkp push bundle [flags]

Flags:
      --bundle strings                         Tarball containing list of images to push. Can also be a glob pattern. (default [])
      --ecr-lifecycle-policy-file string       File containing ECR lifecycle policy for newly created repositories (only applies if target registry is hosted on ECR, ignored otherwise)
      --force-oci-media-types                  force OCI media types
  -h, --help                                   Help for bundle
      --image-push-concurrency int             Image push concurrency (default 1)
      --kubeconfig file                        If pushing to a registry running in a Kubernetes cluster, the kubeconfig file for the cluster. If unspecified, default discovery rules apply.
      --on-existing-tag string                 how to handle existing tags: one of "overwrite", "error", or "skip" (default "overwrite")
      --to-internal-registry-mirror            Push to an internal registry mirror running in a Kubernetes cluster.
      --to-registry string                     Registry to push images to. TLS verification will be skipped when using an http:// registry.
      --to-registry-ca-cert-file string        CA certificate file used to verify TLS verification of registry to push images to
      --to-registry-insecure-skip-tls-verify   Skip TLS verification of registry to push images to (also use for non-TLS http registries)
      --to-registry-password string            Password to use to log in to destination registry
      --to-registry-username string            Username to use to log in to destination registry

Global Flags:
  -v, --verbose int   Output verbosity
```
