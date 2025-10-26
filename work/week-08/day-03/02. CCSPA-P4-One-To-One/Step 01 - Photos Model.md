# ![Django CRUD App - Cat Collector](./assets/hero.png)

![Cat Wave](./assets/cat-wave.png)

**Learning objective:** By the end of this lesson, learners will be able to implement and manage a one-to-one relationship in Django by adding another model related to the Cat model. This one will give users a chance to upload an image (via url) to relate to the cat.

# Show Me That Smile!

The original lesson plan for photo upload utilized Amazon Web Services (AWS) S3 (Simple Storage Service) to allow users to upload a photo from their device, store it in AWS cloud services (S3), obtain the url to the image, and then store that image within our database. Due to restructions in government policy, which we will respect, we will take a slightly different approach and show another way to display some kitty images.

## I'm a model!

Once again, we will need to create a new model to hold our image information and to create a relationship between our Cats and their image.

SO - where do we go to add a new model!? 

`models.py`
```py
# cat model above
class Photo(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True)
    cat = models.OneToOneField(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat.id} @{self.url}"
```

## What do we do after we add or update a model?
1. `python3 manage.py makemigrations` => stage the model for being updated in the database.
2. `python3 manage.py migrate` => make the actual changes to the database.


## Use the Admin Portal / Register the Model
Before we start building the user interface (UI) for our new photos model, let's practice adding a few photos using the Django admin portal. This will give us some data to display and allow us to create our photos' index UI first.

To use the built-in Django admin portal for CRUD operations, we must first register the model. Update `main_app/admin.py` to include the `Photo` model:

```python
from django.contrib import admin
# Add Feeding to the import
from .models import Cat, Feeding, Toy, Photo

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)
# Register the new Photo model
admin.site.register(Photo)
```

Now, navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and click on the **Photo +Add** link.

Notice the select drop-downs for assigning both the Photo and the Cat!

## Serialize Photo Model

`serializers.py`
```python
from django import forms
from .models import Cat, Feeding, Toy, Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'
        
class CatSerializer(serializers.ModelSerializer):
    # this will allow us to include the photo in the cat without having to query for it! Neat!
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
```

## Create Photo view function
``
```python
class PhotoDetail(APIView):
  serializer_class = PhotoSerializer

class PhotoDetail(APIView):
	serializer_class = PhotoSerializer

	def post(self, request, cat_id):
		try:
			# Set Cat ID for Photo
			data = request.data.copy()
			data["cat"] = int(cat_id)

			#  Find Existing Photo and Delete if exists
			existing_photo = Photo.objects.filter(cat=cat_id)
			if existing_photo:
				existing_photo.delete()

			# Create Serializer Instance and Validate
			serializer = self.serializer_class(data=data)
			if serializer.is_valid():
				cat = get_object_or_404(Cat, id=cat_id)
				serializer.save()
				return Response(CatSerializer(cat).data, status=status.HTTP_200_OK)
			print(serializer.errors)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			print(str(err))
			return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Add the `add_photo` URL route..

`urls.py`
```python
# import new view function
PhotoDetail

urlpatterns = [
    path('cats/<int:cat_id>/add-photo/', PhotoDetail.as_view(), name='add-photo'),
]
```

## Create PhotoAPI Request Folder / File
We only have **one** endpoint to use in relation to the photo api. The photo is also only related to the `Cat` model. We can use the `cat-api` for the one photo route and it will be perfectly fine!...

`cat-api.js`
```js
export function addPhoto(catId, formData) {
    return sendRequest(`${url}${catId}/add-photo/`, "POST", formData)
}
```

`CatDetailPage.jsx`
```jsx
<section className="detail-cat-container">
    // add this to top of the cat-container, other items below
    <div className="detail-cat-img">
        { catDetail.photo?.url
            ? <img src={catDetail.photo.url} alt={`A photo of ${catDetail.name}`} className="usr-img" />
            : <img src={skaterCat} alt="A skater boy cat" />
        }
    </div>

</section>
```

**Check out the beautiful work.**
Do you see your kitty photo? (If you added a photo to a Kitty earlier.. if not, dont sweat!)

### Adding the Photo Form (new component!)

`AddPhotoForm.jsx`
```js
import { useState } from "react";

export default function AddPhotoForm({ cat, addPhoto }) {
    const initialState = { url: "", title: "" }
    const [formData, setformData] = useState(initialState)

    function handleChange(evt) {
        setFormData({ ...formData, [evt.target.name]: evt.target.value })
    }
    function handleSubmit(evt) {
        evt.preventDefault();
        addPhoto(cat.id, formData);
        setFormData(initialState);
    }

   return (<>
        <h3>Change { cat.name }'s photo</h3>
        <form onSubmit={handleSubmit} autocomplete="off">   
            <p>
              <label htmlFor="id_url">Url:</label>
              <input value={formData.url} type="text" name="url" required    id="id_url" onChange={handleChange}/>
            </p>
            <p>
              <label htmlFor="id_title">Title:</label>
              <input value={formData.title} type="text" name="title" maxLength="250" required    id="id_title" onChange={handleChange}/>
            </p>
            <button type="submit" class="btn submit">Add Photo</button>
        </form>
    </>)
}
```

### Add the Photo Form to CatDetailPage and Pass Props

`CatDetailPage.jsx`
```jsx
// new component import
import AddPhotoForm from "../../components/Forms/AddPhotoForm";

    async function addPhoto(catId, formData) {
        try {
          const updatedCat = await catAPI.addPhoto(catId, formData);
          setCatDetail(updatedCat);
        } catch (err) {
          console.log(err);
          setCatDetail({...catDetail})
        }
    }

    <div className="cat-details">
      <h1>{catDetail.name}</h1>
      <h2>{catDetail.age > 0 
            ? `A ${catDetail.age} year old ${catDetail.breed}` 
            : `A ${catDetail.breed} kitten.`}
      </h2>
      <p>{catDetail.description}</p>
      <div className="cat-actions">
        <Link to={`/cats/edit/${catDetail.id}`} className="btn warn">Edit</Link>
        <Link to={`/cats/confirm_delete/${catDetail.id}`} className="btn danger">Delete</Link>
      </div>
    </div>
    <section>
      <AddPhotoForm cat={catDetail} addPhoto={addPhoto} />
    </section>

    // ^^^ updated `cat-details` div above with a new <AddPhotoForm /> component and section ^^^
```

### Display Photos on Cat Index Page

We might also want to have our Cat - Photos showing up on our Cat Index Page. 

Currently the images are being displayed in a sub-component => `CatIndexCard`..

We will use [optional chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

`CatIndexCard.jsx`
```jsx
    // updated return statement to display the photo if the `photo` has a `url` property.. 
    // this is called optional chaining! Go look it up!
    return (
        <div className="cat-index-card">
            <Link to={`/cats/${cat.id}`}>
                <div className="cat-index-card-content">
                    {cat.photo?.url
                        ? <img src={cat.photo.url} alt={`A photo of ${cat.name}`} className="usr-img" />
                        : <img src={skaterCat} alt="A skater boy cat" />
                    }
                    <h2>{cat.name}</h2>
                    <p>{cat.age > 0 ? `A ${cat.age} year old ${cat.breed}` : `A ${cat.breed} kitten.`}</p>
                    <p><small>{cat.description}</small></p>
                </div>
            </Link>
        </div>
    )

```

**Excellent! You should be able to add a new photo or replace an existing one!**


