# Jenkins - CI/CD Setup for DevOps All-In-One Playground

This folder contains the Jenkins pipeline configuration for automating the CI/CD process for the DevOps All-In-One Playground application.

## Prerequisites

1. **Jenkins**: Ensure Jenkins is installed and running.
2. **Docker**: Installed on the Jenkins server for building and pushing images.
3. **Docker Hub Credentials**: Set up Docker Hub credentials in Jenkins with IDs `docker-username` and `docker-password`.
4. **kubectl**: Installed and configured on the Jenkins server to deploy applications to Kubernetes.
5. **ArgoCD**: Installed and configured to manage application deployments.

## Setting Up the Pipeline

### Step 1: Add Docker Hub Credentials to Jenkins

1. Go to **Jenkins Dashboard** > **Manage Jenkins** > **Manage Credentials**.
2. Add **Docker Hub credentials** with IDs `docker-username` and `docker-password`:
   - **Username**: Your Docker Hub username.
   - **Password**: Your Docker Hub password.

### Step 2: Create a New Pipeline Job in Jenkins

1. From the Jenkins Dashboard, select **New Item**.
2. Enter a name for the pipeline (e.g., `DevOps-All-In-One-Playground-CI/CD`), select **Pipeline**, and click **OK**.
3. In the **Pipeline** section, select **Pipeline script from SCM**.
4. Enter the repository URL: `https://github.com/vellankikoti/DevOps-All-In-One-Playground.git`.
5. Set the branch to `main`.
6. Save the pipeline configuration.

### Step 3: Run the Pipeline

1. To start the pipeline, click **Build Now** in the project dashboard.
2. The pipeline will:
   - **Checkout Code**: Retrieve the latest code from the GitHub repository.
   - **Build Docker Images**: Build Docker images for the frontend and backend.
   - **Push Docker Images**: Push the images to Docker Hub.
   - **Deploy to Kubernetes**: Apply Kubernetes configuration files.
   - **Sync ArgoCD**: Automatically sync the deployment in ArgoCD.

## Example Pipeline Stages

- **Checkout**: Clones the repository.
- **Build Docker Images**: Builds Docker images for the frontend and backend.
- **Push Docker Images**: Pushes images to Docker Hub.
- **Deploy to Kubernetes**: Deploys the application to the Kubernetes cluster.
- **Sync ArgoCD**: Automatically syncs the deployment in ArgoCD.

---

This Jenkins setup automates the entire build, test, and deployment process, ensuring continuous integration and delivery for the DevOps All-In-One Playground application.

---
