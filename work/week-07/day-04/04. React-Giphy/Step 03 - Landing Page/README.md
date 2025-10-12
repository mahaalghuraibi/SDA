<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. 

# STEP 3 - Landing Page

Our landing page functionaliy will include the following:

- [ ] Load gifs into a gallery when our application loads
- [ ] Display all gifs from the [trending endpoint](https://developers.giphy.com/docs/api/endpoint/#trending) on component mount
- [ ] When a gif is clicked on, display a details page that shows more information about that gif, such as the gif's creator
- [ ] Create a search bar that will search for gifs depending on what is searched and display the results in the gallery. This search bar will use the [search endpoint](https://developers.giphy.com/docs/api/endpoint/#search)


## What to do next?

At this point we can work in multiple directions. Ultimately our goal is to display information from the [Giphy API](https://developers.giphy.com/), which means we will need to access that information first.. so let's visit their documentation and figure out how to gain access... [Giphy Developers site](https://developers.giphy.com/docs/api/)


## GIPHY API KEY
1. Head to [Giphy Developers site](https://developers.giphy.com/docs/api/)
2. Sign Up / Sign In
3. Click on `Dashboard` in the navbar
   - 3.1 => If you have an API Key under "Your API Keys", then all you need to do is copy the key and skip to: `Add API Key to our DotENV File` section.
4. If you do not have an existing API we will create one:
5. Select 'Create an API Key' in the navbar.
6. Select 'Select API' as we do not need anything overly complicated at the moment.
   - 6.1 => Put in your new app's name: `React-Giphy-Search`
   - 6.2 => Select platform: 'web' 
   - 6.3 => Description: 'learning react with api calls'
   - 6.4 => Check the box!
   - 6.5 => 'Create API Key'
  
## Add API Key to our DotENV File

Most projects at some point will have what are called **'environment variables'**. Environment variables are key-value pairs used in software engineering to store configuration settings, credentials, and system-related information outside the application's source code. They help manage different environments (development, testing, production) without modifying the codebase.

These are items you might want to keep secret and prevent from being dispayed and accessed across the internet. They are special to our system and we do not want outsiders being able to access this information. 

SO => we will create a file called a 'dot-env' => `.env` that will hold these variables and we will also check to make sure that we have our gitignore file setup so that we do not push these credentials to our github. 

### Check your gitignore file exists
1. Open a terminal
2. `ls -a` => should show there is a `.gitignore_global`
3. Let's take a quick look to make sure `.env` is in this file...
4. `code .gitignore_global`
5. This will open your gitignore file in vscode and we can search the contents to make sure `.env` is inside the gitignore file.

### Create the DotEnv
1. In the route / top of your giphy project we will create the DotEnv file.. `touch .env` or right click and type in `.env`.
2. Add the API Key via copy / paste and set it to a variable...
   1. GIPHY_API_KEY=paste_your_secret_here

### Make API Requests:
Our goal is to be able to make API requests to Giphy so that we can create some functionlity for the user. We previously expressed we will want two different functions.
1. Show Trending GIF's when we arrive at our website / on the landing page.
2. Search for gifs based on an input search bar at the top of our site.

To find these endpoints we will need to go to thr documentation on the giphy website....

Under the developers website there is an endpoint that it for [giphy developers quick start guide](https://developers.giphy.com/docs/api#quick-start-guide). This is an excellent place to start figuring out how to find an endpoint to send requests to that could yield trending gifs.

If we scroll down the first page a bit, there is already a hint for how to find the endpoint to make the request to... [trending gifs endpoint info...](https://developers.giphy.com/docs/api/endpoint/#trending).

The documentation on this page gives us the information we need to be able to make requests to this endpoint and include information to successfully receive the gifs we want to access...

They provide us with a Gif URL - `api.giphy.com/v1/gifs/trending` - and beneath that it points out `Request Parameters` that are specified as `Key-Value` to be added to our endpoint. The first one is important => `api_key: string(required)`... it says it is required for requests.. It is also telling us the format in which to be able to include the information so that we can be validated by the giphy website... 

To include this information we do this: 
**VITE** must be at the front of the variable!
```js
`api.giphy.com/v1/gifs/trending?api_key=${import.meta.env.VITE_GIPHY_API_KEY}`
// or whatever variable you names your key in your .env file!
```

**^^Let's chat about that^^**

## Making Requests => File Organization and Confirming Success

Our next job is to be able to set ourselves up so that we can see that our request can work. To test this, we need to do this following:

1. Make sure our landing page will load when we load the application.
2. Setup a useEffect() react hook so that the function will fire when when the Landing Page loads.
3. Console.log(apiResponseData) our API response data so that we can confirm our results came back and take a look at the shape of the data that we receive.

### File / Folder Organization
Ultimately we will need to be able to make multiple requests from our front end application to either our own backend or to external apis. Generally speaking, we should be making external application requests from our server to external apis, but for the sake of keeping things simple, and because we are not accessing anything that should be a security issue, we will make the request from our React/Vite app. 

We will update our folder structure to include a `utilities` folder with the purpose of setting a location from which to make requests / hold business logic. 

**Business logic** refers to the rules, processes, and operations that define how data is created, stored, and manipulated in an application based on real-world business requirements. It dictates how a system should function to meet business goals and user needs.

SO => let's add the `utilities` folder to handle our application's data flow and we will create a `giphy.js` file to send this first request. Later we will refactor to continue to be more organized.

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
│   ├── utilities/           <<<<
│   │   ├── giphy.js         <<<<
│   ├── index.css
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
├── package-lock.json
├── postcss.config.js
└── vite.config.js
```

In this file we will need to create an async function that will allow us to asynchronously make requests to our external api. 

**Asynchronous requests** in JavaScript allow a program to continue executing while waiting for an operation, such as fetching data from a server, to complete. This prevents the program from being blocked and improves responsiveness.

How It Works:
Synchronous vs. Asynchronous

Synchronous: Code executes line by line, waiting for each operation to complete before moving to the next.

Asynchronous: Code doesn't wait for an operation to finish before continuing execution.

In this situation we are going to construct our **async function** to allow us to **await** for the data to return from our api call so we can run code accordingly. Essentially... because we are making an external request / leaving our browser, and we do not know when the information will return, we are asking the browser to not run any code related to this request until after the information we are looking for has returned...

```jsx
export async function getTrendingGifs() {
	try {
        const url = `https://api.giphy.com/v1/gifs/trending?api_key=${import.meta.env.VITE_GIPHY_API_KEY}`;
		const res = await fetch(url);
		if (res.ok) return await res.json();
        else throw new Error("bad request")
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}
```

### Testing the Request

We have our request function setup and now we want an actual test to occur. So we need to create a useEffect hook in our landing page component and have it fire one time to see if we receive any results!

```jsx
import { useState, useEffect } from "react";
import * as giphyAPI from "../../utilities/giphy"


export default function LandingPage({}) {
    const [trendingGifs, setTrendingGifs] = useState([])

    useEffect(async () => {
        const data = await giphyAPI.getTrendingGifs();
        setTrendingGifs(data.data)
        console.log(data.data)
    }, [])
    
    return <h1>LandingPage</h1>
}
```

## Displaying the GIFs

We've confirmed we have received our array of gifs and now need to be able to display the gifs when we start our app / end up on our Landing Page. We will need a few elements to accomplish this:

1. A grid to display multiple elements.
2. A "card" to present the gif and any other information we want to display before showing a detail page.
3. A placeholder to display before the content has loaded.

### GIF Display Card

Let's start with the card to display the gif information.

Upfront we can see by looking at a gif object we have access to the image url to display the gif and a title property.. Let's use those two items to display the gif and wrap it in a link for us to go to a detail page.

In our `components` folder let's create a folder and file for `GIFCard` and add the setup for the contents:

```jsx
import { Link } from "react-router"
import "./GIFCard.css"

export default function GIFCard({ gif }) {
   return (
      <div className="gif-card">
         <img src={gif.images.downsized.url} />
         <h5>{gif.title}</h5>
         <Link to={`/giphy/:${gif.id}`}>Details</Link>
      </div>
   )
}
```

```CSS
.gif-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 5px;
    margin: 20px;
    border: 1px solid steelblue;
    border-radius: 5%;
}

.gif-card > h5 {
    margin: 7.5px;
}

.gif-card > img {
    max-height: 150px;
}

.gif-card > a:hover {
    color: red;
}
```

This should be enough to get us started.. We now need to map each gif in our data to our new GIFCard component...

In `LandpingPage.jsx` let's update our component to map the gifs and add them to the UI...

```jsx
import { useState, useEffect } from "react";
import * as giphyAPI from "../../utilities/giphy"
import GIFCard from "../../components/GIFCard/GIFCard";
import "./LandingPage.css"


export default function LandingPage({}) {
    const [trendingGifs, setTrendingGifs] = useState([])

    const trendingGifCards = trendingGifs.map(gif => (
        <GIFCard key={gif.id} gif={gif}/>
    ))

    useEffect(() => {
        async function getGifs() {
            const data = await giphyAPI.getTrendingGifs();
            setTrendingGifs(data.data)
        }
        if (trendingGifs.length <= 0) getGifs()
    }, [])
    
    return (
        <>
            <h3>Trending Gifs:</h3>
            <div className="trending-gifs-container">
                {trendingGifCards}
            </div>
        </>
    )
}
```


**Keep in mind when we map items from an array in react we nee to give react a way to keep track of what is what.. having a unique key is what react is looking for. Our gif's come with a unique id already provided in the data from the giphy api. We can absolutely (and should) use that id.**

Let's add the CSS for the `trending-gifs-container` into a `LandingPage.css` that we need to create in the same folder.

```CSS
.trending-gifs-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```


### DONE!

This should be enough to be able to display our trending GIF's from initial API request from Giphy. Next up we can make our detail page and walk back through using the route parameter to find the gif we are working with on the detail page....


