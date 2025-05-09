# Stack notes

## 🧩 Overview of the Stack

1. Jaeger (Tracing)

   Collects and visualizes distributed traces.

   Helps understand request flows across services.

   OpenTelemetry sends spans to Jaeger (via OTEL Collector).

2. Prometheus (Metrics)

   Collects and stores time-series metrics.

   Scrapes data from services, exporters, and OTEL Collector.

3. Grafana (Visualization)

   Visualizes both metrics from Prometheus and traces from Jaeger.

   Supports alerts, dashboards, and correlation of logs/metrics/traces.

4. OTEL Collector

   Acts as a bridge: receives telemetry from your app, forwards it to Jaeger (traces) and Prometheus (metrics).

## 📦 Architecture Flow

```text
Lambda (via OpenTelemetry SDK)
     ↓
OTEL Collector
 ↙         ↘
Jaeger     Prometheus
     ↘        ↙
        Grafana
```
