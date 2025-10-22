// IMPORTS
import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import { useParams, Link } from "react-router";

// ASSETS
import nerdCat from "../../assets/images/nerd-cat.svg";

// APIs
import * as catAPI from "../../utilities/cat-api";

export default function CatFormPage({ createCat, editCat, deleteCat }) {
    const initialState = { name: "", breed: "", description: "", age: "" }
    const [currCat, setCurrCat] = useState(null);
    const [formData, setFormData] = useState(initialState);
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        async function getAndSetDetail() {
            try {
                const cat = await catAPI.show(id);
                setCurrCat(cat);
                setFormData(cat)
            } catch (err) {
                console.log(err)
                setCurrCat(null)
                setFormData(initialState)
            }
        }
        if (editCat || deleteCat && id) getAndSetDetail()
    }, [id])

    function handleChange(evt) {
        const updatedData = { ...formData };
        setFormData({ ...updatedData, [evt.target.name]: evt.target.value })
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newCat = editCat ? await catAPI.update(formData, currCat.id) : await catAPI.create(formData);
            setFormData(initialState)
            navigate(`/cats/${newCat.id}`)
        } catch (err) {
            console.log(err)
        }
    }

    async function handleDelete(evt) {
        evt.preventDefault();
        const response = await catAPI.deleteCat(currCat.id)
        if (response.success) {
            setFormData(initialState)
            navigate("/cats");
        }
    }

    
    if (deleteCat && !currCat) return <h1>Loading</h1>    
    if (deleteCat && currCat)  return (<>
        <div className="page-header">
            <h1>Delete Cat?</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <h2>Are you sure you want to delete { currCat.name }?</h2>
        <form onSubmit={handleDelete}>
            <Link to={`/cats/${currCat.id}`} className="btn secondary">Cancel</Link>
            <button type="submit" className="btn danger">Yes - Delete!</button>
        </form>
    </>)

    if (editCat && !currCat)  return <h1>Loading</h1>
    if (createCat || editCat) return (<>
        <div className="page-header">
            {editCat ? <h1>Edit {currCat.name}'s Info</h1> : <h1>Add a Cat</h1>}
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                    {!editCat &&
                        <tr>
                            <th><label htmlFor="id_name">Name:</label></th>
                            <td><input value={formData.name} type="text" name="name" maxLength="100" required="" id="id_name" onChange={handleChange} /></td>
                        </tr>
                    }
                    <tr>
                        <th><label htmlFor="id_breed">Breed:</label></th>
                        <td><input value={formData.breed} type="text" name="breed" maxLength="100" required="" id="id_breed" onChange={handleChange} /></td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_description">Description:</label></th>
                        <td>
                            <textarea value={formData.description} name="description" cols="40" rows="10" maxLength="250" required="" id="id_description" onChange={handleChange}></textarea>
                        </td>
                    </tr>
                    <tr>
                        <th><label htmlFor="id_age">Age:</label></th>
                        <td><input value={formData.age} type="number" name="age" required="" id="id_age" onChange={handleChange} /></td>
                    </tr>
                </tbody>
            </table>
            <button type="submit" className="btn end submit">Submit!</button>
        </form>
    </>)
}