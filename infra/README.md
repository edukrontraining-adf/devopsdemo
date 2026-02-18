# Infrastructure as Code (Terraform)

This folder contains all infrastructure automation for the DevOps Demo project.

## 📋 Files Overview

- **main.tf** - Core infrastructure resources (Resource Group, ACR, AKS, Network)
- **variables.tf** - Input variables for customization
- **outputs.tf** - Output values after deployment
- **backend.tf** - Terraform state management configuration
- **terraform.tfvars.example** - Example variables file

## 🚀 Quick Start

### Prerequisites
```bash
# Install Terraform
brew install terraform  # macOS
# or
choco install terraform  # Windows
# or
sudo apt-get install terraform  # Linux

# Install Azure CLI
brew install azure-cli
# or download from https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

# Login to Azure
az login
```

### Setup Steps

1. **Copy and configure variables:**
```bash
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values
```

2. **Create Service Principal:**
```bash
az ad sp create-for-rbac --name DevOpsDemo --role Contributor
# Copy client_id and client_secret to terraform.tfvars
```

3. **Initialize Terraform:**
```bash
terraform init
```

4. **Plan deployment:**
```bash
terraform plan -out=tfplan
```

5. **Apply configuration:**
```bash
terraform apply tfplan
```

6. **Get kubeconfig:**
```bash
az aks get-credentials --resource-group rg-devops-demo --name aks-devops-demo --admin
```

## 📊 Resources Created

- **Azure Resource Group** - Container for all resources
- **Azure Container Registry (ACR)** - Docker image repository
- **Azure Kubernetes Service (AKS)** - Kubernetes cluster
- **Virtual Network (VNet)** - Networking for resources
- **Subnets** - Network segmentation
- **Role Assignments** - Access permissions

## 🔐 Security Best Practices

- Non-root user in containers
- Network security groups
- ACR credentials management
- Service Principal with minimal permissions
- State file encryption

## 🛠️ Advanced Configuration

### Setting up Backend (Remote State)

```bash
# Create storage account for state
az group create --name rg-terraform-state --location eastus
az storage account create --name tfstatedev --resource-group rg-terraform-state --location eastus
az storage container create --name tfstate --account-name tfstatedev
```

Uncomment the backend block in `backend.tf` and run:
```bash
terraform init
```

### Scaling AKS Cluster

Edit `terraform.tfvars`:
```
node_count = 5
```

Then apply:
```bash
terraform apply -auto-approve
```

## 📝 Monitoring & Logging

The infrastructure is configured with:
- Container Insights enabled
- Diagnostic settings for monitoring
- Log Analytics integration

## 🗑️ Cleanup

```bash
terraform destroy
```

⚠️ **Warning:** This will delete all resources!

## 📚 Learn More

- [Terraform AKS Module](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster)
- [Azure DevOps Documentation](https://learn.microsoft.com/en-us/azure/devops/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
