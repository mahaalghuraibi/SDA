# ![Django CRUD App - Cat Collector - Adding a Third Model](./assets/hero.png)

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 3 - Adding a Third Model (Many:Many Models)

**Learning objective:** By the end of this lesson, learners will be able to implement a many-to-many model in Django, and perform full CRUD operations on this third model.

Now it's time to introduce `Toys` for our `Cats`! 

We are essentially going to knockout full CRUD all at the same time. 

We will need to do the following in order to make this approach successful:

### SERVER SIDE TO DOs - Django Rest Framework
1. Add our Toy model
2. Migrations / Migrate our new model
3. Add our Toy model to admin
4. Add our Toy serializer
5. Add Server Side Views / Functionality for full CRUD on Toys
6. Add Server Side URLS for `Toy Index` and `Toy Detail`

### CLIENT SIDE TO DOs - Vite/React
1. Add `allToys` / `currToy` State, Nav `Links`, `Routes`, in `App.jsx`
2. Create: `Toy List Page`, `Toy Detail Page` and `Toy Form Page`
3. Setup `toys-api.js` for all Toy related requests

## Toy model

Let's start by adding the `Toy` model at the bottom of `models.py`:

```python
# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
```

**A new model also means we need to make migrations and migrate in our terminal:**

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Register the new Toy Model in Admin

A new model means a new entry in `admin.py`. Add the toy model below `Cat` and `Feeding`.

```python
from django.contrib import admin
from .models import Cat, Feeding, Toy

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)
```

## Toy Serializer
Of course we need to add the Toy Serializer. 

`Serializers.py` - fully updated:
```python
from rest_framework import serializers
from .models import Cat, Feeding, Toy

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'

class ToySerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = '__all__'
```

## Toy URLS.py

We only need two endpoints to be able to get CRUD up and running effectively for our server. So let's go ahead and drop them in to `urls.py`.

```python
path('toys/', ToyIndex.as_view(), name='toy-index'),
path('toys/<int:toy_id>/', ToyDetail.as_view(), name='toy-detail'),
```

## Toy View Functions `views.py`
```python
from .models import Cat, Feeding, Toy
from .serializers import CatSerializer, FeedingSerializer, ToySerializer

class ToyIndex(generics.ListCreateAPIView):
  serializer_class = ToySerializer
  queryset = Toy.objects.all()

class ToyDetail(APIView):
  serializer_class = ToySerializer
  lookup_field = 'id'
  
  def get(self, request, toy_id):
    try:
      toy = get_object_or_404(Toy, id=toy_id)
      return Response(self.serializer_class(toy).data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def put(self, request, toy_id):
    try:
      toy = get_object_or_404(Toy, id=toy_id)
      serializer = self.serializer_class(toy, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete(self, request, toy_id):
    try:
      toy = Toy.objects.get(id=toy_id)
      toy.delete()
      return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Client Side To Dos
1. `Toys` state:
  - `ToysDetailPage` => `[catToys, setCatToys]`
  - `ToysIndexPage`  => `[allToys, setAllToys]`
  - `ToysFormPage`   => `[currToy, setCurrToys]`
  - `CatDetailPage`  => `[catToys, setCatToys]`
2. Setup client side routing 
  - `ToyIndexPage`
  - `ToyDetailPage`
  - `ToyFormPage`
    - create, edit, delete
3. Toy API / requests for
  - Create
  - Read Index / Show
  - Update
  - Delete

That's a lot!

### START WITH THE TOY-API.js

This will set us up so that we can properly import our API when ready and have the requests all ready to go. The requests are almost exact copies of other requests we have already written. Use your examples!

`toy-api.js`
```js
import sendRequest from "./sendRequest";
const url = "/toys/"

export function index() {
    return sendRequest(url)
}

export function show(id) {
    return sendRequest(`${url}${id}`)
}

export function create(formData) {
    return sendRequest(url, "POST", formData)
}

export function update(id, formData) {
    return sendRequest(`${url}${id}`, "PUT", formData)
}

export function deleteToy(id) {
    return sendRequest(`${url}${id}`, "DELETE")
}
```

### App.jsx - Links and Routes

We will need to create:
- State for holding all toys upon loading our application
- Links to our `ToyCreatePage`, `ToyIndexPage` - to create and list toys.
- Routes in the body of App.jsx to navigate to:
  - `ToyFormPage`   => create, edit, delete
  - `ToyIndexPage`  => list
  - `ToyDetailPage` => show

`App.jsx`
```jsx
// update routes for proper CSS => add 'toys'
const routes = ["about", "cats", "toys"]

// Links to Create and List / Index
<nav>
  <ul>
    <li><Link to="/about">About</Link></li>
    <li><Link to="/cats">All Cats</Link></li>
    <li><Link to="/cats/new">New Cat</Link></li>
    <li><Link to="/toys/new">Add a Toy</Link></li>
    <li><Link to="/toys">All Toys</Link></li>
  </ul>
</nav>

// routes in the body of App.jsx (exactly like our cats!)
<Route path="/toys/:id" element={<ToyDetailPage allToys={allToys} setAllToys={setAllToys}/>} />
<Route path="/toys" element={<ToyIndexPage allToys={allToys} />} />
<Route path="/toys/new" element={<ToyFormPage allToys={allToys} setAllToys={setAllToys} createToy={true} />} />
<Route path="/toys/edit/:id" element={<ToyFormPage allToys={allToys} setAllToys={setAllToys} editToy={true}/>} />
<Route path="/toys/confirm_delete/:id" element={<ToyFormPage allToys={allToys} setAllToys={setAllToys} deleteToy={true}/>} />
```

**Let's comment out the routes for now so that we do not receive errors!**

### Create all Toy Pages and Import in App.jsx
We will be creating three new pages to work with:
  - `ToyFormPage`   => create, edit, delete
  - `ToyIndexPage`  => list
  - `ToyDetailPage` => show

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
│   │   ├── CatDetailPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── CatIndexPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── CatFormPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── ToyIndexPage        <<<<<
│   │   │   ├── index.jsx       <<<<<
│   │   │   └── styles.css      <<<<<
│   │   ├── ToyFormPage         <<<<<
│   │   │   ├── index.jsx       <<<<<
│   │   │   └── styles.css      <<<<<
│   │   ├── ToyDetailPage       <<<<<
│   │   │   ├── index.jsx       <<<<<
│   │   │   └── styles.css      <<<<<
```

### 1. Toy Form Page 

- Our toy form will be its own page, just like the `Cat Form Page`.
- The `CSS` for the form is already existing in the `index.css`.
- Essentially all the same code as what is on the `CatFormPage`. 

Let's compare the CatForm to below to get a sense of speeding up the work we have already done and how we can reuse the `Cat Form Page` code.

`ToyForm.jsx`
```jsx
// IMPORTS
import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import { useParams, Link } from "react-router";
import nerdCat from "../../assets/images/nerd-cat.svg";

// APIs
import * as toyAPI from "../../utilities/toy-api";

export default function ToyFormPage({ createToy, editToy, deleteToy }) {
    const initialState = { name: "", color: "" }
    const [currToy, setCurrToy] = useState(null);
    const [formData, setFormData] = useState(initialState);
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        async function getAndSetDetail() {
          try {
              const toyDetail = await toyAPI.show(id);
              setFormData({ name: toy.name, color: toy.color })
              setCurrToy(toyDetail);
          } catch (err) {
              console.log(err);
              setFormData(initialState);
              setCurrToy(null);
          }
        if (editToy || deleteToy && id) getAndSetDetail()
    }, [id])

    function handleChange(evt) {
        const updatedData = { ...formData };
        setFormData({ ...updatedData, [evt.target.name]: evt.target.value })
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newToy = editToy ? await toyAPI.update(currToy.id, formData) : await toyAPI.create(formData);
            setFormData(initialState)
            navigate(`/toys/${newToy.id}`)
        } catch (err) {
            console.log(err);
        }
    }

    async function handleDelete(evt) {
        try {
          evt.preventDefault();
          const response = await toyAPI.deleteToy(currToy.id)
          if (response.success) {
            setFormData(initialState)
            navigate("/toys");
          }
        } catch (err) {
            console.log(err);
        }
    }

    
    if (deleteToy && !currToy) return <h1>Loading</h1>    
    if (deleteToy && currToy)  return (<>
        <div className="page-header">
            <h1>Delete Toy?</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <h2>Are you sure you want to delete { currToy.name }?</h2>
        <form onSubmit={handleDelete}>
            <Link to={`/toys/${currToy.id}`} className="btn secondary">Cancel</Link>
            <button type="submit" className="btn danger">Yes - Delete!</button>
        </form>
    </>)

    if (editToy && !currToy)  return <h1>Loading</h1>
    if (createToy || editToy) return (<>
        <div className="page-header">
            {editToy ? <h1>Edit {currToy.name}'s Info</h1> : <h1>Add a Toy</h1>}
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                  <tr>
                    <th><label htmlFor="id_name">Name:</label></th>
                    <td><input value={formData.name} type="text" name="name" minLength="3" maxLength="50" required id="id_name" onChange={handleChange}/></td>
                  </tr>
                  <tr>
                    <th><label htmlFor="id_color">Color:</label></th>
                    <td><input value={formData.color} type="text" name="color" maxLength="20" required id="id_color" onChange={handleChange}/></td>
                  </tr>
                </tbody>
            </table>
            <button type="submit" className="btn end submit">Submit!</button>
        </form>
    </>)
}
```
### Update App.jsx =>

- Import the page in app.jsx
- Uncomment the form route
- Test to see that the page loads!

![New Toy Page](./assets/toy-new.png)

Got an error? Not a problem. Our create operation was successful, but our view function has a redirect to a page that doesn't exist yet.

You can confirm the creation of new toys in the Admin dashboard.

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

The next step is to create a place in our UI to view toys and give the server a proper place to redirect.



## Toy Detail Page

![Toy Detail Page Wireframe](./assets/toy-detail-wireframe.png)

Once we create a new Toy we will navigate to the Toy's to check out what has been created. 

Let's create the detail page and then we will go through the process of setting up the route to let us create a toy and navigate to its detail page.

`ToyDetailPage.jsx`
```jsx
// IMPORTS
import "./styles.css";
import { useState, useEffect } from "react";
import { useParams, Link } from "react-router";

// APIs
import * as toyAPI from "../../utilities/toy-api";

export default function ToyDetailPage() {
    const [toyDetail, setToyDetail] = useState(null);
    const { id } = useParams();

    useEffect(() => { 
        async function getAndSetDetail() {
          try {
            const toy = await toyAPI.show(id);
            setToyDetail(toy);
          } catch (err) {
            console.log(err);
            setToyDetail(null);
          }
        }
        getAndSetDetail()
    }, [id])

    if (!toyDetail) return <h3>Your toy details will display soon</h3>

  return (<>
    <div className="toy-detail-card" style={{ borderColor: toyDetail.color }}>
      <div className="toy-detail-card-bg" style={{ backgroundColor: toyDetail.color }}></div>
      <div className="toy-detail-card-content">
        <h2>{ toyDetail.name }</h2>
        <p>A { toyDetail.color } toy</p>
      </div>
    </div>
    <div className="toy-actions">
      <Link to={`/toys/edit/${toyDetail.id}`} className="btn warn">Edit</Link>
      <Link to={`/toys/confirm_delete/${toyDetail.id}`} className="btn danger">Delete</Link>
    </div>
  </>)
}
```

### Toy `detail` CSS
`styles.css`
```css
main.toys {
    display: flex;
    align-items: flex-end;
    justify-content: flex-start;
    min-height: auto;
}

.toy-detail-card {
  width: 224px;
  height: 224px;
  margin: 25px 25px 15px 40px;
  border: solid 2px;
  box-shadow: var(--card-box-shadow);
  position: relative;
}

.toy-detail-card-bg {
  opacity: 0.4;
  position: absolute;
  display: inline-flex;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.toy-detail-card-content {
  padding: 15px;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  flex-direction: column;
  color: var(--text-color);
}

.toy-detail-btn {
  margin-bottom: 15px;
}

.toy-detail-card h2 {
  margin: 7px 0;
  font-size: var(--font-xl);
  z-index: 1;
}

.toy-detail-card p {
  margin: 0;
  font-size: var(--font-reg);
  z-index: 1;
}

.toy-actions {
    margin: 25px 25px 25px 40px
}
```

![toy detail](./assets/toy-detail.png)
Refresh to see your styled details page.


### Toy Index Page
![Toy Index Page Wireframe](./assets/toy-index-wireframe.png)

`ToyIndexPage.html`:
```jsx
// IMPORTS
import "./styles.css";
import { useState, useEffect } from "react"
import { Link } from "react-router";
import string from "../../assets/images/string.svg";
import mouse from "../../assets/images/mouse.svg";
import post from "../../assets/images/post.svg";
import fish from "../../assets/images/fish.svg";

// APIs
import * as toyAPI from "../../utilities/toy-api";

export default function ToyIndexPage() {
    const [allToys, setAllToys] = useState([])

    useEffect(() => {
        async function getAllToys() {
          try {
            const toys = await toyAPI.index();
            setAllToys(toys);
          } catch (err) {
            console.log(err);
            setAllToys([]);
          }
        }
        getAllToys();
    }, [])

    return (<>
        <section className="page-header">
            <h1>All Cat Toys</h1>
            <img src={string} alt="A ball of string" />
            <img src={mouse} alt="A mouse" />
            <img src={post} alt="A scratching post" />
            <img src={fish} alt="A fishy toy" />
        </section>
        <section className="toy-index-card-container">
        {allToys.map(toy => (
          <div key={toy.id} className="toy-index-card" style={{ borderColor: toy.color }}>
            <div className="toy-index-card-bg" style={{ backgroundColor: toy.color }}></div>
            <Link to={`/toys/${toy.id}`}>
              <div className="toy-index-card-content">
                <h2>{ toy.name }</h2>
                <p>A { toy.color } toy</p>
              </div>
            </Link>
          </div>
        ))}
        </section>
    </>)
}
```

This markup includes a cute page header with some cat toy images, as well as a programmatically rendered list of toys from our database.

Test the link in the nav to see the new page.

### Toy `index` CSS

`styles.css`:
```css
.toy-index-card-container {
  padding: 0 40px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.toy-index-card {
  width: 224px;
  height: 224px;
  margin: 10px;
  border: solid 2px;
  box-shadow: var(--card-box-shadow);
  position: relative;
}

.toy-index-card-bg {
  opacity: 0.4;
  position: absolute;
  display: inline-flex;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.card-index-content {
  padding: 15px;
  height: 100%;
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  flex-direction: column;
}

.toy-index-card > a {
  position: absolute;
  top: 0;
  left: 10px;
  width: 100%;
  height: 100%;
  display: inline-block;
  text-decoration: none;
  color: var(--text-color);
}

.toy-index-card h2 {
  margin: 7px 0;
  font-size: var(--font-xl);
}

.toy-index-card p {
  margin: 0;
  font-size: var(--font-reg);
}
```

Refresh to see the final index page!

![Toy Index Page](./assets/toy-index.png)

Nice work!


### UPDATING TOY COLOR PICKER!

Previously in Cat Collector MPA we implemented a date picker that made for a more interesting and visually appealing approach to choosing the date. The application we chose it meant for Vanilla Javascript and wouldn't be as easy to work with in React or as fun if we did the exact same thing in CC-SPA... SO

We're going to implement the ability to choose a color using HTML's built in color-picker input, and then adding a package through Node Package Manager that can map our color picker Hex Number to an Actual Color name, which will update the color name for us and allow us to change our color to any color that exists in the color picker.. Far more cool - I think! 

So let's get started!

In order to do this we will need to update the following items:

1. Install the [Color-2-Name](https://www.npmjs.com/package/color-2-name) package in our react app / node_modules.
2. Update our display for the `toy.color` property to display the color based on the return value from the package.
3. Update our Input in the form to a `type="color"`


Let's do it!

1. In your `frontend` project folder let's install the package
- `npm install color-2-name`

2. Update the Input in `ToyFormPage`
- `const initialState = { name: "", color: "#ff0000" }`
-  change the input type to color: `type="color"`

1. Update All Locations where the toy.color property is being displayed...
- `import { closest } from 'color-2-name';`
- update from: `<p>A { toy.color } toy</p>`
- update to    `<p>A { closest(toy.color).name } toy</p>`

On two pages => `ToyDetailPage`, `ToyIndexPage`


**THATS IT!!.. EASY!!**
