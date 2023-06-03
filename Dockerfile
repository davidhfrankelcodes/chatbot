# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Expose the port the Django app runs on
EXPOSE 8000

# Run migrations and start the Django app
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
