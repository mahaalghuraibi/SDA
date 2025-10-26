# Testing Django REST Authentication

## Lesson Objectives

- Understand the Django test directory structure and file organization
- Comprehensive authentication testing using Django REST Framework's `APITestCase`
- Implement thorough test coverage for JWT authentication flows

## Testing Environment Setup

Previously we worked with our `tests.py` file that was created for us when Django was used to created our `main_app` application. We directly placed testing code in this file `tests.py` and everything was great! Now our testing is about to grow and we need to organize / make space...

We now want to have a testing folder that can handle multiple files. SO! We will `mkdir` or right click to create a new folder called `tests` in our main application...

New folder: `main_app/tests`

Within this new folder we can now hold all of the test files we would like to be able to run for our application. From here we will be able to run the tests with the same command we previously used..

`python manage.py test main_app/tests` will run all files in the testing file that start with `test`. For example:

- `test_models.py`
- `test_authentication.py`

In order for this to work, though... we have to create an `__init__.py` in the same directory! Our folder structure will look like this:

```plaintext
main_app/
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_authentication.py
```

Once you run the command, all test files will run!

**ONE LAST THING**
In order for the environment to work... we need our virtual environment shell up and running.. so don't forget!...

Commands:
`pipenv shell`
`python manage.py test main_app.tests`
**notice the `.` instead of a `/`**

**OR**
`python manage.py test main_app.tests -v 2`
The `-v 2` flag enables verbose output, which is valuable for debugging and understanding test behavior.

## Understanding the Test Structure
When testing Django REST Framework authentication, we organize our tests in a way that mirrors the authentication flow a user would experience. The test file structure follows Django's convention of using the `APITestCase` class, which provides specialized testing capabilities for REST APIs. 

Let's examine our base test class:

```python
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTests(APITestCase):
    def setUp(self):
        """Set up test client and create test user"""
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.token_refresh_url = reverse('token_refresh')
```

The `setUp` method is fundamental to our testing strategy. Every test method needs a fresh environment to ensure accurate results. When the `setUp` method runs before each test, it creates a new `APIClient` instance. This client simulates HTTP requests to our API endpoints, allowing us to test how our authentication system responds to different scenarios. We also create a test user that serves as our baseline for authentication tests. The use of `reverse()` for URLs is particularly important as it maintains test reliability even if URL patterns change in the future.

What is the `reverse()` function? 

The `reverse()` function is imported from Django.urls and is used to find the "url / path" that is associated with the "name" that is passed into the function when called.. `reverse("name of path")`. This ensures the view function we are trying to reach is always the same even if the actual url changes. 

## Testing `User` Registration

The registration process is often the first interaction a user has with your authentication system. Our registration tests need to verify both successful and failed attempts.

By simulating a new user signing up for our application, we ensure the entire registration flow works as expected.

The test sends a POST request with user data, verifies the correct HTTP status code (200 OK), that the response includes both access and refresh tokens and confirms the user was created in the database. Success!

Try it in your Cat Collector Project!

```python
    def test_user_registration_success(self):
        """Test successful user registration"""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        self.assertTrue(User.objects.filter(username='newuser').exists())
```

## Test Registration with Invalid Data

Testing invalid registration scenarios is equally important. This test verifies that our API properly handles and rejects incomplete or invalid registration data. When a client sends insufficient information, our API should respond with a 400 Bad Request status code. This helps ensure our application maintains data integrity and provides clear feedback to users when registration fails.

```python
     def test_user_registration_invalid_data(self):
        """Test user registration with invalid data"""
        # Test missing required fields
        data = {'username': 'incomplete'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Testing User Authentication

After registration, we need to ensure users can successfully log in and receive authentication tokens:

The login test verifies that when a user provides valid credentials, they should receive access and refresh tokens in response. The access token is used for immediate authentication, while the refresh token allows users to obtain new access tokens without re-entering their credentials. This implementation follows JWT best practices, where access tokens have a shorter lifespan for security, while refresh tokens last longer for user convenience.

```python
    def test_user_login_success(self):
        """Test successful user login"""
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(self.login_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
```

## Testing Login with Invalid Credentials

This test ensures that invalid credentials are properly rejected. When incorrect credentials are provided, the API must respond with a 401 Unauthorized status code. This helps prevent unauthorized access and provides appropriate feedback to users attempting to log in.

```python
    def test_user_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
```

## Testing Token Refresh Functionality

JWT authentication requires proper token refresh handling to maintain user sessions:

Token refresh testing is essential for maintaining secure, long-term user sessions. This test simulates the complete token refresh flow: 

1. Obtain tokens through login
2. Use those tokens to request a refresh. 

We verify that the refresh endpoint returns new tokens while maintaining the user's authenticated session. This process is crucial for applications that need to maintain user sessions beyond the initial access token's expiration.

```python
    def test_token_refresh(self):
        """Test token refresh functionality"""
        # First, get a token pair by logging in
        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        login_response = self.client.post(self.login_url, login_data, format='json')

        # Set the authentication header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')

        # Test token refresh
        response = self.client.get(self.token_refresh_url)  # Changed from POST to GET
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
```


## Exercise: Testing Invalid Token Refresh in Django REST Framework

Your task is to implement a test method that verifies how your authentication system handles **invalid** token refresh attempts. This test should ensure that your application properly rejects requests with invalid tokens.

**STEP-BY-STEP**

1. Add a new test method called `test_token_refresh_invalid_token` 
2. Attempt to refresh the token
3. Setup the method to verify that when an invalid token is used to request a refresh, the system responds with a 401 Unauthorized status code.


## Testing Protected Endpoints

Lastly, testing protected endpoints verifies that our authentication middleware correctly guards restricted resources. This test demonstrates both unauthorized and authorized access attempts to protected endpoints. 

1. First confirm that unauthenticated requests are rejected. 
2. Then verify that properly authenticated requests are allowed.

```python
    def test_authentication_required_endpoints(self):
        """Test endpoints that require authentication"""
        # Try accessing protected endpoint without authentication
        cats_url = reverse('cat-index')
        response = self.client.get(cats_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Login and try again
        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        login_response = self.client.post(self.login_url, login_data, format='json')
        token = login_response.data['access']

        # Add token to request header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(cats_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

## Test Cleanup and Maintenance

The `tearDown` method runs after each test, ensuring that authentication credentials don't leak between tests. This is crucial for test isolation and prevents false positives or negatives in our test results.

The `self.client.credentials()` function will reset any previously used credentials by setting them back to 'factory state' or the starting point / being empty.

This is all we need:

```python
    def tearDown(self):
        """Clean up after each test"""
        self.client.credentials()
```

## Summary

This comprehensive authentication testing suite ensures robust security and proper functionality of your Django REST Framework application's authentication system. The tests cover the complete authentication lifecycle, from user registration through protected resource access. By implementing these tests, you create a strong foundation for maintaining authentication security and reliability in your application.

The systematic approach to testing authentication ensures that your application handles user authentication securely and reliably. Regular execution of these tests, especially as part of your continuous integration pipeline, helps catch authentication-related issues early in the development process. Remember that authentication testing is not a one-time task but an ongoing process that should evolve with your application's security requirements.
