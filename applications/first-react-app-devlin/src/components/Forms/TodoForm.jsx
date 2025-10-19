import { useState } from "react"
import { useNavigate } from "react-router"

export default function TodoForm({ handleAddTodo }) {
    // const [cityInput, setCityInput] = useState("Dallas")
    const navigate = useNavigate();

    const initialState = {
        text: "",
        amount: 0,
        done: false
    }
    const [newTodo, setNewTodo] = useState(initialState)

    function handleChange(evt) {
        const updatedTodo = { ...newTodo, [evt.target.name]: evt.target.value }
        setNewTodo(updatedTodo)
    }

    function handleSubmit(evt) {
        evt.preventDefault();
        handleAddTodo(newTodo);
        setNewTodo(initialState)
    }

    return (
        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", justifyContent: "center" }}>
            {/* <label htmlFor="cityInput">City: </label>
            <input id="cityInput" name="cityInput" type="text" value={cityInput} onChange={(evt) => setCityInput(evt.target.value)}/> */}
            <label htmlFor="todoText">New Todo Text: </label>
            <input id="todoText" name="text" type="text" value={newTodo.text} onChange={handleChange} />
            <label htmlFor="todoAmount">New Todo Amount: </label>
            <input id="todoAmount" name="amount" type="number" value={newTodo.amount} onChange={handleChange} />
            <button type="submit">Submit your new todo!!</button>
        </form>
    )
}
