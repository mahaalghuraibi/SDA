import "./styles.css";
import { useState } from "react";
import { useNavigate } from "react-router";
import catCollectorCat from "../../assets/images/splash.svg";
import logoType from "../../assets/images/logotype.svg";
import * as usersAPI from "../../utilities/users-api";

export default function HomePage({ user, setUser }) {
  const initialState = { username: "", password: "" };
  const [formData, setFormData] = useState(initialState);
  const navigate = useNavigate();

  function handleChange(evt) {
    setFormData({ ...formData, [evt.target.name]: evt.target.value });
  }

  async function handleSubmit(evt) {
    evt.preventDefault();
    const userData = await usersAPI.login(formData);
    setUser(userData);
    setFormData(initialState)
    if (userData) navigate("/cats")
  }

  return (<>
    <section className="logo-container">
      <div className="home-cat-container">
        <img src={catCollectorCat} alt="The Cat Collector Cat" />
      </div>
      <img src={logoType} alt="Text reads: Cat Collector" />
    </section>
    {!user && 
      <section>
        <form onSubmit={handleSubmit} className="form-container login">
          <p>
            <label htmlFor="id_username">Username:</label>
            <input value={formData.username} id="id_username" required maxLength="50" name="username" type="text" onChange={handleChange} />
          </p>
          <p>
            <label htmlFor="id_password">Password</label>
            <input value={formData.password} id="id_password" required name="password" type="password" onChange={handleChange} />
          </p>
          <button type="submit" className="btn submit">Login</button>
        </form>
      </section>
    }
  </>)
}