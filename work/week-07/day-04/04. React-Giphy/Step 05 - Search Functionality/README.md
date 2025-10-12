<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. 

# STEP 4 - Search Bar

We're on a roll! We have our application up and running with client side routing, have successfully displayed the trending gifs upon app loading and can display details about one specific gif.

Now we want to be able to have a search bar and add navigation that is conditional based on the page we are on. The intent of the search bar is to allow a user to search for gifs based on keywords. The navigation will allow us to return to the `Landing Page` when we are done looking at the details page.

Let's talk about this - the searfch bar is meant to be displayed on **ALL** pages. It will be on the landing page and on the detail page.. accessible from anywhere in the app. 

Where could we place this component? Are we allowed to place components inside of routes? Let's take a look:

```jsx
  return (
    <Routes>
      <Route path="/*" element={<LandingPage trendingGifs={trendingGifs} />} />
      <Route path="/giphy/:id" element={<GiphyDetailPage trendingGifs={trendingGifs} />} />
    </Routes>
  )
```

Our current return statement has our routes defined and no other information. We have two approaches we could take... We can create a navigation component and import it on all pages individually. BUT, remember, we are lazy and do not want to do extra work... couldn't we just place the navigation inside the routes as an actual component? Let's try it out!...

```jsx
return (
    <div>
        <h3>Navigation</h3>
        <Routes>
          <Route path="/*" element={<LandingPage trendingGifs=  {trendingGifs} />} />
          <Route path="/giphy/:id" element={<GiphyDetailPage trendingGifs=  {trendingGifs} />} />
        </Routes>
    </div>
)
```

While we **cannot** add a non-route component inside the <Routes>, we can wrap the routes in a <div> and add items at the top of this new container without negatively affecting anything below it.. We can now create a <nav> component and import it into `App.jsx`. So let's do it!

You do it! =>

1. Create a new component **folder** for Navigation
2. Create a new component **file** for Navigation.jsx
3. Fill in basic contents for `Navigation.jsx` to get things moving and connectd
4. Import the new component into `App.jsx`
5. Add some basic styling to get the container in place the way you want it.

<details>
    <summary>My Navigation JSX and CSS</summary>

```jsx
import { Link } from "react-router";
import "./Navigation.css";

export default function Navigation() {

    return (
        <nav className="nav-container">
            <form >
                <input type="text" placeholder="search" />
            </form>
            <Link to="*">Landing Page</Link>
        </nav>
    )
}
```

```css
.nav-container {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    min-width: 100vw;
    height: 8vh;
}

.nav-container > form {
    width: 75%;
}

.nav-container > form > input {
    width: 100%;
}
```

</details>

### Search Bar State and Submission

Woohoo!

Did you make sure your navigation bar is displaying properly on all of your pages?

Now we have a few more items to consider...

- How does the search bar function?
  - Is it meant to display on a separate page?
  - Is it meant to replace the contents of the trending gif contents / on the same page (the landing page)?
  - Upon submit, does the search bar request the same endpoint as the trending gifs request?

There's really no reason to create an entirely separate page just for search results that can be displayed in the same fashion. The `Landing Page` can be used and the same gif-state can be used to store the results.. SO - we need to figure out a refactor so we can stay DRY and utilize what we have inplace instead of rewriting again.

What we need to do:
- create the controlled form and connected it to the input in the navigation bar. 
- write a separate function to make a request to the utilities file for whatever search the user inputs
- make the actual fetch request to the correct endpoint.
- navigate to the Landing Page **IF** the user is not currently on the LandingPage client side endpoint so we can see our updated results...

SO => Let's create the form...

`Navigation.jsx`
```jsx
export default function Navigation() {
    const [searchText, setSearchText] = useState("");

    return (
        <nav className="nav-container">
            <form onSubmit={(evt) => searchGIFs(evt, searchText, setSearchText)}>
                <input value={searchText} type="text" placeholder="search" onChange={(evt) => setSearchText(evt.target.value)} />
            </form>
            <Link to="*">Landing Page</Link>
        </nav>
    )
}
```

We've setup a simple form, now controlled by react, and need to be able to send the user's search information to giphy so we can get some results! 

The `searchGIFs` function will need to be sent from our parent component (page-level) `App.jsx`. So let's create it and pass it down!..

I will include a console.log() to show we are receiving the userQuery information to start.

```jsx
  async function searchGIFs(evt, searchText, setSearchText) {
    evt.preventDefault()
    console.log("testing receing user text", searchText)
    setSearchText("")
  }
```

We should be able to enter information into the text form and submit it to the gifSearch function we ave passed down to the navigation component as a prop. Once we submit using the above function we passed as a prop, hitting "enter" on our keyboard will submit call the function, prevent the default function of fully submitting a request to the server (which we do not want), will console log the user's search text and reset the searchText state to be empty again... Yay!

Once this has been confirmed, we can now discuss the process of making the request, which will again require some refactor...

### Refactor Giphy API Requests

We have an existing `getTrendingGifs` external API fetch request that has all of the code we need to be able to make a request. The only difference in the request is going to be the endpoints.. In fact => ALL external requests are going to be extremely similar other than the `method` and the `endpoint`.. The function itself is the exact same and a majority of the information is going to be the same... So we will make it so we can reuse our `sendRequest` function...


SO let's keep it simple, stupid / dry and refactor.. 

```
react-giphy-searcher
├── node_modules/
├── public/
└── src
│   ├── assets/
│   ├── components/
│   ├── pages/
│   │   ├── App
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── LandingPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   │   ├── GiphyDetailPage
│   │   │   ├── index.jsx
│   │   │   └── styles.css
│   ├── utilities/           
│   │   ├── sendRequest.js   <<<<
│   │   ├── giphy.js         
│   ├── index.css
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
├── package-lock.json
├── postcss.config.js
└── vite.config.js
```

**We need to create a function to handle all external requests `sendRequest` and refactor to be able to accept the endpoint we wish to reach. Again, a majority of the information will stay the same.. so we will adjust accordingly..


```js
export async function sendRequest(url) {
	try {
		const res = await fetch(url);
		if (res.ok) return await res.json();
        else throw new Error("bad request")
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}
```

`giphy.js`
```js
export async function getTrendingGifs() {
	try {
		const url = `https://api.giphy.com/v1/gifs/trending?api_key=${import.meta.env.VITE_GIPHY_API_KEY}`;
        return sendRequest(url)
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}
```



**If** you did your refactor correctly, you should still see your trending gifs loading!

**If not ask for help!**

### Search Endpoint

We previously found the information for the search api in the [giphy developers documentation.](https://developers.giphy.com/docs/) We now need to use this endpoint so we can make requests. Once again, our code will be very similar to another set of code already written.. Let's copy the `getTrendingGifs()` function and use it as the starting point to send the request to giphy.com. 

We need to:
- replace the url endpoint and add in the user information for the search we want to perform.
- change the name of the function

`giphy.js`
```js
export async function searchGifs(userQuery) {
	try {
		const url = `https://api.giphy.com/v1/gifs/search?api_key=${import.meta.env.VITE_GIPHY_API_KEY}&q=${userQuery}`;
        return sendRequest(url)
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}
```

### Confirm results!

Back in our `App.jsx` is where we will be making the search request. We need officially make the request:

```jsx
  async function searchGIFs(evt, searchText, setSearchText) {
    evt.preventDefault()
    const searchResults = await giphyAPI.searchGifs(searchText);
    console.log(searchResults, "line 29")
    setSearchText("")
  }
```

We will use our console.logs to be able to check / validate the data. When you enter information into the search bar and click "enter", does it yield results?

You should see a similar structure as before, all related to the content you searched for...

**Refactor to update the data in the Landing Page to display your results!**

**SUCCESS!!**








