# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask app to the container
COPY . .

# Expose the Flask app's port (change 5000 if your Flask app runs on a different port)
EXPOSE 4000

# Define environment variable
ENV NAME World

# Start the Flask app
#flask run --host=0.0.0.0 --port=80
# CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
CMD ["gunicorn", "--reload", "-b", "0.0.0.0:4000", "wsgi:app"]

