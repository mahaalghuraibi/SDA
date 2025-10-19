<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector
Today we start our journey of building a full stack web application using React on the front end and Django Rest Framework on the backend. This process will unfold over the course of several days / parts and will combine the tools we learned this week (react) along with a fresh approach to developing a Django server with a slightly different Django Framework approach / setup. The overall concept is the exact same as our previous Cat Collector.

Then, after the lessons, you will use lab time to repeat what you saw in the lesson by building your own app named anything you want, say - **FinchCollector**.

## Django Rest Framework / Backend SETUP

Time to setup our Django Rest Framework Backend!

1. Create a folder to hold your python virtual environment / files: 
   - `applications/cat-collector-spa/backend`
   - cd into `applications/cat-collector-spa/backend`

2. Create a python virtual environment and we will install Django with: `pipenv shell`

3. This command will create a new `Pipfile` and a `.venv` in your project directory as well as activate the shell -> your terminal prompt should look different: 
- `(catcollector_backend) -> catcollector_backend git:(main)`

1. Install dependencies: `pipenv install django psycopg2-binary djangorestframework`
- this will create a `Pipfile.lock`

1. Start a new Django project within your virtual environment:  `django-admin startproject backend .`

2. **When you are done!... `exit`**

**HINT => you will keep the virtual environment running for as long as you are working. If you are done working for the day and want to close the vscode / project.. disconnect your server and your virtual environments first! It will stay running until then!**
   
3. Let's open the entire project in VSCode: `cd ..` should bring us to the parent folder: `~/code/SDA-Ghazal/applications/cat-collector-spa`. From here we will be able to access all files in both projects, our frontend and backends, and start servers for both of them. `code .` so we can open it in VSCode.


### Create the database

Databases are not automatically created by Django, so let's create one!

 - PSQL:
`CREATE DATABASE catcollectorspa;`

### Creating and registering a "Main App"

To tailor our `catcollector_spa` project for its specific purpose, we need to create our own app that handles our specific needs—collecting cats. It's a good practice to give your app a descriptive, yet general name. In this case, we’ll simply name our app `main_app`.

Create the App with the following command in the proper terminal location:

```bash
python3 manage.py startapp main_app
```

This command initializes a new Django app with the necessary files and directory structure. You’ll now find a `main_app` folder within the top-level project folder, set up as a Python module.​

Let’s include or "register" it as part of the `catcollector` project by adding it to the `INSTALLED_APPS` in `catcollector/settings.py` as well as `'rest_framework'` so can have access to that functionlity.

```python
INSTALLED_APPS = [
    # add main_app here
    'main_app',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Let's check to make sure the project starts up:
- `python manage.py runserver`

Ignore the red message about unapplied migrations, we'll take care of those in a bit.

Browse to `localhost:8000` and make sure you see the rocket on the page:

<img src="https://i.imgur.com/RozMgJ0.png">

### Connecting to the Database

Earlier, we created a dedicated `catcollectorspa` PostgreSQL database. A Django project's configuration lives in **settings.py**. Let's update it to use our `catcollectorspa` database:

**Note:** Some students may have to include the following fields(HOST, USER, PASSWORD), it depends how your Postgres is setup locally. For example, the most common setup for Windows and Linux users may require you to include these three fields to properly connect to your local Postgres instance. 

> 👀 You can also add the 'PORT' property (see below) to change the port to something other than :8000

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catcollectorspa',
    }
}
```

> 👀 By default, Django uses SQLite, a lightweight database that is not recommended for deployment. 

You may be seeing some red text about unapplied migrations in your terminal if your project successfully connected to the `catcollectorspa` database. Let's explain a little more about that and get that cleared up. 

### Migrating the Pending Migrations

We use migrations to update the database's schema over time to meet the project's needs.

There are several migrations **pending** (i.e., *waiting to be applied to the database*) - so let's apply them:

```
python manage.py migrate
```

You should see something similar to this:

![migrations](./assets//migrations.png)

😄 Nice - no more pending migrations! We will cover migrations in more detail in the next lesson.

## 4. Defining Routes (URLs)

### One-time URL Setup

In Django, routes are defined within modules named ***urls.py***.

There's an existing project ***catcollector/urls.py*** that we could add additional routes to, however it is *best practice* for each Django app to define it's own routes and to ***include*** those URLs in the project.

> 👀 There are some helpful comments at the top of ***catcollector/urls.py***.

Start by setting up ***main_app***'s ***urls.py*** file. But wait...there's not one:

1. Create the **urls.py** module: `touch main_app/urls.py`

2. Let's *include* it in the project's urls file - **catcollector/urls.py**

```python
from django.contrib import admin
# Add the include function to the import
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' represents the "starts with" path
    path('', include('main_app.urls')),
]
```


> 👀 Be sure to import the `include` function near the top.
    
Each item in the `urlpatterns` list defines a URL-based route or, as in the case above, mounts the routes contained in another urls.py module.

    
You can now close ***catcollector/urls.py***, since all routes we define from this point forward will be defined within ***main_app/urls.py*** - until we get to authentication that is.

3. Now for the boilerplate needed in ***main_app/urls.py***:

```python
from django.urls import path

urlpatterns = [

]
```

Notice that we've imported the `path` function that will be used to define each route. 

We've also created the required `urlpatterns` list which will hold each route we define for `main_app`.

### Define `main_app`'s Home Page URL

With the setup done, we're ready to define the route to return our first response when a user hits our home route.

In **main_app/urls.py**:

```python
# import Home view from the views file
from .views import Home

urlpatterns = [
  path('', Home.as_view(), name='home'),
]
```

The above code defines a *root* route using an **empty string** and maps it to the `views.home` view function that does not exist yet - making the server unhappy.

The `name='home'` kwarg gives the route a name.  Naming a route is optional, but is considered a best practice.

The Home route has been defined!  On to the view...

## 5. Defining View Functions

In the Home route we referenced a *view* function named `home`.

We will define all of the app's views in **main_app/views.py**.

Let's define the `home` view function and respond with JSON (since we are building a RESTful API):

```python
from rest_framework.views import APIView
from rest_framework.response import Response

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the cat-collector api home route!'}
    return Response(content)
```

**A few things to keep in mind** - We have removed the render import, which traditionally only serves HTML templates, from the original code in the views file with imports from django rest framework:

**APIView:**

- APIView is a class provided by Django Rest Framework that is used as a base for all views in DRF.
- It extends Django's basic View class and provides additional functionality that is specific to working with APIs.
- Using APIView allows you to handle different HTTP methods (GET, POST, etc.) with class methods and provides features like authentication, permissions, and throttling.

**Response:**

- Response is a class in DRF that is used to return responses from your API views.
- It extends the basic HttpResponse from Django but is specifically tailored for returning data in various formats (like JSON, XML, etc.).
- DRF's Response class also handles content negotiation based on the client's request, meaning it can automatically adjust the response format (JSON, HTML, etc.) based on what the client can accept.

## 6. Summary

You now have a minimal (but functional) application setup that responds with JSON.

You now know pretty much *all there is to know* about the structure of a Django app!

## 7. Check you can run both apps!

We now have a standalong backend that can serve as an API (application programming interface) that can serve whatever information we would like for it to serve. In this case, CATS! Yay.. haha.. 

We also have our standalone React/Vite application that will serve as our frontend and make requests to our backend for our Cats and other details!

Next we will setup out frontend static files and work towards making requests to our backend.
