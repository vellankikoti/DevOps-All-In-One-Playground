# ArgoCD Configuration

This directory contains configuration files for deploying and managing the interactive DevOps quiz platform using ArgoCD.

## Features

- **GitOps**: Declarative configuration for application deployments.
- **Automated Syncing**: Tracks changes in Git repositories and updates applications in real time.
- **Rollbacks**: Easily revert to previous application states.

## Components

- **Application Definitions**: Specifies the apps managed by ArgoCD.
- **Project Definitions**: Defines namespaces, repositories, and resource limits for applications.
- **Sync Policies**: Automates updates when changes are pushed to the repository.

## File Descriptions

- **`applications/devops-app.yaml`**: Defines the interactive quiz application.
- **`projects/devops-project.yaml`**: Manages resources and access for the application.

## Prerequisites

- Kubernetes cluster with ArgoCD installed. Follow the [official guide](https://argo-cd.readthedocs.io/en/stable/getting_started/) for installation.
- Kubectl CLI installed and configured.

## Deployment Steps

1. **Install ArgoCD**:
   Follow the official [ArgoCD Installation Guide](https://argo-cd.readthedocs.io/en/stable/getting_started/).

2. **Create a Namespace**:
   ```bash
   kubectl create namespace argocd
   ```

3. **Apply Project Configuration**:
   ```bash
   kubectl apply -f projects/devops-project.yaml
   ```

4. **Apply Application Configuration**:
   ```bash
   kubectl apply -f applications/devops-app.yaml
   ```

5. **Access ArgoCD UI**:
   Retrieve the initial admin password:
   ```bash
   kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
   ```
   Open the UI at `http://<ARGOCD_SERVER>:<PORT>`.

## Notes

- **Git Repository**: Ensure the repository specified in `applications/devops-app.yaml` is accessible.
- **Sync Policy**: Edit sync policies as needed for manual or automated syncing.
- **Access Control**: Use ArgoCD RBAC for fine-grained access.

