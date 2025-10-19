<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Collector

## Part 2 - Cat Details Page

Our next step is to be able to display a specific cat. 

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
│   │   ├── CatIndexPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── CatDetailPage   <<<<<<<
│   │   │   ├── index.jsx   <<<<<<<
│   │   │   └── styles.css  <<<<<<<
```

### Create CatDetailPage

We will first need a Cat Detail Page so we can import it into `App.jsx` and add a route to the page. Then we can get some contents in place for the page. Let's start by creating our two starting point files:
- `CatDetailPage/index.jsx`
- `CatDetailPage/styles.css`

`CatDetailPage.jsx`
```jsx
import "./styles.css"

export default function CatDetailPage() {
  return <h1>This is the Cat Detail Page</h1>
}
```

`App.jsx`
```jsx
import CatDetailPage from "../CatDetailPage";

// new route!
<Route path="/cats/:id" element={<CatDetailPage />} />
```

### Move the allCats State
We will need to do some refactoring to get everything organized and connected properly. Let's do the following:

To Do:
 - wrap each `Cat` with a `Link` so we can `navigate` to the proper cat
 - access the route parameter to get the `id` of the `Cat` we want to view
 - make request to get the info for the Cat
 - display the `Cat`
 - add the CSS for the CatDetail


## Cat Index Page
- Wrap each `Cat` with a `Link` so we can `navigate` to the proper cat
- Link to `/cats/${catId}`

`CatIndexCard.jsx`
```jsx
    return (
      <div className="cat-index-card">
          <Link to={`/cats/${cat.id}`}>
              <div className="cat-index-card-content">
                  <img src={skaterCat} alt="A skater boy cat" />
                  <h2>{cat.name}</h2>
                  <p>{cat.age > 0 ? `A ${cat.age} year old ${cat.breed}` : `A ${cat.breed} kitten.`}</p>
                  <p><small>{cat.description}</small></p>
              </div>
          </Link>
      </div>
    )
```

### Update Cat Detail Page Code =>
 - access the route parameter to get the `id` of the `Cat` we want to view
 - display the `Cat`

`CatDetailPage.jsx`
```jsx
import "./styles.css";
import { useState, useEffect } from "react";
import { useParams } from "react-router";
import skaterCat from "../../assets/images/sk8r-boi-cat.svg";


export default function CatDetailPage() {
    const [catDetail, setCatDetail] = useState(null);
    const { id } = useParams();

    useEffect(() => { 
        function getAndSetDetail() {
            try {
                const cat = await catAPI.show();
                setCatDetail(cat);
            } catch (err) {
                console.log(err);
                setCatDetail(null);
            }
        }
        if (id) getAndSetDetail()
    }, [id])

    if (!catDetail) return <h3>Your cat details will display soon</h3>

    return (
        <section className="detail-cat-container">
          <div className="detail-cat-img">
            <img src={skaterCat} alt="A skater boy cat" />
          </div>
          <div className="cat-details">
            <h1>{ catDetail.name }</h1>
            <h2>{ catDetail.age > 0 
                  ? `A ${catDetail.age} year old ${catDetail.breed}` 
                  : `A ${catDetail.breed} kitten.`} 
            </h2>
            <p>{ catDetail.description }</p>
          </div>
        </section>
    )
}

```

### Add Cat Detail Page CSS =>

`styles.css`
```css
.detail-cat-container {
    padding: 35px 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.detail-cat-container > section {
    min-width: 45%;
    width: 100%;
    border: var(--borders);
    border-radius: var(--card-border-radius);
    padding: 10px;
    box-shadow: var(--card-box-shadow);
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.detail-cat-img {
    min-width: 150px;
    max-width: 350px;
}

.cat-details {
    width: 100%;
}

.cat-details h1 {
    font-size: var(--font-xxl);
    margin: 0;
}

.cat-details h2 {
    font-size: var(--font-xl);
    margin: 0 0 10px;
    margin-top: 0;
    margin-bottom: 10px;
}

.cat-details p {
    font-size: var(--font-reg);
    margin: 5px 0;
}

.cat-actions {
    margin: 20px;
}

.feedings-toy-container {
    display: flex;
    flex-direction: column;
    padding: 0px 30px;
    align-items: center;
    justify-content: space-between;
}

.subsection-title {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
}

.subsection-content {
    margin: 0 8px;
}

.toy-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.toy-info {
    height: 35px;
    width: 70%;
    padding: 5px 10px;
    margin: 5px;
    border-radius: 5px;
    border: solid 2px;
    box-shadow: var(--card-box-shadow);
    position: relative;
    display: flex;
    align-items: center;
}

.toy-container > a {
    width: 100%;
}


.color-block {
    opacity: 0.6;
    position: absolute;
    display: inline-flex;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -10;
}

.unfed,
.fed,
.no-toys,
.all-toys {
    margin: 0;
    font-weight: bold;
}

.unfed,
.no-toys {
    color: var(--danger);
}

.fed,
.all-toys {
    color: var(--submit);
}

.feedings-toy-container > section {
    width: 100%;
    min-width: 360px;
    border: var(--borders);
    border-radius: var(--card-border-radius);
    padding: 10px;
    box-shadow: var(--card-box-shadow);
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-bottom: 35px;
}


.subsection-title img {
    height: 42px;
    margin-left: 8px;
}

.subsection-title img:first-of-type {
    margin-left: 16px;
}

.feedings h2,
.toys h2 {
    font-size: 3.2rem;
    margin: 0;
}

.feedings h3,
.toys h3 {
    font-size: var(--font-xl);
    margin: 10px 0;
}

.subsection-content p,
.subsection-content input,
.subsection-content select {
    font-size: var(--font-l);
}

.subsection-content input,
.subsection-content select {
    margin-left: 5px;
    padding: 3px;
}

.feedings table {
    width: calc(100% - 16px);
    text-align: left;
    border-collapse: collapse;
    margin: 0 8px;
}

.feedings td {
    padding: 8px 5px;
    font-size: var(--font-reg);
}

.feedings th {
    font-size: var(--font-l);
    padding: 5px 5px 0;
    border-bottom: rgb(36, 116, 248) solid 2px;
}

.feedings tr:nth-child(even) {
    background-color: #f3f3fd;
}

.toy-container p {
    margin: 12px 0;
    font-weight: 500;
}

.toy-container a {
    text-decoration: none;
    color: #111;
}

.toy-container .btn {
    padding: 3px 10px;
    margin-left: 10px;
}

#file-input {
    overflow: hidden;
    position: absolute;
    width: 0.1px;
    height: 0.1px;
}

#file-name {
    margin-bottom: 10px;
}

@media only screen and (min-width: 768px) {
    .detail-cat-container {
        padding: 35px 30px;
        flex-direction: row;
        align-items: center;
        justify-content: start;
    }

    .detail-cat-img {
        width: 25%;
        max-width: 250px;
        margin-right: 25px;
    }

    .feedings-toy-container {
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;
    }

    .feedings-toy-container>section {
        width: 45%;
    }
}
```

**Excellent!**

### CatAPI.show() Request

Lastly, we need to make our Cat API request to get the information for the cat whose detail page we are on. 

The following code will add our request to sendRequest, which will then match our url in our Django Rest Framework server...

`cat-api.js`
```js
export function show(catId) {
    return sendRequest(`${url}${catId}/`);
}
```


`view.py`
```python
class CatDetail(APIView):
  serializer_class = CatSerializer
  lookup_field = 'id'

  def get(self, request, cat_id):
    try:
        queryset = Cat.objects.get(id=cat_id)
        cat = CatSerializer(queryset)
        return Response(cat.data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

`urls.py`
```python
# import the new View Function or Directly add to the url pattern
from . import views
# or =>
# from .views import CatDetail

urlspatterns = [
    path('cats/<int:cat_id>/', views.CatDetail.as_view(), name='cat-detail'),
]
```

We should have a beautfiul, working, cat detail page now. Our next step is to be able to **CREATE** some new cats so we can add to our database!