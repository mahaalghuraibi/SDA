import React, { useState } from 'react';
import WeatherForecast from './components/WeatherForecast/WeatherForecast';
import ActivitiesForm from './components/Activities/ActivitiesForm';
import ActivitiesList from './components/Activities/ActivitiesList';
import Activities from './components/Activities/Activities';
import { BrowserRouter, Routes, Route, Navigate, useParams } from "react-router";
import "./App.css";

const initialForecasts = [
  { day: 'Mon', img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/day.svg', imgAlt: 'sun icon', conditions: 'sunny', time: 'Morning' },
  { day: 'Tue', img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/night.svg', imgAlt: 'moon icon', conditions: 'clear', time: 'Night' },
  { day: 'Wed', img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/stormy.svg', imgAlt: 'clouds with lightning icon', conditions: 'stormy', time: 'All Day' },
  { day: 'Thu', img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/cloudy-day.svg', imgAlt: 'sun overcast by clouds icon', conditions: 'overcast', time: 'Evening' },
  { day: 'Fri', img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/cloudy-night.svg', imgAlt: 'moon overcast by clouds icon', conditions: 'cloudy', time: 'Night' },
];

export default function App() {

  const [forecasts, setForecasts] = useState(initialForecasts);
  const [visibleMap, setVisibleMap] = useState(Object.fromEntries(initialForecasts.map(f => [f.day, false])));
  const [activitiesByDay, setActivitiesByDay] = useState({}); // 

  function toggleDetails(day) {
    setVisibleMap(prev => ({ ...prev, [day]: !prev[day] }));
  }

  function removeForecast(day) {
    setForecasts(prev => prev.filter(f => f.day !== day));
    setVisibleMap(prev => {
      const copy = { ...prev };
      delete copy[day];
      return copy;
    });
  }

  const [activities, setActivities] = useState([]);

  function addActivity(newActivity) {
    const name = newActivity.trim();
    if (!name) return;
    if (activities.some(a => a.toLowerCase() === name.toLowerCase())) return;
    setActivities(prev => [...prev, name]);
  }

  // 
  function addDayActivity(dayKey, text) {
    const name = text.trim();
    if (!name) return;
    setActivitiesByDay(prev => {
      const list = prev[dayKey] || [];
      return { ...prev, [dayKey]: [...list, name] };
    });
  }

  // 
  function removeDayActivity(dayKey, index) {
    const list = activitiesByDay[dayKey] || [];
    const updatedList = [...list];
    updatedList.splice(index, 1);
    setActivitiesByDay({
      ...activitiesByDay,
      [dayKey]: updatedList,
    });
  }
//
  return (
    <BrowserRouter>
      <Routes>
      
        <Route
          path="/"
          element={
            <div className="app-wrapper">
              <h1>Local Weather</h1>

              <section className="activities-section">
                <h2>Activities</h2>
                <Activities
                  activities={activities}
                  addActivity={addActivity}
                />
              </section>

              <section className="forecast-list">
                {forecasts.map((f) => (
                  <WeatherForecast
                    key={f.day}
                    {...f}
                    isVisible={!!visibleMap[f.day]}
                    onToggle={() => toggleDetails(f.day)}
                    onRemove={() => removeForecast(f.day)}
                  />
                ))}
              </section>
            </div>
          }
        />

     
        <Route
          path="/day/:day"
          element={
            <DayRouteWrapper
              activitiesByDay={activitiesByDay}
              onAddActivity={addDayActivity}
              onRemoveActivity={removeDayActivity}
            />
          }
        />

        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
//
function DayRouteWrapper({ activitiesByDay, onAddActivity, onRemoveActivity }) {
  const { day } = useParams(); 
  const dayKey = String(day || "").trim();
  return (
    <DayPage
      dayKey={dayKey}
      activitiesByDay={activitiesByDay}
      onAddActivity={onAddActivity}
      onRemoveActivity={onRemoveActivity}
    />
  );
}

// 
function DayPage({ dayKey, activitiesByDay, onAddActivity, onRemoveActivity }) {
  const activities = activitiesByDay[dayKey] || [];

  function handleSubmit(e) {
    e.preventDefault();
    const form = new FormData(e.currentTarget);
    const text = form.get("activity")?.trim();
    if (text) onAddActivity(dayKey, text);
    e.currentTarget.reset();
  }

  return (
    <div className="p-4">
      <h2>Forecast for {dayKey || "Day"}</h2>

      <form onSubmit={handleSubmit} className="flex gap-2 mt-3">
        <input name="activity" placeholder="Add activity..." className="border p-2 flex-1" />
        <button type="submit" className="border px-3">Add</button>
      </form>

      <ul className="mt-4 list-disc pl-6">
        {activities.map((act, i) => (
          <li key={i} className="flex items-center gap-8">
            <span>{act}</span>
            <button onClick={() => onRemoveActivity(dayKey, i)} className="text-red-600">remove</button>
          </li>
        ))}
        {activities.length === 0 && <li>No activities yet.</li>}
      </ul>
    </div>
  );
}

