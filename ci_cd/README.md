# Jenkins - DevOps All-In-One Playground

This folder contains the Jenkins pipeline configuration for automating the CI/CD pipeline. The Jenkins pipeline, defined in `Jenkinsfile`, will build, test, and deploy the application to Kubernetes.

## Prerequisites

1. **Jenkins**: Ensure Jenkins is installed and accessible.
2. **Docker Hub Credentials**: Set up Docker Hub credentials in Jenkins as `docker-username` and `docker-password`.
3. **Kubernetes and ArgoCD**: Installed and configured on your Kubernetes cluster.

## Setting Up the Pipeline

### Step 1: Add Docker Hub Credentials to Jenkins

1. Go to **Jenkins Dashboard** > **Manage Jenkins** > **Manage Credentials**.
2. Add **Docker Hub credentials** with the ID `docker-credentials`:
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
   - **Sync ArgoCD**: Trigger ArgoCD to sync the latest changes.

### Example Pipeline Stages

- **Checkout**: Clones the repository.
- **Build Docker Images**: Builds Docker images for the frontend and backend.
- **Push Docker Images**: Pushes images to Docker Hub.
- **Deploy to Kubernetes**: Deploys the application to the Kubernetes cluster.
- **Sync ArgoCD**: Automatically syncs the deployment in ArgoCD.

---

This Jenkins pipeline automates the entire build, test, and deployment process, ensuring continuous integration and delivery for the DevOps All-In-One Playground application.

---

