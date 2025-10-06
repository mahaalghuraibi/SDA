<h1>
  <span class="headline">Intro to Python Virtual Environments</span>
  <span class="subhead">Concepts</span>
</h1>


**Learning objective:** By the end of this lesson, you will be able to **implement** a virtual environment for a project with the Python dependencies `pipenv` and **explain** the purpose of `Pipfile` and `Pipfile.lock` files in the `pipenv` environment.

<img src="https://datascientest.com/wp-content/uploads/2022/07/python-virtual-environment.jpg" >

## What is a `Virtual Environment`in Python?

A virtual environment in Python is like a separate space where you can work on your Python projects without affecting your computer's main setup. It keeps each project's tools and libraries isolated so they don't interfere with each other or with other programs you're running.

Some reasons we will use virtual environments in our API build:

1. Keep projects codebases separate
1. Make projects easier to share
1. Testing new, experimental libraries

## Installing Dependencies with Pipenv

To use `pipenv`, create a new Python project folder and navigate to it.

Now rather than using `pip` to install dependencies for an application, you can use `pipenv`.


For example:

```sh
pipenv install fastapi
```

This will automatically create two key files: `Pipfile` and `Pipfile.lock`. These are used to keep track of the project's dependencies and their versions. It is designed to declare broad dependencies in a more manageable way.

## Pipfile

The `Pipfile.lock` is automatically updated each time the `Pipfile` changes. It's a snapshot of the exact versions of each package being used, along with their transitive dependencies, at a specific point in time. This means that if you share your project with someone else, you can guarantee they will install exactly the same dependencies as you have, ensuring consistent behavior across different environments. Keep both of these files in version control. Visit the [pipenv documentation](https://pipenv.pypa.io/en/latest/pipfile.html) for more details on the differences between `Pipfile` and `Pipfile.lock`.

Using `pipenv` to install your packages means that you can collaborate on projects, simply clone or download the repo and type `pipenv install` to install all the dependencies.

## How It Works

When you install a package with `pipenv`, it creates a _virtual environment_ for that project. This mimics a development environment where only the packages you have installed for that project exist. It does this by installing all the packages to a uniquely named folder somewhere in the file system of your laptop.

## Python Interpreter
- If you have multiple versions of Python installed (e.g., Python 3.11 and Python 3.9), or you're using virtual environments for different projects, VSCode needs to know **which one** to use.
- The selected interpreter determines:
  - The Python version used to run your code.
  - Which installed packages are available (since each environment has its own).
  - How linting, IntelliSense (code completion), and debugging behave.
  
Setting the **Python interpreter** in **Visual Studio Code (VSCode)** means telling VSCode which version of Python you want it to use for running and debugging your Python code.

### How to Set the Python Interpreter in VSCode

1. **Open Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
2. Type and select: **"Python: Select Interpreter"**.
3. You'll see a list of detected Python environments:
   - System-wide installations (e.g., `/usr/bin/python3`)
   - Virtual environments (e.g., `.venv`, `env/`, conda environments)
   - Installed interpreters via pyenv or other tools
4. Click on the interpreter you want to use for the current workspace.
   1. **IF** the correct one (should be pointing inside your venv) is not in the list.. we can find it by running: `which python` from inside your activates virtual environment
   2. the print out should yield the path to the virtual environment's installed python version
   3. type: `which python` in the backend terminal.. it should return a string like this:    
      1. `/Users/devilone/code/general_assembly/SEB-SDA-Ghazal/internal/applications/  catcollector-spa/backend/.venv/bin/python` 
   4. Select: `Enter interpreter path` under the `Python: Select Interpreter` menu
   5. Paste the the string and submit.

---

## Behind the scenes

VSCode saves your interpreter choice in a `.vscode/settings.json` file inside your project folder, like this:

```json
{
  "python.pythonPath": "/path/to/your/python"
}



## Testing Pipenv

In the current working directory as your virtual environment, create a file called `main.py` and save the following simple code in it:

```py
# main.py

print("pipenv is working!")
```

In order to have Python execute the `main.py` file in the virtual environment, you need to prefix any command with `pipenv run` So for example:

Not in an active shell:
```sh
pipenv run python main.py
```

In an active shell:
```sh
pipenv shell
python main.py
```

Confirm that you see the message `pipenv is working!`.

