# DevOps Demo - Azure DevOps End-to-End Deployment

## 🎯 Core Principle
**Git repository is the single source of truth.**

All infrastructure, application code, and pipeline definitions are managed here for consistent, reproducible deployments.

---

## 📁 Repository Structure

### `/infra`
**Terraform Code** - Infrastructure as Code (IaC)
- Azure resources provisioning
- Networks, storage, compute configurations
- Environment-specific variables

### `/app`
**Application Code** - Simple OpenSource GenAI App
- Source code for the application
- Dependencies and requirements
- Build configuration

### `/k8s`
**Kubernetes YAML Files** - Container Orchestration
- Deployment manifests
- Service configurations
- ConfigMaps and Secrets definitions
- Helm charts (optional)

### `/pipelines`
**Pipeline YAML** - CI/CD Automation
- Build pipelines (CI)
- Release pipelines (CD)
- Testing and deployment automation

---

## 🚀 How to Use

1. **Infrastructure**: Deploy using `infra/` Terraform files
2. **Application**: Build and containerize using `app/` code
3. **Kubernetes**: Deploy containers using `k8s/` manifests
4. **Pipelines**: Automate everything with `pipelines/` definitions

---

## 📝 Getting Started

Each folder contains its own documentation. Start by exploring the individual README files in each directory.

---

**Created for**: Azure DevOps End-to-End Deployment Workshop
