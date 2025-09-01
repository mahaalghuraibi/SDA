<h1>
  <span class="headline">Intro to Git and GitHub</span>
  <span class="subhead">Git Concepts</span>
</h1>

# 🚀 A Brief History of Git and GitHub

## 🐙 Git
Linus Torvalds is a Finnish-American software engineer who created the Linux kernel in 1991 and later developed Git in 2005 to manage Linux kernel development efficiently. He is known for his influence on open-source software and collaborative development practices.

- **Created by:** Linus Torvalds 👨‍💻  
- **Year:** 2005 ⏳  
- **Purpose:** To manage the development of the Linux kernel after disputes with proprietary version control systems.  
- **Key Features:**  
  - 🌍 Distributed version control (every developer has a full copy of the repository)  
  - ⚡ Fast performance for large projects  
  - 🌿 Branching and merging made easy  
  - 🔐 Integrity through SHA-1 hashing  

Git’s design emphasized speed, simplicity, and robust handling of branches, making it ideal for large, collaborative projects. Its distributed nature allowed developers to work independently and merge changes efficiently, which later became essential for online collaboration platforms like GitHub.

## 🐱 GitHub

- **Founded by:** Tom Preston-Werner, Chris Wanstrath, PJ Hyett, and Scott Chacon
- **Year:** 2008 ⏳  
- **Purpose:** A cloud-based platform to host Git repositories and foster collaboration ☁️  
- **Why Git Was Used:**  
  - 🌐 Git’s distributed model allowed GitHub to provide a web-based interface without centralizing all code operations.  
  - 🔀 Efficient branching and merging made collaborative workflows like pull requests possible.  
  - ⚡ Git’s speed and reliability made it scalable for millions of repositories and developers.  

- **Key Features:**  
  - 💻 Web interface for Git repositories  
  - 📝 Pull requests for code review  
  - 📋 Issue tracking and project management  
  - 👥 Social features like followers and contribution graphs  

GitHub transformed Git from a developer tool into a social platform for software development, enabling millions of developers to collaborate on projects worldwide 🌎.

---

**References:**  
- [Git Official Site](https://git-scm.com/)  
- [GitHub About](https://github.com/about)


## What is version control?

Version control keeps track of changes made to files over time. It also makes working in teams easier because it enables people to work on the same project without overriding each other's changes.

## Why use version control?

As developers, version control lets us:

- Review changes made over time and see who did what.
- Work with others.
- Experiment without impacting the main codebase. If the new idea works, it can be added to the main project.
- Return to an older version, particularly useful if a bug has been introduced into the code.
- Work offline, then sync later when reconnected.

## Git-flavored version control

We'll use [Git](https://git-scm.com/) - the world's most popular version control system. [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) created Git in 2005 to help develop his main project at the time - Linux.

Git is designed to track code changes. Using Git enables developers to collaborate, manage code history, test ideas, and more. Git can work alone or with social platforms that layer in additional features. Git has a few core concepts, which follow:

### Git repository

A Git repository (aka Git repo, or just repo) is essentially a copy of a project. What makes the repo special is that it holds key details for every line of code in a project regarding:

- Who touched which part of the code.
- What they changed.
- When it happened.

This information helps developers use Git to collaborate, track changes through time, or even revert to previous versions when necessary.

Git repositories can be stored locally on a developer's machine or hosted on remote servers like GitHub.

### Git branch

Branches are used to test new things or build new features, and they help developers working on the same project avoid accidentally messing up each other's code. For now, we'll work primarily in the `main` branch.

In this course, we will use the `main` branch as our central source of truth and the default branch name. This is also the default branch name on GitHub.

### Remotes

A remote is a reference to a repository hosted on an external server, allowing synchronization and collaboration between a local Git repository and its counterpart located elsewhere.

In this course, remotes typically take the form of a URL pointing to a repository on GitHub, but other code-sharing platforms like GitLab and BitBucket exist. When collaborating, these external repositories provide a centralized location for sharing, updating, and accessing a codebase among multiple team members. We'll discuss remotes in more detail when we cover GitHub itself.
