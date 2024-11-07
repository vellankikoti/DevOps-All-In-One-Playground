import os
import subprocess
import time

def check_service(service_name):
    """Checks if a service is running."""
    status = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)
    return status.stdout.strip() == "active"

def restart_service(service_name):
    """Restarts the specified service."""
    subprocess.run(["sudo", "systemctl", "restart", service_name])
    print(f"Service '{service_name}' has been restarted.")

def monitor_and_restart(service_name, interval=30):
    """Monitors the service and restarts if it’s down."""
    while True:
        if not check_service(service_name):
            print(f"Service '{service_name}' is down. Attempting to restart...")
            restart_service(service_name)
        else:
            print(f"Service '{service_name}' is running.")
        time.sleep(interval)

if __name__ == "__main__":
    service = "your-service-name"  # Replace with your service name
    monitor_and_restart(service)
