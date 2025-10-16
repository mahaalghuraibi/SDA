const TodoList = ({ todos }) => {
  if (todos.length === 0) return <p>No todos yet.</p>;

  return (
    <ul>
      {todos.map((t) => (
        <li key={t.id}>{t.text}</li>
      ))}
    </ul>
  );
};

export default TodoList;
