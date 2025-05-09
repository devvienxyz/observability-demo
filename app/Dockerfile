FROM public.ecr.aws/lambda/python:3.12

# Set the working directory in the container
WORKDIR /var/task

# Copy Poetry files for dependency management
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-root

# Copy the rest of the application code
COPY . .

# Set the Lambda function entry point
CMD ["app.handler"]
