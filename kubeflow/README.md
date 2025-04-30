# Kubeflow install

```bash
while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 15; done
```
