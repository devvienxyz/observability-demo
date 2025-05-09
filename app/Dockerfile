FROM public.ecr.aws/lambda/python:3.12

# Set the working directory in the container
WORKDIR /var/task

# Copy the requirements.txt into the container
COPY requirements.txt ./

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the Lambda function entry point
CMD ["app.handler"]
