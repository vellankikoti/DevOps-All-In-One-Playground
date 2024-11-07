
# Observability - DevOps All-In-One Playground

This folder contains configurations for setting up observability using Prometheus, Grafana, and OpenTelemetry. These tools collect, visualize, and analyze metrics and traces from the backend and frontend services in the application.

## Prometheus Setup

Prometheus is configured to scrape and store metrics from multiple sources, including:
- **Backend**: Exposed on port `5000`.
- **Frontend**: Exposed on port `3000`.
- **Prometheus** itself for self-monitoring.
- **OpenTelemetry Collector** for distributed tracing and additional metrics.

### Configuration

- **File**: `prometheus.yml`
- **Usage**: Modify `scrape_configs` to add or update target endpoints for metrics scraping.

### Start Prometheus

1. Run Prometheus with the configuration file:
   ```bash
   prometheus --config.file=observability/prometheus.yml
   ```

2. Access Prometheus at:
   ```
   http://localhost:9090
   ```

---

## Grafana Setup

Grafana provides a user-friendly interface to visualize metrics stored in Prometheus.

### Import Dashboard

- **File**: `dashboards/sample-dashboard.json`
- **Usage**: Import this JSON file into Grafana to visualize metrics from the backend, frontend, and system resources (CPU, memory).

### Start Grafana

1. Run Grafana:
   ```bash
   grafana-server
   ```
2. Access Grafana at:
   ```
   http://localhost:3000
   ```

---

## OpenTelemetry Setup

OpenTelemetry is configured to collect traces and additional metrics from the backend and frontend, then exports them to Prometheus.

### Configuration

- **File**: `opentelemetry/otel_config.yaml`
- **Usage**: Update endpoints and exporters as needed.

### Start OpenTelemetry Collector

1. Run the OpenTelemetry collector:
   ```bash
   otelcol --config=observability/opentelemetry/otel_config.yaml
   ```

---

## Custom Metrics with OpenTelemetry

The `metrics.py` script collects custom application metrics and exposes them for scraping by Prometheus.

### File: `opentelemetry/metrics.py`

This script sets up a Flask application that provides metrics on request latency and total request count.

#### Usage

1. Ensure you have the required packages installed:
   ```bash
   pip install flask prometheus_client
   ```

2. Run the script:
   ```bash
   python opentelemetry/metrics.py
   ```

3. Access the metrics at:
   ```
   http://localhost:8000/metrics
   ```

4. The application processes requests on:
   ```
   http://localhost:5000/process
   ```

With this setup, you can monitor the application's performance and visualize key metrics and traces in real-time.

---
