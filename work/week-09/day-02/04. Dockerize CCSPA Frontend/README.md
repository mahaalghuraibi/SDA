### Summary
We are going to continue off of The last lesson

### Dockerizing the React Frontend (30 minutes)

When building a modern React application, Docker provides a powerful way to ensure consistency between development and
production environments. The process of containerizing a frontend application streamlines both setup and deployment,
making the application highly portable and efficient to manage.

To begin this process, we create a `Dockerfile` in the React project's root directory. This file serves as a blueprint
for containerizing the React frontend application. Here's a detailed breakdown of the Dockerfile:

```dockerfile
FROM node:20

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

The configuration starts with `FROM node:16`, which uses Node.js 16 as the base image. The `WORKDIR /app` command sets
up the working directory inside the container. Next, we copy the `package.json` and `package-lock.json` files and run
`npm install` to install all dependencies. After this, we copy the entire project into the container using `COPY . .`.
Port `3000` is exposed to allow access to the development server, and finally, we set the command to run the development
server with `CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]`.

This containerized approach eliminates common issues related to dependency versions and configuration differences across
different machines. Whether you're developing, testing, or deploying the application, the container provides a
consistent environment, significantly improving the workflow efficiency for all team members involved in the project.

### Updating docker-compose

Go to your docker-compose.yml and change the copy the content from below into the file to include your frontend information.

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

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: "react_frontend"
    ports:
      - "5173:5173"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    depends_on:
      - api

  db: #name of the service
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

The configuration defines three main services. The API service manages our Django backend, executing necessary database
migrations before starting the development server. It mounts the backend directory as a volume, enabling real-time code
changes, and exposes port `8000` for access. Environment variables are loaded from a `.env.dev` file, ensuring secure
configuration management.

The frontend service builds our React application, exposing it on port `3000`. It implements volume mounting for the
frontend directory while preserving the `node_modules` directory, facilitating development with hot-reloading
capabilities. The service runs in development mode and starts only after the API service is ready.

The database service utilizes the official PostgreSQL image, with data persistence managed through a named volume. It's
configured with specific credentials for development purposes, including a custom `username`, `password`, and `database`
name. The `postgres_data` volume ensures that database information persists across container restarts.

This orchestration creates a development environment where all components work together harmoniously, with proper
dependency management ensuring services start in the correct order. The configuration emphasizes developer experience
with features like hot-reloading and persistent data storage, while maintaining isolation between services.