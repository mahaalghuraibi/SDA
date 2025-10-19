import { Link } from "react-router"

export default function DisplayTodos({ todos }) {
  // const { text, amount, done } = todo;

  return (
    <>
      {todos.length > 0 ?
        todos.map((todo, idx) => (
        <Link to={`/todos/${idx}`} key={idx}>
          <ul  style={{ border: "1px solid red", paddingRight: "10px" }}>
            <li>Text: {todo.text}</li>
            <li>Amount: {todo.amount}</li>
            <li>Done: {todo.done ? "Completed" : "Incomplete"}</li>
          </ul>
        </Link>
        ))
        : <h3>Please add a todo!!</h3>
      }
    </>
  )
}
