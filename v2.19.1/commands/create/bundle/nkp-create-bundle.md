# `nkp create bundle`

```text
Create a bundle containing container images and/or Helm charts

Usage:
  nkp create bundle [flags]

Flags:
      --all-platforms                Download images for all platforms specified in the image manifests
      --helm-charts-file string      YAML file containing configuration of Helm charts to create bundle from
  -h, --help                         Help for bundle
      --image-pull-concurrency int   Image pull concurrency (default 1)
      --images-file string           File containing list of images to create bundle from, either as YAML configuration or a simple list of images
      --merge                        Merge new images into existing bundle file if it already exists
      --oci-artifacts-file string    File containing list of oci artifacts to create bundle from, either as YAML configuration or a simple list of images
      --output-file string           Output file to write bundle to (default "bundle.tar")
      --overwrite                    Overwrite bundle file if it already exists
      --platform platformSlice       platforms to download images for (required format: <os>/<arch>[/<variant>]) (default [linux/amd64])
  -v, --verbose int                  Output verbosity
```
