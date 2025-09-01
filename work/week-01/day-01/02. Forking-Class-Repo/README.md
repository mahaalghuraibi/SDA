<img width="100%" src="https://i.imgur.com/oVEZlbP.png"><br/>

# Forking The Class Repository from GHE

- The class repository contains all of the information you will need for the course.
- Lectures, Projects, Labs, Homework, it's all here!

To use this repository, fork and clone it by following the instructions below 👇

## 1. Log In to GitHub Enterprise
Before you can access and submit the assignments, make sure that you're logged in to your GA **Enterprise** GitHub account. If you have not signed up yet, here's the link to do so: [https://git-invite.generalassemb.ly](http://git-invite.generalassemb.ly)

After logging in/signing up with your account, you will have read-only access to the GA class org. However, you most certainly will want to be able to make changes (e.g., add notes, save code exercises, etc) to different repositories in the class org. In order to make changes to files from the classroom org you will have to **fork** and **clone** a repository.


## 2. Forking a Repository
<img width="100%" src="https://i.imgur.com/7f2uAe2.gif">

Forking a repository copies the entire contents of a repository on an individual's GitHub account (someone else's) to another GitHub account (yours). This allows users to make a copy of an entire repository that can then be changed without impacting the original repository.

1. Navigate to the class repository:
   
[Class Repository Link]()

1. In the top-right corner of the page, click the `Fork` button.
  
  <p align="center"><kbd><img width="800px" src="https://i.imgur.com/NOQAJVD.png"></kbd></p>

3. On the next screen, you should verify that the "Owner" is your personal GitHub Enterprise account and that the repository name is correct. Both of these values should be correct when automatically populated, but double-checking is always a good idea. If everything looks right, click the *Create fork* button.
  
  <p align="center"><kbd><img width="800px" src="https://i.imgur.com/UpTpLOL.png"></kbd></p>
  
4. You’ll see a brief screen indicating that the repository is being forked to your personal GitHub.
  
  <p align="center"><kbd><img width="800px" src="https://i.imgur.com/67dQKH0.png"></kbd></p>
  
5. Once this is complete, you’ll be redirected to your GitHub Enterprise account where the fork was created. Click on the *Code* button to display a URL, which we’ll copy to the clipboard:
  
  <table>
    <tr>
      <th><img src="https://i.imgur.com/UEJYNaY.png"></th>
      <th><img src="https://i.imgur.com/aFd14j3.png"></th>
    </tr>
  </table>

Once you've completed the steps above, you will now have a forked copy of the GitHub repo. In order to get a copy as a local repository on your machine, follow the steps below to clone that repo. 👇


## Step 4: Cloning a Repository
<img width="100%" src="https://i.imgur.com/WVtHI7R.gif">

Cloning allows us to take the current state of a project from a remote repository on GitHub and make a copy onto a local repository on your computer. You'll use this command anytime you want to make a copy of a project that already exists on GitHub. This is typically the next action you'll take after you fork an existing repository so that you're able to work on it on your local machine.

1. Navigate to the parent directory where you want the cloned directory to exist. For example:
    ```
    cd ~/code
    ```

    🚨 ***When you clone a repository, a directory (matching the repository’s name) will be created automatically.  It’s important that you don’t create an additional directory locally, as that may cause issues/confusion later on down the road.***

1. Using the URL from GitHub, clone the repository
    ```
    git clone https://github.com/<original author>/my-project.git
    ```
    Your link should look different than this, as it will have your GitHub username & project name in it!

    🚨 ***When you clone a repository, an origin remote will automatically be set using the URL that you used to clone it.  If you’ve cloned a repository that you don’t own (or have write access to), you won’t be able to push changes!***

1. Navigate into the directory and open in VS Code
    ```
    cd my-project
    code .
    ```


## Step 5 (OPTIONAL): Pushing Up Your Work
Once you’ve completed the above steps to clone the repository to your machine, you can push changes made to your code using the following commands:
```
git add -A
git commit -m 'a meaningful, concise commit message here'
git push origin main
```

Once your files are pushed up into your fork, others will be able to visit your fork online and view your work!


## Step 6: Updating Your Fork
At the start of each unit, that unit's lectures will be added and/or updated in the classroom repository. To bring those updates over into your fork of the repository, you can run the following commands:

RUN THIS ONLY ONCE:
```bash
git remote add upstream https://git.generalassemb.ly/ENT-SDA-SEB-216-IP/SDA-SIRAJ.git
```

RUN THIS EACH WEEK:
```bash
git pull upstream main
git push origin main
```
> The first command pulls the new code in the class repo into your local copy of your fork
>
> The second command is optional and pushes the new code that's now in your local repo up to your online repo


**WE WILL REMIND YOU / LET YOU KNOW WHEN THERE ARE RESOURCES THAT NEED TO BE PULLED / UPDATED.**