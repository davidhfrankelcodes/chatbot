# Chatbot Project

This is a 'Chatbot' project repository by [David Frankel](https://github.com/davidhfrankelcodes). 

## Project Structure

The main project repository contains the following files and directories:

- chatbot: A directory that contains the core Django project settings.
- web: A directory that contains the main web application for the chatbot.
- .gitignore: A file that specifies which files and directories Git should ignore.
- Dockerfile: A file that contains instructions for Docker to build an image.
- docker-compose.yaml: A file that defines services, networks, and volumes for Docker.
- manage.py: A command-line utility for administrative tasks.
- requirements.txt: A file that lists the Python packages that are needed for the project.

### chatbot Directory

The chatbot directory contains the following files:

- \_\_init\_\_.py: An empty file that helps Python determine where to find packages.
- asgi.py: A file that sets up the ASGI application for the project.
- settings.py: A file that contains settings for the Django project.
- urls.py: A file that defines the URL configurations for the Django project.
- wsgi.py: A file that sets up the WSGI application for the project.

### web Directory

The web directory contains the following files and directories:

- migrations: A directory that contains Django migration files.
- templates: A directory that contains Django template files.
- \_\_init\_\_.py: An empty file that helps Python determine where to find packages.
- admin.py: A file that defines the admin interface for the Django project.
- apps.py: A file that configures the Django app for this project.
- models.py: A file that defines the data models for the Django project.
- tests.py: A file that contains tests for the Django project.
- urls.py: A file that defines the URL configurations for the Django project.
- views.py: A file that defines the views for the Django project.

## Getting Started

To get started with the project, you should clone the repository, navigate to the project directory, and install the required packages with pip by running `pip install -r requirements.txt`.

To start the Django development server, you can use the command `python manage.py runserver`.

