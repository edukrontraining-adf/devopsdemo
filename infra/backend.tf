# Terraform State Management
# This file defines where Terraform state is stored
#
# Before using this backend configuration:
# 1. Create a storage account in Azure: rg-terraform-state
# 2. Create a container named "tfstate"
# 3. Uncomment the backend block and update values
#
# Commands to initialize backend:
#   az group create --name rg-terraform-state --location eastus
#   az storage account create --name tfstatedev --resource-group rg-terraform-state --location eastus
#   az storage container create --name tfstate --account-name tfstatedev

# Option 1: Local State (Development Only - NOT recommended for production)
# State file is stored locally in terraform.tfstate
# Good for learning and testing

# Option 2: Azure Storage Backend (Recommended for Production)
# Uncomment and configure this once backend is set up:
#
# terraform {
#   backend "azurerm" {
#     resource_group_name  = "rg-terraform-state"
#     storage_account_name = "tfstatedev"
#     container_name       = "tfstate"
#     key                  = "prod.terraform.tfstate"
#   }
# }

# Option 3: Terraform Cloud Backend
# Requires account at app.terraform.io
#
# terraform {
#   cloud {
#     organization = "your-org-name"
#     workspaces {
#       name = "devops-demo"
#     }
#   }
# }
