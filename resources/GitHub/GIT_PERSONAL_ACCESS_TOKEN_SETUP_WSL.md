# Configuring Git Credential Management in WSL 2

## 1. Goal

This guide documents the process of setting up Git inside Windows Subsystem for Linux (WSL 2) to use the native **Windows Credential Manager**. This will make it easier to push to github without having to enter your username and password everytime.

## 2. Prerequisites

Before you begin, make sure you have the following:

* **WSL 2 Installed**: You should have a working WSL 2 environment with Ubuntu.
* **Git for Windows**: The latest version of [Git for Windows](https://git-scm.com/download/win) must be installed on your host Windows machine.
* **A Personal Access Token (PAT)**: You need a PAT from your GitHub with a `repo` scope
    * [You can create one here](https://github.com/settings/tokens/new) if you haven't already.
    * Copy the token and save it somewhere secure temporarily. You will only need it once.

## 3. Setup 

### Step 1: Remove the incorrect Github credentials from Windows Credentials Manager

1. Open the Start Menu and search for "Credential Manager". Once open it should like so:
   
![shot1](https://git.generalassemb.ly/ENT-SDA-SEB-216-IP/SDA-SIRAJ/assets/37351/b6a8a9fe-01b6-41fa-8b56-5b48077f10ae)

2. Click on "Windows Credentials" as selected above

3. Look for an entry named git:https://github.com in the list (you may have one for each account):
   
![shot2](https://git.generalassemb.ly/ENT-SDA-SEB-216-IP/SDA-SIRAJ/assets/37351/432243e9-990f-482b-8986-14551c5b221b)

4. Click on it to expand it, and then click "Remove".
   
![shot3](https://git.generalassemb.ly/ENT-SDA-SEB-216-IP/SDA-SIRAJ/assets/37351/6ceb8000-efc7-4d44-9ead-f390115cf619)

5. Confirm you want to delete the key
   
![shot4](https://git.generalassemb.ly/ENT-SDA-SEB-216-IP/SDA-SIRAJ/assets/37351/b17ed79e-1dc7-463e-be9d-ee6363245a00)

### Step 2: Configure WSL Git to Use the Windows Credential Manager

All commands in this step are to be run **inside your WSL terminal**.

1.  Open your WSL/Ubuntu terminal.
2.  Run the following command to tell your WSL Git installation where to find the Windows credential helper:

```bash
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"
```

#### **Explanation of the Command:**

* `git config --global`: Sets a Git configuration for your user account inside WSL.
* `credential.helper`: Specifies the program Git should use to store and retrieve credentials.
* `"/mnt/c/Program\ Files/..."`: This is the crucial part. It provides the full path to the Git Credential Manager.

### Step 3: The One-Time Authentication

With the helper configured, you now need to perform one action that requires authentication. This will trigger the credential manager to prompt you for your details, which it will then save for all future sessions.

1.  Inside your WSL terminal, navigate to a repository or clone a new private one.
2.  Perform an action like `git pull` or `git push`.

    ```bash
    git push
    ```

3.  The Git Credential Manager will now activate and prompt you for your credentials one at a time. It might look like this if it's on your terminal:

![shot5](https://git.generalassemb.ly/ENT-SDA-SEB-216-IP/SDA-SIRAJ/assets/37351/ffbb60c2-e0e4-43d9-8ca7-80003b945620)

4.  ❗❗ Enter your credentials as follows:
    * **Username**: Enter your GitHub username.
    * **Password**: **PASTE YOUR PERSONAL ACCESS TOKEN HERE.** Do **not** use your regular GitHub account password.

### Step 4: Verification

Once the command succeeds, your PAT is now securely stored in the Windows Credential Manager.

* **Test It**: Run another Git command that requires authentication (e.g., `git pull` again). It should now complete immediately without asking for a username or password.
* **Confirm in Windows**: You can optionally open the **Credential Manager** on your Windows host, go to **Windows Credentials**, and you will now see an entry listed for `git:https://github.com`. This confirms the credential was successfully stored.

Your setup is now complete. Pushing to GitHub should no longer require you to authenticate.
