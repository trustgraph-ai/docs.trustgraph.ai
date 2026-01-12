Verify that all pods are running:

```bash
kubectl -n trustgraph get pods
```

You should see output similar to this (pod names will have different random suffixes):

```
NAME                                        READY   STATUS      RESTARTS   AGE
agent-manager-74fbb8b64-nzlwb               1/1     Running     0          5m
api-gateway-b6848c6bb-nqtdm                 1/1     Running     0          5m
cassandra-6765fff974-pbh65                  1/1     Running     0          5m
pulsar-d85499879-x92qv                      1/1     Running     0          5m
text-completion-58ccf95586-6gkff            1/1     Running     0          5m
workbench-ui-5fc6d59899-8rczf               1/1     Running     0          5m
...
```

All pods should show `Running` status. Some init pods (names ending in `-init`) may fail or be shown `Completed` status - this is normal, their job is
to initialise cluster resources and then exit.
