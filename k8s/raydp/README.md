# Ray Cluster on Kubernetes setup. (Include raydp frame work.)

## Ray Cluster on Kubernetes

Using helm chart

```bash
# kuberay install
$ helm repo add kuberay https://ray-project.github.io/kuberay-helm/
$ helm repo update

# kuberay operator on kubernetes.
$ helm install kuberay-operator kuberay/kuberay-operator --version 1.2.2
```

```bash
$ kubectl get pods
# NAME                                READY   STATUS    RESTARTS   AGE
# kuberay-operator-67fb47ddc7-nsm8x   1/1     Running   0          28s
```

## Running Ray Job

I need 2 worker pods in my ray cluster. So I changed the configuration file `yaml`.

[yaml file](https://github.com/seunggihong/mydocker/blob/main/raydp/raydp-job.pytoch.yaml) 👈

And i used `nyc taxi` example. This example used `Spark` and `Pytorch` for data load/preprocessing and model training.

[Example](https://github.com/oap-project/raydp/blob/master/examples/pytorch_nyctaxi.py) 👈

```yaml

....
workerGroupSpecs:
  - replicas: 2 # -> num workers
    minReplicas: 1
    maxReplicas: 5
    groupName: small-group
    rayStartParams: {}
    template:
      spec:
        containers:
          - name: ray-worker
            image: onggizam/raydp:1.0.0
            resources:
              limits:
                cpu: '1'
                memory: '10G'
              requests:
                cpu: '1'
                memory: '10G'
....
```

```bash
$ kubectl apply -f {SCRIPT_PATH}/raydp-job.pytorch.yaml
```

We created three pods in our Kubernetes cluster: one head pod and two worker pods.

```bash
# Check the rayjob
$ kubectl get rayjob
# NAME                  JOB STATUS   DEPLOYMENT STATUS   RAY CLUSTER NAME                       START TIME             END TIME   AGE
# rayjob-raydpcluster   RUNNING      Running             rayjob-raydpcluster-raycluster-fsnxk   2025-02-05T11:01:00Z              29s
```

Showing training steps.

```bash
$ kubectl logs -f {RAYJOB_POD_NAME}
```

If you want to show the ray cluster dashboard, you should port-forwarding.

```bash
# port forwarding.
$ export HEAD_POD=$(kubectl get pods --selector=ray.io/node-type=head -o custom-columns=POD:metadata.name --no-headers)
$ kubectl port-forward service/raycluster-kuberay-head-svc 8265:8265
```

## Down Ray Cluster

```bash
$ kubectl delete -f {SCRIPT_PATH}/raydp-job.pytorch.yaml # ray cluster / job
$ helm uninstall kuberay-operator # kuberay operator
```
