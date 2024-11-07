
# Observability - DevOps All-In-One Playground

This observability setup includes Prometheus, Grafana, OpenTelemetry, and Jaeger to monitor and trace the DevOps All-In-One Playground application.

## 📦 Installation

### Prerequisites
- **Docker** and **Docker Compose** for containerized observability setup
- **Kubernetes** and **kubectl** (if deploying on Kubernetes)

## Prometheus Setup

### Run Prometheus with Docker
1. Start Prometheus with the configuration file:
   ```bash
   docker run -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
   ```

Prometheus will be available at `http://localhost:9090`.

### Run Prometheus on Kubernetes
1. Apply the Prometheus configuration in Kubernetes:
   ```bash
   kubectl apply -f kubernetes/prometheus-deployment.yaml
   ```

## Grafana Setup

### Run Grafana with Docker
1. Start Grafana and link it with Prometheus:
   ```bash
   docker run -d -p 3000:3000 --name=grafana grafana/grafana
   ```

2. Add Prometheus as a data source in Grafana:
   - URL: `http://prometheus:9090`

3. Import the `sample-dashboard.json` from the `grafana/dashboards/` folder to set up the sample dashboard.

### Run Grafana on Kubernetes
1. Apply the Grafana configuration in Kubernetes:
   ```bash
   kubectl apply -f kubernetes/grafana-deployment.yaml
   ```

Grafana will be available at `http://localhost:3000`.

## Jaeger Setup (Optional for Tracing)

### Run Jaeger with Docker
1. Start Jaeger:
   ```bash
   docker run -d --name jaeger -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 -p 16686:16686 -p 14268:14268 jaegertracing/all-in-one:1.21
   ```

Jaeger will be available at `http://localhost:16686`.

### Run Jaeger on Kubernetes
1. Apply the Jaeger configuration in Kubernetes:
   ```bash
   kubectl apply -f kubernetes/jaeger-deployment.yaml
   ```

## OpenTelemetry Setup (Optional for Distributed Tracing)

1. Instrument the backend and frontend with OpenTelemetry SDKs.
2. Configure OpenTelemetry to send traces to Jaeger:
   ```yaml
   OTEL_EXPORTER_JAEGER_ENDPOINT=http://jaeger:14268/api/traces
   ```

---

This observability setup provides full visibility into the application, allowing you to monitor metrics, visualize traces, and gain insights into system health.

---

