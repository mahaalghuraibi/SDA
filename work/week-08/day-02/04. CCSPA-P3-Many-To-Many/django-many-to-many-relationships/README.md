<!-- {% raw %} -->
# ![Django CRUD App - Cat Collector - Django Many-to-Many Relationships](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to create and manage a many-to-many relationship between Cats and Toys using Django's built-in features.

## Many-to-Many Relationships in Relational Databases

In relational databases like those used by Django, creating many-to-many relationships between two entities requires an intermediary or join table.

A join table acts as a bridge connecting two other tables by storing foreign keys that reference the primary keys of these tables. Each row in a join table represents a link between one entry in each of the connected tables.

For instance, if a `Cat` can play with many `Toys`, and each `Toy` can be used by many `Cats`, the join table will store pairs of foreign keys pointing to the respective entries in the `Cats` and `Toys` tables.

![Join Table](./assets/relational-db.png)

### Associating `Cats` with `Toys`

Now that we will set up full CRUD capabilities for the `Toy` model, our next step is to define a many-to-many relationship between `Cats` and `Toys`. This allows multiple cats to interact with multiple toys interchangeably.

When you associate a `Cat` with a `Toy`, you add a row to the join table containing the foreign keys of the cat and toy involved. In reverse, dissociating a `Cat` from a `Toy` simply involves removing the corresponding row from the join table, without deleting any records from the `Cat` or `Toy` tables themselves.

## Many-to-Many Relationship in Django

As usual, the Django framework handles a lot of the heavy lifting when it comes to working with many-to-many relationships between Models.

Forms and templates aside, all we need to do to implement a many-to-many relationship using Django is:

1. Add a `ManyToManyField` on **one** of the Models
2. Create the migration and migrate it to update the database

Django will ensure that a "hidden" join table is created that links the rows of the other two tables together.

Given that our application's focus is on `Cats`, we are more likely interested in a cat’s toys, than a toy’s cats, so we’ll add the new attribute to the `Cat` model and name it "toys":

```python
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Add the M:M relationship
    toys = models.ManyToManyField(Toy)
```

**Because we’ve made a change to a Model:**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Update Cat Serializer

As we add relationships to our models, our serializers are automatically going to be looking to validate and expect for these new fields to show up in our forms. When we create a new cat, however, we do not want to be in a position where we are expected to include toys with the new cat. Just like our feedings and eventually our users. So, we will include a field on the model.Serializer to essentially tell the serializer that we acknowledge the field is there and that it can safely validate a new Cat if it does not include a `toy_id`.

`serializers.py`
```python
class CatSerializer(serializers.ModelSerializer):
    # the read only property will allow us to overlook validating the new relationship / field.
    toys = ToySerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
```

### Modify the `CatDetailPage` to display `toys` and update the useEffect get/set function.

Now, let's update the `cats/detail.html` template to display each toy with a **"Give Toy"** button that will eventually link the toy to the cat. Again, at the moment, we are just setting ourselves up to display all of the toys, not create relationships to the cat.

```jsx
// IMPORTS
import { closest } from 'color-2-name';

// IMAGES
import string from "../../assets/images/string.svg"
import mouse from "../../assets/images/mouse.svg"
import fish from "../../assets/images/fish.svg"

// APIs
import * as toyAPI from "../../utilities/toy-api";

// ADD new allToys state
const [allToys, setAllToys] = useState([])

// update useEffect.getAndSetDetail function:
  useEffect(() => {
    async function getAndSetDetail() {
      const cat = await catAPI.show(id);
      const feedings = await feedingsAPI.catFeedings(id);
      const toys = await toysAPI.index();
      setCatDetail(cat);
      setCatFeedings(feedings);
      setAllToys(toys);
    }
    if (id) getAndSetDetail()
  }, [id])

// ADD THIS FUNCTION =>
async function handleAddToy(toyId) {
// :: coming soon ::
}

async function handleRemoveToy(toyId) {
// :: coming soon ::
}

// <div> FEEDINGS TOYS CONTAINER 
<section class="feedings">

</section>

// ADD THIS NEW TOY SECTION BELOW THE EXISTING FEEDINGS CONTAINER, INSIDE "feedings-toys-container"
<section class="toys">
  <div class="subsection-title">
    <h2>Toys</h2>
    <img src={string} alt="A ball of string" />
    <img src={mouse} alt="A mouse" />
    <img src={fish} alt="A fishy toy" />
  </div>
  <h3>Available Toys</h3>
  <div className="subsection-content">
    {allToys.map(toy => (
    <div key={toy.id} className="toy-container">
      <div className="toy-info">
        <div className="color-block" style={{ backgroundColor: toy.color }}></div>
        <Link to={`/toys/${toy.id}`}>
          <p>A { closest(toy.color).name } { toy.name }</p>
        </Link>
      </div>
    </div>
    ))}
  </div>
</section>
// end of "feedings-toys-container"
// </div>
```

In the code above:
- we access our toy-api.js for toy related requests
- create a new state to hold all of our toys
- each toy is being rendered with its `color` and `name` properties listed.
- each toy is also contains a simple form with a "Give Toy" button, which allows users to associate or "give" a toy to a cat.
- The form handleAssociateToy function will ultimately handle creating the relationship of the toy to the cat and receiving all updated info / state for toys.

**Take a moment to add toys if you don't see any listed! We will need them!**

![All Available Toys on Details Page](./assets/cat-toys-available.png)


## Associating `Cats` and `Toys`

Next, we will implement the functionality to link toys to cats using the many-to-many relationship we created earlier. This involves setting up a new view function that handles the association process when a user clicks the "Give Toy" button next to a toy in the cat's detail page.

## WORKING BACKWARDS! 

### Create the View Function =>
We will go ahead and setup our view function to provide us with our two different toy states we need related to the specific `Cat`. One that represents the toys a cat has and another that represents the toys the cat does not have...

**Excluding Non-Cat Toys**
- The first half of this expression `Toy.objects.exclude(id__in = ` retrieves all Toy objects that do not have an `id` that is in the list of associated toy `ids`. The `exclude()` method is the opposite of `filter()`, which means it will get all toys except those whose `ids` are listed in the previous query. The `id__in` is a field lookup that checks if the `id` field of the `Toy` model is within the provided list.

- The second half of this expression `cat.toys.all().values_list('id')` retrieves a list of `ids` for all the toys associated with a specific cat. This is done by first accessing all toy instances linked to the cat through the many-to-many relationship `(cat.toys.all())`, and then narrowing the data down to just the `ids` of these toys using `values_list('id')`.

```python
class AddToyToCat(APIView):

  def post(self, request, cat_id, toy_id):
    try:
      cat = get_object_or_404(Cat, id=cat_id)
      toy = get_object_or_404(Toy, id=toy_id)
      cat.toys.add(toy)
      toys_cat_does_have = Toy.objects.filter(cat=cat_id)
      toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
      return Response({
        "toysCatHas": ToySerializer(toys_cat_does_have, many=True).data,
        "toysCatDoesntHave": ToySerializer(toys_cat_doesnt_have, many=True).data
        }, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

### Define the URL pattern
Remember => the urls have to match to be successful!...

`urls.py`
```python
# new import
AddToyToCat

# New URL to associate a toy with a cat
path('cats/<int:cat_id>/associate-toy/<int:toy_id>/', AddToyToCat.as_view(), name='associate-toy'),
```

### Add Request URL in Cat-API.js
We need to add a requst from one of our API files to create the association between a cat and a toy.

This will require id's for both the cat and the toy. And we will place it in the cat-api since our main model is our `Cat` model.

`cat-api.js`
```js
export function addToyToCat(catId, toyId) {
    return sendRequest(`${url}${catId}/associate-toy/${toyId}/`, "POST")
}
```


### Add the FORM and Create DisplayCatToys Component

Next, we will need to accomplish multiple tasks:
- Add state to represent our `ToysCatHas` and `ToysCatDoesntHave` so that we can display them separately.
- Add the form to the toys mapping function so we can add and remove toys 
- Move the UI for mapping `Toys` into a reuseable component and setup for both uses.
  - we do this to clean up the UI / save space and to reuse the component
- Update `catAPI.show(catId)` request...

We will also want to change the way we are fetching our data. Currently we have three individual API requests to get three separate pieces of information for the same page => This is ineficient.. If we are already making one request to the server, why not update the one request to make three individual database requests and sending all of the data together. We will update the initial `catAPI.show(catId)` to do this...

### Update our `CatDetailsPage` =>

`CatDetailsPage.jsx`
```jsx
// delete imports:
import * as feedingsAPI from "../../utilities/feeding-api";
import * as toyAPI from "../../utilities/toy-api";

// new State:
const [toysCatHas, setToysCatHas] = useState([]);
const [toysCatDoesntHave, setToysCatDoesntHave] = useState([]);

// delete:
const [allToys, setAllToys] = useState([]);

  useEffect(
    // delete:
    const cat = await catAPI.show(id);
    const feedings = await feedingsAPI.catFeedings(id);
    const toys = await toysAPI.index();
    setCatDetail(cat);
    setCatFeedings(feedings);
    setAllToys(toys);
    // create:
    const catDetailData = await catAPI.show(id);
    setCatDetail(catDetailData.cat);
    setCatFeedings(catDetailData.feedings);
    setToysCatHas(catDetailData.toysCatHas);
    setToysCatDoesntHave(catDetailData.toysCatDoesntHave);
    // ...
  )

  // update function to 
  async function handleAddToy(evt, toyId) {
    try {
      evt.preventDefault()
      const toyData = await catAPI.addToyToCat(catDetail.id, toyId);
      setToysCatHas(toyData.toysCatHas);
      setToysCatDoesNotHave(toyData.toysCatDoesntHave);
    } catch (err) {
      console.log(err);
      setToysCatHas([...toysCatHas]);
      setToysCatDoesNotHave([...toysCatDoesntHave]);
    }
  }

  // add the TOY FORM / move the entire code block to another component => 
  // DisplayCatToys.jsx
  {toysCatHas.map(toy => (
  <div key={toy.id} className="toy-container">
    <div className="toy-info">
      <div className="color-block" style={{ backgroundColor: toy.color }}></div>
      <Link to={`/toys/${toy.id}`}>
        <p>A { closest(toy.color).name } { toy.name }</p>
      </Link>
    </div>

    <form onSubmit={handleAddToy}>
      <button type="submit" className="btn submit">Give Toy</button>
    </form>

  </div>
  ))}
```

### DisplayCatToys Component

We are going to end up writing essentially the exact same setup for displaying toys and the ability to add / remove them. We just need to pass tso different functions to the form, which we can pass down as a prop! SO, we are going to set ourselves up to reuse a component!...

- Create: `/components/DisplayCatToys/index.jsx` or `/components/DisplayCatToys/DisplayCatToys.jsx`

`DisplayCatToys`
```jsx
import { Link } from "react-router"
import { closest } from "color-2-name"

export default function DisplayCatToys({ toy, submitFunction, formAction }) {
    return (
        <div className="toy-container">
          <div className="toy-info">
            <Link to={`/toys/${toy.id}`}>
                <p>A { closest(toy.color).name } { toy.name }</p>
            </Link>
            <div className="color-block" style={{ backgroundColor: toy.color }}></div>
          </div>
          <form onSubmit={(evt) => submitFunction(evt, toy.id)}>
            <button type="submit" className="btn submit">{formAction}</button>
          </form>
        </div>
    )
}
```

- Update `CatDetailPage` to use the new component! Let's talk about what information (props) to send it and why?!

`CatDetailPage`
```jsx
import DisplayCatToys from "../../components/DisplayCatToys/DisplayCatToys";

const catToys = toysCatHas.map(toy => (
  <DisplayCatToys key={toy.id} toy={toy} submitFunction={handleAddToy} formAction="Give Toy" />
))

// ... conditional display if cat does / does not have toys
  { toysCatHas.length > 0 
    ? catToys
    : <p className="no-toys">{catDetail.name} doesn't have any toys!</p>
  }

```

#### UPDATE / REFACTOR `CatDetail(APIView)` - `GET` request to query for all of the data and return...

```python
class CatDetail(APIView):
  serializer_class = CatSerializer
  lookup_field = 'id'

  def get(self, request, cat_id):
    try:
      cat = get_object_or_404(Cat, id=cat_id)
      feedings = Feeding.objects.filter(cat=cat_id)
      toysCatHas = Toy.objects.filter(cat=cat_id)
      toysCatDoesntHave = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))
      return Response({
          "cat": CatSerializer(cat).data,
          "feedings": FeedingSerializer(feedings, many=True).data,
          "toysCatHas": ToySerializer(toysCatHas, many=True).data,
          "toysCatDoesntHave": ToySerializer(toysCatDoesntHave, many=True).data
      }, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Conditional Display of `ToysCatHas`... 

Now that we have verified we are able to make associations between cats and toys, we should display them back to the user.

```jsx
  // above return statement
  const catToys = toysCatHas.map(toy => (
    <DisplayCatToys key={toy.id} toy={toy} submitFunction={handleAddToy} formAction="Give Toy" />
  ))

  // main content:
  <h3>{ catDetail.name }'s Toys</h3>
  <div className="subsection-content">
    { toysCatHas.length > 0 
      ? { catToys }
      : <p className="no-toys">{catDetail.name} doesn't have any toys!</p>
    }
  </div>
  <h3>Available Toys</h3>
  <div className="subsection-content">
    <!-- Available toys will go here here -->
  </div>
</section>
```

## REMOVING TOYS
As an improvement to the user experience, you might consider removing toys from the available list once they have been given to a cat. To do this we will only have to make a few adjustment because we set ourselves up early on to be able to handle both adding and removing...

TODO =>
- a new `view.py` function to remove a toy and return the appropriate information
- a new `urls.py` endpoint
- a new `cat-api.js` function for the request
- a new mapping of `setToysCatDoesntHave`

## TRY IT!
## 🎓 You Do: Remove a `Toy` from a `Cat`

![All Available Toys](./assets/cat-toys-all.png)


Implement the following user story:

_As a User, when viewing the detail page for a cat, I want to be able to remove a toy from that cat_

This process will be nearly identical to what we did when adding an association, but with the opposite action.

1. Create the view function. _Hint: Check out Django's **[.remove()](https://docs.djangoproject.com/en/5.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.remove)** method._

```python
class RemoveToyFromCat(APIView):

  def post(self, request, cat_id, toy_id):
    try:
      cat = get_object_or_404(Cat, id=cat_id)
      toy = get_object_or_404(Toy, id=toy_id)
      cat.toys.remove(toy)
      toys_cat_does_have = Toy.objects.filter(cat=cat_id)
      toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
      return Response({
        "toysCatHas": ToySerializer(toys_cat_does_have, many=True).data,
        "toysCatDoesntHave": ToySerializer(toys_cat_doesnt_have, many=True).data
        }, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

2. Define the URL.

```python
# new import:
RemoveToyFromCat

path('cats/<int:cat_id>/remove-toy/<int:toy_id>/', RemoveToyFromCat.as_view(), name='remove-toy'),
```

3. Add the request in `cat-api.js`

`cat-api.js`
```js
export function removeToy(catId, toyId) {
    return sendRequest(`${url}${catId}/remove-toy/${toyId}/`, "POST")
}
```


4. Update the `CatDetailPage` functions, components, etc..

`CatDetailPage.jsx`
```jsx
import DisplayCatToys from "../../components/DisplayCatToys/DisplayCatToys";

  // update function to 
  async function handleRemoveToy(evt, toyId) {
    try {
      evt.preventDefault()
      const toyData = await catAPI.removeToyFromCat(catDetail.id, toyId);
      setToysCatHas(toyData.toysCatHas);
      setToysCatDoesNotHave(toyData.toysCatDoesntHave);
    } catch (err) {
      console.log(err);
      setToysCatHas([...toysCatHas]);
      setToysCatDoesNotHave([...toysCatDoesntHave]);
    }
  }

const noCatToys = toysCatHas.map(toy => (
  <DisplayCatToys key={toy.id} toy={toy} submitFunction={handleRemoveToy} formAction="Take Toy" />
))


  { noCatToys.length > 0 
    ? { noCatToys }
    : <p class="all-toys">{{cat.name}} already has all the available toys 🥳</p>
  }
```


<!-- {% endraw %} -->