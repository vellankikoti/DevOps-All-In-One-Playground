
# Kubernetes Deployment - DevOps All-In-One Playground

This Kubernetes setup allows you to deploy the DevOps All-In-One Playground application on a Kubernetes cluster. It includes configurations for the frontend, backend, and PostgreSQL database.

## Prerequisites
- **Kubernetes** and **kubectl** installed
- **Docker** to build images, if necessary

## Deploying the Application

### Step 1: Apply ConfigMap for Database Initialization
1. Create a ConfigMap for the PostgreSQL `init.sql` file:
   ```bash
   kubectl apply -f kubernetes/db-init-config.yaml
   ```

### Step 2: Deploy the Database
1. Deploy the PostgreSQL database:
   ```bash
   kubectl apply -f kubernetes/database-deployment.yaml
   ```

### Step 3: Deploy the Backend Service
1. Deploy the backend service with environment variables for database connection:
   ```bash
   kubectl apply -f kubernetes/backend-deployment.yaml
   ```

### Step 4: Deploy the Frontend Service
1. Deploy the frontend service:
   ```bash
   kubectl apply -f kubernetes/frontend-deployment.yaml
   ```

## Verify Deployments

1. Check that all pods are running:
   ```bash
   kubectl get pods
   ```

2. Check services to find NodePort or LoadBalancer IPs for accessing frontend and backend:
   ```bash
   kubectl get services
   ```

### Accessing the Application

- **Frontend**: Access using the IP and NodePort displayed under `frontend-service`.
- **Backend**: Access using the IP and NodePort displayed under `backend-service`.

This Kubernetes setup is designed to provide seamless deployment, scaling, and access to all application components.

---

