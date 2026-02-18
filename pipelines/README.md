# Azure DevOps Pipelines

This folder contains CI/CD pipeline definitions for automated build, test, and deployment.

## 📋 Available Pipelines

### CI Pipeline (ci-pipeline.yml)
Continuous Integration - Runs on every commit to main/develop
- ✅ Python dependency installation
- ✅ Unit tests with coverage
- ✅ Security scanning (Bandit)
- ✅ Code quality checks (Pylint)
- ✅ Docker image build
- ✅ Push to Azure Container Registry

**Triggered by:**
- Code changes in `app/`, `pipelines/`, `k8s/`
- Branches: `main`, `develop`

### CD Pipeline (cd-pipeline.yml)
Continuous Deployment - Deploys to Kubernetes
- 🚀 Dev environment deployment
- 🚀 QA environment deployment  
- 🚀 Production environment deployment
- 📊 Health checks and monitoring

**Triggered by:**
- Successful CI pipeline + code in `main` branch

## 🔧 Setup Requirements

Before running pipelines, create these Service Connections in Azure DevOps:

### 1. Azure Container Registry Connection
```
Name: AzureContainerRegistry
Type: Docker Registry
Registry Type: Azure Container Registry
Subscription: Your Azure subscription
Registry: acrdevopsdemo
Service connection name: AzureContainerRegistry
```

### 2. Kubernetes Cluster Connection
```
Name: AKSCluster
Type: Kubernetes
Cluster: aks-devops-demo
Namespace: default
Service connection name: AKSCluster
Grant access to all pipelines: ✓
```

### 3. Azure Subscription Connection
```
Name: Azure-Subscription
Type: Azure Resource Manager
Subscription: Your subscription ID
Service principal: Auto-created recommended
```

## 📝 Configuration Steps

### Step 1: Create Pipelines in Azure DevOps

1. Go to **Pipelines** → **New Pipeline**
2. Select **Azure Repos Git**
3. Choose your repository
4. Select **Existing Azure Pipelines YAML file**
5. Point to `pipelines/ci-pipeline.yml`
6. Save and run

Repeat for CD pipeline with `pipelines/cd-pipeline.yml`

### Step 2: Update Variables

Edit the pipeline YAML files and update:
- `containerRegistry` → Your ACR login server
- `imageRepository` → Your image name
- `kubernetesConnection` → Your K8s connection name

### Step 3: Create Environments (for CD)

In Azure DevOps:
1. **Pipelines** → **Environments**
2. Create: `dev`, `qa`, `production`
3. Add approvals for production (optional)

## 🚀 Manual Pipeline Trigger

```bash
# Via Azure CLI
az pipelines run --name ci-pipeline --project devops-demo

# Via REST API
curl -X POST https://dev.azure.com/{org}/{project}/_apis/pipelines/{pipelineId}/runs?api-version=7.0 \
  -H "Authorization: Basic {base64_encoded_pat}" \
  -H "Content-Type: application/json"
```

## 📊 Pipeline Stages Explained

### Build Stage
```
✓ Install dependencies
✓ Run unit tests
✓ Security scanning
✓ Quality checks
✓ Build Docker image
✓ Push to ACR
```

### Deploy Stages
```
Dev  (Immediate deployment)
  ↓
QA   (After Dev succeeds)
  ↓
Prod (After QA succeeds + requires approval)
```

## 🔒 Security Best Practices

1. **Use Service Connections** - Don't hardcode credentials
2. **Secrets in Key Vault** - Store sensitive values
3. **Approval Gates** - Require approval before production
4. **Branch Policies** - Enforce code review
5. **Container Scanning** - Check image vulnerabilities
6. **Security Scanning** - Run Bandit, SonarQube

## 📈 Monitoring Pipeline Runs

```bash
# View pipeline runs
az pipelines runs list --project devops-demo

# View specific run details
az pipelines runs show --id <run-id> --project devops-demo
```

## 🧪 Testing Locally

### Test Pipeline YAML Syntax
```bash
# Install Azure Pipelines Extension
az extension add --name azure-devops

# Validate pipeline
az pipelines build definition show --name ci-pipeline
```

### Run Docker Build Locally
```bash
docker build -f app/Dockerfile -t genai-app:test .
docker run -p 5000:5000 genai-app:test
```

## 🔧 Customization Examples

### Add Email Notification
```yaml
- task: SendEmail@1
  inputs:
    emailAddress: 'team@example.com'
    subject: 'Build $(Build.BuildNumber) Failed'
```

### Add Slack Notification
```yaml
- task: SlackNotification@0
  inputs:
    webhookUrl: $(SlackWebhook)
    message: 'Build completed: $(Build.BuildNumber)'
```

### Run Integration Tests
```yaml
- script: |
    kubectl apply -f k8s/
    sleep 30
    curl http://localhost/health
  displayName: 'Run Integration Tests'
```

## 📚 Common Pipeline Variables

```yaml
$(Build.BuildId)              # Unique build ID
$(Build.BuildNumber)          # Build number
$(Build.SourceBranch)         # Branch name
$(Build.SourcesDirectory)     # Source code path
$(System.DefaultWorkingDirectory)  # Working directory
$(Agent.BuildDirectory)       # Build directory
```

## 🚨 Troubleshooting

### Pipeline Fails to Build Docker Image
```
❌ Error: docker: not found
✅ Solution: Ensure Docker is installed on agent
```

### Service Connection Authentication Failed
```
❌ Error: 401 Unauthorized
✅ Solution: Check service connection credentials and permissions
```

### Kubernetes Deployment Timeout
```
❌ Error: Rollout status timeout
✅ Solution: Check pod logs, increase timeout in pipeline
```

## 📊 Pipeline Metrics

Track in Azure DevOps:
- Build success rate
- Average build time
- Deployment frequency
- Deployment success rate
- Lead time for changes

## 📚 Learn More

- [Azure Pipelines Documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/)
- [YAML Schema Reference](https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/)
- [Service Connections](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints)
- [Environments & Approvals](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments)
