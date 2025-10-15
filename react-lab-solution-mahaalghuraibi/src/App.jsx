import React, { useState } from 'react';
import WeatherForecast from './components/WeatherForecast/WeatherForecast';
import ActivitiesForm from './components/Activities/ActivitiesForm';
import ActivitiesList from './components/Activities/ActivitiesList';
import Activities from './components/Activities/Activities';

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

  //
  const [activities, setActivities] = useState([]);

  //
  function addActivity(newActivity) {
    const name = newActivity.trim();
    if (!name) return;
    if (activities.some(a => a.toLowerCase() === name.toLowerCase())) return;
    setActivities(prev => [...prev, name]);
  }

  return (
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
        {forecasts.map(f => (
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
  );
}
