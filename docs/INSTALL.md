
# Installation Guide

Follow these steps to set up the DevOps All-In-One Playground on your local machine or development environment.

## Prerequisites

1. **Docker**: Ensure you have Docker installed. You can download it from [Docker's official site](https://www.docker.com/get-started).
2. **Kubernetes**: Set up a Kubernetes cluster (e.g., using Minikube or a cloud provider).
3. **kubectl**: Install kubectl to manage your Kubernetes cluster.
4. **Python**: Ensure Python is installed (version 3.6 or later).
5. **Node.js**: Install Node.js for the frontend application.

## Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/vellankikoti/DevOps-All-In-One-Playground.git
   cd DevOps-All-In-One-Playground
   ```

2. Navigate to the respective directories and build the Docker images:
   ```bash
   cd frontend
   docker build -t your_dockerhub_username/devops-frontend:latest .
   
   cd ../backend
   docker build -t your_dockerhub_username/devops-backend:latest .
   ```

3. Start the services using Docker Compose (if applicable):
   ```bash
   docker-compose up -d
   ```

4. Apply the Kubernetes configurations:
   ```bash
   kubectl apply -f kubernetes/
   ```

5. Set up observability tools by following the respective configuration guides in the observability directory.

You are now ready to use the DevOps All-In-One Playground!
