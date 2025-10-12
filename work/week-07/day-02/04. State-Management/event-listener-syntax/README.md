<h1>
  <span class="headline">React State Management</span>
  <span class="subhead">Event Listener Syntax</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to respond to events with event handler functions.

## Event listeners

React lets you respond to events using built-in event handlers. These event handlers are passed custom functions that will be invoked in response to specific user actions.

In this lesson, we'll create a function that responds to button clicks. This function will display a message in the console, telling us which button was clicked. We'll use two buttons for this: one to represent 'Light Mode' and the other for 'Dark Mode'.

Later, we'll refactor these buttons to actually switch the app's design between light and dark modes. For now, let's focus on setting up the buttons and ensuring our function can identify which one is clicked.

Let's start by creating two buttons and a placeholder for our handler function. Add the new code for this in `App.jsx`:

```jsx
// src/App.jsx

import { useState } from 'react';
import './App.css';

const App = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  // placeholder function for handling mode changes
  // we'll implement the functionality in the next step
  const handleDarkMode = () => {
    // TODO: implement the logic to handle a user clicking the dark mode button
    console.log('Dark Mode!');
  };

  const handleLightMode = () => {
    // TODO: implement the logic to handle a user clicking the light mode button
    console.log('Light Mode!');
  };

  // add a new div with buttons inside
  // wrap both divs in a fragment
  return (
    <>
      <div className={isDarkMode ? 'dark' : 'light'}>
        <h1>Hello world!</h1>
      </div>
      <div>
        <button onClick={handleDarkMode}>Dark Mode</button>
        <button onClick={handleLightMode}>Light Mode</button>
      </div>
    </>
  );
};

export default App;
```

Conventionally, we attach a `handle` prefix to the name of event handler functions. Since these functions will eventually be responsible for toggling between the two modes, names like `handleDarkMode` and `handleLightMode` are fitting.

When one of our buttons is clicked, we want to log a message based on which button it was – 'Dark Mode!' for the dark button and 'Light Mode!' for the light button.

Test your buttons to make sure the correct mode is logged to the console. Nice job!

## Don't invoke event handler functions

In React, handling events in the UI looks similar to how it's done in HTML, but with a few key differences to keep in mind:

1. First, React events are always named using camelCase: `onClick`, `onSubmit`, etc.

2. Secondly, when you assign a function to an event handler in React, remember not to call the function directly. Since the JavaScript inside JSX brackets executes immediately during render, invoking the function when you pass it to the event handler will cause it to fire off without a click event!

Instead, we only want to pass the function as a reference, and React will call the function when the user clicks the element:

- ***Incorrect*** (function is invoked immediately)

  ```jsx
  <button onClick={handleDarkMode()}>Dark Mode</button>
  ```

- ***Correct*** (function is passed as a reference and will be called on click)

  ```jsx
  <button onClick={handleDarkMode}>Dark Mode</button>
  ```
