
# DevOps-All-In-One-Playground

**DevOps-All-In-One-Playground** is the ultimate resource for DevOps engineers to practice, deploy, and master a wide range of tools and scenarios in real-world environments. This repository integrates essential DevOps tools and observability solutions, providing an adaptable, easy-to-setup application for learning and experimentation.

## 📖 Overview

This playground is designed to bring together critical DevOps tools like Git, Jenkins, Docker, Kubernetes, ArgoCD, and Terraform, along with observability stacks (Prometheus, Grafana, OpenTelemetry, Jaeger). It allows you to set up, monitor, and test configurations, deployments, and CI/CD pipelines with an application built to be scalable, interactive, and long-lasting.

### Key Features
- **End-to-End CI/CD Pipelines**: Integrate CI/CD using GitHub Actions or Jenkins to automate testing and deployment.
- **Containerization and Orchestration**: Dockerized setup with Kubernetes deployments for easy scalability.
- **Observability Stack**: Monitor the app with Prometheus, Grafana, OpenTelemetry, and Jaeger for full visibility.
- **Adaptable and Cloud-Ready**: Deploy locally or on any cloud, making it ideal for learning or testing in real environments.
- **GitOps-Friendly**: Integrate ArgoCD for GitOps-style deployments.

## 🗂 Repository Structure

```plaintext
DevOps-All-In-One-Playground/
├── frontend/               # React app for UI
├── backend/                # Node.js API for CRUD operations
├── database/               # PostgreSQL setup and schema
├── observability/          # Prometheus, Grafana, OpenTelemetry, Jaeger configurations
├── kubernetes/            # Kubernetes YAML files for deployments and services
├── .github/workflows/      # CI/CD pipeline configuration
├── docs/                   # Documentation for setup and usage
└── docker-compose.yml      # Docker Compose setup for local development
```

Each folder contains a `README.md` with specific setup instructions for that component.

## 🚀 Quick Start Guide

This guide will help you get the **DevOps-All-In-One-Playground** up and running locally.

### Prerequisites
- **Docker** and **Docker Compose**
- **Node.js** and **npm** (if you want to test frontend/backend without Docker)
- **Kubernetes** and **kubectl** (if deploying on Kubernetes)
- **Prometheus** and **Grafana** (optional, for observability)

### Step 1: Clone the Repository
```bash
git clone https://github.com/vellankikoti/DevOps-All-In-One-Playground.git
cd DevOps-All-In-One-Playground
```

### Step 2: Run Locally with Docker Compose
This command will start the `frontend`, `backend`, and `database` services.
```bash
docker-compose up -d
```

- Access the frontend at `http://localhost:3000`
- The backend API is available at `http://localhost:5000`
- The PostgreSQL database runs on port `5432`

### Step 3: Access Observability Tools (Optional)
To monitor application metrics, configure **Prometheus** and **Grafana** using the files in the `observability/` directory. This setup will give you access to pre-configured dashboards for tracking metrics and performance.

### Step 4: Deploy on Kubernetes
To deploy on a Kubernetes cluster (local or cloud-based):
1. Make sure Kubernetes and `kubectl` are installed.
2. Apply the Kubernetes configurations:

   ```bash
   kubectl apply -f kubernetes/
   ```

3. Verify deployments and services:
   ```bash
   kubectl get pods
   kubectl get services
   ```

### Step 5: Set Up CI/CD Pipeline
This repo includes a GitHub Actions workflow (`.github/workflows/ci-cd.yml`) to automate build and deployment on every push to the `main` branch.

To use Jenkins, configure your Jenkins pipeline to integrate with this repository and enable automated builds and deployments.

## 📊 Observability and Monitoring

The `observability/` folder provides configurations for:
- **Prometheus**: Metrics collection and alerting.
- **Grafana**: Dashboard visualization for system health and performance.
- **OpenTelemetry & Jaeger**: Distributed tracing and detailed application monitoring.

With these tools, you can observe real-time metrics, view traces, and monitor the application's health.

## 🎯 Use Cases

- **Learning DevOps Tools**: Perfect for practicing real-world DevOps skills.
- **Building CI/CD Pipelines**: Integrate and test complete automation pipelines.
- **Monitoring and Observability**: Set up comprehensive monitoring solutions to gain insights into application performance.
- **Cloud-Ready Deployments**: Deploy on any cloud platform or on-premises Kubernetes cluster.

## Getting Started

For detailed setup instructions, refer to the [Setup Guide](docs/setup_guide.md).

---

**Enjoy exploring the DevOps-All-In-One-Playground!** This repository is designed to help DevOps engineers learn, deploy, and practice DevOps concepts through hands-on, real-world scenarios.

---

## 📬 Feedback

If you have suggestions or encounter any issues, feel free to open an issue or submit a pull request. Your contributions are always welcome!

---

Happy DevOps-ing! 🚀
