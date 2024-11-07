
# Ansible - DevOps All-In-One Playground

This folder contains Ansible playbooks for managing deployments in Kubernetes, along with additional interactive tasks to make the deployment more informative and engaging.

## Overview

The `deploy.yml` playbook in this folder performs the following actions:
1. **Deploy Kubernetes Configurations**: Applies the Kubernetes deployment files.
2. **Health Check**: Verifies if the backend pod is running successfully.
3. **Fetch IP Address**: Retrieves the NodePort IP for the frontend service, making it accessible.
4. **Time-Based Greeting**: Displays a greeting based on the current server time (e.g., Good Morning, Good Afternoon).

This setup ensures that deployments are interactive and informative, making it clear when the application is ready and accessible.

## 📦 Prerequisites

- **Ansible**: Ensure Ansible is installed on your machine.
- **kubectl**: Installed and configured to access the Kubernetes cluster.

## Running the Playbook

To execute the playbook, use the following command:

```bash
ansible-playbook deploy.yml
```

### Example Output

- **Deployment Confirmation**: Confirms that Kubernetes configurations have been applied.
- **Backend Health Check**: Verifies if the backend pod is healthy.
- **Frontend NodePort IP**: Provides the IP or NodePort to access the frontend service.
- **Time-Based Greeting**: Displays a friendly greeting based on the current time.

Example output may look like this:

```plaintext
TASK [Deploy application to Kubernetes] ********************************************************************
ok: [localhost]

TASK [Display deployment output] ***************************************************************************
ok: [localhost] => (item=Your application deployment output)

TASK [Check backend pod status] ****************************************************************************
ok: [localhost] => {
    "msg": "Backend pod is running and healthy"
}

TASK [Display frontend NodePort] ***************************************************************************
ok: [localhost] => {
    "msg": "Frontend is accessible on NodePort 30001"
}

TASK [Display greeting based on time] **********************************************************************
ok: [localhost] => {
    "msg": "Good afternoon! The application is deployed successfully."
}
```

## Customization

You can add more tasks to the playbook for further interactivity or to gather additional information about the environment.

---

This Ansible playbook is designed to simplify the deployment process and ensure real-time feedback on the application’s status.

---

