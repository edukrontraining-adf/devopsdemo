# Kubernetes Manifests

This folder contains all Kubernetes YAML files for deploying the GenAI application to AKS.

## 📋 Files Overview

- **deployment.yaml** - Pod deployment with replicas, resource limits, health checks
- **service.yaml** - ClusterIP service for internal networking
- **ingress.yaml** - HTTP ingress for external access
- **hpa.yaml** - Horizontal Pod Autoscaler (auto-scaling)
- **configmap.yaml** - Configuration data
- **secrets.template.yaml** - Sensitive data (API keys, passwords)

## 🚀 Deployment

### Single Command Deployment
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
kubectl apply -f hpa.yaml
kubectl apply -f configmap.yaml
```

### Or Deploy Everything
```bash
kubectl apply -f .
```

## 🔍 Verify Deployment

```bash
# Check pods
kubectl get pods -o wide

# Check services
kubectl get svc

# Check ingress
kubectl get ingress

# Check pod logs
kubectl logs -f deployment/genai-app
```

## 📊 Understanding the Manifests

### Deployment
- **3 replicas** - For high availability
- **Rolling update** - Zero-downtime updates
- **Health checks** - Liveness & readiness probes
- **Resource limits** - CPU & memory management
- **Security policies** - Non-root user, drop capabilities

### Service
- **ClusterIP type** - Internal access only
- **Port mapping** - 80 → 5000 (container port)
- **Load balancing** - Distributes traffic between pods

### Ingress
- **Route /api/** - Path-based routing
- **Host-based routing** - Domain routing support
- **TLS ready** - HTTPS configuration available

### HPA (Horizontal Pod Autoscaler)
- **Min replicas:** 2
- **Max replicas:** 10
- **Triggers:** CPU > 70%, Memory > 80%
- **Scale-up:** 15 seconds
- **Scale-down:** 5 minutes

## 🔐 Managing Secrets

### Create Secrets
```bash
# From literal
kubectl create secret generic openai-secrets \
  --from-literal=api-key=your-api-key-here

# From file
kubectl create secret generic openai-secrets \
  --from-file=api-key=./api-key.txt

# Verify
kubectl get secrets
kubectl describe secret openai-secrets
```

## 📈 Scaling & Updates

### Manual Scaling
```bash
# Scale to 5 replicas
kubectl scale deployment genai-app --replicas=5
```

### Rolling Update
```bash
# Update image
kubectl set image deployment/genai-app \
  genai-app=acrdevopsdemo.azurecr.io/genai-app:v2

# Check rollout status
kubectl rollout status deployment/genai-app

# Rollback if needed
kubectl rollout undo deployment/genai-app
```

## 🔧 Customization

### Change Replica Count
Edit `deployment.yaml` in spec section:
```yaml
replicas: 5  # Change this
```

### Change Resource Limits
Edit resource requirements:
```yaml
resources:
  requests:
    cpu: 100m        # Change this
    memory: 128Mi    # And this
  limits:
    cpu: 500m
    memory: 512Mi
```

### Change Image
Update image field in deployment:
```yaml
image: acrdevopsdemo.azurecr.io/genai-app:v2.0
```

## 🧪 Testing Deployment

### Port Forward
```bash
kubectl port-forward service/genai-app 8080:80
# Access at http://localhost:8080
```

### Execute Commands in Pod
```bash
kubectl exec -it deployment/genai-app -- /bin/sh
```

### Check Pod Logs
```bash
kubectl logs -f deployment/genai-app --all-containers=true
```

## 🎯 Best Practices

1. **Always use resource limits** - Prevents resource hogging
2. **Configure health checks** - Ensures pod recovery
3. **Use ConfigMaps** - Separate config from code
4. **Manage secrets securely** - Never commit secrets
5. **Implement HPA** - Auto-scale based on demand
6. **Use readiness probes** - Prevents traffic to unhealthy pods
7. **Anti-affinity rules** - Spread pods across nodes

## 📊 Monitoring

### Check Pod Status
```bash
kubectl describe pod <pod-name>
kubectl top pods
```

### Check Node Status
```bash
kubectl get nodes
kubectl describe node <node-name>
```

### View Events
```bash
kubectl get events --sort-by='.lastTimestamp'
```

## 🚨 Troubleshooting

### Pod Not Running
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Service Not Accessible
```bash
kubectl get svc
kubectl describe svc genai-app
```

### HPA Not Scaling
```bash
kubectl describe hpa genai-app-hpa
kubectl get hpa --watch
```

## 📚 Learn More

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [AKS Best Practices](https://learn.microsoft.com/en-us/azure/aks/best-practices)
- [Deployment Strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
