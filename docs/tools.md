# Observability Tools

## Tools

### Opentelemetry

OpenTelemetry is a set of APIs, libraries, agents, and instrumentation that enables the collection of telemetry data (metrics, logs, and traces) from your applications. It helps to track the behavior of your application in production to identify performance bottlenecks, errors, or other issues.

trace: This module is responsible for tracing. Traces are used to follow the path of a request through your system (e.g., Lambda invocations, function calls).

AwsLambdaInstrumentor: This is specific to AWS Lambda. It automatically instruments AWS Lambda functions, so it collects telemetry data (like traces) for you. When you call AwsLambdaInstrumentor().instrument(), it starts collecting traces.

TracerProvider: This is used to configure how traces are collected. You're creating a new trace provider here for your Lambda.

OTLPSpanExporter: This is used to send the collected trace data to an exporter (like a trace collector, Jaeger, or Prometheus).

BatchSpanProcessor: This processes the trace data in batches to send it efficiently to the trace exporter.

### Grafana

Grafana is a popular open-source platform for visualizing and analyzing time-series data (e.g., metrics, logs, traces).

Grafana's role: You can use Grafana to visualize telemetry data such as metrics (e.g., response times, request counts) and traces (e.g., Lambda function execution details) coming from your application.

It connects to various data sources, including Prometheus, Jaeger, and OpenTelemetry.

### Prometheus

Prometheus is an open-source monitoring system and time-series database that collects metrics from configured targets at specified intervals. It is often used to monitor the health and performance of your infrastructure.

Prometheus' role: Prometheus will collect metrics (such as CPU usage, memory usage, request count, and latency) from your Lambda functions or other services in your environment.

It is typically integrated with Grafana to visualize these metrics over time.

However, note that OpenTelemetry does not collect metrics by default (you would need to set it up separately for that) – Prometheus typically does this, and you can use it to store and query those metrics.

### Jaeger

Jaeger is an open-source distributed tracing system that helps you monitor and troubleshoot the performance of microservices architectures.

Jaeger's role: It collects and visualizes traces collected by OpenTelemetry (like the traces from your Lambda function).

It's commonly used to visualize traces over time, find performance bottlenecks, and understand how requests flow through your system.

## How they're connected in this observability setup

### Components & Roles

| Component         | Type                   | Role                                                                  |
| ----------------- | ---------------------- | --------------------------------------------------------------------- |
| **Lambda**        | Compute                | Your application logic runs here                                      |
| **OpenTelemetry** | Tracing & Metrics SDK  | Captures traces and (optionally) metrics from your code               |
| **OTLP Exporter** | Telemetry exporter     | Sends data from OpenTelemetry to backends (Datadog, Jaeger, etc.)     |
| **Datadog**       | Observability Platform | Central platform to monitor, trace, and alert across infrastructure   |
| **Jaeger**        | Trace Visualizer       | (Optional) Visualize raw traces locally                               |
| **Prometheus**    | Metrics Backend        | Scrapes metrics and stores them (often used locally)                  |
| **Grafana**       | Dashboard UI           | Visualizes metrics (from Prometheus) and traces (from Jaeger/Datadog) |
