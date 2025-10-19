<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Colletor

Today we start our journey of building a full stack web application using React on the front end and Django Rest Framework on the backend. This process will unfold over the course of several days / parts and will combine the tools we learned this week (react) along with a fresh approach to developing a Django server with a slightly different framework. The overall concept is the exact same as our previous Cat Collector, but with a few small changes. 

## Part 1 - Project Organization, React Routing, Assets / Base Styling

Like we have done previously in our vite / react projects, we will again add client side routing and organize our project structure for our front end. We know we will have, at the least, the following pages and project folders.. so let's implement them and some basic starter code...!

### Project Organization

```
Cat Collector SPA:
├── node_modules/
├── public/
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
│   ├── utilities/           
│   │   ├── sendRequest.js
│   │   ├── cat-api.js         
│   ├── index.css
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
├── package-lock.json
├── postcss.config.js
└── vite.config.js
```

1. Reorganizing `src/` by adding folders:
    - assets
      - images
    - components
    - pages
      - App
      - HomePage
      - AboutPage
    - utilities
  
2. We can also go ahead and create starter files for the ones that don't exist yet...
    - pages
      - App
        - `App.js`
        - `styles.css`
      - HomePage
        - `index.jsx`
        - `styles.css`
      - AboutPage
        - `index.jsx`
        - `styles.css`
    - utilities
      - `sendRequest.js`
      - `cat-api.js`
  
#### **NOTE!**
We can name the component `.jsx` file as something more explicit or just use `index.jsx`. Here is the difference:

If the file is named `Button.jsx`
```jsx
import Button from './components/Button/Button.jsx';

<Button />
```

If the file is named `index.jsx`
```jsx
import Button from './components/Button';

<Button />
```

They both work - this is one of those decisions **__YOU__** get to make as a developer. Your organizational preference and methods may be different. That's ok! My intent is to show you options so you can make your own decision as to what makes sense. In a larger project writing less code and not having to explicitly write every single detail can save space and time.

### Component contents
In each `.jsx` file we should go ahead and add the boiler plate info for component and connect each css file... We will be using the same setup for each.. so let's go ahead and start with one so we don't have to update a lot of other information:

```jsx
import "./styles.css";

export default function HomePage() {
    return <h1>This is the Home Page</h1>
}
```

**All we have to do is change the jsx filename and function names!**

### React Routing

We need our app to have a starting point just like we did in Cat Collector. Using components is very similar to using **templates** and **partials** within the templates. 

Our `App.jsx` will be our `base` template that will have everything else exist as a component inside of that (if it is a main page) or as a component within one of the main pages. So, let's setup `App.jsx` to act as our `base.html` like we did in Cat Collector MPA.

We need to update the return statement to reflect the Cat Collector UI that we want, add in client side routing for the Pages to go inside App.jsx, and update the styling accordingly.

`App.jsx` =>
```jsx
  import "./App.css"
  import { Route, Routes, Link } from 'react-router';

export default function App() {

  return (
    <>
      <header>
        <div className="header-logo-container">
          <a href="/">
            <img src="" alt="The Cat Collector Logo" />
          </a>
        </div>
        <nav>
          <ul>
            <li><Link to="/about">About</Link></li>
          </ul>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/*" element={<h2>Home Page</h2>} />
          <Route path="/about" element={<h2>About Page</h2>} />
        </Routes>
      </main>
    </>
  );
}
```

### Base Assets

We will end up using the same asset files and css styling.. so let's go ahead and drop in that information into the appropriate places..

The contents of the `./Cat Collector Assets` folder in the same directory as this read me will contain all of our static assets such as images and icons. We will want to copy and paste those items into our project assets folder under an `images` folder we will need to create...

- `/assets/images/...Cat Collector Assets`
```
  - /assets/images/
    - cat-cone.svg
    - cat-in-box.svg
    - cat-onigiri.svg
    - cool-cat.svg
    - fish.svg
    - happy-cat.svg
    - header-logo.svg
    - kitty-kabob.svg
    - logotype.svg
    - mouse.svg
    - nerd-cat.svg
    - post.svg
    - sk8r-boi-cat.svg
    - splash.svg
    - string.svg
    - teacup-cat.svg
```

**We have our assets! Let's use them:**

Now we can update our header and favicons in:
- `index.html`
- `App.jsx`

Just like in Cat Collector MPA except this time the `index.html` holds the main header / icon / favicon for the application and `App.jsx` holds our main page content because it fits inside the `root` div where React works its magic.

`index.html`
```html
  <head>
    <meta charset="UTF-8" />
    <link rel="shortcut icon" type="image/png" href="./src/assets/images/splash.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Cat Collector SPA</title>
  </head>
```

`App.jsx`
```jsx
import headerLogo from "../../assets/images/header-logo.svg";

<img src={headerLogo} alt="The Cat Collector Logo" />
```


### Base Styling

We will now want to setup our styling for both `index.css`, which is imported in `main.jsx` in our React application. Ultimately we want to be able to expand the full width and height of the screen. If we are only manipulating the information inside of the `#root div`, we will only be affecting contents inside of that container, which does not expand the full space. SO => let's refactor a bit!

- We will need to move the `index.css` file from our `src` folder up to the root of our application.
- Delete the `"./index.css"` import inside of `main.jsx`
- add a `link` in `index.html` to access the `index.css` file
- add the Cat Collector CSS to the `index.css` file..

`index.html`
```html
  <head>
    <meta charset="UTF-8" />
    <link rel="shortcut icon" type="image/png" href="./images/splash.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./index.css" />
    <title>Cat Collector SPA</title>
  </head>
```

`index.css`
```css
html {
  box-sizing: border-box;
}

/* The Universal Selector */
*,
/* All elements*/
*::before,
/* All ::before pseudo-elements */
*::after {
  /* All ::after pseudo-elements */
  /* height & width will now include border & padding by default
     but can be over-ridden as needed */
  box-sizing: inherit;
}

/* resets font size to be 62.5% of the user preference - 
     in most browser configurations this will be 10px */
:root {
  font-size: 62.5%;
}

body {
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto',
    'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
    'Helvetica Neue', sans-serif;
  min-height: 100vh;
  --nav-bg: rgba(104, 197, 248, 0.7);
  --nav-bg-ff: rgba(104, 197, 248, 0.9);
  --borders: rgb(36, 116, 248) solid 2px;
  --text-color: rgb(17, 20, 17);
  --link-hover-color: rgb(16, 56, 158);
  --button-bg: rgb(245, 245, 245);
  --button-bg-hover: rgb(226, 226, 226);
  --submit: rgb(26, 128, 0);
  --warn: rgb(255, 102, 0);
  --danger: rgb(220, 20, 30);
  --secondary: rgb(57, 57, 57);
  --card-box-shadow: 5px 5px 6px -1px #aaa;
  --font-xtreme: 4.2rem;
  --font-xxl: 3.6rem;
  --font-xl: 2.4rem;
  --font-l: 1.8rem;
  --font-reg: 1.6rem;
  --card-border-radius: 6px;
}

#root {
  width: 100%;
  height: 100%;
}

header {
  width: 100%;
  background: var(--nav-bg-ff);
  /* rgba(104, 197, 248, .9) */
  border-bottom: var(--borders);
}

nav {
  padding: 10px;
}

ul {
  margin: 0;
  list-style: none;
  padding: 0;
}

main {
  width: 100%;
  padding: 0 10px;
}

h2 {
  font-size: var(--font-xl);
}

nav a {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 600;
  font-size: 16px;
}

nav a:hover {
  color: var(--link-hover-color);
}

nav ul {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}

nav li {
  padding: 5px 8px;
}

.header-logo-container {
  margin: auto;
  padding: 10px 20px 0;
  max-width: 500px;
}

.page-header {
  display: flex;
  align-items: center;
  margin: 20px;
}

.btn {
  font-size: var(--font-l);
  padding: 8px 16px;
  border-radius: 6px;
  border-width: 2px;
  border-style: solid;
  text-decoration: none;
  background-color: var(--button-bg);
  font-weight: 600;
  cursor: pointer;
  font-family: inherit;
  margin-right: 10px;
}

.btn:hover {
  background-color: var(--button-bg-hover);
}

.submit {
  color: var(--submit);
  border-color: var(--submit);
}

.secondary {
  color: var(--secondary);
  border-color: var(--secondary);
}

.warn {
  color: var(--warn);
  border-color: var(--warn);
}

.danger {
  color: var(--danger);
  border-color: var(--danger);
}

.page-header h1 {
  font-size: var(--font-xxl);
  margin: 0;
}

.page-header img {
  height: 40px;
  margin-left: 15px;
}

.page-header img:first-of-type {
  margin-left: 20px;
}

.page-content {
  font-size: var(--font-reg);
}

.usr-img {
  width: 100%;
  border-radius: var(--card-border-radius);
}

/* FORMS */

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

@media only screen and (min-width: 768px) {
  header {
    position: sticky;
    display: flex;
    flex-direction: row;
    top: 0;
    align-items: center;
  }

  main {
    max-width: 1300px;
    min-height: calc(100vh - 53px);
  }

  nav,
  .header-logo-container {
    margin: 10px 0;
    padding: 0 15px;
  }

  /* visual fix to help align logo */
  .header-logo-container {
    padding-top: 3px;
    width: 213px;
  }

  nav {
    margin-left: auto;
    display: flex;
    justify-content: center;
  }

  nav ul {
    flex-wrap: nowrap;
  }

  .page-header h1 {
    font-size: var(--font-xtreme);
  }

  .page-header img {
    height: 50px;
    margin-left: 20px;
  }

  .page-header img:first-of-type {
    margin-left: 25px;
  }

  @supports (-webkit-backdrop-filter: none) or (backdrop-filter: none) {
    header {
      background: var(--nav-bg);
      -webkit-backdrop-filter: blur(3px);
      backdrop-filter: blur(3px);
    }
  }
}

@media only screen and (min-width: 1024px) {
  main {
    min-height: calc(100vh - 55px);
  }

  header {
    width: calc(100vw - 40px);
    max-width: 1920px;
    top: 20px;
    background-color: transparent;
    border-bottom: none;
  }

  nav,
  .header-logo-container {
    margin: 0;
    background: var(--nav-bg-ff);
    border: var(--borders);
    border-radius: 18px;
  }

  nav {
    margin-left: auto;
  }

  .header-logo-container {
    /* visual fix to help align logo */
    padding-top: 6px;
    width: 256px;
    height: 35px;
  }

  @supports (-webkit-backdrop-filter: none) or (backdrop-filter: none) {
    header {
      -webkit-backdrop-filter: none;
      backdrop-filter: none;
    }

    nav,
    .header-logo-container {
      background: rgba(104, 197, 248, 0.6);
      -webkit-backdrop-filter: blur(3px);
      backdrop-filter: blur(3px);
    }
  }
}
```

### Check the Changes

From here we should be able to run our react/vite app: `npm run dev` and navigate to `localhost:5173` to ensure the changes updated. Your site should look like this:

![About page with CSS added](./assets/css-added.png)

## Lastly: Update Route Elements:
Our `Route` `element` properties are currently pointing to displaying <h2> elements instead of the actual pages we want it to display. So let's import the Page components and update our Routes to display them.


Currently:
`App.jsx` =>
```jsx
<Routes>
  <Route path="/*" element={<h2>Home Page</h2>} />
  <Route path="/about" element={<h2>About Page</h2>} />
</Routes>
```

Update:
`App.jsx` =>
```jsx
// top of App.jsx
import HomePage from '../HomePage';
import AboutPage from '../AboutPage';

// in return statement
<Routes>
  <Route path="/*" element={<HomePage />} />
  <Route path="/about" element={<AboutPage />} />
</Routes>
```

## About Page

Replace the entire contents of `about.html` with the following code:

`AboutPage.jsx`
```jsx
export default function AboutPage() {
    return (<>
        <h1>About the Cat Collector</h1>
        <hr />
        <p className="page-content">
          I like long romantic walks down the produce aisle. Also, I am currently job
          seeking!
        </p>
    </>)
}
```

**We will not have any specific styling added to the `AboutPage.jsx` file, so we will NOT import or create a styles.css => we can delete the file.**
