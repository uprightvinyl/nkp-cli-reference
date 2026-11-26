# `nkp legacy create`

```text
Create one of [cluster, nodepool]

Usage:
  nkp legacy create [command]

Available Commands:
  cluster     Create a cluster
  nodepool    Create a nodepool

Flags:
  -h, --help   Help for create

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy create [command] --help" for more information about a command.
```

## Subcommands

### `nkp legacy create cluster`

```text
Create a cluster

Usage:
  nkp legacy create cluster [command]

Available Commands:
  eks         Create a Konvoy cluster in EKS not using ClusterClass

Flags:
  -h, --help   Help for cluster

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy create cluster [command] --help" for more information about a command.
```

### `nkp legacy create cluster eks`

```text
Create a Konvoy cluster in EKS not using ClusterClass

Usage:
  nkp legacy create cluster eks [flags]

Flags:
      --additional-security-group-ids strings   A comma separated list of existing security group IDs to use for machines in addition to those created automatically (default [])
      --additional-tags stringToString          Tags to apply to the provisioned infrastructure (default [])
  -c, --cluster-name name                       Name used to prefix the cluster and all the created resources.
      --dry-run                                 Only print the objects that would be created, without creating them.
  -h, --help                                    Help for eks
      --kubeconfig string                       Path to the kubeconfig for the management cluster. If unspecified, default discovery rules apply.
      --kubernetes-pod-network-cidr cidr        The Kubernetes Pod network CIDR to use in the cluster (default 192.168.0.0/16)
      --kubernetes-service-cidr cidr            The Kubernetes Service CIDR to use in the cluster (default 10.96.0.0/12)
      --kubernetes-version string               Kubernetes version (default "1.32.0")
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
      --worker-replicas int32                   Number of workers (default 4)

Global Flags:
  -v, --verbose int   Output verbosity
```

### `nkp legacy create nodepool`

```text
Create a nodepool

Usage:
  nkp legacy create nodepool [command]

Available Commands:
  eks         Create a nodepool in EKS.

Flags:
  -h, --help   Help for nodepool

Global Flags:
  -v, --verbose int   Output verbosity

Use "nkp legacy create nodepool [command] --help" for more information about a command.
```

### `nkp legacy create nodepool eks`

```text
Create a nodepool in EKS.

NAME must
  - have no more than 63 characters
  - consist of lower case alphanumeric characters, '-', or '.'
  - must start and end with an alphanumeric character

Usage:
  nkp legacy create nodepool eks NAME [flags]

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
      --kubernetes-version string               Kubernetes version (default "1.32.0")
  -n, --namespace string                        If present, the namespace scope for this CLI request. (default "default")
      --no-proxy strings                        No Proxy list for nodes (default [])
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
