# CI/CD with GitHub Actions - DevOps All-In-One Playground

This folder contains configurations for automating the CI/CD pipeline using GitHub Actions. This setup enables continuous integration and delivery for the DevOps All-In-One Playground application directly from your GitHub repository.

## GitHub Actions Workflow

### Workflow Configuration

- **File**: `.github/workflows/ci-cd.yml`
- **Triggers**: The workflow is triggered on `push` and `pull_request` events to the `main` branch.

### Steps in the CI/CD Pipeline

1. **Checkout Code**: Checks out the latest code from the repository.
2. **Set up Docker Buildx**: Prepares the environment for building Docker images.
3. **Log in to Docker Hub**: Authenticates to Docker Hub using repository secrets.
4. **Build Docker Images**: Builds images for the frontend and backend applications.
5. **Push Docker Images**: Pushes the built images to Docker Hub.
6. **Deploy to Kubernetes**: Applies the Kubernetes configuration.
7. **Sync ArgoCD**: Synchronizes the application in ArgoCD to ensure the latest changes are deployed.

### Adding Secrets to Your Repository

1. Go to your GitHub repository.
2. Click on **Settings** > **Secrets and variables** > **Actions**.
3. Click on **New repository secret**.
4. Add the following secrets:
   - **DOCKER_USERNAME**: Your Docker Hub username.
   - **DOCKER_PASSWORD**: Your Docker Hub password.

With this setup, your application will automatically build, test, and deploy on code changes, streamlining the development workflow.

---
