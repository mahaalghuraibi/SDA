import "./styles.css";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg";
import logoType from "../../assets/images/today-s-mood-277365833.webp";
import * as usersAPI from "../../utilities/users-api";

export default function HomePage({ user, setUser }) {
  const navigate = useNavigate();
  const initialState = { username: "", password: "" };
  const [formData, setFormData] = useState(initialState);

  function handleChange(evt) {
    setFormData({ ...formData, [evt.target.name]: evt.target.value });
  }

  async function handleLogin(evt) {
    try {
      evt.preventDefault();
      const loggedInUser = await usersAPI.login(formData);
      setUser(loggedInUser);
      navigate("/notes");
    } catch (err) {
      setUser(null);
    }
  }

  return (
    <>
      <section className="logo-container">
        <div className="home-mood-container">
          <img src={moodImg} alt="Mood Notes Main" />
        </div>
        <img src={logoType} alt="Text reads: Mood Notes" />
      </section>

      {!user && (
        <section>
          <form onSubmit={handleLogin} className="form-container login">
            <h1>Login</h1>
            <p>
              <label htmlFor="id_username">Username:</label>
              <input
                value={formData.username}
                type="text"
                name="username"
                maxLength="150"
                required
                id="id_username"
                onChange={handleChange}
              />
            </p>
            <p>
              <label htmlFor="id_password">Password:</label>
              <input
                value={formData.password}
                type="password"
                name="password"
                required
                id="id_password"
                onChange={handleChange}
              />
            </p>
            <button type="submit" className="btn submit">Login</button>
          </form>
        </section>
      )}
    </>
  );
}
