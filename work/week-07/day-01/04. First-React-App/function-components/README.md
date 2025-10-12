<h1>
  <span class="headline">Building Your First React App</span>
  <span class="subhead">Function Components</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to create and export function components in React.

## Function components

React components are essentially JavaScript functions that combine markup, CSS, and JavaScript into reusable UI elements. When crafting larger applications, React's approach to components allows us to write significantly more manageable code.

We've already created the `App.jsx` function component, but let's take a step back and break down the process of creating a new component from scratch using `App` as our example.

### Step 1: Define the function

The first step when creating a function component is to define the function. React function components are composed the same way as normal JavaScript functions:

```jsx
// src/App.jsx

const App = () => {

};
```

> 🧠 From the React Docs: 'React components are regular JavaScript functions, but their names must start with a capital letter, or they won't work!'

### Step 2: Add markup

Next, we add the markup inside the function's `return` statement. Here we have an `<h1>` element with the text content `Hello, world!`.

```jsx
// src/App.jsx

const App = () => {
  
  return (
    <h1>Hello, world!</h1>
  );
};
```

> 🧠 Markup inside of the `return` statement is what will be displayed to the user.

Note that the markup we add goes inside of a `return`. It is also surrounded by `( )` because we've split what will be returned across multiple lines. Without the parenthesis, code on the lines after the `return` would be ignored.

### Step 3: Export the function

React uses [ES Module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) syntax to import and export files. `export default` allows us to denote a main function in a file to export, which can then be imported into other files.

```jsx
// src/App.jsx

const App = () => {
  
  return (
    <h1>Hello world!</h1>
  );
};

export default App;
```

### Step 4: Importing/using the component

With the component exported, we can now use it anywhere in our application. Vite has already imported it in the `src/main.jsx` file, let's check it out:

```jsx
// src/main.jsx

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
// we import the default export from App.jsx
// we can name the function whatever we want here, so we'll call it App
import App from './App.jsx'

// we then use the component below. Note that the tag is self-closing
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```
