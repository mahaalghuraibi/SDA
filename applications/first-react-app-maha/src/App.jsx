import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Profile from "./Profile";

function App() {
  const person = {
    firstName: "Maha",
    age: 25,
    old: true,
  };

  return (
    <div>
      <h1>This is the first React application</h1>
      <h1>{person.firstName} is {person.age} years old</h1>

      <h3 style={{ color: person.old ? "red" : "yellow" }}>
        Is {person.firstName} old? {person.age > 20 ? "Yes" : "No"}
      </h3>

      {person.age === 50 && <h3>That is 50</h3>}
    </div>
  );
}

export default App;
