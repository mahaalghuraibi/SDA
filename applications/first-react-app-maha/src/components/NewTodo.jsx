import { useState } from 'react';

const NewTodo = (props) => {
  const [newTodo, setNewTodo] = useState('');

  const handleChange = (e) => {
    setNewTodo(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    props.addTodo(newTodo);   // نرفع القيمة للأب
    setNewTodo('');           // نفرّغ الحقل بعد الإرسال
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="todoInput">Todo: </label>
      <input
        id="todoInput"
        name="todo"
        type="text"
        value={newTodo}
        onChange={handleChange}
      />
      <button type="submit">Create to-do</button>
    </form>
  );
};

export default NewTodo;
