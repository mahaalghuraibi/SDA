<h1>
  <span class="headline">React State Management</span>
  <span class="subhead">Updating Complex State</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to update arrays in the state while maintaining immutability using the `useState()` hook

## Working with arrays in state

So far, we've focused on updating a simple boolean value in the state. While toggling a boolean is straightforward and common, many real-world scenarios in React involve more complex state structures, like objects and arrays.

As applications become complex, you'll often find yourself managing these more robust data types. Therefore, it's important to understand how to update objects and arrays in state correctly.

Let's look at a more detailed example to illustrate this:

```jsx
import { useState } from 'react';

const ExampleComponent = () => {
  const [cats, setCats] = useState([
    { name: 'Myshka', breed: 'Ragdoll' },
    { name: 'Malta', breed: 'Turkish Angora' },
  ]);

  const addCat = (newCat) => {
    // spread current cats array and newCat object into a new array
    const newCatsArray = [...cats, newCat];
    // call state setter function with this new array
    setCats(newCatsArray);
  };

  return (
    <>
      <button onClick={() => addCat({ name: 'Kira', breed: 'Ragamuffin' })}>
        Add Cat
      </button>
      <ul>
        {cats.map((cat, idx) => (
          <li key={idx}> {cat.name} </li>
        ))}
      </ul>
    </>
  );
};

export default ExampleComponent
```

In this `ExampleComponent`, we're working with a state variable named `cats`, which is initialized as an array containing objects. Each object represents a cat, with properties like its name and breed.

This setup is a common pattern in React applications, where you manage a list of items as an array in your state.

To simplify our example and focus on the state management aspect, we're directly passing a new cat object to the `addCat()` function when the button is clicked.

In a more practical application, this data might come from a form input where users can add details of a new cat. However, we use hardcoded data here to demonstrate how the state updates with new items for our learning purposes.

Here's how it works: Upon clicking the button, `addCat()` is called with a predefined cat object. Inside `addCat()`, we use the spread operator `...` to create a new array containing all the existing cats and the new one.

This method ensures we're ***not modifying the original state directly*** but creating a brand new version of it shaped exactly how we want. This is a key practice in state management in React, which ensures smooth and predictable state updates.

```jsx
  const addCat = (newCat) => {
    // spread current cats array and newCat object into a new array
    const newCatsArray = [...cats, newCat];
    // call state setter function with this new array
    setCats(newCatsArray);
  };
```

After `setCats()` is invoked, React will determine if it should re-render based on a comparison between the old value of state and the new value of state.

If we didn't make a new array to pass to `setCats()` and instead just pushed the object into state directly, both the old value and the new value would point to the same array in memory. As a result, React would skip re-rendering, and the list of cats wouldn't change for the user. As you can imagine, this mismatch between the state of the app and the information rendered to the user is a big problem!

This is why we need to maintain immutability. Instead of mutating the array, we need to make a copy of the original array, make changes to that copy, and then replace the original with it!

Below is a more concise version of this pattern that you could also use here. This example and the above are functionally identical.

```jsx
  const addCat = (newCat) => {
    setCats([...cats, newCat]);
  };
```
