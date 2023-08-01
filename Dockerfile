# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install project dependencies (if any)
RUN pip install -r requirements.txt

# Specify the command to run your project
CMD ["python", "your_script.py"]
