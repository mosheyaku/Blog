# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Pillow
RUN apt-get update && \
    apt-get install -y libjpeg-dev zlib1g-dev && \
    pip install --no-cache-dir Pillow

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
