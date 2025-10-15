import React from "react";
import ActivitiesForm from "./ActivitiesForm";
import ActivitiesList from "./ActivitiesList";

export default function Activities({ activities, addActivity }) {
  return (
    <>
      <ActivitiesForm addActivity={addActivity} />
      <ActivitiesList activities={activities} />
    </>
  );
}
