<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 2 - Updating and Deleting Cats

Our next step is to complete the Update and Delete functionalities for our Cats.

Let's discuss the items that we will need =>

 - new react / client side routing for `edit` and `delete`
 - new links on the `CatDetailPage` to move to the `edit` / `delete` form pages.
 - A form for **updating** our cats. (reuse `CatFormPage`)
 - A form for **"confirm delete"** like we had in our previous Cat Collector
 - requests for each from the frontend to the backend. 
   - One for Update
   - One for Delete
 - Update our application's state..

In the previous Cat Collector we had a template called `cat_form.html`. This template was used for both create and delete functionalities, as the form is the exact same other than the removal of one input. We're going to do the same! Developers are **lazy** and do not want to write any extra code or repeat themselves. 

Let's start by setting up our new routes for editing and deleting a cat. They are going to display the same component as we will be reusing a fair amount of the logic.

 - add the route to head to our edit page
 - add the `cats/edit/:id` route
 - add the `cats/confirm_delete/:id` route
  
`App.jsx`
```jsx
<Route path="/cats/new"                element={<CatFormPage createCat={true} />}/>
<Route path="/cats/edit/:id"           element={<CatFormPage editCat={true}   />}/>
<Route path="/cats/confirm_delete/:id" element={<CatFormPage deleteCat={true} />}/>
```

### Update the CatDetailPage
We will need to make some adjustments! 

Let's add some buttons to be able to go to our endpoints for update and delete!

- import `Link` from `react-router`
- add our two new `edit` and `update` `Links` to the UI

```jsx
import { Link } from "react-router";

// <div className="cat-details">
// ...
// </div>
<div class="cat-actions">
  <Link to={`/cats/edit/${catDetail.id}`} class="btn warn">Edit</Link>
  <Link to={`/cats/confirm_delete/${catDetail.id}`} class="btn danger">Delete</Link>
</div>
```

### Updating CatFormPage

We will need to make a few updates to the `form page`!
 - need the ID of the cat we are going to edit (useParams and useEffect)
 - need to display the cat information in the form.
 - we do not want the Cat's Name to be editable (so we need to hide the input)
 - we will need different requests to the server for create / update / delete
 - we will need logic to decide which information to display when.. so let's drop this info inside the page and discuss what is going on..


`CatFormPage.jsx`
```jsx
// IMPORTS
import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import { useParams, Link } from "react-router";

// ASSETS
import nerdCat from "../../assets/images/nerd-cat.svg";

// APIs
import * as catAPI from "../../utilities/cat-api";

export default function CatFormPage({ createCat, editCat, deleteCat }) {
    const initialState = { name: "", breed: "", description: "", age: "" }
    const [currCat, setCurrCat] = useState(null);
    const [formData, setFormData] = useState(initialState);
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        async function getAndSetDetail() {
            try {
                const cat = await catAPI.show(id);
                setCurrCat(cat);
                setFormData(cat)
            } catch (err) {
                console.log(err)
                setCurrCat(null)
                setFormData(initialState)
            }
        }
        if (editCat || deleteCat && id) getAndSetDetail()
    }, [id])

    function handleChange(evt) {
        const updatedData = { ...formData };
        setFormData({ ...updatedData, [evt.target.name]: evt.target.value })
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newCat = editCat ? await catAPI.update(formData, currCat.id) : await catAPI.create(formData);
            setFormData(initialState)
            navigate(`/cats/${newCat.id}`)
        } catch (err) {
            console.log(err)
        }
    }

    async function handleDelete(evt) {
        evt.preventDefault();
        const response = await catAPI.deleteCat(currCat.id)
        if (response.success) {
            setFormData(initialState)
            navigate("/cats");
        }
    }

    
    if (deleteCat && !currCat) return <h1>Loading</h1>    
    if (deleteCat && currCat)  return (<>
        <div className="page-header">
            <h1>Delete Cat?</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <h2>Are you sure you want to delete { currCat.name }?</h2>
        <form onSubmit={handleDelete}>
            <Link to={`/cats/${currCat.id}`} className="btn secondary">Cancel</Link>
            <button type="submit" className="btn danger">Yes - Delete!</button>
        </form>
    </>)

    if (editCat && !currCat)  return <h1>Loading</h1>
    if (createCat || editCat) return (<>
        <div className="page-header">
            {editCat ? <h1>Edit {currCat.name}'s Info</h1> : <h1>Add a Cat</h1>}
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                    {!editCat &&
                        <tr>
                            <th><label htmlFor="id_name">Name:</label></th>
                            <td><input value={formData.name} type="text" name="name" maxLength="100" required="" id="id_name" onChange={handleChange} /></td>
                        </tr>
                    }
                    <tr>
                        <th><label htmlFor="id_breed">Breed:</label></th>
                        <td><input value={formData.breed} type="text" name="breed" maxLength="100" required="" id="id_breed" onChange={handleChange} /></td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_description">Description:</label></th>
                        <td>
                            <textarea value={formData.description} name="description" cols="40" rows="10" maxLength="250" required="" id="id_description" onChange={handleChange}></textarea>
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_age">Age:</label></th>
                        <td><input value={formData.age} type="number" name="age" required="" id="id_age" onChange={handleChange} /></td>
                    </tr>
                </tbody>
            </table>
            <button type="submit" className="btn end submit">Submit!</button>
        </form>
    </>)
}
```

## Making the requests

If we take a look inside of our two submit functions, we can see see **three** different requests being made. 
 - Create
 - Update
 - Delete

Each of them has their own requirements for the information that needs to be sent back to server for proper CRUD to occur accordingly. We will create and track our two newest routes as the request moves through the following files =>

=> 1. `CatFormPage` => 2. `cat-api` => 3. `sendRequest.js` => 4. (server) `urls.py` => 5. `views.py` => 6. run code and respond

`cat-api.js`
```js
import sendRequest from "./sendRequest";
const url = "/cats/"

export async function index() {
    return sendRequest(url)
}

export async function create(formData) {
    return sendRequest(url, "POST", formData)
}

export async function update(formData, catId) {
    return sendRequest(`${url}${catId}/`, "PUT", formData)
}

export async function deleteCat(catId) {
    return sendRequest(`${url}${catId}/`, "DELETE")
}
```

`urls.py`
```py
urlpatterns = [
  path('', Home.as_view(), name='home'),
  path('cats/', CatsIndex.as_view(), name='cat-index'),
  path('cats/<int:cat_id>/', CatDetail.as_view(), name='cat-detail'),
]
```

`views.py`
```py
# New import! get_object_or_404 => 
# this built in function will throw an error for us if the object does not exist!
from django.shortcuts import get_object_or_404

class CatDetail(APIView):
  serializer_class = CatSerializer
  lookup_field = 'id'

  def get(self, request, cat_id):
    try:
        queryset = get_object_or_404(Cat, id=cat_id) # pass in the Cat model so it knows where to look!
        cat = self.serializer_class(queryset)
        return Response(cat.data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def put(self, request, cat_id):
    try:
        cat = get_object_or_404(Cat, id=cat_id)
        serializer = self.serializer_class(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete(self, request, cat_id):
    try:
        cat = get_object_or_404(Cat, id=cat_id)
        cat.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

```

**OK! Let's discuss!!!!**

We made one addition to the `urls.py` by creating an update and delete endpoint / url to collect those requests for a specific Cat. Within that one `view` function we were able to route to specific function based on the requests we made from the frontend. From there we ran code that would allow us to update or delete the cat depending on the request and return the appropriate information which would then either update the cat data in react or remove the cat from the state in our react application.

Success!!