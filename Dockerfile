# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the gunicorn server
## 	•	--workers=3: Specifies the number of worker processes for handling requests. The optimal number of workers
## is typically (2 * CPUs) + 1. Adjust this based on the number of CPU cores available.
#	•	--threads=2: Specifies the number of threads per worker. This allows each worker to handle multiple requests
## concurrently. Adjust this based on your application’s I/O characteristics and load.
#	•	--timeout=120: Specifies the maximum number of seconds a worker can take to handle a request before being
## killed and restarted. Adjust this based on your application’s performance requirements.
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3", "--threads=2", "--timeout=120"]