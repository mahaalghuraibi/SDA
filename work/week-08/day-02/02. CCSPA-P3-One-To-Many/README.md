<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 3 - A cat’s got to eat! (One:Many Models)

In this lesson, we'll explore how to add another model in Django to demonstrate working with **one-to-many** relationships.

We'll use an Entity-Relationship Diagram (ERD) to illustrate this relationship:

![ERD](./assets/one-to-many-erd.png)

## Adding a new `Feeding` Model

Using the ERD above as a guide, let’s add a new `Feeding` Model (below the current `Cat` Model) in our `models.py`.

```python
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=self.meals[0][0])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    # this function will still work in DRF if needed
    # we can intentionally setup the serializer to add to our model
    # or we can take a new approach!
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date'] 
```

## Make and Run the Migrations

We changed our `models.py` file, so it’s that time again! Open your terminal and run:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Use the Admin Portal to create some new feedings

```python
from django.contrib import admin
from .models import Cat, Feeding

admin.site.register(Cat)
admin.site.register(Feeding)
```

## Feeding Serializer

We now have a new model and intend to be able to access the information in the same way that did a Cat. This means we will also need a serializer for the `Feeding` so we can send the information to the frontend.

In our `main_app` folder we will create a new file called `serializers.py` and add the following code:

`serializers.py`
```python
from rest_framework import serializers
from .models import Cat, Feeding

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

# new serializer below
class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
```

### New Feedings URL =>
Add your new url for matching...

`urls.py`
```python
from .views import FeedingsIndex

# urlpatterns =>
  path('cats/<int:cat_id>/feedings/', FeedingsIndex.as_view(), name='feeding-create'),
```

### New Feedings View Function =>
A standard API view that will retrieve / `GET` feedings related to the specific Cat whose `cat_id` we passed in as a route parameter.

```python
class FeedingsIndex(APIView):
  serializer_class = FeedingSerializer

  def get(self, request, cat_id):
    try:
      queryset = Feeding.objects.filter(cat=cat_id)
      return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

### Create Your New API =>
Add your new utility file and setup to access to the sendRequest file so we can make requests.

At the moment we are only accessing toys that have been created in the admin portal. So we only need to be able to GET feedings related to a specific cat. As expected for restful routing we will send the request to `/cats/cat_id/feedings` so we can retrieve and create all feedings related to a specific cat (one to many relationship).

`feedings-api.js`
```js
import sendRequest from "./sendRequest";

export function catFeedings(catId) {
    return sendRequest(`/cats/${catId}/feedings/`)
}
```

## Displaying a Cat’s Feedings

The cat's detail page is the perfect place to display a cat's feedings because it provides a comprehensive view of all the important information about that specific cat in one place. This is similar to how you would see a list of all tasks on a project detail page. By showing feedings on the cat's detail page, users can easily see the feeding history along with other details about the cat, making the information more accessible and organized.

### Update the `CatDetailPage`

We want to be able to display all feedings related to a specific cat. This means adding the ability to make the request from the Cat Detail Page in the same useEffect that is allowing us to get our Cat's Detail information. A second request will also warrant another set of state for the Cat's Feedings. 

![Feedings UI](./assets/feedings-ui.png)

```jsx
import catCone from "../../assets/images/cat-cone.svg";
import catOniGirl from "../../assets/images/cat-onigiri.svg";
import kittyKabob from "../../assets/images/kitty-kabob.svg";

// APIs
import * as feedingsAPI from "../../utilities/feeding-api";

// CONSTANTTS
const MEALS = {
  'B': 'Breakfast',
  'L': 'Lunch',
  'D': 'Dinner',
}


// update useEffect to set the feedings
    const [catFeedings, setCatFeedings] = useState([]);

    useEffect(() => { 
        async function getAndSetDetail() {
            // ...
            // add lines below!
            const feedings = await feedingsAPI.catFeedings(id);
            setCatFeedings(feedings);
            // ...
        }
        getAndSetDetail()
    }, [id])

// <!-- Existing cat-container above -->
<div class="feedings-toy-container">
  <section class="feedings">
    <div class="subsection-title">
      <h2>Feedings</h2>
      <img src={catCone}    alt="An ice cream cone cat" />
      <img src={catOniGirl} alt="A cat as onigiri" />
      <img src={kittyKabob} alt="A kabob of kittens" />
    </div>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Meal</th>
        </tr>
      </thead>
      <tbody>
        {catFeedings.map((meal, ind) => (
            <tr key={ind}>
                <td>{meal.date}</td>
                <td>{MEALS[meal.meal]}</td>
            </tr>
        ))}
      </tbody>
    </table>
  </section>
</div>
```


## Adding new feedings from the Detail page via `Feeding Form`

Next, we will add functionality for users to add feedings directly from a cat's detail page. This requires integrating a form on the page that can handle the creation of new feedings linked to that specific cat.

Just like our previous CatCollector MPA we are going to add a form for Feeding to the `Cat Detail Page`. Do we remember **why** we place the feeding on the `Cat Detail Page`? 

In a one-to-many relationship there for sure is going to be one model that holds the foreign key of the other model and those items will only belong to one specific item. 

Therefore it makes sense to place the form on the Cat Detail page, as that is the feeding that belongs to that specific cat. So let's do it!

Quick note! => Because this form is going to be on a page that already exists, we will create a new component folder and file to hold the information and then import it into our Cat Detail Page. While we could place the form directly on the page, and most likely will not reuse it, it will help to break down some of the code into other files so that the detail page isn't have heavy / difficult to read.

`/components/Forms/FeedingForm.jsx`
```jsx
import { useState } from "react";
import * as feedingAPI from "../../utilities/feeding-api"

export default function FeedingForm({ catDetail, catFeedings, setCatFeedings }) {
    const today = new Date().toISOString().slice(0, 10);
    const initialState = { date: today, meal: "B", cat: catDetail.id}
    const [formData, setFormData] = useState(initialState)

    function handleChange(evt) {
        const updatedData = { ...formData, [evt.target.name]: evt.target.value }
        setFormData(updatedData)
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const updatedFeedings = await feedingAPI.create(formData, catDetail.id);
            setCatFeedings(updatedFeedings)
            setFormData(initialState);
        } catch (err) {
            console.log(err);
            setCatFeedings([...catFeedings])
        }
    }

    return (
        <form className="form-container" onSubmit={handleSubmit}>
            <p>
                <label htmlFor="id_date">Feeding date:</label>
                <input value={formData.date} type="date" name="date" placeholder="Select a date" onChange={handleChange} />
            </p>
            <p>
                <label htmlFor="id_meal">Meal:</label>
                <select value={formData.meal} name="meal" id="id_meal" onChange={handleChange} >
                    <option value="B">Breakfast</option>
                    <option value="L">Lunch</option>
                    <option value="D">Dinner</option>
                </select>
            </p>
            <button type="submit" className="btn submit">Add Feeding</button>
        </form>
    )
}
```

## Add the Feeding Form to CatDetailPage

`CatDetailPage`
```jsx

import FeedingForm from "../../components/Forms/FeedingForm";

<div className="feedings-toy-container">
    <section className="feedings">
      <div className="subsection-title">
        <h2>Feedings</h2>
        <img src={catCone}    alt="An ice cream cone cat" />
        <img src={catOniGirl} alt="A cat as onigiri" />
        <img src={kittyKabob} alt="A kabob of kittens" />
      </div>
      <h3>Add a Feeding</h3>
      <FeedingForm catDetail={catDetail} catFeedings={catFeedings} setCatFeedings={setCatFeedings} />
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Meal</th>
          </tr>
        </thead>
        <tbody>
          {catFeedings.map((meal, ind) => (
              <tr key={ind}>
                  <td>{meal.date}</td>
                  <td>{MEALS[meal.meal]}</td>
              </tr>
          ))}
        </tbody>
      </table>
    </section>
  </div>
```

## Create new `feeding-api` request

Its time to complete our form functionality by setting up the route we'll use as the form action for a new `Feedings`.

`feeding-api.js`
```js
export function create(formData, catId) {
    return sendRequest(`/cats/${catId}/feedings/`, "POST", formData)
}
```

## Add the View function

This view is designed to handle the submission of a feeding form associated with a specific cat.

Let’s create an `add_feeding` view function in `main_app/views.py` :

```python
class FeedingsIndex(APIView):
  serializer_class = FeedingSerializer

  def get(self, request, cat_id):
    try:
      queryset = Feeding.objects.filter(cat=cat_id)
      return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def post(self, request, cat_id):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      queryset = Feeding.objects.filter(cat=cat_id)
      feedings = FeedingSerializer(queryset, many=True)
      return Response(feedings.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

### What if there are no feedings yet?

We can also add some conditional logic in our markup that tells the user whether or not a cat has been fed.

Replace the existing feedings table with the following:

```jsx
<h3>Past Feedings</h3>
{ catFeedings.length > 0 
  ?
  <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Meal</th>
      </tr>
    </thead>
    <tbody>
      {catFeedings.map((meal, ind) => (
        <tr key={ind}>
          <td>{meal.date}</td>
          <td>{MEALS[meal.meal]}</td>
        </tr>
      ))}
    </tbody>
  </table>
  :
  <div className="subsection-content">
    <p>⚠️ {catDetail.name} has not been fed!</p>
  </div>
}
```

Now if a cat has a feeding count of `0` in the database, you'll see a warning message.

Feed your cats!

## Check the feeding status

When a cat has not been fully fed for the day, we'll show:

![Cat Not Fed](./assets/cat-not-fed.png)

When the cat has received all its meals for the day:

![Cat Fed](./assets/cat-fed.png)

To display the feeding status:

```jsx
const today = new Date().toISOString().slice(0, 10);
const todaysFeedingCount = catDetail.feedings.filter(feeding => new Date(feeding.date).toISOString().slice(0, 10) === today)

return (
    <form onSubmit={handleSubmit}>
            { todaysFeedingCount.length >= 3
                ? <p className="fed">{catDetail.name} has been fed all their meals for today!</p>  
                : <p className="unfed">{catDetail.name} might be hungry!</p>
            }
        <p>
            <label htmlFor="id_date">Feeding date:</label>
            <input value={formData.date} type="date" name="date" placeholder="Select a date" onChange={handleChange} />
        </p>
        <p>
            <label htmlFor="id_meal">Meal:</label>
            <select value={formData.meal} name="meal" id="id_meal" onChange={handleChange} >
                <option value="B">Breakfast</option>
                <option value="L">Lunch</option>
                <option value="D">Dinner</option>
            </select>
        </p>
        <button type="submit" className="btn submit">Add Feeding</button>
    </form>
)
```
