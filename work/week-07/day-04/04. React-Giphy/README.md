<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. The intent for this in-class walk through is to show you two different ideas...

1. Ways in which we can structure our react / frontend applications to be more organized and easier to follow.
2. To show you how to make API requests from the frontend to other applications and to our own servers.
3. **NOTE** => as a safety standard you generally want to keep API requests in your server and NOT in your frontend applications.. especially if it is going to be using an API key. While there are times where this may occur.. in general external requests from your project are more safely made from your server since it is harder to access.

## Goals

Here's what we need for our MVP:
- [ ] A working react application w/ Giphy API access
- [ ] Load gifs into a gallery when our application loads
- [ ] Display all gifs from the [trending endpoint](https://developers.giphy.com/docs/api/endpoint/#trending) on component mount
- [ ] When a gif is clicked on, display a details page that shows more information about that gif, such as the gif's creator
- [ ] Create a search bar that will search for gifs depending on what is searched and display the results in the gallery. This search bar will use the [search endpoint](https://developers.giphy.com/docs/api/endpoint/#search)


## Project Set Up
### Sign up for an API key
Before starting this project, you'll need to go to the [Giphy Developers site](https://developers.giphy.com/docs/api/) and obtain an API key.
1.  Create an account and sign in.
1.  Set up an app by clicking the Create App in the navbar to obtain your beta key.


### Scaffold Your Project
1. Using Vite, create a React app called `react-giphy-searcher`
2. Create a `components` folder inside `src`
3. Inside the `components` folder, create another folder called `App`
4. Move `App.jsx` into the `src/components/App` folder and rename `App.jsx` to `index.jsx`
5. Move `App.css` into the `src/components/App` folder and rename `App.css` to `styles.css `
6. You file structure should look like this:
    ```
    react-giphy-searcher
    ├── node_modules/
    ├── public/
    └── src
    │   ├── assets/
    │   ├── pages/
    │   │   ├── App
    │   │   │   ├── index.jsx
    │   │   │   └── styles.css
    │   ├── index.css
    │   └── main.jsx
    ├── .gitignore
    ├── index.html
    ├── package.json
    ├── package-lock.json
    ├── postcss.config.js
    └── vite.config.js
    ```

7. Replace the code in `App.jsx` with the following:
   
```jsx
export default function App() {
   return (
     <div>
       <h1>React Giphy Searcher</h1>
     </div>
   );
}
```

### Store your API Key Securely
As developers, we need to guard against our API keys being pushed to GitHub. One way to ensure that this doesn't happen is to store them in a separate file that is not tracked in Git at all.

As we have done before, we will create a `.env` file to store the API key.

1. Create a new file in the project root directory called `.env`
1. Inside this file add the following, replacing where it reads `Your API Key Goes Here` with your Giphy API key:
```bash
VITE_GIPHY_KEY='Your API Key Goes Here'
```

Vite automatically loads environment variables, and exposes variables prefixed with `VITE_` to the React app. This means that _if your server is already running_, you need to stop it and restart it after adding or changing an environment variable, so do that now.

You can access the environment variable in a React component like this using this syntax:
`import.meta.env.VITE_SOME_KEY`

You can `console.log` it in a component to see if your environment is set up correctly.
```jsx
function App() {
  console.log(import.meta.env.VITE_GIPHY_KEY)
  return (
    <div>
      <h1>React Giphy Searcher</h1>
    </div>
  );
}

export default App;
```

If you would like to learn more about Vite and environment variables, you can visit [this page](https://vitejs.dev/guide/env-and-mode.html).


## Structuring Your React App
Currently your application file structure matches what's outlined above. ***We recommend you build your app with the same file structure as what we've built in class.***

However, there is no one correct way to build a React application. You can read [this article](https://david-gilbertson.medium.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed) for more information on why there's no one true way. 

Ultimately, you will be in control of what components you make, how you name them, and where you store them. Ensure however, that you are observing a consistent separation of concerns.

<hr>

### Requirements
- Create a landing page that displays 50 trending gif images from the *Trending* API endpoint.
    - Consider how you might implement the `useEffect` hook to query the API
    - Consider how you might implement the `useState` hook to store the API response.
- Your landing page should be styled with Tailwind CSS.

Here's a possible mockup depicting what the landing page could look like:

![Landing Page](https://i.imgur.com/RE0DGhs.png)

> **NOTE:** The image above depicts a search bar at the top of the page - you do not need to build the search bar yet! If you do, it does not need to be functional. 👍


### Bonus
- On your landing page, display 10 gifs and build out pagination functionality so that you can view 10 different gifs each time you paginate forwards or backwards.

<hr>

## Deliverable Part 2
For this deliverable you'll be building something similar to what we've done in Aesthetic Domain Part 5, where you'll be incorporating React Router into your application.


### Requirements
- Install `react-router-dom` into your application.
- Update your `main.jsx` file with the appropriate syntax
- Refactor your `App` component to contain the following routes:
    - `HomePage`
    - `DetailsPage`
- Move your gallery of gifs into a new component (maybe you could call it `HomePage` 👀) and have that component render when the user first opens your site.
- When you click on a gif, route to the `DetailsPage` component that displays the following details:
    - The gif image
    - The gif title
    - The user (the gif creator)'s avatar, username, and link to their Giphy profile
- Use Tailwind CSS to display the details page in a professional and neat manner


### Bonus
We will need to do this for Part 3 anyways, but if you want you can get a head start on it now!
- Create a search bar. This can be on a separate page or you can build it above the gallery on your home page.
- The search bar doesn't have to be functional yet!


## Deliverable Part 3
For this deliverable you'll be building something similar to what we've done in Aesthetic Domain part 6, where you'll be incorporating search functionality into your application.


### Requirements
- If you haven't already done so, create a search bar. This can be on a separate page or you can build it above the gallery on your home page.
- Using state, store a user's input from the search bar
- Once the user submits their search, query the [search endpoint](https://developers.giphy.com/docs/api/endpoint/#search) with the user's search string.
- Display the (up to) 50 results that are returned in a gallery below the search bar.
- Display the string the user searched above the gallery somewhere. You can refer to this picture for an example:
  
    ![Search Page](https://i.imgur.com/FRi9uBf.png)