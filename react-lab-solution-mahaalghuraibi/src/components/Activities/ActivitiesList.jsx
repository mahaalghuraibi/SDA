import React from "react";
import "./ActivitiesList.css";

export default function ActivitiesList({ activities }) {
  if (activities.length === 0) {
    return <p className="muted">No activities yet</p>;
  }

  return (
    <ul className="activities-list">
      {activities.map((activity, i) => (
        <li key={i} className="activity-item">
          {activity}
        </li>
      ))}
    </ul>
  );
}
