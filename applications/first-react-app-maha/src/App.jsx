// src/App.jsx
import { useState } from 'react';
import './App.css';
import Navbar from './components/NavBar/NavBar.jsx';
import FounderListItem from './components/FounderListItem/FounderListItem.jsx';
import IncrementButton from './components/IncrementButton.jsx';

const App = () => {
  const navLinks = [
    { href: "/", text: "Home" },
    { href: "/about-us", text: "About Us" },
    { href: "/money-pit", text: "Investment Opportunities" },
    { href: "/the-fine-print", text: "Terms of Service" },
  ];

  const founders = [
    { name: "Elizabeth Holmes", title: "CEO", credential: "MBA from SuperLegit University", id: 1 },
    { name: "Sam Bankman-Fried", title: "CFO", credential: "CPA from TotallyReal State", id: 2 },
    { name: "Matt Damon", title: "CMO", credential: "Was in that movie you saw", id: 3 },
  ];

  const [mode, setMode] = useState('light');
  const handleMode = (modeValue) => setMode(modeValue);

  const [cats, setCats] = useState([
    { name: 'Myshka', breed: 'Ragdoll' },
    { name: 'Malta', breed: 'Turkish Angora' },
  ]);
  const addCat = (newCat) => setCats([...cats, newCat]);

  const [cityInput, setCityInput] = useState('');
  const handleCityChange = (event) => setCityInput(event.target.value);

  // ===== نموذج + تحقق =====
  const [title, setTitle] = useState('The full name will appear here.');
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    password: '',
    passwordConfirmation: '',
  });
  const [errors, setErrors] = useState({
    firstName: '',
    lastName: '',
    password: '',
    passwordConfirmation: '',
  });

  const checkErrors = ({ target }) => {
    if (target.name === 'firstName') {
      setErrors({
        ...errors,
        firstName:
          target.value.length < 3
            ? 'Your first name must be at least three characters long.'
            : '',
      });
    }
    if (target.name === 'lastName') {
      setErrors({
        ...errors,
        lastName:
          target.value.length < 2
            ? 'Your last name must be at least two characters long.'
            : '',
      });
    }
    if (target.name === 'password') {
      setErrors({
        ...errors,
        password:
          target.value.length < 6
            ? 'Your password must be at least six characters long.'
            : '',
        passwordConfirmation:
          formData.passwordConfirmation !== target.value
            ? 'The passwords do not match.'
            : '',
      });
    }
    if (target.name === 'passwordConfirmation') {
      setErrors({
        ...errors,
        passwordConfirmation:
          formData.password !== target.value
            ? 'The passwords do not match.'
            : '',
      });
    }
  };

  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
    checkErrors(event);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setTitle(`Your name is: ${formData.firstName} ${formData.lastName}`);
    setFormData({
      firstName: '',
      lastName: '',
      password: '',
      passwordConfirmation: '',
    });
    setErrors({
      firstName: '',
      lastName: '',
      password: '',
      passwordConfirmation: '',
    });
  };

  const formIsInvalid = Object.values(errors).some(Boolean);
  const formHasMissingData = !Object.values(formData).every(Boolean);
  // ========================

  // ===== عدّاد + رفع حالة عبر دالة تُمرَّر كـ prop =====
  const [count, setCount] = useState(0);
  const addOne = () => {
    setCount(count + 1);
    // أو أفضلية الأمان عند التحديث المتتالي:
    // setCount((c) => c + 1);
  };
  // =====================================================

  return (
    <>
      <div className={mode}>
        <Navbar links={navLinks} />

        <main>
          <h1>Welcome to Hyperbo.ly</h1>
          <h2>The future is firmly in front of us!</h2>
          <p>If you can't explain it to a fifth-grader, our product does it.</p>
        </main>

        <h2>Our Founders</h2>
        <ul>
          {founders.map((f) => (
            <FounderListItem key={f.id} {...f} />
          ))}
        </ul>

        <div style={{ marginTop: '2rem' }}>
          <button onClick={() => handleMode('light')}>Light Mode</button>
          <button onClick={() => handleMode('dark')}>Dark Mode</button>
          <button onClick={() => handleMode('neon')}>Neon Mode</button>
          <button onClick={() => handleMode('night')}>Night Mode</button>
        </div>

        {/* 🧮 عدّاد مع رفع الحالة عبر دالة تمر كـ prop */}
        <section style={{ marginTop: '2rem' }}>
          <h2>🧮 Counter Practice</h2>
          <p>Count: {count}</p>
          <IncrementButton addOne={addOne} />
        </section>

        {/* نموذج مع تحقق */}
        <section style={{ marginTop: '2rem' }}>
          <h2>{title}</h2>
          <form onSubmit={handleSubmit}>
            <div>
              <label htmlFor="firstName">First Name: </label>
              <input
                id="firstName"
                name="firstName"
                value={formData.firstName}
                onChange={handleChange}
              />
              {errors.firstName && <p className="error">{errors.firstName}</p>}
            </div>

            <div>
              <label htmlFor="lastName">Last Name: </label>
              <input
                id="lastName"
                name="lastName"
                value={formData.lastName}
                onChange={handleChange}
              />
              {errors.lastName && <p className="error">{errors.lastName}</p>}
            </div>

            <div>
              <label htmlFor="password">Password: </label>
              <input
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
              />
              {errors.password && <p className="error">{errors.password}</p>}
            </div>

            <div>
              <label htmlFor="passwordConfirmation">Password Confirmation: </label>
              <input
                type="password"
                id="passwordConfirmation"
                name="passwordConfirmation"
                value={formData.passwordConfirmation}
                onChange={handleChange}
              />
              {errors.passwordConfirmation && (
                <p className="error">{errors.passwordConfirmation}</p>
              )}
            </div>

            <button type="submit" disabled={formIsInvalid || formHasMissingData}>
              Submit
            </button>
          </form>
        </section>

        <section style={{ marginTop: '2rem' }}>
          <h2>🏙️ City</h2>
          <label htmlFor="cityInput">City: </label>
          <input
            id="cityInput"
            type="text"
            value={cityInput}
            onChange={handleCityChange}
          />
          <p style={{ marginTop: '0.5rem' }}>
            You typed: {cityInput || '—'}
          </p>
        </section>

        <section style={{ marginTop: '3rem' }}>
          <h2>🐱 My Cat List</h2>
          <button
            onClick={() => addCat({ name: 'Kira', breed: 'Ragamuffin' })}
            style={{ marginBottom: '1rem' }}
          >
            Add Cat
          </button>
          <ul>
            {cats.map((cat, index) => (
              <li key={index}>
                <strong>{cat.name}</strong> — {cat.breed}
              </li>
            ))}
          </ul>
        </section>
      </div>
    </>
  );
};

export default App;
