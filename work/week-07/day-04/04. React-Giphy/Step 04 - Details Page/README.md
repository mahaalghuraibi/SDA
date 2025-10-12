<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. 

# STEP 4 - Detail Page

Let's keep moving!

Our next step is to create a detail page for a spcific GIF from our excellent giphy API.

Currently our page looks like this:

```jsx
export default function GiphyDetailPage({}) {
    return <h1>GiphyDetailPage</h1>
}
```

We are working towards being able to display information (details) about the gif, but first we need to be able to access the specific gif we are referring to.

To do this we will need to import a few items:
- useEffect (to run code on page load)
- useState (to hold the data of the specific gif)
- useParams (to be able to access the route paramter)

```jsx
import { useEffect, useEffect } from 'react';
import { useParams } from "react-router";

export default function GiphyDetailPage({}) {
    return <h1>GiphyDetailPage</h1>
}
```

### Setup useState, useEffect, useParams
Next let's setup state to hold the data of the gif and grab the id from react-router...

```jsx
import { useEffect, useEffect } from 'react';
import { useParams } from "react-router";

export default function GiphyDetailPage({}) {
    const [gifDetail, setGifDetail] = useState(null);
    const { id } = useParams();

    console.log(id, gifDetail)
    return <h1>GiphyDetailPage</h1>
}
```


What happened? Did the console print anything? Why not????

(HINT => go look at App.jsx)..

We need to update the element for the detail route and import the component up top!...

```jsx
// import component...
import GiphyDetailPage from '../GiphyDetailPage/GiphyDetailPage';

  return (
    <Routes>
      <Route path="/*" element={<LandingPage />} />
      <Route path="/giphy/:id" element={<GiphyDetailPage />} />
    </Routes>
  )
```

Now if we click on a detail we should be brought to the page and the console.log() should show us the id of the item we clicked on! Success!

### Pass the props and set the state

**ONE**
We need to be able to access our array of gifs to be able to find the gifs we clicked on.. So where is our array currently located?

We will need to refactor.. the state is located in `LandingPage` and we need to access the same state in a parallel component, `DetailPage`. So, let's **lift** the state up one component level to App and then pass the array of gifs as a prop to both `LandingPage` and `DetailPage`..

HINT => delete unused imports and bring them in where needed!

**TWO**
Pass the props to both child components. 

Let's talk - what about the useEffect that loads the gifs on the landing page? Should that need be on the same page as the state that is holding it and accessing the api... Logically the answer to me would be 'YES'... so let's move that too!

Once moved.. check if it works... 

You should have one more error.. don't forget to **destructure** your props in the components!

NOW => we should have landing page gifs being displayed and we should still have our id being found in the console form the route parameter...

**THREE**
Next we need to have two events. When the component first loads the gifDetail variable is going to be assigned to null, which means that when we try to display data about the gif... `{gif.title}` we will receive an error. SO we need to prevent / take into these circumstances and we also need code to run once we do get the route parameter. We'll achieve this with the useEffect...

```jsx
export default function GiphyDetailPage({ trendingGifs }) {
    const [gifDetail, setGifDetail] = useState(null);
    const { id } = useParams();

    useEffect(() => { 
        // once we find the id, we need to get the info from the trendingGifs and set it to our detail state...
        const gifData = trendingGifs.find(gif => gif.id === id);
        // KEEP IN MIND THE .find METHOD RETURNS A REFERENCE.. DO NOT MUTATE THIS INFORMATION DIRECTLY
        setGifDetail(gifData);
    }, [id]) // this means the useEffect will run when the id variable is updated / changes

    if (!gifDetail) return <h3>Your gif details will display soon</h3>

    return (
        <div>
            <h1>Your Gif Details will go here</h1>
        </div>
    )
}
```

Once the gifDetail state is updated successfully react will see the changes and will update the UI / return statement accordingly. 

**FOUR**

Next we need to create a basic UI to be able to display our gif details... I will provide something simple to work with so we can keep  moving...

First reset the css in `App.css`:
`App.css`:
```css
#root {
  width: 100vw;
  height: 100vh;
}
```

Then add the UI in the return statement for giphy detail:
```jsx
import "./giphyDetailPage.css";

    return (
        <div className="giphy-detail-container">
            <h1>{gifDetail.title}</h1>
            <img src={gifDetail.images.downsized_large.url} alt={gifDetail.alt_text} />
            <div className="giphy-details">
                <h5>Upload Date: </h5>
                <h5>{gifDetail.import_datetime}</h5>
                <h5>Rating: </h5>
                <h5>{gifDetail.rating}</h5>
                <h5>Source: </h5>
                <h5>{gifDetail.source}</h5>
            </div>
        </div>
    )
```


Now `GiphyDetailPage.css`:
```css
.giphy-detail-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    height: 100vw;
}

.giphy-details {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    align-items: flex-start;
}
```


And that's it!

We've successfully setup a basic detail page!

Now let's start our next step of implementing a search bar...






