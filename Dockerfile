# Use the official Python image as a parent image
FROM python:3.9-slim

# Set environment variables
ENV TELEGRAM_BOT_TOKEN=""
ENV OPENAI_API_KEY=""

# Create a working directory
WORKDIR /chatgtp

# Copy the Python script and requirements.txt into the container
COPY python-telegram-bot .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python-telegram-bot"]
