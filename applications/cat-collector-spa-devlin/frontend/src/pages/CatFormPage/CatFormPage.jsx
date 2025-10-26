import { useState, useEffect } from "react"
import { useNavigate, Link, useParams } from "react-router";
import nerdCat from "../../assets/images/nerd-cat.svg";
import * as catAPI from "../../utilities/cat-api";

export default function CatFormPage({ createCat, editCat, deleteCat }) {
    const initialState = { name: "", breed: "", description: "", age: 0 }
    const [formData, setFormData] = useState(initialState);
    const navigate = useNavigate();
    const { id } = useParams();
    const [currCat, setCurrCat] = useState(null);

      useEffect(() => {
        async function getCatDetail() {
          const catDetailData = await catAPI.detail(id);
          setCurrCat(catDetailData);
          setFormData(catDetailData);
        }
        if (editCat && id || deleteCat && id) getCatDetail()
      }, [id])


    function handleChange(evt) {
        const newFormData = { ...formData, [evt.target.name]: evt.target.value }
        setFormData(newFormData)
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newCat = editCat ? await catAPI.update(formData, currCat.id) : await catAPI.create(formData);
            setFormData(initialState);
            navigate(`/cats/${newCat.id}`);
        } catch (err) {
            console.log("Error creating new cat: ", err)
        }
    }

    async function handleDelete(evt) {
        evt.preventDefault()
        const res = await catAPI.deleteCat(currCat.id);
        if (res?.success) {
            navigate("/cats")
        } else {
            console.log(res)
            alert("There was an error in deleting the Cat - please contact admin.")
        }
    }

    if (deleteCat && !currCat) return <h1>Loading</h1> 
    if (deleteCat && currCat) 
    return (<>
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

    if (editCat && !currCat) return <h1>Loading</h1> 
    if (editCat || createCat)
    return (<>
        <div className="page-header">
            <h1>Add a Cat</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                    {!editCat &&
                        <tr>
                            <th><label htmlFor="id_name">Name:</label></th>
                            <td><input value={formData.name} type="text" name="name" maxLength="100" required id="id_name" onChange={handleChange} /></td>
                        </tr>
                    }
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
