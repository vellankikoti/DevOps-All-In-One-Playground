
# Python Scripts - DevOps All-In-One Playground

This folder contains Python scripts for automating various DevOps tasks, monitoring, and data parsing. These scripts are designed to assist with infrastructure management, data extraction, and interacting with cloud resources, making them essential for DevOps workflows.

## Folder Structure

- **automation/** - Scripts for automating common tasks, such as restarting services or connecting to remote servers.
  - `restart_service.py` - Monitors a service and restarts it if it goes down.
- **monitoring/** - Scripts to monitor application metrics and expose them to monitoring systems like Prometheus.
  - `custom_metrics.py` - Generates a custom latency metric for Prometheus.

## Automation Scripts

### 1. `restart_service.py`

This script monitors a specified service on a remote server and restarts it if the service is down. Useful for ensuring critical services remain operational.

#### Usage

1. Replace `"your-service-name"` in `restart_service.py` with the service you want to monitor.
2. Run the script:
   ```bash
   python automation/restart_service.py
   ```

The script checks the service status at regular intervals and restarts it if necessary.

### 2. Additional Automation Scripts

This folder also includes other Python scripts commonly used by DevOps engineers. Below are some examples:

- **Connect to Remote Server via SSH** - Script to establish an SSH connection and run commands remotely.
- **List EC2 Instances** - Retrieves a list of EC2 instances in a specified AWS region.
- **Check EC2 Instance Health** - Monitors the health of a specified EC2 instance.

## Monitoring and Metrics Scripts

### 1. `custom_metrics.py`

This script simulates request latency and exposes it as a Prometheus metric, allowing you to monitor custom latency metrics on the Prometheus endpoint.

#### Usage

1. Start the custom metrics server:
   ```bash
   python monitoring/custom_metrics.py
   ```
2. Access the metrics at:
   ```plaintext
   http://localhost:8000/metrics
   ```

This exposes the `app_request_latency_seconds` metric, which can be used to configure alerts or analyze application performance.

### Additional Scripts in the Repository

The repository includes other essential scripts for DevOps tasks:

1. **Get List of EC2 Instances** - Lists all EC2 instances in a specified AWS region.
2. **Fetch CloudWatch Metrics** - Retrieves metrics from CloudWatch for specific AWS resources.
3. **Extract IP Addresses from Text** - Finds and lists IP addresses from any given text input.
4. **Read URLs from a File and Save to JSON** - Converts URLs in a file into a JSON array for easier management.
5. **Get Logs of a Kubernetes Pod** - Retrieves logs from a specified Kubernetes pod.

## Running the Scripts

To execute any of the scripts, ensure you have the necessary dependencies installed (e.g., boto3 for AWS scripts, kubernetes for Kubernetes scripts, Prometheus client for metrics). Use `pip install -r requirements.txt` if provided, or install dependencies individually as needed.

---

These Python scripts offer powerful, customizable tools for managing DevOps environments, automating tasks, and monitoring critical infrastructure metrics. Feel free to modify them as needed to fit your specific requirements.

---
