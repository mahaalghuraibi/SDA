<img width="100%" src="https://i.imgur.com/7zglvQY.gif" />

# React Giphy Searcher
We are going to build a searchable interface for the [Giphy API](https://developers.giphy.com/) using React. 

# STEP 2 - React Routing

We will install react router, as usual, and generate routing account for the following:
 - `npm i react-router`
 - Home / Landing Page
 - Giphy Detail Page


1. Install React Router

With `react-router` installed, the next step is to set it up in our project.

We'll start by importing `BrowserRouter` in our entry file, (`src/main.jsx`). `BrowserRouter` is a component in React Router that enables navigation. It allows your app to update the URL and display different pages without reloading the whole page.

Add the following import to `src/main.jsx`:

```jsx
// src/main.jsx

import { BrowserRouter } from 'react-router';
```

Next, wrap the `<App />` component with `<BrowserRouter>`:

```jsx
// src/main.jsx

// Nest the App component inside the BrowserRouter component to enable routing:
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
```

2. Structure / Organize Application

We want to start organizing our information to set ourselves up for success. This means adding a `pages` folder and a `components` folder inside of `./src`.

We know that we will have the three following main app pages:
 - App (handles all routing / wraps the entire app)
 - LandingPage
 - GiphyDetailPage

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
│   ├── index.css
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
├── package-lock.json
├── postcss.config.js
└── vite.config.js
```

3. Setup our routes:
```jsx
// src/App.jsx
    <Routes>
      <Route path="/*" element={<h2>Home Page</h2>} />
      <Route path="/giphy/:id" element={<h3>This will display a giphy detail</h3>} />
    </Routes>
```

**don't forget to import Route and Routes from `react-router`:**
```jsx
import { Route, Routes } from 'react-router';
```

4. Create the pages and import the page-level components.

 - create the "landing page" and import in `app.jsx`
 - create the "detail page" and import in `app.jsx`

```jsx
export default function LandingPage() {
  return <h3>This is the landing page.</h3>
}
```


## Quick CSS Update:

Let's update our CSS slightly just to prep for later:

`index.css`:
```css
body {
  margin: 0;
  display: flex;
  min-width: 100vw;
  min-height: 100vh;
}
```

We are just updating the body of the applcication so we have our content starting at the top and page can expand the length and width.