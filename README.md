# Local AWS Lambda Observability Demo

This project simulates an AWS Lambda function locally using Docker, instrumented with OpenTelemetry to demonstrate full-stack observability. It integrates tracing, metrics, and dashboards with Jaeger, Prometheus, and Grafana.

---

## 🔧 Stack Overview

- **App**: Python Lambda function using AWS Lambda base image
- **OpenTelemetry**: SDK + Collector for exporting telemetry data
- **Jaeger**: View distributed traces
- **Prometheus**: Collect metrics
- **Grafana**: Visualize metrics from Prometheus

---

## 🚀 Getting Started

### 1. **Clone the repo**

```bash
git clone <repo-url>
cd <project-folder>
```

### 2. **Start the environment**

```bash
docker compose up --build
```

### 3. **Invoke the Lambda locally**

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

---

## 📊 Observability Access

| Tool       | URL                       |
|------------|----------------------------|
| **Jaeger** | [http://localhost:16686](http://localhost:16686) |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) |
| **Grafana**    | [http://localhost:3000](http://localhost:3000) |

> Default Grafana login: `admin` / `admin`

---

## 📂 Project Structure

```txt
├── app
│   ├── app.py             # Lambda handler with OTel tracing
│   └── Dockerfile         # AWS Lambda base image + deps
├── otel-collector-config.yaml
├── prometheus.yml
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

---

## 🧪 Testing

Send a POST request to simulate a Lambda invocation:

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

Then check:

- **Jaeger** for traces
- **Prometheus** for metrics (scraped from OTel Collector)
- **Grafana** (add Prometheus as a data source)

---

## 📦 Poetry Setup (Optional)

If you want to manage Python dependencies locally:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

---

## ✅ Notes

- This does **not** require AWS credentials.
- You can extend this by exporting data to Datadog via OTLP or Agent.

---

## 📌 To Do

- Add Loki for log aggregation
- Export to Datadog (optional: Datadog Agent in Docker)
- Add sample Grafana dashboards (JSON exports)

---

## 📘 References

- [OpenTelemetry Docs](https://opentelemetry.io/docs/)
- [AWS Lambda Runtime Interface Emulator](https://github.com/aws/aws-lambda-runtime-interface-emulator)
- [Grafana](https://grafana.com/)
- [Jaeger](https://www.jaegertracing.io/)
- [Prometheus](https://prometheus.io/)

---

Built for fast demos and observability POCs without touching AWS. ✅

## Other Docker commands

```bash
# list running docker containers
docker compose ps

# check lambda logs
docker compose logs lambda
```
