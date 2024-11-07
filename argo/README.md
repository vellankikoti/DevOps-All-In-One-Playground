
# ArgoCD - DevOps All-In-One Playground

This folder contains the ArgoCD configuration for GitOps-style deployment of the DevOps All-In-One Playground. ArgoCD will continuously monitor your GitHub repository and automatically deploy updates to your Kubernetes cluster.

## Prerequisites

- **ArgoCD**: Installed on your Kubernetes cluster. For installation, refer to the [ArgoCD documentation](https://argo-cd.readthedocs.io/en/stable/getting_started/).

## Setup Steps

### Step 1: Apply the ArgoCD Application Configuration

1. Use `kubectl` to apply the `argo-app.yaml` configuration:
   ```bash
   kubectl apply -f argo/argo-app.yaml
   ```

2. This command registers the application with ArgoCD, allowing it to monitor and deploy updates from your GitHub repository (`https://github.com/vellankikoti/DevOps-All-In-One-Playground.git`).

### Step 2: Access the ArgoCD Dashboard

1. Port-forward the ArgoCD server to access the dashboard:
   ```bash
   kubectl port-forward svc/argocd-server -n argocd 8080:443
   ```
2. Visit `https://localhost:8080` in your browser.

3. Log in with the ArgoCD credentials (default username is `admin`).

### Step 3: Monitor and Manage Deployments

- Once logged in, view and manage the `devops-playground` application from the ArgoCD dashboard.
- ArgoCD will automatically sync any changes pushed to the `main` branch of your GitHub repository and deploy them to the Kubernetes cluster.

## Customization

You can modify the `argo-app.yaml` file to:
- Change the Git repository URL or branch.
- Adjust the synchronization policies (e.g., manual or automated).
- Specify different namespaces or cluster destinations.

---

This ArgoCD setup enables continuous delivery and automated synchronization, ensuring that your Kubernetes cluster stays in sync with the `DevOps-All-In-One-Playground` repository.

---

