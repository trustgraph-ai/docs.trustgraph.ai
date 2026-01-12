After deployment completes, a configuration file permitting access to the
Kubernetes cluster is written to kube.cfg.  This file should be treated as
a secret as it contains access keys for the Kubernetes cluster.

Check you can access the cluster:

```sh
export KUBECONFIG=$(pwd)/kube.cfg

# Verify access
kubectl get nodes
```

You should see your Scaleway Kapsule nodes listed as `Ready`.
