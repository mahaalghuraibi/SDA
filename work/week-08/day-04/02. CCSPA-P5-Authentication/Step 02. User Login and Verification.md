# ![Django CRUD App - Cat Collector](./assets/hero.png)

![Cat Wave](./assets/cat-wave.png)

**Learning objective:** By the end of this lesson, learners will be able to login and validate a `User` within the Django Rest Framework system as well as setup related frontend functionalities.

# Server Side Login Functionality

## Setup and Approach

We will start by setting up our login function / urls since it requires the leat amount of code and makes the most sense. Then target our React frontend and its necessary code to make this happen... 

Our new import:
- authenticate => built in function from django authentication that will compare the username and password to ensure they match properly 

## Views.py

`views.py`
```python
# new import!
from django.contrib.auth import authenticate

class LoginView(APIView):

  def post(self, request):
    try:
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        refresh = RefreshToken.for_user(user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data}
        return Response(content, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## URLs.py

```python
from .views import LoginView

urlpatterns = [
  path('users/login/', LoginView.as_view(), name='login'),
]
```

# Client Side / Frontend Functionality

## HomePage and UserLoginForm

Just like our MPA Cat Collector we will use our `HomePage` as the location of Login Functionality. 

This will require another form, but much less information, so we can keep the form and related state on the homepage. It is dependent upon the user being logged in. So let's be ready to accept the user object as props / destructure the user object...

FULL UPDATE =>
`HomePage.jsx`
```jsx
// IMPORTS
import "./styles.css";
import { useState } from "react";

// IMAGES
import catCollectorCat from "../../assets/images/splash.svg";
import logoType from "../../assets/images/logotype.svg";

// APIs
import * as usersAPI from "../../utilities/users-api";


export default function HomePage({ user, setUser }) {
  const initialState = { username: "", password: "" }
  const [formData, setFormData] = useState(initialState)

  function handleChange(evt) {
    setFormData({ ...formData, [evt.target.name]: evt.target.value})
  }

  async function handleLogin(evt) {
    evt.preventDefault();
    console.log("time to login!!!!")
  }

  return (<>
    <section className="logo-container">
      <div className="home-cat-container">
        <img src={catCollectorCat} alt="The Cat Collector Cat" />
      </div>
      <img src={logoType} alt="Text reads: Cat Collector" />
    </section>
    {!user &&
      <section>
        <form onSubmit={handleLogin} className="form-container login">
          <h1>Login</h1>
          <p>
            <label htmlFor="id_username">Username:</label>
            <input value={formData.username} type="text" name="username" maxLength="150" required id="id_username" onChange={handleChange}/>
          </p>
          <p>
            <label htmlFor="id_password">Password:</label>
            <input value={formData.password} type="password" name="password" required id="id_password" onChange={handleChange} />
          </p>
          <button type="submit" className="btn submit">Login</button>
        </form>
      </section>
    }
  </>)
}
```

**Check to make sure your form is displaying and if you click the submit button you receive your "time to login!!" console log!!**

## Login Request in Users API

Our login request is going to be quite similar to our signup request.. infact, it is nearly identical!

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

// updated login function!
export async function login(formData) {
    try {
        const response = await sendRequest(`${url}/login/`, "POST", formData)
        localStorage.setItem('token', response.access);
        console.log(response, "login check response")
        return response.user
    } catch (err) {
        localStorage.removeItem('token');
        return null;
    }
}

export async function logout() {
    localStorage.removeItem('token');
}
```

I think we are ready! Update your handleLogin() function in `HomePage.jsx`

`HomePage.jsx`
```jsx
import { useNavigate } from "react-router";

async function handleLogin(evt) {
    try {
      evt.preventDefault();
      const loggedInUser = await usersAPI.login(formData);
      setUser(loggedInUser);
      navigate("/cats");
    } catch (err) {
      setUser(null);
    }
}
```







