# Kubernetes Configuration

This directory contains Kubernetes manifests for deploying the interactive DevOps quiz platform, including backend, frontend, and database components. The configuration is designed for production-grade scalability and efficiency.

## Components

### 1. Backend
- **Deployment**: Manages backend application pods.
- **Service**: Exposes backend to the frontend for API interactions.
- **Resource Limits**: Configured to ensure optimal performance.

### 2. Frontend
- **Deployment**: Hosts the React-based frontend application.
- **Service**: Makes the frontend accessible to users.
- **Ingress**: Configures domain and HTTPS for public access.

### 3. Database
- **Deployment**: Runs the database for storing user data and quiz questions.
- **Service**: Exposes the database internally to the backend.
- **Persistent Volume**: Ensures data persistence.

### 4. Monitoring and Observability
- **Prometheus**: Collects metrics from Kubernetes nodes and pods.
- **Grafana**: Visualizes metrics with pre-configured dashboards.
- **Jaeger**: Traces application workflows for debugging.

## File Descriptions

- **`deployment.yaml`**: Defines pod specifications for each component.
- **`service.yaml`**: Exposes components within the cluster or to the public.
- **`ingress.yaml`**: Handles external access via domain names and HTTPS.
- **`namespace.yaml`**: Isolates resources for better organization.

## Prerequisites

- Kubernetes cluster (minikube, kind, or a managed service like GKE, EKS, or AKS).
- Kubectl CLI installed and configured.

## Deployment Steps

1. **Create a Namespace**:
   ```bash
   kubectl apply -f namespace.yaml
   ```

2. **Deploy Backend**:
   ```bash
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f backend-service.yaml
   ```

3. **Deploy Frontend**:
   ```bash
   kubectl apply -f frontend-deployment.yaml
   kubectl apply -f frontend-service.yaml
   kubectl apply -f ingress.yaml
   ```

4. **Deploy Database**:
   ```bash
   kubectl apply -f database-deployment.yaml
   kubectl apply -f database-service.yaml
   ```

5. **Verify Deployments**:
   ```bash
   kubectl get pods -n <namespace>
   kubectl get svc -n <namespace>
   ```

## Notes

- **Resource Limits**: All deployments include resource requests and limits for production stability.
- **Ingress**: Ensure DNS settings point to your cluster's ingress controller.
- **Secrets**: Use Kubernetes Secrets for sensitive data like database credentials.

