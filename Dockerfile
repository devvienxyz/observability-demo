FROM public.ecr.aws/lambda/python:3.12
WORKDIR /var/task
COPY app.py ./
RUN pip install --no-cache-dir opentelemetry-sdk opentelemetry-exporter-otlp \
    opentelemetry-instrumentation opentelemetry-instrumentation-aws-lambda \
    requests flask
CMD ["app.handler"]