# DevOps-All-In-One-Playground 🚀

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#detailed-setup">Detailed Setup</a> •
  <a href="#tools-integrated">Tools Integrated</a> •
  <a href="#contributing">Contributing</a>
</p>

Welcome to the **DevOps-All-In-One-Playground** - your comprehensive hands-on laboratory for mastering modern DevOps practices! This playground is designed to provide a rich learning environment for both beginners and seasoned professionals, offering a full-stack application setup with integrated DevOps tools.

## 🎯 Overview

This repository is a one-stop resource for DevOps engineers, featuring:
- A complete sample application stack using Python for the backend and React for the frontend.
- Pre-configured environments for essential DevOps tools.
- Comprehensive monitoring and observability setup.
- Real-world deployment scenarios and examples.

## ✨ Features

### 1. Complete Application Stack
- **Backend**: Python/Flask REST API with PostgreSQL
- **Frontend**: React-based user interface
- **Database**: PostgreSQL with initial schema and migrations

### 2. DevOps Tools Integration
- **Containerization**: Docker with multi-stage builds
- **Orchestration**: Kubernetes configurations for scalable deployments
- **CI/CD**: Jenkins, GitHub Actions, and GitLab CI for automated pipelines
- **GitOps**: ArgoCD for managing Kubernetes resources
- **Infrastructure as Code**: Terraform for provisioning cloud resources
- **Configuration Management**: Ansible for automating application setup and configuration
### 3. Observability Stack
- **Metrics**: Prometheus for collecting and querying metrics
- **Visualization**: Grafana dashboards for data visualization
- **Tracing**: OpenTelemetry with Jaeger for distributed tracing
- **Logging**: ELK Stack integration for centralized logging

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git
- Kubernetes cluster (optional)
- AWS account (optional)
- Python environment
- Ansible installed

### Basic Setup


### Verify Installation
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- Grafana: http://localhost:3001
- Prometheus: http://localhost:9090

## 📂 Repository Structure

```plaintext
DevOps-All-In-One-Playground/
├── sample-app/                  # Sample application
│   ├── backend/                 # Python/Flask backend
│   │   ├── app.py               # Main application file
│   │   ├── requirements.txt     # Python dependencies
│   │   ├── Dockerfile           # Dockerfile for backend
│   │   ├── tests/               # Unit tests for backend
│   │   │   └── test_app.py      # Example test file
│   │   └── README.md            # Documentation for backend
│   ├── frontend/                # React frontend
│   │   ├── src/                 # Source files
│   │   ├── public/              # Public assets
│   │   ├── package.json         # Node.js dependencies
│   │   ├── Dockerfile           # Dockerfile for frontend
│   │   └── README.md            # Documentation for frontend
│   ├── database/                # Database setup
│   │   ├── schema.sql           # SQL schema
│   │   ├── Dockerfile           # Dockerfile for database
│   │   └── README.md            # Documentation for database
│   └── README.md                # Overall app documentation
├── docker/                      # Docker configurations
│   ├── docker-compose.yml       # Docker Compose file
│   ├── .env                     # Environment variables
│   └── README.md                # Docker setup instructions
├── kubernetes/                  # Kubernetes manifests
│   ├── deployment.yaml          # Deployment configuration
│   ├── service.yaml             # Service configuration
│   ├── ingress.yaml             # Ingress configuration
│   ├── configmap.yaml           # ConfigMap for environment variables
│   └── README.md                # Kubernetes setup instructions
├── terraform/                   # Terraform configurations
│   ├── main.tf                  # Main Terraform file
│   ├── variables.tf             # Variables for Terraform
│   ├── outputs.tf               # Outputs for Terraform
│   └── README.md                # Terraform setup instructions
├── cicd/                        # CI/CD configurations
│   ├── Jenkinsfile              # Jenkins pipeline script
│   ├── .github/                 # GitHub Actions workflows
│   │   └── workflows/
│   │       └── ci.yml           # CI workflow for GitHub Actions
│   └── README.md                # CI/CD setup instructions
├── argocd/                      # ArgoCD setup
│   ├── applications/            # ArgoCD application definitions
│   │   └── quiz-platform.yaml   # ArgoCD app for quiz platform
│   ├── projects/                # ArgoCD project definitions
│   │   └── devops-project.yaml  # ArgoCD project definition
│   └── README.md                # ArgoCD setup instructions
├── observability/               # Monitoring tools
│   ├── prometheus/              # Prometheus configuration
│   ├── grafana/                 # Grafana configuration
│   ├── opentelemetry/           # OpenTelemetry collector
│   ├── jaeger/                  # Jaeger tracing setup
│   └── README.md                # Observability setup instructions
├── docs/                        # Documentation
│   ├── INSTALL.md               # Installation instructions
│   ├── USAGE.md                 # Usage instructions
│   ├── CONTRIBUTING.md          # Contribution guidelines
│   └── README.md                # General repo documentation
└── LICENSE                      # MIT License

```

## 🛠 Tools Integrated

### Development & Deployment
- **Python**: Backend development
- **Docker & Docker Compose**: Containerization
- **Kubernetes**: Orchestration
- **Helm Charts**: Kubernetes package management
- **ArgoCD**: GitOps continuous delivery
- **Terraform**: Infrastructure as Code
- **Ansible**: Configuration management

### CI/CD Pipelines
- **Jenkins**: Continuous integration
- **GitHub Actions**: Workflow automation
- **GitLab CI**: CI/CD pipelines

### Monitoring & Observability
- **Prometheus**: Metrics collection
- **Grafana**: Data visualization
- **OpenTelemetry & Jaeger**: Distributed tracing
- **ELK Stack**: Logging

## 📚 Learning Paths

### 1. Basic Path
- Deploy the sample application
- Monitor basic metrics
- Implement simple CI/CD pipeline

### 2. Intermediate Path
- Kubernetes deployment
- Monitoring and alerting
- Distributed tracing

### 3. Advanced Path
- GitOps with ArgoCD
- Infrastructure as Code
- Custom metrics and SLOs

## 🔧 Detailed Setup

### 1. Local Development

bash

Deploy monitoring stack
kubectl apply -f observability/

Access Grafana
kubectl port-forward svc/grafana 3000:3000


## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### How to Contribute
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

Need help? Check out:
- [Documentation](docs/)
- [Issue Tracker](../../issues)
- [Discussions](../../discussions)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vellankikoti/DevOps-All-In-One-Playground&type=Date)](https://star-history.com/#vellankikoti/DevOps-All-In-One-Playground&Date)

## 📊 Project Status

![GitHub stars](https://img.shields.io/github/stars/vellankikoti/DevOps-All-In-One-Playground?style=social)
![GitHub forks](https://img.shields.io/github/forks/vellankikoti/DevOps-All-In-One-Playground?style=social)
![GitHub issues](https://img.shields.io/github/issues/vellankikoti/DevOps-All-In-One-Playground)
![GitHub pull requests](https://img.shields.io/github/issues-pr/vellankikoti/DevOps-All-In-One-Playground)

---

<p align="center">
  Made with ❤️ for the DevOps community
</p>
