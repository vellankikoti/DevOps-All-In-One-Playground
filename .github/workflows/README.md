# CI/CD Setup - DevOps All-In-One Playground

This CI/CD setup uses GitHub Actions to automate the build, test, and deployment process for the DevOps All-In-One Playground application.

## 📦 Prerequisites

- **GitHub Repository** with code and Dockerfiles
- **GitHub Secrets**:
  - `DOCKER_USERNAME`: Your Docker Hub username
  - `DOCKER_PASSWORD`: Your Docker Hub password
  - `KUBECONFIG`: Your Kubernetes configuration file contents (base64 encoded if needed)

## Workflow Overview

The GitHub Actions workflow, defined in `.github/workflows/ci-cd.yml`, is triggered on every push to the `main` branch. It performs the following steps:

1. **Checkout Code**: Retrieves the latest code from the repository.
2. **Install Dependencies and Run Tests**:
   - **Frontend**: Installs dependencies, builds the app, and runs tests.
   - **Backend**: Installs dependencies, runs tests, and connects to a PostgreSQL database for testing.
3. **Build and Push Docker Images**:
   - Builds Docker images for frontend and backend.
   - Pushes images to Docker Hub using credentials stored in GitHub Secrets.
4. **Deploy to Kubernetes**:
   - Applies Kubernetes deployment files to update the frontend, backend, and database services.

## Setting Up GitHub Secrets

1. Go to your GitHub repository.
2. Navigate to **Settings > Secrets and variables > Actions > New repository secret**.
3. Add the following secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username.
   - `DOCKER_PASSWORD`: Your Docker Hub password.
   - `KUBECONFIG`: Contents of your Kubernetes configuration file.

## Running the Workflow

1. Make a push to the `main` branch.
2. The workflow will automatically run, performing all build, test, and deployment steps.

Monitor the workflow progress under **Actions** in the GitHub repository.

---

This GitHub Actions workflow provides continuous integration and continuous deployment (CI/CD) for the DevOps All-In-One Playground, ensuring a seamless and automated deployment process.

---
