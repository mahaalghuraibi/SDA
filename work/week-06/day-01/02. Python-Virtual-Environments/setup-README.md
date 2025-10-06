<h1>
  <span class="headline">Intro to Python Virtual Environments</span>
  <span class="subhead">Setup</span>
</h1>

## Setup

1. In the current `02. Python-Virtual-Environments` directory create a new directory called: `pipenv-test`

2. CD into the new `pipenv-test` directory

3. Check that `pipenv` is installed: `pipenv --version`

4. If it is not installed: `pip3 install pipenv` or 

5. If you receive a warning that `pipenv` is installed but **not found in your terminal**, we will need to fix this... Look below for the commands based on your environmet:


### **For macOS (zsh)**

If you are using macOS and **Zsh** (the default shell on macOS Catalina and later), run:
```bash
echo 'export PATH="$HOME/Library/Python/3.9/bin:$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
(🛠 **Note:** If you are using a different Python version (such as 3.10 or 3.11), update `3.9` in the path accordingly.)
---


### **For Git Bash on Windows**

If you are using **Git Bash** on Windows, add Pipenv’s installation path to your `PATH` variable:

```bash
echo 'export PATH="$HOME/AppData/Roaming/Python/Python39/Scripts:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
(🛠 **Note:** If your Python version is **not 3.9**, replace `Python39` with your correct version (such as `Python310` for Python 3.10)
---


### **For Linux (Ubuntu)**
On **Ubuntu (or any Linux system using Bash)**, run:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
(🛠 **Note:** This ensures user-installed Python packages (including Pipenv) are available system-wide.)
---


### **Final Verification**

After applying the appropriate fix, restart your terminal and check if Pipenv is now accessible by running:

```bash
pipenv --version
```

If you see a version number, the setup is complete! 🎉

## Open project folder

Open the `pipenv-test` directory in VSCode:

```bash
code .
```
