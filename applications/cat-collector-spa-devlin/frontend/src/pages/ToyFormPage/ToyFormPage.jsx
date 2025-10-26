import { useState, useEffect } from "react"
import { useNavigate, Link, useParams } from "react-router";
import nerdCat from "../../assets/images/nerd-cat.svg";
import * as toyAPI from "../../utilities/toy-api";

export default function ToyFormPage({ createToy, editToy, deleteToy }) {
    const initialState = { name: "", color: "#ff0000" }
    const [formData, setFormData] = useState(initialState);
    const navigate = useNavigate();
    const { id } = useParams();
    const [currToy, setCurrToy] = useState(null);

      useEffect(() => {
        async function getToyDetail() {
          const toyDetailData = await toyAPI.detail(id);
          setCurrToy(toyDetailData);
          setFormData(toyDetailData);
        }
        if (editToy && id || deleteToy && id) getToyDetail()
      }, [id])


    function handleChange(evt) {
        const newFormData = { ...formData, [evt.target.name]: evt.target.value }
        setFormData(newFormData)
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newToy = editToy ? await toyAPI.update(formData, currToy.id) : await toyAPI.create(formData);
            console.log(newToy, "toy form page 32")
            setFormData(initialState);
            navigate(`/toys/${newToy.id}`);
        } catch (err) {
            console.log("Error creating new toy: ", err)
        }
    }

    async function handleDelete(evt) {
        evt.preventDefault()
        const res = await toyAPI.deleteToy(currToy.id);
        if (res?.success) {
            navigate("/toys")
        } else {
            console.log(res)
            alert("There was an error in deleting the Toy - please contact admin.")
        }
    }

    if (deleteToy && !currToy) return <h1>Loading</h1> 
    if (deleteToy && currToy) 
    return (<>
        <div className="page-header">
            <h1>Delete Toy?</h1>
            <img src={nerdCat} alt="A cat using a computer" />
        </div>
        <h2>Are you sure you want to delete { currToy.name }?</h2>
        <form onSubmit={handleDelete}>
            <Link to={`/toys/${currToy.id}`} className="btn secondary">Cancel</Link>
            <button type="submit" className="btn danger">Yes - Delete!</button>
        </form>
    </>)

    if (editToy && !currToy) return <h1>Loading</h1> 
    if (editToy || createToy)
    return (<>
        <div className="page-header">
            <h1>Add a Toy</h1>
            <img src={nerdCat} alt="A toy using a computer" />
        </div>
        <form className="form-container" onSubmit={handleSubmit}>
            <table>
                <tbody>
                    {!editToy &&
                        <tr>
                            <th><label htmlFor="id_name">Name:</label></th>
                            <td><input value={formData.name} type="text" name="name" maxLength="50" required id="id_name" onChange={handleChange} /></td>
                        </tr>
                    }
                    <tr>
                        <th><label htmlFor="id_color">Color:</label></th>
                        <td><input value={formData.color} type="color" name="color" maxLength="20" required id="id_color" onChange={handleChange} /></td>
                    </tr>
                </tbody>
            </table>
            <button type="submit" className="btn end submit">Submit!</button>
        </form>
    </>)

}
