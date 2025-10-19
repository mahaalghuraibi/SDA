# ![Django CRUD App - Cat Collector](./assets/hero.png)

![Cat Wave](./assets/cat-wave.png)

**Learning objective:** By the end of this lesson, learners will be able to relate a User to a specific Cat and protect routes that should not be accessible if a user is not logged in.

# Relating Users to Cats

### Cat Model

Nothing new here - eactly the same as Multi-Page Cat Collector!

`models.py`
```python
# new import!
from django.contrib.auth.models import User

# update cat model!

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    # add the new line of code to unclude a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

## What do we do after we add or update a model?

```bash
python3 manage.py makemigrations
```

Which then presents us with this message:

```plaintext
You are trying to add a non-nullable field 'user' to cat without a default;
we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
```

Option `1)` is our best option because it will allow us to enter the `id` of a user, which we created in an earlier lesson (the superuser).

Press `1` and `[enter]`, which will then prompt us to enter that value:

```plaintext
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available,
so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>>
```

Our superuser’s `id` should be `1`, so type `1` and press `[enter]`.

The migration file will then be created. Let’s migrate the changes. In your terminal enter the following:

```bash
python3 manage.py migrate
```

Congrats, the one-to-many relationship between `User` and `Cat` has been established and all existing cats have been collected by the superuser!

## Updating Cat Serializer
We are going to update the Cat Serializer object to include a user field. We will do this for two reasons:

1. Including the field with `read_only=true` will prevent the validation of the serializer from throwing an error if the user_id is not provided upon `serialzer.is_valid()` function call. We are not passing the user id in the request object ahead of time as we want the validated user in the request object to be assigned after validation.

2. If we remove this `user = serializers.PrimaryKeyRelatedField(read_only=True)` code from the serializer an error will be thrown that says the validation is expecting a user_id to be there. This allows us to bypass, validate the formData, and then add the user. Same concept with two different perspectives. Another approach.

`serializers.py`
```python
class CatSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)
    toys = ToySerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
```

## Including The JWT in the Request

In order to make successful requests related to the logged in user in the front end, Django Rest Framework now requires us to provide information about the logged in user. If we make a request without this information and `print(request.user)` in our server.. it prints out: `AnonymousUser`! This won't work for us.. 

We need to include our JWT in our requests!

Let's head to `sendRequest.js` to make the update =>

### Adding the JWT to requests

`sendRequest.js`
```js
export default async function sendRequest(url, method = 'GET', payload) {
    // check if there is a token for a logged in / stored user
    const token = localStorage.getItem('token');

	const options = { method };
	if (payload) {
		options.headers = { 'Content-Type': 'application/json' };
		options.body = JSON.stringify(payload);
	}

    // this will add an Authorization header whether or not headers exist
    if (token) {
        options.headers = options.headers || {};
        options.headers.Authorization = `Bearer ${token}`;
    }

	try {
		const res = await fetch(`http://127.0.0.1:8000${url}`, options);
		if (res.ok) return res.json();
	} catch (err) {
		console.log(err, "error in send-request");
		throw new Error(err);
	}
}
```
**Thats it!**
If you make a request to an endpoint in the server and `print(request.user)` you will see the info of the user that logged in! Cooool!


## Update CatCreate View Function

We now want to ensure that any new cats being created will specifically be related to the logged in user. We also want to ensure that the logged in user can only access the cats created by that User. Check out the code below and take a look at the changes. There is commented code / spacing to show where the changes are...

`Views.py - CatsIndex`
```python
class CatsIndex(generics.ListCreateAPIView):
  serializer_class = CatSerializer

  def get(self, request):
    try:
      queryset = Cat.objects.filter(user=request.user)
      serializer = CatSerializer(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def post(self, request, *args, **kwargs):
    try:
      serializer = self.serializer_class(data=request.data, context={'request': request})
      if serializer.is_valid():
        serializer.save(user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({"error": str(err)})
```


**That's it!** All of our view functions are in place and ready to accept all requests. Our next job is to protect our routes!

## Adding Permissions and Protecting Routes on the Server

Just like our previous round of Cat Collector, we have existing functionality built into our framework that will setup permissions for us. We will import a permissions module to access functions to protect our routes using one line of code, and then place that information on each of our API views...

`views.py`
```python
# add permissions as an import from rest_framework
from rest_framework import generics, status, permissions

# add to the following functions:

class CatsIndex(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = CatSerializer

class CatDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = CatSerializer

class FeedingsIndex(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = FeedingSerializer

class ToyIndex(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ToySerializer
  queryset = Toy.objects.all()

class ToyDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ToySerializer
  lookup_field = 'id'

class AddToyToCat(APIView):
  permission_classes = [permissions.IsAuthenticated]

class RemoveToyFromCat(APIView):
  permission_classes = [permissions.IsAuthenticated]

class PhotoDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = PhotoSerializer
```

That should take care of our views!

## One Last thing! => Refresh Token and Auto-Login

We now have a users token stored in the browser's `localStorage` and ready to go as long as the user has not specifically logged out at some point. When we return to our website, so long as the token has not expired, we should expect to be able to log back in and not think twice about it. Its a great feature for users!

Let's add a `useEffect()` in our App.jsx to check if there is a user token in storage and take care of ensuring the token is fresh / uptodate. It's a simple process with one new endpoint and very little code!

As usual, we'll start with the server by setting up our view function to refresh the token, then the url, then head back to our react app and set things up!

### Views.py

`views.py`
```python
# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    try:
      user = User.objects.get(username=request.user.username)
      try:
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh),'access': str(refresh.access_token),'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
      except Exception as token_error:
        return Response({"detail": "Failed to generate token.", "error": str(token_error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      return Response({"detail": "Unexpected error occurred.", "error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

```

### URLS.py

`urls.py`
```python
# add the new endpoint
path('users/token/refresh/', views.VerifyUserView.as_view(), name='token_refresh'),
```

## New Request in users-api

Take a look at the code and read the logic of what we are attempting to do?...

`users-api.js`
```js
export async function getUser() {
    try {
        const token = localStorage.getItem('token');
        if (token) {
            const response = await sendRequest(`${url}/token/refresh/`)
            localStorage.setItem('token', response.access);
            return response.user
        }
        return null;
    } catch (err) {
        console.log(err);
        return null;
    }
}
```

## App.jsx => useEffect()

Our last step is to call our getUser() function in our App.jsx...

`App.jsx`
```jsx
import { getUser } from '../../utilities/users-api';

const [user, setUser] = useState(getUser());
```

**That's it!**

