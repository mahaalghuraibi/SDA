# ![Django CRUD App - Cat Collector](./assets/hero.png)

![Cat Wave](./assets/cat-wave.png)

**Learning objective:** By the end of this lesson, learners will be able to login, signup, and validate a `User` within the Django Rest Framework system as well as setup these functionalities in the front end as well. Not that we have two separate entities, front and band ends, we will need to account for both sides! So let's get started!

## Setup

We will be working with a different approach to web Authentication. The `Json Web Token` or `JWT` is a base64 encoded URL napproach of representing `claims` or pieces of information between two different parties (front and back ends). The idea is that the format allows us to share sensitive information like passwords, username / email, etc. in a format that does not expose that information directly to the general public. Keep in mind this information is **NOT** encrypted.

### Django Rest Framework Docs on Authentication
[DRF Authentication Docs](https://www.django-rest-framework.org/api-guide/authentication/)

### Simple JWT Package Installation

We will be using a package to help speed along and simplify our approach to implementing JWT into our projects. Just like all of the built in functionalities that we have had access to already, this package can be installed to offer us code to simplify our process so that we do not have to write all of the code ourselves. We will install the appropriate configurations in settings.py now so that our boilerplate code is in place and ready to go.

Let's start by adding our `Simple JWT` package:

- disconnect your backend server if it is running
- ensure you are in the `backend` folder that contains your virtual environment
- install the package with: `pipenv install djangorestframework-simplejwt`
  - (or `python -m pipenv ...`)

Once installed we will move to configuring the package in `settings.py`...

### Settings.py
Now we can configuring our `simple-jwt` package in `settings.py`...

Generally speaking anywhere in the project works. I will place this set of code AFTER the MIDDLEWARE dictionary. 

`settings.py`
```python
# Configuration for simple JWT
# add the import at the top...
from datetime import timedelta

# MIDDLEWARE = {}
# .....
# Configuration for django-rest-framework-simplejwt
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}
```

### .ENV and SECRET_KEY
If you look, there is a `SIGNING_KEY` property inside the `SIMPLE_JWT` config dictionary that has a value of `SECRET_KEY`... The secret key is meant to be a secret key within your project that is few people have access to to be able to keep things safe. This is where the .env comes into play to maintain security for your project. 

We will create our .env file in our `backend` folder at the same level as our Pipfile. Inside we will add a `SECRET_KEY=<your info here>` and **move** our `SECRET_KEY` from our `settings.py` to our `.env`. It is located towards the top of yur `settings.py` (do not include the quotes!).

We will need a python package to access the .env file and then configure access to the information as well as update the secret to point to the information in your `.env` file.

#### Install `python-dotenv`
Let's start by installing the package. 
Which pip are you working with?...
- `pip --version` or `pip3 --version`

IF you are working with `python`:
- `pip install python-dotenv`
IF you are working with `python3`:
- `pip3 install python-dotenv`

#### CREATE .ENV
Once the package is installed we can create the .env
- `touch .env` or right-click on the `backend` folder where your `Pipfile` is and create the `.env` file.

Add your new secret code:

`.env`
```
SECRET_KEY=  DJANGO SECRET KEY FROM SETTINGS.PY
```

#### CONFIGURE .ENV
Now we will need access in `settings.py` to get the secret key...

`settings.py`
```python
# add the following imports / variables:
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")

# now the SECRET_KEY variable is set to our project secret key and
# is hidden in our .env file instead of publicly available.
```

**NOTES => KEEP IN MIND!**
**THIS INFORMATION HAS ALREADY BEEN MADE PUBLICLY ACCESSIBLE**
**ONCE YOU COMMIT && PUSH THIS INFORMATION ON THE VERY FIRST DAY WE MADE THIS PROJECT, WE ALREADY EXPOSED OUR INFORMATION**
**AT THE MOMENT IT DOES NOT MATTER AS WE ARE NOT STORING SPECIALTY INFORMATION IN OUR PROJECTS**
**DOWN THE ROAD YOU WILL WANT TO IMPLEMENT THIS INFORMATION ON DAY 1 AND NOT DAY 5 OF YOUR PROJECTS / BEFORE YOU PUSH CODE TO THE PUBLIC**

## Django User Model and Serializer

Just like Django Web Framework, our User model is built into the system through `django.contrib.auth.models`. We will import this model so we can build our `UserSerializer`.

`serializers.py`
```python
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Add a password field, make it write-only
    # prevents allowing 'read' capabilities (returning the password via api response)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user
```

**Notes** The `UserSerializer` overrides the create functionality to specify the password property as being `read-only` and the `create()` function to ensure validated data is used for the properties of username, email, and password.

## User View Functions

We will need three separate view functions to handle all user based functionalities.

- ONE => User Login
- TWO => User Signup / Registration
- Three => User Verification

We will take care of signup in this first step today.

## User Signup / Registration View Function

We can't really do much if we cannot signup / create a new user. SO we will start here!

`views.py`
```python
# import User model, UserSerializer, and RefreshToken...
from django.contrib.auth.models import User
from .serializers import CatSerializer, FeedingSerializer, ToySerializer, PhotoSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# User Registration
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    try:
      response = super().create(request, *args, **kwargs)
      user = User.objects.get(username=response.data['username'])
      refresh = RefreshToken.for_user(user)
      content = {'refresh': str(refresh), 'access': str(refresh.access_token), 'user': response.data }
      return Response(content, status=status.HTTP_201_CREATED)
    except Exception as err:
      return Response({ 'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

**A RefreshToken is a long-lived token used to obtain a new access token after the current one expires, without requiring the user to log in again.**

**An Access Token is a short-lived token used to make authorized requests to protected urls. We will use this throughout our project to keep things simple in a learning environment, but show that we have access to both so that you can make more complicated setups in the future.**

This will allow us to maintain verification in the background without having to bother the user / kick them out. Much better user experience!

### User Signup / Registraion URL

As usaul we will need a url / path to match the User Signup View function we just created.

`urls.py`
```python
from .views import CreateUserView

urls = [
    path('users/signup/', CreateUserView.as_view(), name='signup'),
]
```

This should complete our setup for making requests to our backend to handle user signup! Not too bad! BUT => there's much more to go to get this to work effectively!

## FRONTEND

The ultimate goal is to make it so that the User can stay logged in / maintain a session in their browser so long as they do not implicitely "logout" / remove their credentials.

To make this possible we will need to implement the following items:

- User State for conditional routing && navigation
- `SignupPage.jsx` page for signup / form
- `Navigation` component to declutter the `App.jsx` file as it grows
- `user-api.js` for making User related requests
- a function to handle storing the JWT response in localStorage.

### Users API

As usual we will create a new api / requests file related to our new resource (Users) and it will go into our utilities folder. Form here we will setup some functions / boilerplate, but for now will keep the main contents empty...

`utilities/users-api.js`
```js
import sendRequest from "./sendRequest";
const url = "/users/"

export function signup() {

}

export function login() {

}

export function logout() {

}
```

### User State and Logout Function
Time to refactor!

Let's start by setting up our application state and one logout function so that we can conditionally decide which routes and links to display based on User State.

Our `App.jsx` file is the top level location for handling application state and gives us the ability to conditionally update our `Navbar`, `Homepage`, and `Routes` accordingly...

First we will create our User State, `logout`, `login`, `signup` functions. Then setup the pages / components we will need, then come back to App.jsx to import all new items and properly pass down all props.. Its a process!!

`App.jsx`
```jsx
// make sure useState is imported!
const [user, setUser] = useState(null)


```

### Navigation as a Component

Our Navigation is about to get a bit larger and complicate our App.jsx... so let's subdivide into a separate component...

Instead of using a ternary operator and complicate the readability of the file, we will divide it into two `if` statements. One for a truthy User and one for a falsy User object...

`/components/Navbar/Navbar.jsx`
```jsx
// imports
import { useNavigate, Link } from "react-router";

// APIs
import * as usersAPI from "../../utilities/users-api";

export default function Navbar({ user, setUser }) {
    const navigate = useNavigate();

    // will refresh state and set us back to home without a user
    function handleLogout() {
        usersAPI.logout()
        setUser(null);
        navigate("/")
    }

    if (user) {
        return (
            <>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/cats">All Cats</Link></li>
                <li><Link to="/cats/new">New Cat</Link></li>
                <li><Link to="/toys/new">Add a Toy</Link></li>
                <li><Link to="/toys">All Toys</Link></li>
                <form id="logout-form" onSubmit={handleLogout}>
                    <button type="submit">Log out</button>
                </form>
            </>
        )
    }

    if (!user)
        return (
            <>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/home">Home</Link></li>
                <li><Link to="/signup">SignUp</Link></li>
            </>
        )

}
```

### Ugly Logout Form Button and Signup Button

Let's add our CSS to our top-level `index.css`!..

Down by the other form css items is great!

```css
#logout-form button {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 600;
  font-size: 16px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  font-family: inherit;
}

#logout-form button:hover {
  color: var(--link-hover-color);
}

.form-container.signup > button {
  max-width: 25%;
  align-self: end;
  margin-right: 40px;
}

.form-container.signup > table > tbody > tr > th {
  width: 25%;
}

.form-container.signup input {
  width: 100%;
  align-self: end;
  margin-right: 40px;
}
```

**Questions??**

### SignUpPage

Next, our SignUp Page has it's own route (like CCMPA) so we will do the same!

`SignupPage.jsx`
```jsx
// IMPORTS
import { useState } from "react";
import { useNavigate } from "react-router";

// IMAGES
import nerdCat from "../../assets/images/nerd-cat.svg";

// APIs
import * as usersAPI from "../../utilities/users-api.js"

export default function SignupPage({ setUser }) {
    const navigate = useNavigate();
    const initialState = { username: "", password: "", confirmPassword: "", email: "" }
    const [formData, setFormData] = useState(initialState)
    const [errors, setErrors] = useState({ username: '', password: '', email: '', confirmPassword: '' });
    let disabledSubmitBtn = Object.values(errors).every(val => val === "") && Object.values(formData).every(val => val !== "") ? false : true

    function handleChange(evt) {
        setFormData({ ...formData, [evt.target.name]: evt.target.value });
        checkErrors(evt);
    }

    function checkErrors({ target }) {
        const updateErrors = { ...errors }

        if (target.name === 'username') {
            updateErrors.username = target.value.length < 3 ? 'Your username must be at least three characters long.' : "";
        }
        if (target.name === 'password') {
            updateErrors.password = target.value.length < 3 ? "Your password must be at least three characters long." : "";
        }
        if (target.name === 'confirmPassword') {
            updateErrors.confirmPassword = target.value !== formData.password ? "Your passwords must match." : "";
        }
        if (target.name === 'email') {
            updateErrors.email = !target.value.includes("@") ? "Your password must be a real email / include the '@' symbol." : "";
        }

        setErrors(updateErrors);
    };

    async function handleSubmit(evt) {
        try {
            evt.preventDefault()
            const newUser = await usersAPI.signup(formData);
            setUser(newUser);
            setFormData(initialState)
            navigate("/cats")
        } catch (err) {
            console.log(err);
            setUser(null);
        }
    }

    return (<>
        <div className="page-header">
            <h1>Sign Up</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form onSubmit={handleSubmit} className="form-container signup">
            <table>
                <tbody>
                    <tr>
                        <th><label htmlFor="id_username">Username:</label></th>
                        <td>
                            <input type="text" value={formData.username} name="username" minLength="3" maxLength="150" onChange={handleChange} />
                            <br/>
                            { errors.username && <p>{errors.username}</p> }
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_email">Email:</label></th>
                        <td>
                            <input type="text" value={formData.email} name="email" minLength="3" maxLength="150" onChange={handleChange} />
                            <br/>
                            { errors.email && <p>{errors.email}</p> }
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_password1">Password:</label></th>
                        <td>
                            <input type="password" value={formData.password} name="password" minLength="3" onChange={handleChange} />
                            <br/>
                            { errors.password && <p>{errors.password}</p> }
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_password2">Password confirmation:</label></th>
                        <td>
                            <input type="password" value={formData.confirmPassword} name="confirmPassword" onChange={handleChange}/>
                            <br/>
                            { errors.confirmPassword && <p>{errors.confirmPassword}</p> }
                        </td>
                    </tr>
                </tbody>
            </table>
            <button type="submit" disabled={disabledSubmitBtn} className="btn submit">Submit!</button>
        </form>
    </>)
}
```

### Update App.jsx

Let's add our updated navigation and signup page components to App!

`App.jsx`
```jsx
import Navbar from '../../components/Navbar/Navbar';
import SignupPage from '../SignupPage/SignupPage';

    // add Navbar =>
    <ul>
      <Navbar user={user} setUser={setUser} />
    </ul>

    // add new signup route / page
    <Routes>
        <Route path="/signup" element={<SignupPage user={user} setUser={setUser} />}/>
    </Routes>


```
**Check that your signup page can load AND that your form validators work to ensure you are ready to go to take the next step. If it works, you should navigate to the HomePage and see your console.log("checking handle submit signup")**


## Signup Request / Create User

We've successfully setup the majority of the items (finally!) that we will need to implement User Create / Signup. Our next step is to ensure our User Signup Request in `users-api.js` is ready to go with the correct path, method, and information to complete `Signup` functionality.


### Users-API.js Request =>
We have a starting point from earlier that we will continue to add on to. The `/users/` url is the base path we will be using and we will also use our sendRequest file to submit the resuqest to the server. Let's complete our signup function to submit the request.

We are submitting formData to `create` our new User... which means a POST request along with the formData from our signup form page. In our `urls.py` we have a path of `/users/register/` that we need to match.. so we will do that!

We want to be able to see what is returned so we can understand what information to deal with.. we will refactor later!

`users-api.js`
```js
import sendRequest from "./sendRequest";
const url = "/users"

export async function signup(formData) {
    console.log(formData, "checking formdata")
    const user = await sendRequest(`${url}/register/`, "POST", formData)
    console.log(user)
    return user;
}

export function login() {

}

export function logout() {

}
```

**Let's Talk!!**

What did we receive?!?!?!?

```js
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTA3NzUwOSwiaWF0IjoxNzQ0OTkxMTA5LCJqdGkiOiJlODczNGU5OWUyYWQ0ZTg1YWEwMDU1ZmYzZGVkMTM0ZCIsInVzZXJfaWQiOjR9.PEw7rw2NfsdmKwhcxxrTtnKoNlARRAVSwOrvsj7SSIU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MDc3NTA5LCJpYXQiOjE3NDQ5OTExMDksImp0aSI6IjdhYjcxMjBiNGI5MjRkOWY4ZGFjZDVmMmMxNGQ0OTk3IiwidXNlcl9pZCI6NH0.5ta5tOQhYB53MhybKCMa9-Y1vIRbrma8AZlezjAkr7Q",
    "user": {
        "id": 4,
        "username": "devil4",
        "email": "devil4@4.com"
    }
}
```

**WHAT IS ALL OF THAT!!!!???**

Back to our conversation about the JSON Web Token =>

When we setup our User Create view function we responded with 3 items: `refresh`, `access`, and `user`.

- Refresh represents a 'long-lived' token meant to be used to refesh your access token after it has expired.
  
- Access represents your 'short-lived' token meant to be used in an `Authorization Header` like this: `Authorization: Bearer <access_token>`. We will be doing this shortly!
  
- User represents the unencoded user that we will set our applications logged in user in state. Notice there is no specifically sensitive information - it does not include any password info!

- For the purpose of this course, we will only need to use the Access token directly to accomplish our tasks. The point is to recognize you have access to this information to perform more secure requests at a later time.

**Before we move on!!** We will want to refactor our `signup` funcion to store the access token in local storage for all subsequent requests for when a user is logged in and working to access server side routes that should only be accessed if a user is logged in! 

#### TODO:
- Cleanup the signup function 
- Set the access token in local storage
- Return the newly created User


`users-api.js`
```js
import sendRequest from "./sendRequest";
const url = "/users"

export async function signup(formData) {
    try {
        const response = await sendRequest(`${url}/signup/`, "POST", formData)
        localStorage.setItem('token', response.access);
        return response.user
    } catch(err) {
        localStorage.removeItem('token');
        return null;
    }
}

export async function login() {

}

export async function logout() {

}

```

## Logout

We still have multiple steps to go to get our full User functionality in place. By far the EASIEST item to take care of is logging out the user. Logging out does not reqire anything other than removing the current token from the localStorage and setting our User State back to `null`! So let's take care of that really quickly!

`users-api.js`
```js

export async function logout() {
    localStorage.removeItem('token');
}

```

One line of code! Head to `Step 02. User Login and Verification`!