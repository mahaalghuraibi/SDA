// src/Day03.jsx
import NavBarTodos from "./components/NavBar/NavBarTodos";
import TodoForm from "./components/Forms/TodoForm";
import DisplayTodos from "./components/DisplayTodos/DisplayTodos";
import { Routes, Route } from "react-router-dom";
import { useState } from "react";

const App = () => {
  const [todos, setTodos] = useState([]);
  function handleAddTodo(todo) {
    setTodos(prev => [...prev, todo]);
  }

  return (
    <>
      <NavBarTodos />
      <h1>Day 03</h1>

      <Routes>
        <Route path="/" element={<h1>Home Page</h1>} />
        <Route path="/todo/new" element={<TodoForm handleAddTodo={handleAddTodo} />} />
        <Route path="/todos" element={<DisplayTodos todos={todos} />} />
      </Routes>
    </>
  );
};

export default App;
