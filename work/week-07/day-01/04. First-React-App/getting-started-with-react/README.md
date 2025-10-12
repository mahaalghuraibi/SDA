<h1>
  <span class="headline">Building Your First React App</span>
  <span class="subhead">Getting Started with React</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to explore the React file structure created by Vite, and start the development server.

## Getting started with React

You just built your first React app! Congrats! We used a tool called [Vite](https://vite.dev/guide/) to help accomplish this. Here's how they describe it in their own words:

> 💡 Vite (French word for "quick", pronounced like "veet") is a build tool that aims to provide a faster and leaner development experience for modern web projects.

Build tools accomplish a lot, but in brief, Vite gives us a couple of essential capabilities:

- A starting file structure with sensible defaults.
- A development server that serves our application locally.

## Default file structure

This section provides a high-level overview of the React app's file structure. Don't worry about the specifics here. The important thing to note is the three most essential files created by Vite initially: `index.html`, `App.jsx`, and `main.jsx`. Let's explore how these files interact.

The entry point into our application is the `index.html` file located at the root of our project. You can see its contents below:

```html
<!-- index.html -->

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

The `index.html` file represents the entirety of the HTML we deliver to users of this application. It has some familiar boilerplate and two elements in the body - a `<div>` with an `id` of `"root"` and a `<script>` that calls the `src/main.jsx` file. Let's check out our JSX file:

```jsx
// src/main.jsx

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

In our `index.html`, Vite created a `<div>` with an id of `"root"`. This HTML element is important because it establishes the root of our React application, as shown in this line:

```jsx
createRoot(document.getElementById('root'))
```

Passing the DOM element to `createRoot()` means React will use that element as the root. React calls this a "root DOM node" because React DOM manages everything inside it. Our app will exist inside this element; nothing but React should interact with anything inside it.

The element we designate as the root has methods such as `render()`, which allow us to display rendered React content. This means we can pass React components to `root.render()` like so:

```jsx
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

The React `root` is now rendering a single `App` component (ignore the `StrictMode` component for now), which is being imported from `src/App.jsx`:

```jsx
// src/App.jsx

const App = () => {

  return (
    <h1>Hello world!</h1>
  );
};

export default App;
```

You can begin to see how this app's pieces interact with one another. The `index.html` file loads the `main.jsx` file as the entry point to our React application, which itself renders the `App` component.

![Entry point](./assets/react-entry-point-v1.png)

## Running the development server

To start the development server and view our app in the browser, we'll use the following command:

```bash
npm run dev
```

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
```

Navigate there, and you should see the `<h1>` from our `App.jsx` component displayed!

## Other files

Vite created a few other files and directories for us when we created this project. Some may be familiar to you, while others will not. In the project root, we have:

- `public` directory - for holding static files, such as images, served by your HTML.
- `.eslintrc.cjs` - for syntax highlighting to inform you of warnings or errors.
- `.gitignore` - ensures we don't send environment details to GitHub.
- `vite.config.js` - for configuring the Vite app.

You don't need to worry about the contents of these files for now, but they will be helpful down the road as you go on your React journey.
