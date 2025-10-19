import { useState, useEffect } from "react";
import { useParams } from "react-router"

export default function DisplayDetail({ todos }) {
    const [todoDetail, setTodoDetail] = useState(null)
    const { todoId } = useParams();

    useEffect(function() {
        if (!todoId) return 
        const currTodo = todos[todoId];
        setTodoDetail(currTodo)
    }, [todoId])

    if (!todoDetail) return (<h1>Display Todo Detail Coming Soon</h1>)

    return (
        <ul style={{ border: "1px solid red", paddingRight: "10px" }}>
            <li>Text: {todoDetail.text}</li>
            <li>Amount: {todoDetail.amount}</li>
            <li>Done: {todoDetail.done ? "Completed" : "Incomplete"}</li>
        </ul>
    )
}
