<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Check Python Install

This week we are going to learn how to program with Python!

SO - we shall check the installation of the following items:

- Python 3
- PIP3 (Python Package Manager) -> (Pip Installs Packages)
- PIPENV
  - Pipenv is a tool that combines Python package management (pip) and virtual environment management (venv/virtualenv) into a single workflow. It makes working on Python projects much cleaner and more reproducible.

Let's use the following commands to check the installs:

## PYTHON3
#### CHECK PYTHON3
- MAC
  - `python3 —version` || `python3 -V`
- UBUNTU
  - `python3 —version` || `python3 -V`

#### INSTALL PYTHON3
- MAC
  - `brew install python`
- UBUNTU
  - `sudo apt update`
  - `sudo apt install python3`

	***************

## PIP3
#### CHECK PIP3
- MAC
  - `pip3 --version` || `pip3 -V`
  
- UBUNTU
  - `pip3 --version` || `pip3 -V`

#### INSTALL PIP3
- MAC
  - `brew install python`
  
- UBUNTU
  - `sudo apt install python3-pip`

	***************

## PIPENV
#### CHECK PIPENV
- MAC
  - `pipenv --version`
- UBUNTU
  - `pipenv --version`

#### INSTALL PIPENV
- MAC
  - `brew install pipenv`
  
- UBUNTU
  - `pip3 install --user pipenv`
  - `export PATH="$HOME/.local/bin:$PATH"` 
    - (request support from teacher if needed)
  - `source ~/.bashrc`   # or `source ~/.zshrc`
  - `pipenv --version`