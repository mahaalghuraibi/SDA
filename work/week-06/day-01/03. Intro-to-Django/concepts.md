# ![Intro to Django - Concepts](./assets/hero.png)

<img src="https://i.imgur.com/RWixB90.png">

## What is Django?

Django is by far the most popular Python-based web framework, and its popularity continues to grow thanks to the growth of Python itself.

Django was publicly released in 2005 and was named by one of its creators, [Adrian Holovaty](https://en.wikipedia.org/wiki/Adrian_Holovaty), after his favorite guitarist, [Django Reinhardt](https://en.wikipedia.org/wiki/Django_Reinhardt).

Django is specifically engineered to develop highly secure web applications rapidly. It provides a rich set of tools and features that streamline the creation of complex, data-driven sites. Django follows the "batteries-included" philosophy, meaning it includes built-in solutions for many of the common challenges in web development, such as user authentication, site maps, and content administration.

These components, designed to work together seamlessly, allow developers to focus on the unique features of their web applications without worrying about the underlying infrastructure.

## Why use Django?

Django stands out from minimalist frameworks like Express by offering robust features that streamline the development of complex web applications.

Here are some key advantages of using Django:

- **Object-relational mapper (ORM)**: Django's ORM provides a high-level abstraction, allowing developers to interact with databases using Python rather than SQL. This enables developers to write database queries using Python code, making it simpler to create, retrieve, update, and delete database entries.
- **Built-in administrative interface**: Django includes a ready-to-use admin interface that allows developers and site administrators to manage database data through a web interface. This powerful tool facilitates quick interactions with databases right out of the box.
- **Comprehensive user authentication**: Its user authentication system handles user accounts, groups, permissions, and cookie-based user sessions. This built-in capability makes it easier to develop secure sites and reduces the amount of code developers need to write.
- **A rich ecosystem of tools and libraries**: Django provides numerous built-in features for common web development needs, such as sending emails, generating RSS feeds, and managing content in various languages.
- **Strong community and documentation**: Django benefits from extensive, well-maintained documentation and a large, active community. This network provides substantial support for troubleshooting, sharing knowledge, and extending the capabilities of your applications through third-party packages.
- [Documentation](https://docs.djangoproject.com/en/5.1/)

## Components of a Django Project

<img src="https://i.imgur.com/1fFg7lz.png">
<br/><br/>
This diagram visualizes the relationship between the different components of a Django project. The quirky thing about Django is how it names its high-level components. What we think of as a web **application**, Django calls a **project**. Further, what we think of as part of an app's functionality, or **modules**, Django refers to as **apps** A Django _project_ can have many _apps_, and a Django _app_ can belong to multiple _projects_. More on this later.

## Django MVT Architecture

Django's architecture is similar, but different than that of MVC:

<img src="https://i.imgur.com/rA4BtNv.png">

Django adopts the Model-View-Template (MVT) architecture, a variant of the more widely known Model-View-Controller (MVC) architecture. While both architectures aim to separate concerns within an application, Django's MVT architecture has distinct roles for each component.

- **Model**: Defines the data structure. These are Python classes that define the fields and behaviors of the data you're storing. Django models can interact with a database seamlessly to retrieve, store, update, and delete data.
- **View**: Handles the business logic and is the bridge between models and templates. In Django, views retrieve data from the models and pass it to the templates. Views in Django perform roles similar to controllers in MVC, essentially directing traffic within the application.
- **Template**: Manages the presentation layer. Templates are HTML files that allow Python-like expressions for dynamic content generation. This separation from the actual business logic in views allows for cleaner, more maintainable code.

### Terminology in Django

Django uses unique terminology for its components, which can initially be confusing:

- **Project**: In Django, what you might typically think of as a ***web application*** is called a ***project***. This top-level container for your web application houses the configuration and ties everything together.
- **Apps**: What are often considered features or modules in other frameworks are called ***apps*** in Django. An app is a web application that does something such as a blog, a database of public records, or a simple poll app. A project can contain multiple apps, which can be reused in different projects.

A Django ***project*** is a complete website with multiple pages, while a Django ***app*** is a web application that does something specific and can be integrated into any project.
