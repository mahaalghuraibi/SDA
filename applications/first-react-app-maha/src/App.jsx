import { useState } from 'react';

const App = () => {
  const [title, setTitle] = useState('The full name will appear here.');
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <>
      <h2>{title}</h2>

      <form>
        <label htmlFor="firstName">First Name: </label>
        <input
          id="firstName"
          name="firstName"
          value={formData.firstName}
          onChange={handleChange}
        />

        <label htmlFor="lastName"> Last Name: </label>
        <input
          id="lastName"
          name="lastName"
          value={formData.lastName}
          onChange={handleChange}
        />
      </form>

      <button
        type="button"
        onClick={() =>
          setTitle(`${formData.firstName} ${formData.lastName}`.trim())
        }
      >
        Show Full Name
      </button>
    </>
  );
};

export default App;
