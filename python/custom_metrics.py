from prometheus_client import start_http_server, Gauge
import random
import time

# Define a Prometheus metric
REQUEST_LATENCY = Gauge('app_request_latency_seconds', 'Latency of requests in seconds')

def simulate_request():
    """Simulates a request with random latency."""
    latency = random.uniform(0.1, 1.0)
    REQUEST_LATENCY.set(latency)
    print(f"Simulated request latency: {latency} seconds")
    time.sleep(1)

if __name__ == "__main__":
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Starting custom metrics server on http://localhost:8000/metrics")
    
    while True:
        simulate_request()
