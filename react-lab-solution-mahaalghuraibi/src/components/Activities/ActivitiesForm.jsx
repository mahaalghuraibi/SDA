import React, { useState } from "react";
import "./ActivitiesForm.css";

export default function ActivitiesForm({ addActivity }) {
  const [activity, setActivity] = useState("");

  function handleSubmit(event) {
    event.preventDefault(); 
    addActivity(activity);  
    setActivity("");        
  }

  return (
    <form className="activity-form" onSubmit={handleSubmit}>
      <input
        type="text"
        value={activity}
        onChange={(event) => setActivity(event.target.value)}
        placeholder="Add activity"
      />
      <button type="submit">Add</button>
    </form>
  );
}
