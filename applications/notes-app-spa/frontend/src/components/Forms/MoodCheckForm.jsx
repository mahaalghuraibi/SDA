import { useState } from "react";
import * as moodchecksAPI from "../../utilities/moodchecks-api";

export default function MoodCheckForm({ noteDetail, moodChecks, setMoodChecks }) {
  const today = new Date().toISOString().slice(0, 10);
  const initialState = { date: today, period: "M", note: noteDetail.id };
  const [formData, setFormData] = useState(initialState);

  const todaysMoodCount = moodChecks.filter(
    (check) => new Date(check.date).toISOString().slice(0, 10) === today
  );

  function handleChange(e) {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const updatedMoodChecks = await moodchecksAPI.create(formData, noteDetail.id);
      setMoodChecks(updatedMoodChecks);
      setFormData(initialState);
    } catch (err) {
      console.log(err);
      setMoodChecks([...moodChecks]);
    }
  }

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      {todaysMoodCount.length >= 3 ? (
        <p className="fed">😊 {noteDetail.title} has been checked for all moods today!</p>
      ) : (
        <p className="unfed">😟 {noteDetail.title} still needs more mood checks today!</p>
      )}

      <p>
        <label htmlFor="id_date">Mood date:</label>
        <input
          value={formData.date}
          type="date"
          name="date"
          placeholder="Select a date"
          onChange={handleChange}
        />
      </p>
      <p>
        <label htmlFor="id_period">Period:</label>
        <select
          value={formData.period}
          name="period"
          id="id_period"
          onChange={handleChange}
        >
          <option value="M">Morning</option>
          <option value="A">Afternoon</option>
          <option value="N">Night</option>
        </select>
      </p>
      <button type="submit" className="btn submit">
        Add Mood Check
      </button>
    </form>
  );
}
