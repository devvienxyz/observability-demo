from opentelemetry import trace
from opentelemetry.instrumentation.aws_lambda import AwsLambdaInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

import json

trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "local-lambda"})))
otlp_exporter = OTLPSpanExporter(endpoint="http://otel-collector:4318/v1/traces")
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))
AwsLambdaInstrumentor().instrument()

tracer = trace.get_tracer(__name__)


def handler(event, context):
    with tracer.start_as_current_span("lambda-root-span"):
        return {"statusCode": 200, "body": json.dumps("Hello from local Lambda!")}
