```markdown
# Observability Configuration

This directory contains configurations for setting up a complete observability stack for the interactive DevOps quiz platform. It includes monitoring, logging, and tracing using Prometheus, Grafana, and Jaeger, along with OpenTelemetry integration for distributed tracing.

## Features

- **Monitoring**: Prometheus collects metrics from Kubernetes nodes, pods, and the application.
- **Dashboards**: Grafana visualizes metrics with pre-configured dashboards for Kubernetes resources and application performance.
- **Tracing**: Jaeger provides end-to-end distributed tracing for debugging and performance analysis.
- **OpenTelemetry**: Captures and exports telemetry data (logs, metrics, and traces) to observability tools.

## Components

### 1. Prometheus
- Collects metrics from Kubernetes and application endpoints.
- Configured to scrape metrics from:
  - Kubernetes API server
  - Application endpoints (backend and frontend)

### 2. Grafana
- Visualizes metrics with dashboards for:
  - Kubernetes cluster health
  - Application resource usage
  - Database performance
- Pre-configured with Prometheus as the data source.

### 3. Jaeger
- Provides distributed tracing to monitor application workflows.
- Captures traces for user interactions like login, quiz attempts, and score generation.

### 4. OpenTelemetry
- Integrated into the application for standardized telemetry data.
- Sends traces to Jaeger and metrics to Prometheus.

## Prerequisites

- A running Kubernetes cluster with sufficient resources.
- Kubectl CLI installed and configured.

## File Descriptions

- **`prometheus.yaml`**: Prometheus deployment and configuration.
- **`grafana.yaml`**: Grafana deployment with pre-configured dashboards.
- **`jaeger.yaml`**: Jaeger deployment and service for distributed tracing.
- **`otel-collector.yaml`**: OpenTelemetry collector configuration for logs, metrics, and traces.
- **`dashboards/`**: Grafana dashboard JSON files for easy import.

## Deployment Steps

### 1. Deploy Prometheus
```bash
kubectl apply -f prometheus.yaml
```

### 2. Deploy Grafana
```bash
kubectl apply -f grafana.yaml
```
- Access Grafana:
  ```bash
  kubectl -n monitoring port-forward svc/grafana 3000:3000
  ```
  Open your browser at `http://localhost:3000`. Default credentials: `admin/admin`.

### 3. Deploy Jaeger
```bash
kubectl apply -f jaeger.yaml
```
- Access Jaeger:
  ```bash
  kubectl -n monitoring port-forward svc/jaeger-query 16686:16686
  ```
  Open your browser at `http://localhost:16686`.

### 4. Deploy OpenTelemetry Collector
```bash
kubectl apply -f otel-collector.yaml
```

### 5. Verify Configuration
- **Prometheus**: Check targets and scrape configurations at `http://localhost:9090/targets`.
- **Grafana**: Import dashboards from the `dashboards/` directory.
- **Jaeger**: Trace application workflows via the Jaeger UI.

## Notes

- **Application Instrumentation**:
  - Ensure the backend application has Prometheus metrics endpoints and OpenTelemetry libraries configured.
  - Integrate logs and traces for key user actions (e.g., login, quiz attempts).

- **Resource Limits**:
  - All deployments include resource limits for stability in production environments.

- **Custom Dashboards**:
  - Modify or create dashboards in the `dashboards/` directory and import them into Grafana.

## Pre-configured Dashboards

1. **Kubernetes Cluster Health**:
   - Node usage (CPU, memory, disk)
   - Pod status and resource usage
2. **Application Metrics**:
   - Backend API latency and request count
   - Database query performance
3. **User Analytics**:
   - Active users
   - Quiz completion rates
4. **Tracing Details**:
   - User interactions across services via Jaeger.

## Conclusion

This observability stack provides a comprehensive view of the platform's health and performance. Logs, metrics, and traces are integrated to ensure seamless debugging and proactive issue resolution.

For troubleshooting or enhancements, refer to the individual configurations or explore [Prometheus Documentation](https://prometheus.io/docs/), [Grafana Documentation](https://grafana.com/docs/), and [Jaeger Documentation](https://www.jaegertracing.io/docs/).
```