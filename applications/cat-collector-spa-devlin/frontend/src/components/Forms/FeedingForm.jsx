import { useState } from "react"
import * as feedingAPI from "../../utilities/feeding-api";

export default function FeedingForm({ catDetail, catFeedings, setCatFeedings }) {
    const today = new Date().toISOString().slice(0, 10)
    const todaysFeedingCount = catFeedings.filter(feeding => new Date(feeding.date).toISOString().slice(0, 10) === today)
    const initialState = { meal: "B", date: today, cat: catDetail.id }
    const [formData, setFormData] = useState(initialState)

    function handleChange(evt) {
        setFormData({ ...formData, [evt.target.name]: evt.target.value })
    }

    async function handleSubmit(evt) {
        try {
            evt.preventDefault();
            const newFeeding = await feedingAPI.create(catDetail.id, formData);
            
            setCatFeedings([...catFeedings, newFeeding].sort((a, b) => new Date(b.date) - new Date(a.date)));
            setFormData(initialState)
        } catch (err) {
            console.log(err);
        }

    }

    return (
        <form className="form-container" onSubmit={handleSubmit}>
            { todaysFeedingCount.length >= 3
                ? <p className="fed">{catDetail.name} has been fed all their meals for today!</p>  
                : <p className="unfed">{catDetail.name} might be hungry!</p>
            }
            <p>
                <label htmlFor="id_date">Feeding date:</label>
                <input value={formData.date} type="date" name="date" placeholder="Select a date" onChange={handleChange} />
            </p>
            <p>
                <label htmlFor="id_meal">Meal:</label>
                <select value={formData.meal} name="meal" id="id_meal" onChange={handleChange} >
                    <option value="B">Breakfast</option>
                    <option value="L">Lunch</option>
                    <option value="D">Dinner</option>
                </select>
            </p>
            <button type="submit" className="btn submit">Add Feeding</button>
        </form>
    )
}
