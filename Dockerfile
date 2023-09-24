# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Optionally, if you need SQLite3 installed uncomment the line below
# RUN apt-get update && apt-get install -y sqlite3

# Make port 8502 available to the world outside this container
EXPOSE 8502

# Define environment variable
ENV NAME World

# Run app.py when the container launches, also specify that Streamlit should run on port 8502
CMD ["streamlit", "run", "--server.port", "8502", "app.py"]
