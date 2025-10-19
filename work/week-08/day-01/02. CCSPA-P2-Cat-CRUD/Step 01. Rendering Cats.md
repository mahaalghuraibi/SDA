<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 2 - CRUDing Cats

We'll start off by setting up our UI that will render all of our cats. This will be it's own client-side endpoint that will be used to render the cats. This means adding a new route, a new page level component, and doing all of the setup to make this process occur - let's get started!

### Setup
1. First let's create our new `pages` folder: `CatIndexPage` and add its contents:
```
└── src
│   ├── assets/
│   ├── components/
│   ├── pages/
│   │   ├── App
│   │   │   ├── App.jsx
│   │   │   └── styles.css
│   │   ├── HomePage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── AboutPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── CatDetailPage   <<<<<<<
│   │   │   ├── index.jsx   <<<<<<<
│   │   │   └── styles.css  <<<<<<<
│   │   ├── CatIndexPage    <<<<<<<
│   │   │   ├── index.jsx   <<<<<<<
│   │   │   └── styles.css  <<<<<<<
```

- Basic UI for Cat IndexPage

`CatIndexPage.jsx`
```jsx
import "./styles.css";
import coolCat from "../../assets/images/cool-cat.svg";
import happyCat from "../../assets/images/happy-cat.svg";
import teacupCat from "../../assets/images/teacup-cat.svg";
import catInBox from "../../assets/images/cat-in-box.svg";


export default function CatIndexPage() {
    return (<>
      <section className="page-header">
        <h1>Cat List</h1>
        <img src={coolCat} alt="A cool cat" />
        <img src={happyCat} alt="A happy cat" />
        <img src={teacupCat} alt="A cat in a teacup" />
        <img src={catInBox} alt="A cat in a box" />
      </section>
      <section className="index-card-container">
 
      </section>
    </>)
}
```

- Cat Index Page Styling
Let's grab our styling for the "page-header" and "card-container" classes.

**WHY IS THERE NO PAGE HEADER?**
=> it's already defined in the top level index.css!!

```css
.index-card-container {
  padding: 0 30px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
```


1. Import your new page at the top of `App.jsx`:
```jsx
import CatIndexPage from '../CatIndexPage';
```

1. Add your new route to `App.jsx`:
```jsx
<Route path="/cats" element={<CatIndexPage />} />
```

1. Add in the **Link** in the **nav** to be able to navigate to the page... 
```jsx
<nav>
 <ul>
   <li><Link to="/about">About</Link></li>
   <li><Link to="/cats">All Cats</Link></li>
 </ul>
</nav>
```

1. Make sure you can navigate to your page! - `Click!`


### Setup State, UI, and Request your Cats!
Our next step is to setup our User Interface to be able to view our Cats, store the state that represents our cats, and be able to request all of the cats from our server. We will **adapt** the same exact styling and setup from Cat Collector MPA to use in Cat Collector SPA... 

6. All Cats State:
   
`CatIndexPage.jsx`
```jsx
import { useState } from "React";
// other imports here

export default function CatIndexPage() {
    const [allCats, setAllCats] = useState([]);

    // this will not display anything yet...
    const displayAllCats = allCats.map(c => "")

    return (<>
        <section className="page-header">
            <h1>Cat List</h1>
            <img src={coolCat} alt="A cool cat" />
            <img src={happyCat} alt="A happy cat" />
            <img src={teacupCat} alt="A cat in a teacup" />
            <img src={catInBox} alt="A cat in a box" />
        </section>
        <section className="card-container">
            {displayAllCats}
        </section>
    </>)
}
```

7. Display Cat Component

We will need a componet that we can **reuse** to display any cats we find in our database for the index page... So, we'll create a `CatIndexCard` component!

```
└── src
│   ├── assets/
│   ├── components/
│   │   ├── CatIndexCard
│   │   │   ├── index.jsx
│   │   │   └── styles.css
```

`CatIndexCard/index.jsx`:
```jsx
import "./styles.css";
import skaterCat from "../../assets/images/sk8r-boi-cat.svg";

export default function CatIndexCard({ cat }) {

    return (
        <div className="cat-index-card">
            <div className="cat-index-card-content">
                <img src={skaterCat} alt="A skater boy cat" />
                <h2>{cat.name}</h2>
                <p>A {cat.age > 0 ? `${cat.age} year old ${cat.breed}` : `A ${cat.breed} kitten.`}</p>
                <p><small>{cat.description}</small></p>
            </div>
        </div>
    )
}
```

8. Cat Index Card Styling
We'll want that beautiful display of cats that we had in CCMPA =>

```css
.cat-index-card {
    width: 275px;
    margin: 10px;
    border: var(--borders);
    box-shadow: var(--card-box-shadow);
}

.cat-index-card-content {
    padding: 10px;
    width: 100%;
}

.cat-index-card > a {
    text-decoration: none;
    color: var(--text-color);
}

.cat-index-card h2 {
    margin: 10px 0;
    font-size: var(--font-xl);
}

.cat-index-card p {
    margin: 5px 0;
    font-size: var(--font-reg);
}
```

**CHECK IN**
We currently are blindly creating UI. We have no way of **TESTING** or checking that the UI is working the way we want it to. Before we start making requests to our backend for the cats in our database, let's add some cats to our front end that are hard coded so we can see the results...

`CatIndexPage.jsx` => add this as the starting state in the allCats useState():
```js
cats = [
    {name: 'Lolo', breed: 'tabby', description: 'Kinda rude.', age: 3},
    {name: 'Sachi', breed: 'tortoiseshell', description: 'Looks like a turtle.', age: 0},
    {name: 'Fancy', breed: 'bombay', description: 'Happy fluff ball.', age: 4},
    {name: 'Bonk', breed: 'selkirk rex', description: 'Meows loudly.', age: 6},
]
```

**AND** Let's import our CatIndexCard / use it to display the cats!!
`CatIndexCard`
```jsx
import CatIndexCard from "../../components/CatIndexCard";
//
//
const displayAllCats = allCats.map((c, ind) => <CatIndexCard key={ind} cat={c}/>);
//
//
<section>
  {displayAllCats}
</section>
```

**YOU SHOULD NOW SEE YOUR CATS BEING DISPLAYED**

### Let's get our Kittens!!

Our next step is to make our request from our front end to our backend to be able to **GET** our cats from our database to display them instead of our hard-coded-kitties that we currently have. We have NOT yet setup our backend to be able to respond with our Cats, but we will work towards that.

From previous labs and lessons we know how to setup our request from the front end so that we can get what we are looking for. This will be no different. SO... we will start the process of making the request for our origin file `CatIndexPage.jsx` and jump to `./utilities/cats.js` then to `./utilities/sendRequest.js` => then to our backend API!

`CatIndexpage.jsx`
```jsx
// IMPORTS
import { useEffect } from "React";

// APIs
import * as catAPI from "../../utilities/cat-api";

export default function CatIndexPage() {

    const [allCats, setAllCats] = useState([]);

    useEffect(() => {
        async function getAllCats() {
            try {
                const catData = await catAPI.index()
                console.log(catData)
            } catch (err) {
                console.log(err);
            }
        }
        if (allCats.length === 0) getAllCats()
    }, [])

    return()
}
```

`cat-api.js`
```js
import { sendRequest } from "./sendRequest";
const url = "/cats/"

export async function index() {
    return sendRequest(url)
}
```

`sendRequest.js`
```js
export default async function sendRequest(url, method = 'GET') {

	const options = { method };

	try {
		const res = await fetch(`http://localhost:8000${url}`, options);
		if (res.ok) return res.json();
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}
```

**RECAP**
We are making 3 leaps! From our `CatIndexPage` to our `cat-api.js` file to our `sendRequest.js` and ultimately to our backendAPI that will handle the request!

Does this seem complicated? Why is it necessary? Why not just make the request from the original file starting point????

Ultimately as your application grows you will see the same requests, same functionality, and same approaches occuring. What will change is your variables and small details about the requests. THIS is what code organization looks like.

Let's talk about our **updated** sendRequest function...

Prevously we were only making **GET** requests. BUT we will ultimately be doing far more than this... CRUD requires.. **CREATE**, **READ**, **UPDATE**, and **DELETE** requests... So we have to be able to specify those requests... the update is to be able specify the resource endpoint - `/cats/` and then specify the request **method** in an options object: { method: "GET" }. Inside of the parameters we set a default parameter of "method" as a "GET" request. 


If we did our homework correctly - we should see an error response like this:

`Access to fetch at 'http://localhost:8000/cats' from origin 'http://localhost:5173' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.`

Time to go setup our backend to receive requests!...

### Backend - Working with AJAX, CSRF & CORS
- [Django Rest Framework CORS Documentation](https://www.django-rest-framework.org/topics/ajax-csrf-cors/)
- [MDN Documentation on CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)

Because we are working with two different origins - one application (frontend) is set to port 5173 and one application(backend) is set to port 8000 - we are running into a security issue. Actually... the system is setup exactly as it is supposed to - the server is blocking requests that do not come from the same origin! This is great! We just have to setup our project to allow of react front end access to our Django Backend...

### Install 'corsheaders' package:
[Django CORS Headers Docs](https://pypi.org/project/django-cors-headers/)

First item of business is to install the 'corsheaders' package in our backend:
1. `exit` your pipenv shell if you have not yet
2. `pipenv install django-cors-headers`
3. your Pipfile should now display: `django-cors-headers = "*"`
4. Let's add `corsheaders` into our `installed apps` in `settings.py`

`settings.py`
```python
INSTALLED_APPS = [
    # add 'corsheaders' here
    'main_app',
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

5. We've now got some new middlewear to use!

`settings.py`
```python
MIDDLEWARE = [
    # ADD YOUR NEW MIDDLEWARE BELOW..
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

6. Specify Which Origins are Allowed:
We are only interested in allowing our specific origin / frontend to have access to our backend. SO - we can specify all origins to false and specify the one origin we want to allow...

`settings.py`
```python
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOW_HEADERS = '*'
CORS_ALLOWED_ORIGINS=[
    "http://localhost:5173"
]
```

**NOTE** There are plenty of other options that allow us to be more specific about what is and is not allowed within our application with the intent of increasing security... In this case, we do not need to be more specific as our application is not in danger of being misused by the outside world. We just needed to setup ourselves up to be able to access our backend from our frontend.. let's try it! Send the request again...

- reenter your `pipenv shell` and run your server... `python3 manage.py runserver`

## Create the URL / Endpoint

This should allow to be able to make a request to our backend.. NOW we need to set ourselves up with an endpoint to test that it works!

1. Setup Request / Response Cycle:

`urls.py`
```python
from .views import Home, Cats

urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('/cats/', Cats.as_view(), name='cat-index'),
]
```

`views.py`
```python
class Cats(APIView):
  def get(self, request):
    print("should be hitting api view")
    content = {'message': "Let's get some kitties!"}
    return Response(content)
```

if that worked! =>

2. Send back some Cats!

`views.py`
```python
class Cats(APIView):
  def get(self, request):
    content = [
        {"name": 'Lolo', "breed": 'tabby', "description": 'Kinda rude.', "age": 3},
        {"name": 'Sachi', "breed": 'tortoiseshell', "description": 'Looks like a turtle.', "age": 0},
        {"name": 'Fancy', "breed": 'bombay', "description": 'Happy fluff ball.', "age": 4},
        {"name": 'Bonk', "breed": 'selkirk rex', "description": 'Meows loudly.', "age": 6},
    ]
    return Response(content)
```

**You should see some cats!**

3. Update the state and render your cats!!

Update your useEffect and useState to add the state returned from our Django server... you should see this:

<img width="100%" src="https://i.imgur.com/JsP3RlB.png" />
