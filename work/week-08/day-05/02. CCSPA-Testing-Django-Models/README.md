# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Testing Django Models

### Lesson Objectives

Our goal for this lesson is to clarify what to test, why we test, and how to use Django's Built-In `TestCase` functionality to test our Django Models. 

In a general sense, we test applications to:

- Catch bugs early
- Prevent regressions (things breaking that used to work)
- Safely refactor or extend your code
- Build confidence in your app’s stability
- Document how your code is expected to behave

**Can't we do this manually, though?**
Yes! You can, and should! BUT => What makes testing through code more reliable than testing as a human? Think about it? What is this kind of testing through code, called?

**Automated Testing**

Authomated testing is the process of writing and using the computer / code to consistently use the same tests to validate and ensure our environment has not changed anything important as we have continued to develop our applications. Using automated testing ensures quality and consistentcy in our applications. It helps: 

1. ✅ Speed & Efficiency
- Automated tests run in seconds (or less), no matter how many times you run them.
- Manual testing takes much longer and doesn’t scale.

🧠 Example: Clicking through a form manually vs. running python manage.py test and validating 10+ cases instantly.

2. 🛡️ Consistency & Reliability
- Automated tests always follow the same steps — no human error, no skipped steps.
- Manual tests are prone to mistakes: forgetting to click a button, using the wrong input, etc.

3. ♻️ Repeatability
- Automated tests run the same tests every time you change your code.
- Manual testing is harder to repeat consistently — and you might forget to check something critical.

4. 🧨 Early Bug Detection (Regression Prevention)
- Automated tests catch bugs as soon as they're introduced, often before they go live.
- protect against regressions — things that used to work breaking after a new change.

📉 Without tests: You fix one thing, break another.

🔁 With tests: If something breaks, the tests alert you immediately.

5. 📋 Documentation of Expected Behavior
- Tests double as living documentation for how your code is supposed to work.

New developers (or even future you) can read tests to understand what the app is supposed to do.

6. 💥 Safe Refactoring
- Want to clean up, rename, or refactor code?

If you have solid tests, you can do it with confidence — the tests will let you know if you broke anything.

7. ⚙️ Can Be Automated in CI/CD
- Automated tests can run every time you push to GitHub using CI tools like GitHub Actions or GitLab CI.

That means your app is always being tested, even if you forget.


### Testing Django Models with Django TestCase

In Django applications, models are the backbone that handle data management and database interactions. Ensuring the reliability of models through comprehensive testing is crucial. Django provides a robust framework for testing through the `django.test` module, leveraging Python's built-in unittest framework.

We will cover different types of tests using our `Cat Collector SPA` models (cats, toys, feedings, photos, users). These models demonstrate common relationships: One-To-One, One-to-Many, Many-to-Many, and ForeignKey constraints.


### Setup

Upon creating our `cat-collector-spa/backend` project and `main_app` application, Django also included a `tests.py` file for us... that's the perfect spot to add these tests! Party!

You should the first line of code in the file => 

`from django.test import TestCase`... 

We can add the other modules / imports below that we will need to access:
- access models (cat, toy, feeding) from `main_app.models`
- access user from `django.contrib.auth.models`
- `from datetime import date` so we can check dates on our Cat Feedings

### Goals
**reminder => our goal is to automate the process checking and ensuring that: 
- items are being created properly have a expected property to confirm
  - cat
  - user
  - photo
  - feeding
  - toy
- relationships are being created properly
  - cat < feedings
  - cat <> toys
  - cat > user (foreign key)
  - cat - photo (ensure only one)
- built in model methods work accordingly
  - check the feedings are ordered properly (Meta class)
  - we do not have any other built or specific model related functionalities
- deleting properly deletes and cascades
  - delete cat = zero feedings and no related photo
  - delete user = zero cats


## LETS DO THIS!

The `TestCase` class sets up an isolated test environment with a temporary database.

The `setUp` method initializes data before each test is run. 

This ensures a consistent test environment and avoids code

Copy the test file contents below and read through the information to understand what is being done => 
**Create**
- Create one `User`
- Create one `Cat`
- Create two `Toy`s
- Create two `Feeding`s
- Create one `Photo`

**RELATE**
- Relate `User` -> `Cat`
- Relate one `Toy` to `Cat`
- Relate `Photo` to `Cat`

**RUN THE FILE WITH `python manage.py test`**

```python
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Cat, Feeding, Photo, Toy
from datetime import date

class ModelsTest(TestCase):
    def setUp(self):
        # user;
        self.user = User.objects.create_user(username='testuser', password='12345')
        # toys;
        self.toy1 = Toy.objects.create(name='Mouse',   color='Gray')
        self.toy2 = Toy.objects.create(name='Ball',    color='Red')
        self.toy3 = Toy.objects.create(name='Feather', color='white')
        # cat; each related to user
        self.cat1 = Cat.objects.create(name='Felix',   breed='Tabby', description='Playful cat',   age=3, user=self.user)
        self.cat2 = Cat.objects.create(name='Whiskers',breed='Tabby', description='A playful cat.',age=5, user=self.user)
        # feeding; two related to cat1
        self.feeding1 = Feeding.objects.create(date=date(2025, 1, 1), meal='B', cat=self.cat1)
        self.feeding2 = Feeding.objects.create(date=date(2024, 1, 1), meal='L', cat=self.cat1)
        self.feeding3 = Feeding.objects.create(date=date(2023, 1, 1), meal='D', cat=self.cat2)
        # photo; each related to one cat
        self.photo1 = Photo.objects.create(cat=self.cat1, url='http://url1.com', title='First')
        self.photo2 = Photo.objects.create(cat=self.cat2, url='http://url2.com', title='First')
        # relate toy1 and toy2 to cat
        self.cat1.toys.set([self.toy1, self.toy2])

    # TESTS
    # tests start with "test_"
    # example

    def test_user_create(self):
        self.assertEqual(str(self.user), 'testuser')

```

**Each test starts with this clean, controlled dataset.!!**

### Testing Creation with String Representations

**Testing `Toy` String Representation**

The `__str__` method in Django models defines the human-readable representation of an object. Testing it ensures models
display correctly in Django Admin and other interfaces.

```python
    # -------------------
    # String Representations / creation (using __str__ to ensure property return)
    # -------------------

    def test_user_create(self):
        self.assertEqual(str(self.user), 'testuser')
    
    def test_cat_create(self):
        self.assertEqual(str(self.cat1), 'Felix')
        self.assertEqual(str(self.cat2), 'Whiskers')

    def test_toy_create(self):
        self.assertEqual(str(self.toy1), 'Mouse')
        self.assertEqual(str(self.toy2), 'Ball')
        self.assertEqual(str(self.toy3), 'Feather')

    def test_feeding_create(self):
        self.assertEqual(str(self.feeding1), 'Breakfast on 2025-01-01')
        self.assertEqual(str(self.feeding2), 'Lunch on 2024-01-01')
        self.assertEqual(str(self.feeding3), 'Dinner on 2023-01-01')

    def test_photo_create(self):
        self.assertEqual(str(self.photo1), 'http://url1.com')
        self.assertEqual(str(self.photo2), 'http://url2.com')```

### Testing Model Relationships (15 minutes)

Relationships between models => One-To-One, One-to-Many, Many-to-Many => are integral to Django's ORM.

Read the code and discuss!

```python
    # -------------------
    # Relationships
    # -------------------
    
    def test_cat_toys_relationship(self):
        self.assertEqual(self.cat1.toys.count(), 2)
        self.assertIn(self.toy1, self.cat1.toys.all())
        self.assertIn(self.toy2, self.cat1.toys.all())

    def test_cat_user_relationship(self):
        self.assertEqual(self.cat1.user.username, 'testuser')

    def test_cat_feeding_relationship(self):
        self.assertEqual(self.feeding1.cat, self.cat1)
        self.assertEqual(self.feeding1.meal, 'B')
        self.assertEqual(self.feeding2.cat, self.cat1)
        self.assertEqual(self.feeding2.meal, 'L')
        self.assertEqual(self.feeding3.cat, self.cat2)
        self.assertEqual(self.feeding3.meal, 'D')

    def test_cat_photo_relationship(self):
        self.assertEqual(self.photo1.cat, self.cat1)
        self.assertEqual(self.photo2.cat, self.cat2)

```

### Testing Data Ordering

Django allows models to be ordered using the `Meta` class. Testing ensures data is retrieved in the correct sequence.

```python
    # -------------------
    # Model Methods / Ordering
    # -------------------
    
    def test_feeding_ordering(self):
        feedings = list(self.cat1.feeding_set.all())
        self.assertEqual(feedings[0].date, date(2025, 1, 1))
        self.assertEqual(feedings[1].date, date(2024, 1, 1))
```

### Testing Cascade Deletes

Cascade deletion ensures related objects are deleted automatically when their parent is removed.

```python
    # -------------------
    # Cascade Deletions
    # -------------------
    
    # 1 user, two related cats => 0 cats left after delete
    def test_deleting_user_cascades_to_cat(self):
        self.user.delete()
        self.assertEqual(Cat.objects.count(), 0)

    # cat2 had ONE feeding => should still be two in database related to cat1!
    def test_deleting_cat_cascades_to_feedings(self):
        self.cat2.delete()
        self.assertEqual(Feeding.objects.count(), 2)

    # cat1 had one photo out of two => 1 left over!
    def test_deleting_cat_cascades_to_photo(self):
        self.cat1.delete()
        self.assertEqual(Photo.objects.count(), 1)
```

## Summary

In this lesson, we explored the fundamentals of testing Django models:

- `setUp` Method: Establishing a consistent test environment
- String Representation Tests: Ensuring models display correctly
- Relationship Tests: Checking integrity of Many-to-Many and ForeignKey associations.
- Ordering Tests: Confirming data retrieval order.
- Cascade Delete Tests: Ensuring data integrity through proper cascading behavior.

Comprehensive model testing helps catch errors early, maintain data integrity, and ensure business rules are
consistently enforced. Regularly writing tests as part of development enhances code quality and reduces the likelihood
of bugs in production.
