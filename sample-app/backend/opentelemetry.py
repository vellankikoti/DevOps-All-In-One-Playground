from opentelemetry import trace
from opentelemetry.ext.flask import FlaskInstrumentor
from opentelemetry.exporter.prometheus import PrometheusMetrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource

resource = Resource.create({"service.name": "flask-backend"})
trace.set_tracer_provider(MeterProvider(resource=resource))

metrics = PrometheusMetrics(app)
FlaskInstrumentor().instrument_app(app)