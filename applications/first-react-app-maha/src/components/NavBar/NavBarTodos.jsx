// src/components/Forms/TodoForm.jsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function TodoForm({ handleAddTodo }) {
  const navigate = useNavigate();

  const initialState = { text: "", amount: 0, done: false };
  const [newTodo, setNewTodo] = useState(initialState);

  function handleChange(e) {
    setNewTodo({ ...newTodo, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    handleAddTodo(newTodo);
    setNewTodo(initialState);
    navigate("/todos");
  }

  return (
    <>
      <h3>New Todo Text:</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="text"
          value={newTodo.text}
          onChange={handleChange}
          placeholder="Enter your todo text"
          required
        />
        <h3>New Todo Amount:</h3>
        <input
          type="number"
          name="amount"
          value={newTodo.amount}
          onChange={handleChange}
          placeholder="Enter amount"
          required
        />
        <br />
        <button type="submit">Submit your new todo!!</button>
      </form>
    </>
  );
}
