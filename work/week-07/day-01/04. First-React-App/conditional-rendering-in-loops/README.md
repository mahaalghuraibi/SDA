<h1>
  <span class="headline">Building Your First React App</span>
  <span class="subhead">Conditional Rendering in Loops</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to use loops to create lists in React and apply conditions to change how each list item is displayed based on its data.

## Conditional rendering in loops

We've learned how to render data in JSX conditionally, loop over data, and transform it into JSX list elements. There may be times when you wish to do both - for example, let's say you want to iterate over `todos` and mark when a task is complete.

We can use `map()` to iterate over the `todos` data, transforming each element into an `<li>` element. Inside each `<li>`, we'll include the conditional rendering code we used earlier, attaching a prefix if `todo.done` is truthy. The result looks like the following:

```jsx
const App = () => {
  const todo = { text: 'A brand new task', done: true }
  const todos = [
    {text: 'Learn JavaScript', done: true},
    {text: 'Learn JSX', done: false},
    {text: 'Learn HTML', done: true},
    {text: 'Learn CSS', done: true},
    {text: 'Master React', done: false},
  ];

  return (
    <>
      <h1>JavaScript in JSX</h1>
      <p>{todo.text}</p>

      <h2>Conditional Rendering</h2>
      <p>{todo.done ? `Task Completed - ${todo.text}` : todo.text }</p>

      <h2>Looping with JSX</h2>
      <ul>
        {todos.map((todo, index) =>
          <li key={index}>
            {todo.text}
          </li>
        )}
      </ul>

      <h2>Looping and Conditional Rendering</h2>
      <ul>
        {todos.map((todo, index) => 
          <li key={index}>
            {todo.done ? `Task Completed - ${todo.text}` : todo.text}
          </li>
        )}
      </ul>
    </>
  );
}

export default App
```

Run the app and check the result!
