
from prometheus_client import start_http_server, Counter, Histogram
from flask import Flask, request
import time

app = Flask(__name__)

# Define a Counter metric to count requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests received')

# Define a Histogram metric to measure request latency
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds')

@app.route('/metrics', methods=['GET'])
def metrics():
    """Endpoint for Prometheus to scrape metrics."""
    return generate_latest(), 200, {'Content-Type': REGISTRY_CONTENT_TYPE}

@app.route('/process', methods=['GET'])
@REQUEST_LATENCY.time()  # Measure request latency
def process_request():
    """Simulate processing a request."""
    REQUEST_COUNT.inc()  # Increment request counter
    time.sleep(0.5)  # Simulate some processing time
    return "Request processed!"

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8000)  # Expose metrics on port 8000
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app on port 5000
