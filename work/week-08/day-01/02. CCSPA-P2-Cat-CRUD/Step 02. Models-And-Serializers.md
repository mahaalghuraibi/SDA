<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 2 - Models and Serializers
We've successfully connected our React frontend with our DRF backend and have been able to render some awesome looking Cats from our API.. 

Now we need to implement CRUD based on an actual model. Just like we did before in our Cat Collector MPA, we will be setting up a model, migrating changes, using the admin portal, and performing CRUD. 

### REVIEW

Cat Collector Final ERD:

![Final ERD](./assets/cat-collector-erd.png)


Here’s the **Cat** entity from the ERD and the code to define the equivalent Model:

![Cat Model](https://i.imgur.com/gwlOAXc.png)

Exactly the same as it was in the previous approach.

### Serialization

The difference in the django rest framework setup is that we will need to serialize the data from our backend to be able to `Respond` to a request from the front end with JSON data. 

> Serializers allow complex data such as querysets and model instances to be converted to native Python data types that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

Seializers are:
- The bridge between your database models and your APIs.
- Tools that help you structure, validate, and transform your data when exposing it over HTTP.

**NOTE** We are now going to walk through implementing our main Cat model, and then updating our Cat Index view function to be able to return the cats from our postgresql database.

1. Cat Model
   
Let's start by implementing our Cat model in main_app/models.py

`models.py`
```python
from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

2. Setup Migration Files and Migrate
 - `ctrl+c` to exit your running server
 - `python3 manage.py makemigrations`
 - `python3 manage.py migrate`

3. Check out your psql shell and tables:

```sql
catcollector=# \dt
                     List of relations
 Schema |            Name            | Type  |    Owner
--------+----------------------------+-------+-------------
 public | auth_group                 | table | user
 public | auth_group_permissions     | table | user
 public | auth_permission            | table | user
 public | auth_user                  | table | user
 public | auth_user_groups           | table | user
 public | auth_user_user_permissions | table | user
 public | django_admin_log           | table | user
 public | django_content_type        | table | user
 public | django_migrations          | table | user
 public | django_session             | table | user
 public | main_app_cat               | table | user    <- Our new table!
(11 rows)

catcollector=#
```

4. Let's populate some values to work with!
```sql
insert into main_app_cat values
(default, 'Benji', 'calico', 'This kitty kat loves to explore the outdoors.', 2),
(default, 'Felix', 'tabby', 'A curious boy that has used at least six of his nine lives.', 1),
(default, 'Tofu', 'siamese', 'Loves long walks on the beach and trying to catch little fish.', 7),
(default, 'Veronica', 'persian', 'A lazy cat that is aging gracefully. Always looking for a sunny spot to rest.', 10),
(default, 'Dolce', 'ragdoll', 'Fluffy and optimistic. Loves catnip.', 3),
(default, 'Natalya', 'siberian', 'Used to cold environments. On the hunt for prey.', 8),
(default, 'Heathcliff', 'sphinx', 'Fat cat with an endless appetite.', 9),
(default, 'Bill', 'maine coon', 'Tuna, tuna tuna!', 4),
(default, 'Dev', 'devon rex', 'Always jumping and playful. Feed him a treat!', 4),
(default, 'Mary', 'oriental', 'Beautiful coat of fluffy fur. Loves to cuddle.', 2),
(default, 'Hussein', 'ragdoll', 'Will sleep on your head and meow up a storm when it is time to wake up.', 3),
(default, 'Shelly', 'calico', 'Pretty girl that loves watching her big brother bird named, Tweety!', 3);
```

5. Check your info in the psql shell: `select * from main_app_cat;`

**Should see your cats!**

6. Create your Superuser
- `python3 manage.py createsuperuser`
- Forgot your password? => `python3 manage.py changepassword <user_name>`
- Register our model in `main_app/admin.py`:

```python
from django.contrib import admin
# import your models here
from .models import Cat

# Register your models here
admin.site.register(Cat)
```

7. Setup our Serializer

Thankfully our rest_framework module comes installed with the code that we need to enable serialization to occur. Once again, syntactic sugar / abstraction to the rescue. We could go through the process of figuring out how it all works behind the scenes by looking at our packages, but we don't need to. It is not something we will remember or highly likely something you will ever have to do specifically. If you do, then you will research, find code, and work towards solving the problem. At the moment, "we have bigger ficsh to fry" as we say. So we will implement the code to access the serialization model, and keep moving...

In our `main_app` folder we will create a new file called `serializers.py` and add the following code:

`serializers.py`
```python
from rest_framework import serializers
from .models import Cat

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
```

7. Update our `URLS.py`
We should now have access to some Cats in our database and want to update our Cat URL to be able to get those cats using our rest_framework APIView. 

- updating the URL naming to be more appropriate:

`urls.py`
```python
from .views import Home, CatsIndex

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('/cats', CatsIndex.as_view(), name='cat-index'),
]
```
- Updating the views.py file to add 'generics' and our 'CatSerializer' so we can serialize the data from our database and send it back to React.
  
`views.py` 
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Cat
from .serializers import CatSerializer

class CatsIndex(APIView):
  serializer_class = CatSerializer

  def get(self, request):
    try:
      queryset = Cat.objects.all()
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

**CHECK TO SEE YOU RECEIVED YOUR CATS!**

### HomePage Update

Let's take this time to update our `HomePage.jsx`

Ultimately our homepage is going to be our LandingPage / Login Page. We should start building it though, in the background, while we work towards building out the rest of the site. So we're gonna slide this little side thought in right here...

Let's add our UI:

`HomePage.jsx`
```jsx
import "./styles.css";
import catCollectorCat from "../../assets/images/splash.svg";
import logoType from "../../assets/images/logotype.svg";

export default function HomePage() {
  return (
    <section className="logo-container">
      <div className="home-cat-container">
        <img src={catCollectorCat} alt="The Cat Collector Cat" />
      </div>
      <img src={logoType} alt="Text reads: Cat Collector" />
    </section>
  )
}
```

**Time to chat!**
We've intentionally built Cat Collector SPA to be a copy of Cat Collector MPA. The outcome should look like the exact same. However => we are running into a road block. Because we are working with different frameworks, the functionality and approach to development is slightly differnet, which means that accomplishing the same tasks may not always be the same. 

Previously when we used Django Templating we would load `CSS` files based on the specific page that was being loaded. In a single page application, we no longer have this luxury. Once the application is loaded, the CSS files are loaded and ready to go, which means the CSS selectors in each file are being matched whenever they are being rendered. 

If we look in `index.css` (our base html linked in our `index.html`) we can see that we already have css that points to some of the same properties. These properties are used in multiple locations throughout the application and realistically if we are loading more css on the `HomePage` specifically, then it is meant to only be for that page. While there are items within the CSS below that will only exist on the HomePage... we will need to create a way for us to display the `HomePage` css for the overlapping items only when the `HomePage` is the current route / location in our clientside routing. 

SO...

The original CSS file is below.. 

`./styles.css`
```css
main {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  height: 100%;
}

main > section {
  width: 100%;
  padding: 10px 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.header-logo-container {
  display: none;
}

.logo-container {
  max-width: 375px;
}

.cat-container {
  width: 80%;
}

.login {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 80%;
}

.login h1 {
  font-size: clamp(3.2rem, 3vw, 4.8rem);
  margin: 10px 0;
}

.login > p {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: 14px 0 0px;
}

.login label {
  font-size: var(--font-reg);
  margin-bottom: 6px;
}

.login input {
  font-size: var(--font-l);
  padding: 2px 4px;
}

.login .btn {
  align-self: flex-end;
  margin-right: 0;
  margin-top: 16px;
}

@media only screen and (min-width: 768px) {
  main {
    justify-content: space-around;
  }

  main > section {
    width: 40%;
  }

  .login {
    border: var(--borders);
    padding: 20px;
    border-radius: var(--card-border-radius);
    box-shadow: var(--card-box-shadow);
    width: 100%;
  }

  .logo-container {
    max-width: 520px;
  }
}
```

Following this statement is going to be the updated `CSS` file that will have some changed classnames that we can use for only when the current client side routing is set to `/HomePage`.

To be able to conditionally display the classnames for ONLY when our client side routing is `/Homepage` we will create a variable that allows us to conditionally add the classnames we want to add...

`./styles.css`
```css
main.home {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    height: 100%;
}

main.home > section {
    width: 100%;
    padding: 10px 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.header-logo-container.home {
    display: none;
}

.logo-container {
    max-width: 375px;
}

.home-cat-container {
    width: 80%;
}

.login {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 80%;
}

.login h1 {
    font-size: clamp(3.2rem, 3vw, 4.8rem);
    margin: 10px 0;
}

.login > p {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 14px 0 0px;
}

.login label {
    font-size: var(--font-reg);
    margin-bottom: 6px;
}

.login input {
    font-size: var(--font-l);
    padding: 2px 4px;
}

.login .btn {
    align-self: flex-end;
    margin-right: 0;
    margin-top: 16px;
}

@media only screen and (min-width: 768px) {
    main.home {
        justify-content: space-around;
    }

    main.home > section {
        width: 40%;
    }

    .login {
        border: var(--borders);
        padding: 20px;
        border-radius: var(--card-border-radius);
        box-shadow: var(--card-box-shadow);
        width: 100%;
    }

    .logo-container {
        max-width: 520px;
    }
}
```

Once we have added the proper CSS to the `HomePage/styles.css` we can then work towards setting up the conditional css we need to have in place.

### useLocation

useLocation is another fantastic `React Hook` that will allow us to get the current location of the client side route that we last navigated to / are currently on. Using this information, we can conditionally decide which `classNames` we want to display based on the current route... 

**We will want to add a route to ensure that any route points to the `home` route so that proper "pathname" in the useLocation hook is set.**

`Route to point to pathname '/home'`
```jsx
<Route path="/*" element={ <Navigate to="/home"/>}/>
```

`App.jsx`
```jsx
// import the hook
import { useLocation, Navigate } from 'react-router';

// access the location information
const location = useLocation();

// setup a variable for route based CSS styling
  const routes = ["about", "cats", "home"]
  const mainCSS = routes.filter(r => location.pathname.includes(r) ? r : "").join(" ")

    return (
    <>
      <header>
        <div className={`${mainCSS} header-logo-container`}>
          <Link href="/">
            <img src={headerLogo} alt="The Cat Collector Logo" />
          </Link>
        </div>
        <nav>
          <ul>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/cats">All Cats</Link></li>
          </ul>
        </nav>
      </header>
      <main className={mainCSS}>
        <Routes>
          <Route path="/*" element={<HomePage />}/>
          <Route path="/about" element={<AboutPage />}/>
          <Route path="/cats" element={<CatIndexPage allCats={allCats} />}/>
          <Route path="/*" element={ <Navigate to="/home"/>}/>
        </Routes>
      </main>
    </>
  );

```
