
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
├── backend/                      # Backend application (Flask)
│   ├── app.py                    # Main Flask application file
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # Docker configuration for backend
│   ├── questions.json            # Quiz questions for the application
│   ├── tests/                    # Unit tests for backend
│   │   └── test_app.py           # Example test file
│   └── README.md                 # Backend documentation
├── frontend/                     # Frontend application (React)
│   ├── src/                      # Source files
│   │   ├── App.js                # Main application file
│   │   ├── Home.js               # Landing page component
│   │   ├── Progress.js           # Progress tracking component
│   │   ├── Result.js             # Result display component
│   │   ├── components/           # Additional reusable components
│   │   │   ├── Header.js         # Header for navigation
│   │   │   └── Challenge.js      # Quiz component for each section
│   │   ├── styles/               # CSS files for styling
│   │   │   ├── App.css           # Global styles
│   │   │   ├── Header.css        # Header-specific styles
│   │   │   └── Progress.css      # Progress tracker styles
│   │   ├── api/                  # API utility functions
│   │   │   └── api.js            # Functions for backend interaction
│   ├── index.js                  # Entry point for React application
│   ├── public/                   # Static files
│   │   └── index.html            # Main HTML file
│   ├── Dockerfile                # Docker configuration for frontend
│   └── README.md                 # Frontend documentation
├── database/                     # Database setup
│   ├── init.sql                  # SQL script for initializing database
│   ├── Dockerfile                # Docker configuration for database
│   └── README.md                 # Database documentation
├── docker/                       # Docker Compose setup
│   ├── docker-compose.yml        # Compose configuration for all services
│   ├── .env                      # Environment variables for Docker
│   └── README.md                 # Docker documentation
├── kubernetes/                   # Kubernetes manifests
│   ├── namespace.yaml            # Namespace configuration
│   ├── ingress.yaml              # Ingress configuration
│   ├── frontend-deployment.yaml  # Deployment for frontend
│   ├── backend-deployment.yaml   # Deployment for backend
│   ├── database-deployment.yaml  # Deployment for database
│   ├── database-pvc.yaml         # Persistent Volume Claim for database
│   ├── service.yaml              # Service configuration for all components
│   └── README.md                 # Kubernetes documentation
├── argocd/                       # ArgoCD configuration
│   ├── applications/             # Application definitions for ArgoCD
│   │   └── devops-app.yaml       # Example application
│   ├── projects/                 # Project definitions for ArgoCD
│   │   └── devops-project.yaml   # Example project
│   └── README.md                 # ArgoCD documentation
├── terraform/                    # Infrastructure as Code (IaC) setup
│   ├── main.tf                   # Main Terraform configuration
│   ├── variables.tf              # Variables for Terraform
│   ├── outputs.tf                # Outputs for Terraform
│   ├── eks-cluster.tf            # EKS cluster setup
│   ├── s3-bucket.tf              # S3 bucket for state storage
│   └── README.md                 # Terraform documentation
├── observability/                # Monitoring and observability
│   ├── grafana/                  # Grafana configuration
│   │   ├── dashboards/           # Prebuilt dashboards
│   │   │   ├── k8s-dashboard.json # Kubernetes monitoring dashboard
│   │   │   ├── app-dashboard.json # Application monitoring dashboard
│   │   │   └── server-dashboard.json # Server monitoring dashboard
│   ├── prometheus/               # Prometheus configuration
│   │   ├── prometheus.yml        # Prometheus config file
│   │   ├── k8s-metrics-rules.yml # Kubernetes metrics alert rules
│   │   └── server-metrics-rules.yml # Server metrics alert rules
│   ├── opentelemetry/            # OpenTelemetry configuration
│   │   └── otel-collector.yml    # OpenTelemetry collector config
│   ├── jaeger/                   # Jaeger tracing setup
│   │   ├── jaeger-deployment.yaml # Jaeger deployment config
│   │   └── jaeger-service.yaml   # Jaeger service config
│   └── README.md                 # Observability documentation
├── docs/                         # Documentation
│   ├── INSTALL.md                # Installation instructions
│   ├── USAGE.md                  # Usage instructions
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   └── README.md                 # General documentation
└── LICENSE.md                    # Licensing information
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
