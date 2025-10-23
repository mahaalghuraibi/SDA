// IMPORTS
import { useState } from "react";
import { useNavigate } from "react-router-dom";

// IMAGES
import moodImg from "../../assets/images/mood.jpg"; 

// APIs
import * as usersAPI from "../../utilities/users-api";

export default function SignupPage({ setUser }) {
    const navigate = useNavigate();
    const initialState = { username: "", password: "", confirmPassword: "", email: "" };
    const [formData, setFormData] = useState(initialState);
    const [errors, setErrors] = useState({ username: '', password: '', email: '', confirmPassword: '' });

    let disabledSubmitBtn = Object.values(errors).every(val => val === "") &&
        Object.values(formData).every(val => val !== "") ? false : true;

    function handleChange(evt) {
        setFormData({ ...formData, [evt.target.name]: evt.target.value });
        checkErrors(evt);
    }

    function checkErrors({ target }) {
        const updateErrors = { ...errors };

        if (target.name === 'username') {
            updateErrors.username = target.value.length < 3 ? 'Username must be at least 3 characters.' : "";
        }
        if (target.name === 'password') {
            updateErrors.password = target.value.length < 3 ? 'Password must be at least 3 characters.' : "";
        }
        if (target.name === 'confirmPassword') {
            updateErrors.confirmPassword = target.value !== formData.password ? 'Passwords must match.' : "";
        }
        if (target.name === 'email') {
            updateErrors.email = !target.value.includes("@") ? "Email must include '@' symbol." : "";
        }

        setErrors(updateErrors);
    }
    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const { username, email, password } = formData;  
            const newUser = await usersAPI.signup({ username, email, password });
            if (!newUser) return;                           
            setUser(newUser);
            setFormData(initialState);
            navigate("/notes");
        } catch (err) {
            console.log(err);
            setUser(null);
        }
    }


    return (
        <>
            <div className="page-header">
                <h1>Sign Up</h1>
                <img src={moodImg} alt="Mood Notes signup" />
            </div>
            <form onSubmit={handleSubmit} className="form-container signup">
                <table>
                    <tbody>
                        <tr>
                            <th><label>Username:</label></th>
                            <td>
                                <input type="text" value={formData.username} name="username" onChange={handleChange} />
                                {errors.username && <p>{errors.username}</p>}
                            </td>
                        </tr>
                        <tr>
                            <th><label>Email:</label></th>
                            <td>
                                <input type="text" value={formData.email} name="email" onChange={handleChange} />
                                {errors.email && <p>{errors.email}</p>}
                            </td>
                        </tr>
                        <tr>
                            <th><label>Password:</label></th>
                            <td>
                                <input type="password" value={formData.password} name="password" onChange={handleChange} />
                                {errors.password && <p>{errors.password}</p>}
                            </td>
                        </tr>
                        <tr>
                            <th><label>Confirm Password:</label></th>
                            <td>
                                <input type="password" value={formData.confirmPassword} name="confirmPassword" onChange={handleChange} />
                                {errors.confirmPassword && <p>{errors.confirmPassword}</p>}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <button type="submit" disabled={disabledSubmitBtn} className="btn submit">Submit!</button>
            </form>
        </>
    );
}
