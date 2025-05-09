from opentelemetry import trace
from opentelemetry.instrumentation.aws_lambda import AwsLambdaInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

import json

# Set up OpenTelemetry tracer provider
trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "local-lambda"})))
otlp_exporter = OTLPSpanExporter(endpoint="http://otel-collector:4318/v1/traces")
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))

tracer = trace.get_tracer(__name__)


# # Move instrumentation inside the handler
# def handler(event, context):
#     AwsLambdaInstrumentor().instrument()  # Add this here, not outside the handler


#     with tracer.start_as_current_span("lambda-root-span"):
#         return {"statusCode": 200, "body": json.dumps("Hello from local Lambda!")}
# def handler(event, context):
#     print("Received event: ", event)
#     try:
#         # Parse event here if needed
#         event_data = json.loads(event)
#     except json.JSONDecodeError as e:
#         print(f"Error parsing event: {e}")
#         return {"statusCode": 400, "body": "Invalid input"}
#     return {"statusCode": 200, "body": "ok"}
def handler(event, context):
    print("Event:", event)  # Log the event to CloudWatch
    return {"statusCode": 200, "body": "ok"}
