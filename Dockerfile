    # Use an official Python runtime as a parent image
FROM python:3.11-slim

ARG DISCORD_TOKEN
# Set the working directory in the container
WORKDIR /app

ENV DISCORD_TOKEN=$DISCORD_TOKEN

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "bot.py"]
