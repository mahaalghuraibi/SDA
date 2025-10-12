<h1>
  <span class="headline">React State Management</span>
  <span class="subhead">Refactoring State</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to refactor a React component's state to handle multiple modes using a string-based state variable.

## Flexible state management

In the previous lesson, we toggled between light and dark modes using a `boolean` state. However, real-world applications often require more versatile state management. Let's refactor our component to use a string-based state accommodating multiple modes or themes.

## Refactor the state variable

First, we'll change our state from a ***boolean*** to a ***string***. This will allow us to store different mode values, such as our current 'light' or 'dark', and add more like 'neon', 'night', or others.

Update the following in `App.jsx`:

```jsx
// src/App.jsx

const App = () => {
  const [mode, setMode] = useState('light');

  // Rest of the component
};
```

## Consolidating the handler functions

We can also make our code easier to manage and use a single handler function to set state. Instead of setting the state to `true` or `false`, it will now set the mode state to a passed in `modeValue` string:

```jsx
// src/App.jsx

  const handleMode = (modeValue) => {
    console.log(modeValue);
    setMode(modeValue);
  };
```

The refactored `handleMode()` function can handle any mode string passed to it. This versatility makes it easy to add new modes without modifying the function's logic. You can call `handleMode('light')`, `handleMode('night')`, or any other mode string, and the function will work seamlessly.

As new modes are introduced, you don't need to revisit this function to make updates, making it more maintainable.

With the `handleMode()` handler function in place you can now remove the `handleLightMode()` and `handleDarkMode()` functions

> 💡 We could have used a single handler function when our state was a boolean value as well, we only split it up to demonstrate the simplest possible event handler syntax possible before introducing this more concise method.

### Potential pitfalls

The function assumes that the passed string is a valid mode. If an invalid string is passed, it might lead to unexpected behaviors or a broken UI. For example, if `handleMode('unknown')` is called, the app might apply a non-existent CSS class.

Depending on how complex this state becomes, it may be necessary to add validation logic to ensure the passed-in string has a corresponding CSS class before using it to set state.

## Update the event handlers on buttons

Now, we'll update the buttons' `onClick` handlers to pass the respective mode string.

Normally, when you use `onClick={handleMode}`, you're telling React to call the `handleMode()` function when the event occurs. However, if you need to pass an argument to `handleMode()`, like `'dark'` or `'light'`, you can't just write `onClick={handleMode('dark')}`. This would call the function immediately when the component renders, not when the button is clicked.

To ensure that `handleMode()` is called with an argument only after the click event, we wrap it inside an *anonymous function*. The arrow function `() =>` doesn't execute right away; it only runs when the button is clicked.

```jsx
// src/App.jsx
      <div>
        <button onClick={() => handleMode('dark')}>Dark Mode</button>
        <button onClick={() => handleMode('light')}>Light Mode</button>
      </div>
```

Inside the anonymous function, you can then call `handleMode('dark')`. This way, the `handleMode()` function gets called with the correct parameter, but only in response to the click event.

You can now add additional buttons that pass in their own unique theme names. Don't forget to add the new themes to your CSS file!

## Apply the mode to the component

Let's refactor the new `mode` state to dynamically set the class for your component.

```jsx
// src/App.jsx

      <div className={mode}>
        <h1>Hello world!</h1>
      </div>
```

## Final app component

Your final refactor in `App.jsx` should look something like this:

```jsx
// src/App.js

import { useState } from 'react';
import './App.css';

const App = () => {
  const [mode, setMode] = useState('light');

  const handleMode = (modeValue) => {
    setMode(modeValue);
  };

  return (
    <>
      <div className={mode}>
        <h1>Hello world!</h1>
      </div>
      <div>
        <button onClick={() => handleMode('dark')}>Dark Mode</button>
        <button onClick={() => handleMode('light')}>Light Mode</button>
      </div>
    </>
  );
};

export default App;
```

Great work!

## 🎓 You Do

Add new themes!

Use the following CSS classes to add two new themes to your application.

Build two new buttons that will apply these themes.

```css
.neon {
  background-color: #0f0f0f; /* Dark background */
  color: #39ff14; /* Bright neon green text */
  border: 3px solid #39ff14; /* Neon green border */
  text-shadow: 0 0 5px #39ff14; /* Glowing text effect */
}
```

```css
.night {
  background-color: #1a1a2e; /* Deep blue night sky background */
  color: #e0e0e0; /* Soft white text for readability */
  border: 2px solid #0f3460; /* Dark blue border for depth */
}
```
