
# Frontend - DevOps All-In-One Playground

This is the frontend for the DevOps All-In-One Playground, built with React. It allows users to create, view, update, and delete records via the backend API.

## 📦 Installation

### Prerequisites
- **Node.js** and **npm**

### Run Locally
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the app:
   ```bash
   npm start
   ```

The app will be accessible at `http://localhost:3000`.

### Run with Docker
To build and run the app in a Docker container:
1. Build the Docker image:
   ```bash
   docker build -t devops-frontend .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 3000:3000 devops-frontend
   ```

## 🚀 Deployment
For deployment on Kubernetes or other platforms, use the provided Dockerfile and Kubernetes configurations.

---
