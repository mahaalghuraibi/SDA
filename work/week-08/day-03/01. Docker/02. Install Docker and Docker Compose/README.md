# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Installing Docker and Docker Compose
| Title                                | Type   | Duration | Author        |
|--------------------------------------|--------|----------|---------------|
| Installing Docker and Docker Compose | Lesson | 0:30     | Suresh Sigera |

### Introduction

In this lesson, we will cover how to install Docker and Docker Compose on Windows, macOS, and Linux. By the end of this
lesson, you will have a fully functional Docker setup ready for containerized application development.

##### Prerequisites

Before installing Docker, ensure that your system meets the following requirements:

- Windows 10/11 Pro, Enterprise, or Education (Docker requires WSL 2 or Hyper-V on Windows)
- macOS 10.15 (Catalina) or later
- Linux (Ubuntu, Debian, CentOS, Fedora, etc.) with sudo/root access

#### Step 1: Installing Docker

**Windows (Using Docker Desktop)**

1. Visit [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/).
2. Click Download for Windows.
3. Run the installer (Docker Desktop Installer.exe).
4. Follow the installation wizard:
    - Enable WSL 2 if prompted.
    - Restart your computer after installation.
5. Open Docker Desktop and ensure it is running.
6. Verify the installation by running the following command in PowerShell or Command Prompt: `docker --version`

**macOS (Using Docker Desktop)**

1. Visit Docker Desktop for [Mac](https://docs.docker.com/desktop/setup/install/mac-install/).
2. Download the Apple Silicon or Intel chip version based on your Mac model.
3. Open the .dmg file and drag Docker to the Applications folder.
4. Open Docker Desktop from Applications and follow the setup.
5. Verify the installation in the terminal: `docker --version`

#### Step 2: Installing Docker Compose

**Windows & macOS (Included with Docker Desktop)**

Docker Compose comes pre-installed with Docker Desktop, so no additional installation is needed. Verify with:

```text
docker compose version
```

Now that Docker and Docker Compose are installed, you can start working with containers! Continue by learning how to
build and manage custom Docker images, networking, and container orchestration.