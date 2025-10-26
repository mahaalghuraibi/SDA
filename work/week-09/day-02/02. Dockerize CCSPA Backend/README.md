### Introduction (5 minutes)

Modern web development often involves complex environments with multiple services working together. In this lesson,
we'll explore how to streamline the development process by containerizing a full-stack application using Docker. We'll
focus on a React frontend communicating with a Django backend, all orchestrated through Docker Compose. This approach
solves common development challenges like environment inconsistencies, dependency management, and service coordination,
ultimately creating a more efficient and reliable development workflow.


### Learning Objectives

After completing this lesson, you will be able to:

- Create a Dockerfile to containerize a Django backend application with proper configurations
- Set up a Docker environment for a React frontend application with development features
- Configure Docker Compose to orchestrate multiple services including frontend, backend, and database
- Manage containerized applications using Docker Compose commands
- Implement development-friendly features like hot-reloading and volume mounting
- Troubleshoot common issues in a containerized development environment

Let's begin by exploring how to containerize each component of our full-stack application.

### Dockerizing the Django Backend (60 minutes)

#### Creating the `.env.dev` File

Start by creating a file named `.env.dev` in the root of your `backend` directory. This file will hold your
environment-specific variables such as database connection details and security keys. It’s crucial to store sensitive
information like database passwords and Django’s secret key in environment files to keep them out of your version
control system.

```text
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=cats_django_dev
SQL_USER=docker_django_user
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

The `.env.dev` file begins with `DEBUG=1`, enabling Django's debug mode to assist with development by providing detailed
error messages and a debugging interface. The `SECRET_KEY` is included to serve as a cryptographic key used by Django
for signing data, ensuring the security of various application components. The `DJANGO_ALLOWED_HOSTS` entry specifies
the domains that are permitted to access the Django application, helping to prevent unauthorized or malicious access.
Additionally, the database settings such as `SQL_ENGINE`, `SQL_DATABASE`, `SQL_USER`, and related configurations define
the connection details for PostgreSQL, a relational database that will operate in a separate Docker container, forming a
critical part of the backend infrastructure.

#### Updating Django's `settings.py`

Navigate to the `backend/catcollector/settings.py` file to configure Django's database connection using environment
variables defined in the `.env.dev` file.

Find the `DATABASES` setting in `settings.py` and modify it to load values from the environment:

```python
import os

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
```

The environment variables in Django can be accessed using `os.environ.get()`, which provides flexibility when
configuring different setups. This method allows you to retrieve values dynamically, and includes a fallback mechanism -
if a particular environment variable isn't found, it will use default values such as `django.db.backends.sqlite3`. This
approach is particularly important when it comes to database configuration, as the database connection settings play a
vital role in enabling Django to communicate with a PostgreSQL database container within your Docker environment.

#### Creating requirements.txt
In the root of your backend folder create a file call requirements.txt.
Inside of this file copy and paste the following text

```
django
psycopg2-binary
djangorestframework
django-cors-headers
djangorestframework-simplejwt
python-dotenv
```

#### `Creating the Dockerfile` for Backend

Now we’ll create the `Dockerfile` inside the `backend` directory to define the steps to containerize the Django
application. This will ensure that we can run our Django app inside a Docker container without worrying about
dependencies or configurations on our host machine.

```dockerfile
# Base image
FROM python:3.10

# Set working directory
WORKDIR /usr/src/backend

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all application files
COPY . .

# Expose application port
EXPOSE 8000

# Define default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

The Dockerfile begins with `FROM python:3.9`, which specifies Python `3.9` as the base image - a version chosen for its
broad compatibility with modern Django installations. Within the container, `/usr/src/backend` is designated as the
working directory through `WORKDIR`, establishing the location where Django's project files will be stored. The build
process continues with two critical steps: first copying the requirements.txt file into the container, then using pip to
install all the necessary Python packages and dependencies that Django requires. Following this, `COPY . .` transfers
all project files into the container's working directory. The configuration then exposes port `8000`, which enables
external access to the Django development server running inside the container. Finally, the default command is defined
using CMD `["python", "manage.py", "runserver", "0.0.0.0:8000"]`, which launches Django's development server and
configures it to listen on all network interfaces `(0.0.0.0)`.

This containerized approach eliminates common issues related to dependency versions and configuration differences across
different machines. Whether you're developing, testing, or deploying the application, the container provides a
consistent environment, significantly improving the workflow efficiency for all team members involved in the project.

### Orchestrating a Full-Stack Application with Docker Compose (60 minutes)

When developing a full-stack application, Docker Compose helps orchestrate multiple containerized services seamlessly.
Let's explore how to configure our development environment using a `docker-compose.yml` file that coordinates our Django
backend, React frontend, and PostgreSQL database.

Create a `docker-compose.yml` file in your project's root directory with the following configuration:

```dockerfile
services:
  api: #name of the service
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: "backend_api" #name of the container
    command: >
      bash -c "python manage.py makemigrations && 
               python manage.py migrate && 
               python manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./backend/:/usr/src/backend/
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env.dev
    depends_on:
      - db

  db:
    image: postgres:16
    container_name: db
    restart: always
    environment:
      POSTGRES_USER: docker_django_user
      POSTGRES_PASSWORD: hello_django
      POSTGRES_DB: cats_django_dev
    volumes:
      - postgres_data:/var/lib/postgresql
    ports:
      - "5432:5432"


volumes:
  postgres_data:
```

### Running Your Dockerized Full-Stack Application (30 minutes)

Now that we have our Docker Compose configuration set up, let's walk through the process of running and managing our
containerized application. This section will cover everything from starting the services to troubleshooting common
issues.

First, open your terminal and navigate to the project directory containing your `docker-compose.yml` file:

```text
cd /path/to/your/project/root
```

To start all services defined in your Docker Compose configuration, use the following command:

```text
docker compose up
```

If you prefer to run the containers in the background (detached mode), add the `-d` flag:

```text
docker compose up -d
```

Once the services are running, you can verify their status using the `docker ps` command. This will display a list of
all running containers along with their ports and current status. Your application services should now be accessible:

- Django Backend: [http://localhost:8000](http://localhost:8000)

During development, you may need to monitor the application logs for debugging purposes. View the logs for all services
using:

```text
docker compose logs
```

If you make changes to any of your `Dockerfiles`, you'll need to rebuild the services. Force a rebuild using:

```text
docker compose up --build
```

When you're finished working on your application, shut down all services with:

```text
docker-compose down
```

This command stops and removes all containers and networks associated with your Docker Compose configuration, ensuring a
clean shutdown of your development environment.

Remember to check that your environment variables are properly configured in your `.env` files, as these are crucial for
the correct functioning of your services. Each service may require specific environment variables, and any
misconfiguration can lead to startup issues.

This orchestrated approach to running your full-stack application ensures a consistent development environment and makes
it easy to manage multiple services simultaneously. The containerized setup allows team members to work with identical
environments, reducing the "it works on my machine" problem and streamlining the development process.