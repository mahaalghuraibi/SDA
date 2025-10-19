<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 2 - Creating Cats!

We're displaying our cats successfully as an index page and on a detail page. 

We need to be able to **create** cats to make this worth it!

As usual, Django gives us the ability to reuse functionality. In this case, we can send a `POST` request to `/cats`, which is our standard approach, but we can forward the request to the same function and the same endpoint that we already have setup. The point being - we do not need to setup anymore code on the server to be able to create cats. We just need the abillity to send information to our backend.. SO => we need a form!

## Create Cat Form

In our first round of Cat Collector we used an endpoint / route `cats/new` to bring us to a page where we could see the form to create a new `Cat`. So let's do that!

We will need the following:
 - a navigation button to go to the page to create a new cat
 - a new page level component
 - build the page with a form to create the new cat
 - submit the new cat
 - be able to add the newly created cat to our React Cat App's state...

Once again, start from the beginning:

### Cats/new Route
- create our link
- create our route in routes

```jsx
import CatFormPage from '../CatFormPage';

<ul>
  <li><Link to="/about">About</Link></li>
  <li><Link to="/cats">All Cats</Link></li>
  <li><Link to="/cats/new">All Cats</Link></li>
</ul>

<Routes>
  <Route path="/*"        element={<HomePage />}/>
  <Route path="/about"    element={<AboutPage />}/>
  <Route path="/cats/:id" element={<CatDetailPage />}/>
  <Route path="/cats"     element={<CatIndexPage />}/>
  <Route path="/cats/new" element={<CatFormPage />}/>
</Routes>
```


### CreateCat Page

- add our new CatFormPage folder
- add our new index.jsx and styles.css

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
│   │   ├── CatFormPage      <<<<<<
│   │   │   ├── index.jsx    <<<<<<
│   │   │   └── styles.css   <<<<<<
```

 - build the page with a form to create the new cat
 - submit the new cat
 - navigate to detail of newly created cat
  
`CatFormPage`
```jsx
// IMPORTS
import "./styles.css";
import { useState } from "react";
import { useNavigate } from "react-router";
import nerdCat from "../../assets/images/nerd-cat.svg";

// APIs
import * as catAPI from "../../utilities/cat-api";

export default function CatFormPage() {
    const initialState = { name: "", breed: "", description: "", age: "" }
    const [formData, setFormData] = useState(initialState);
    const navigate = useNavigate();

    function handleChange(evt) {
      const updatedData = { ...formData };
      setFormData({ ...updatedData, [evt.target.name]: evt.targetvalue })
    }

    async function handleSubmit(evt) {
      try {
        evt.preventDefault();
        const newCat = await catAPI.create(formData);
        setFormData(initialState)
        navigate(`/cats/${newCat.id}`)
      } catch (err) {
        console.log(err);
      }
    }

    return (<>
        <div className="page-header">
            <h1>Add a Cat</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                    <tr>
                        <th><label htmlFor="id_name">Name:</label></th>
                        <td><input value={formData.name} type="text" name="name" maxLength="100" required id="id_name" onChange={handleChange} /></td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_breed">Breed:</label></th>
                        <td><input value={formData.breed} type="text" name="breed" maxLength="100" required id="id_breed" onChange={handleChange} /></td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_description">Description:</label></th>
                        <td>
                            <textarea value={formData.description} name="description" cols="40" rows="10" maxLength="250" required id="id_description" onChange={handleChange}></textarea>
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_age">Age:</label></th>
                        <td><input value={formData.age} type="number" name="age" required id="id_age" onChange={handleChange}/></td>
                    </tr>
                </tbody>
            </table>
            <button type="submit" className="btn end submit">Submit!</button>
        </form>
    </>)
}

```

`index.css` (add to index.css!!!) => globally used form styles!
```css
.form-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.form-container > p > * {
  margin-right: 5px;
}

.form-container > p > label {
  font-size: large;
}

.form-container > table {
  padding: 0 40px;
  width: 100%;
  border-spacing: 0 20px;
}

.form-container > table > tbody > tr > th {
  text-align: left;
  padding: 6px 20px 0 0;
  font-weight: normal;
  vertical-align: top;
  font-size: var(--font-reg);
}

.form-container > table > tbody > tr > td {
  max-width: 60%;
}

.form-container > table > tbody > tr > td > * {
  width: 100%;
  padding: 2px 4px;
  font-size: var(--font-l);
}

.form-container > table > tbody > tr > td > textarea {
  height: calc(4 * var(--font-l) + 8px);
  font-family: inherit;
}

.form-container > .btn.end {
  align-self: flex-end;
  margin-right: 40px;
}
```

### Cat API POST Request =>
 - update cat-api for the new request
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
```

### Update sendRequest.js for POST => 
`sendRequest.js`
```js
export default async function sendRequest(url, method = 'GET', payload) {

	const options = { method };

	if (payload) {
		options.headers = { 'Content-Type': 'application/json' };
		options.body = JSON.stringify(payload);
	}

	try {
		const res = await fetch(`http://127.0.0.1:8000${url}`, options);
		if (res.ok) return res.json();
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}
```

## Cats Post Request!

`views.py`
```python
  def post(self, request, *args, **kwargs):
    try:
      serializer = self.serializer_class(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

**Success! You should have a new Cat being created in the database, being returned in the `POST` request and navigating in react / client side routing to the detail page for the new cat!** 

 - If you don't - let us know you want help!
