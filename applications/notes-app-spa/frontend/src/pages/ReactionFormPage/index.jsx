import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useParams, Link } from "react-router-dom";
import nerdCat from "../../assets/images/today-s-mood-277365833.webp";
import * as reactionAPI from "../../utilities/reactions-api";

export default function ReactionFormPage({ createReaction, editReaction, deleteReaction }) {
    const initialState = { emoji: "" };
    const [currReaction, setCurrReaction] = useState(null);
    const [formData, setFormData] = useState(initialState);
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        if ((editReaction && id) || (deleteReaction && id)) getAndSetDetail();
        async function getAndSetDetail() {
            try {
                const reactionDetail = await reactionAPI.show(id);
                setFormData({ emoji: reactionDetail.emoji });
                setCurrReaction(reactionDetail);
            } catch (err) {
                console.log(err);
                setFormData(initialState);
                setCurrReaction(null);
            }
        }
    }, [id]);

    function handleChange(evt) {
        const updatedData = { ...formData };
        setFormData({ ...updatedData, [evt.target.name]: evt.target.value });
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newReaction = editReaction
                ? await reactionAPI.update(currReaction.id, formData)
                : await reactionAPI.create(formData);
            setFormData(initialState);
            navigate(`/reactions/${newReaction.id}`);
        } catch (err) {
            console.log(err);
        }
    }

    async function handleDelete(evt) {
        try {
            evt.preventDefault();
            const response = await reactionAPI.deleteReaction(currReaction.id);
            if (response.success) {
                setFormData(initialState);
                navigate("/reactions");
            }
        } catch (err) {
            console.log(err);
        }
    }

    if (deleteReaction && !currReaction) return <h1>Loading...</h1>;
    if (deleteReaction && currReaction) return (
        <>
            <div className="page-header">
                <h1>Delete Reaction?</h1>
                <img src={nerdCat} alt="A cat using a computer" />
            </div>
            <h2>Are you sure you want to delete {currReaction.emoji}?</h2>
            <form onSubmit={handleDelete}>
                <Link to={`/reactions/${currReaction.id}`} className="btn secondary">Cancel</Link>
                <button type="submit" className="btn danger">Yes - Delete!</button>
            </form>
        </>
    );

    if (editReaction && !currReaction) return <h1>Loading...</h1>;
    if (createReaction || editReaction) return (
        <>
            <div className="page-header">
                {editReaction ? <h1>Edit Reaction</h1> : <h1>Add a Reaction</h1>}
                <img src={nerdCat} alt="A cat using a computer" />
            </div>
            <form className="form-container" onSubmit={handleSubmit}>
                <table>
                    <tbody>
                        <tr>
                            <th><label htmlFor="id_emoji">Emoji:</label></th>
                            <td>
                                <input
                                    value={formData.emoji}
                                    type="text"
                                    name="emoji"
                                    maxLength="10"
                                    required
                                    id="id_emoji"
                                    onChange={handleChange}
                                />
                            </td>
                        </tr>
                    </tbody>
                </table>
                <button type="submit" className="btn end submit">Submit!</button>
            </form>
        </>
    );
}
