import { useState } from "react";
import * as feedingAPI from "../../utilities/feedings-api";

export default function FeedingForm({ catDetail, catFeedings, setCatFeedings }) {
  const today = new Date().toISOString().slice(0, 10);
  const initialState = { date: today, meal: "B", cat: catDetail.id };
  const [formData, setFormData] = useState(initialState);

  function handleChange(evt) {
    const updatedData = { ...formData, [evt.target.name]: evt.target.value };
    setFormData(updatedData);
  }

  async function handleSubmit(evt) {
    try {
      evt.preventDefault();
      const updatedFeedings = await feedingAPI.create(formData, catDetail.id);
      setCatFeedings(updatedFeedings);
      setFormData(initialState);
    } catch (err) {
      console.log(err);
      setCatFeedings([...catFeedings]);
    }
  }

  const todaysFeedingCount = catDetail.feedings
    ? catDetail.feedings.filter(
        (feeding) =>
          new Date(feeding.date).toISOString().slice(0, 10) === today
      )
    : [];

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      {todaysFeedingCount.length >= 3 ? (
        <p className="fed">
          {catDetail.name} has been fed all their meals for today!
        </p>
      ) : (
        <p className="unfed">{catDetail.name} might be hungry!</p>
      )}

      <p>
        <label htmlFor="id_date">Feeding date:</label>
        <input
          value={formData.date}
          type="date"
          name="date"
          placeholder="Select a date"
          onChange={handleChange}
        />
      </p>

      <p>
        <label htmlFor="id_meal">Meal:</label>
        <select
          value={formData.meal}
          name="meal"
          id="id_meal"
          onChange={handleChange}
        >
          <option value="B">Breakfast</option>
          <option value="L">Lunch</option>
          <option value="D">Dinner</option>
        </select>
      </p>

      <button type="submit" className="btn submit">
        Add Feeding
      </button>
    </form>
  );
}

