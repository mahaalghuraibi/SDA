// IMPORTS
import "./styles.css";
import { useState } from "react";
import { useNavigate } from "react-router";
import nerdCat from "../../assets/images/nerd-cat.svg";

// APIs
import * as catAPI from "../../utilities/cat-api";

export default function CatFormPage() {
    const initialState = { name: "", breed: "", description: "", age: "" }
    const [formData, setFormData] = useState(initialState);
    const navigate = useNavigate();

    function handleChange(evt) {
      const updatedData = { ...formData };
      setFormData({ ...updatedData, [evt.target.name]: evt.target.value })
    }

    async function handleSubmit(evt) {
      try {
        evt.preventDefault();
        const newCat = await catAPI.create(formData);
        setFormData(initialState)
        navigate(`/cats/${newCat.id}`)
      } catch (err) {
        console.log(err);
      }
    }

    return (<>
        <div className="page-header">
            <h1>Add a Cat</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                    <tr>
                        <th><label htmlFor="id_name">Name:</label></th>
                        <td><input value={formData.name} type="text" name="name" maxLength="100" required id="id_name" onChange={handleChange} /></td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_breed">Breed:</label></th>
                        <td><input value={formData.breed} type="text" name="breed" maxLength="100" required id="id_breed" onChange={handleChange} /></td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_description">Description:</label></th>
                        <td>
                            <textarea value={formData.description} name="description" cols="40" rows="10" maxLength="250" required id="id_description" onChange={handleChange}></textarea>
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_age">Age:</label></th>
                        <td><input value={formData.age} type="number" name="age" required id="id_age" onChange={handleChange}/></td>
                    </tr>
                </tbody>
            </table>
            <button type="submit" className="btn end submit">Submit!</button>
        </form>
    </>)
}
