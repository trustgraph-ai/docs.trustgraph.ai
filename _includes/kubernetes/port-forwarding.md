Since the Kubernetes cluster is running on Scaleway, you'll need to set up port-forwarding to access TrustGraph services from your local machine.

**Open three separate terminal windows** and run these commands (keep them running):

**Terminal 1 - API Gateway:**

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
kubectl -n trustgraph port-forward svc/api-gateway 8088:8088
```

**Terminal 2 - Workbench UI:**

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
kubectl -n trustgraph port-forward svc/workbench-ui 8888:8888
```

**Terminal 3 - Grafana:**

```bash
export KUBECONFIG=$(pwd)/kubeconfig.yaml
kubectl -n trustgraph port-forward svc/grafana 3000:3000
```

With these port-forwards running, you can access:

- **TrustGraph API**: [http://localhost:8088](http://localhost:8088)
- **Web Workbench**: [http://localhost:8888](http://localhost:8888)
- **Grafana Monitoring**: [http://localhost:3000](http://localhost:3000)

{: .note }
Keep these terminal windows open while you're working with TrustGraph. If you close them, you'll lose access to the services.
