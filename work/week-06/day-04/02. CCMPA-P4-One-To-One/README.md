# ![Django CRUD App - Cat Collector](./assets/hero.png)

![Cat Wave](./assets/cat-wave.png)

**Learning objective:** By the end of this lesson, learners will be able to implement and manage a one-to-one relationship in Django by adding another model related to the Cat model. This one will give users a chance to upload an image (via url) to relate to the cat.

# Show Me That Smile!

The original lesson plan for photo upload utilized Amazon Web Services (AWS) S3 (Simple Storage Service) to allow users to upload a photo from their device, store it in AWS cloud services (S3), obtain the url to the image, and then store that image within our database. Due to restructions in government policy, which we will respect, we will take a slightly different approach and show another way to display some kitty images.

## I'm a model!

Once again, we will need to create a new model to hold our image information and to create a relationship between our Cats and their image.

SO - where do we go to add a new model!? - `models.py`


```py
class Photo(models.Model):
    url = models.CharField(max_length=250)
    # this will add a property with the date when created
    created_at = models.DateField(auto_now_add=True) 
    # below will add an update property that will update the date each time the object is updated.
    updated_at = models.DateField(auto_now=True)
    # like the feeding model - we will delete any related images if a Cat is deleted
    cat = models.OneToOne(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat.id} @{self.url}"
```

### Let's discuss:

Just to show more built-in functionality included with Django - let's say we want to be able to access information about when an object is created or last updated. We can add two fields to maintain this information for us. 

- [Django models.DateField Docs](https://docs.djangoproject.com/en/5.1/ref/models/fields/#datefield)

All we need is this two lines of code in the model! Cool!

## What do we do after we add or update a model?

1. `python3 manage.py makemigrations` => stage the model for being updated in the database.
2. `python3 manage.py migrate` => make the actual changes to the database.

## Use the Admin Portal to add a photo / test

Before we start building the user interface (UI) for our new photos model, let's practice adding a few photos using the Django admin portal. This will give us some data to display and allow us to create our photos' index UI first.

### Registering the Model

To use the built-in Django admin portal for CRUD operations, we must first register the model. Update `main_app/admin.py` to include the `Photo` model:

```python
from django.contrib import admin
# Add Feeding to the import
from .models import Cat, Feeding, Photo

admin.site.register(Cat)
# Register the new Feeding model
admin.site.register(Feeding)
admin.site.register(Photo)
```

Now, navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and click on the **Photo +Add** link.

Notice the select drop-downs for assigning both the Photo and the Cat!

## Where to next?

We need to accomplish several items (as usual) to get our photo upload to work.

- We need to decide where the photo upload will occur?
    - Requires a form to accept a title and url link.
- We need to create a route in `urls.py` to accept the information, create our new entry in our new table.
    - requires a url, and a view function
- We need to be able to display the new information.
    - requires an area to display the information.

**Which one should happen first? Does it matter?**

Since we've added a photo to one cat - let's make sure we can display the photo if it exists and display the form if not!

We will do this out the detail page of a cat since each photo will be a one to one for that specific cat, which is how we have access to that cat's id...

Inside of the `cat-container` section we will add some code to conditionally render the photo if it exists and our default photo if it does not...

```py
<section class="cat-container">
  <div class="cat-img">
    {% if cat.photo.url %}
    <img src="{{cat.photo.url}}" alt="A photo of {{cat.name}}" class="usr-img" />
    {% else %}
    <img src="{% static 'images/sk8r-boi-cat.svg' %}" alt="A skater boy cat" />
    {% endif %}
  </div>
</section>
```

**Check out the beautiful work.**
Do you see your kitty photo?

### Creating and Adding the Photo Form:
Just like the Cat `Feeding Form`, we will use Django's `ModelForm` to generate the `Photo Form` for us. The `ModelForm` will once again embed feeding-related inputs within a custom `<form>` tag, manage form validation, and save new photo entries to the database.

## Create the `ModelForm` for the `Photo` Model

We could define the `ModelForm` inside of the `models.py` module, but we’re going to follow a best practice of defining it inside of a `forms.py` module instead. Run the following in the terminal:

Let’s open it and update / add this code:

```python
from django import forms
from .models import Feeding, Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['url', 'title']
```

## Passing an instance of `PhotoForm`

`PhotoForm` is a class that needs to be instantiated in the `cat_detail` view function so that it can be rendered inside of `detail.html`.

Here’s the updated `cat_detail` view function in `main_app/views.py`:

```python
from .models import Cat
# Import the FeedingForm
from .forms import FeedingForm, PhotoForm

# Other view functions above

# update this view function
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    photo_form = PhotoForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'photo_form': photo_form,
        'toys': toys_cat_doesnt_have
    })
```

`photo_form` is set to an instance of `PhotoForm` and then it’s passed to `detail.html` just like `cat` and the `FeedingForm`!

#### Adding the photo form:

Next, let's add the photo form right under the other cat related action items of update and delete.

```html
    <div class="cat-actions">
      <a href="{% url 'cat-update' cat.id %}" class="btn warn">Edit</a>
      <a href="{% url 'cat-delete' cat.id %}" class="btn danger">Delete</a>
    </div>
    <!-- new photo form below -->
    <h3>Change {{ cat.name }}'s photo</h3>
    <form action="{% url 'add-photo' cat.id %}" method="POST" class="subsection-content" autocomplete="off">
        {% csrf_token %} 
        {{ photo_form.as_p }}
      <button type="submit" class="btn submit">Add Photo</button>
    </form>
    <!-- new photo form above -->
  </div>
</section>
```

Beautiful! Now...
  
# Add the `add_photo` URL route..

In **`urls.py`**:

```python
urlpatterns = [
    # Other paths above
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    # new path below
    path('cats/<int:cat_id>/add-photo/', views.add_photo, name='add-photo'),
]
```

Pretty much like the `add-feeding` route!

Notice once again, we’re going to capture the cat’s `id` using a URL parameter named `cat_id`.

The server currently shows an error because we’ve referenced an `add_photo` _view function_ that doesn’t exist. Let’s take care of that next…

# Code the `add_photo` View Function

We need to:
- Import the Photo Form
- Write the view function to create the relationship...

```py
def add_photo(request, cat_id):
    form = PhotoForm(request.POST)
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_photo = form.save(commit=False)
        new_photo.cat_id = cat_id
        # Remove old photo if it exists
        cat_photo = Photo.objects.filter(cat_id=cat_id)
        if cat_photo.first():
            cat_photo.first().delete()
        new_photo.save()
    return redirect('cat-detail', cat_id=cat_id)
```

Excellent! You should be able to add a new photo or replace an existing one!


