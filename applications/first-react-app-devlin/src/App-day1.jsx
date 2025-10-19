
import './App.css'
import Profile from './Profile';

function App() {

  const person = {
    "firstName": "Devlin",
    "lastName": "Booth",
    age: 50,
    old: true,
  }

  const todos = [
    { text: 'Learn JavaScript', done: true },
    { text: 'Learn JSX', done: false },
    { text: 'Learn HTML', done: true },
    { text: 'Learn CSS', done: true },
    { text: 'Master React', done: false },
  ];

  const todo = { text: 'Master React', done: false }

  const newTodos = todos.map((todo, idx) => (
    <ul key={idx}>
        <li>{todo.text}</li>
        <li>{todo.done ? `Task Completed - ${todo.text}` : todo.text}</li>
    </ul>
  ))

  return (<>
    <h1>This is the first react application</h1>
    <h1>Devlin is {person.age} old?</h1>
    <h3 style={{ color: `${person.old ? "red" : "yellow"}` }}>Is Devlin old? {person.old ? "yes" : "no"}</h3>
    {person.age === 49 && <h3>That is 50</h3>}
    {todo.done && <h3>{todo.text} is complete</h3>}
    <Profile />
    <p>{todo.text}</p>
    <h2>Conditional Rendering</h2>
    <p>{todo.done ? `Task Completed - ${todo.text}` : todo.text}</p>
    {todos.map((todo, idx) => (
      todo.done &&
      <ul key={idx}>
        <li>{todo.text}</li>
        <li>{todo.done ? `Task Completed - ${todo.text}` : todo.text}</li>
        {todo.done && <li>`Task Completed - ${todo.text}`</li>}
      </ul>
    ))}
    <h1>NEW TODOS BELOW</h1>
    {newTodos}
    <h1>NEW TODOS BELOW THREE</h1>
    {todos.map((todo, idx) => (
      todo.done ?
      <ul key={idx}>
        <li>{todo.text}</li>
        {/* <li>{todo.done ? `Task Completed - ${todo.text}` : todo.text}</li> */}
        {todo.done && <li>Task Completed - ${todo.text}</li>}
      </ul>
      :
      <h3>{todo.text} not done!!!!</h3>
    ))}
  </>)
}

export default App
