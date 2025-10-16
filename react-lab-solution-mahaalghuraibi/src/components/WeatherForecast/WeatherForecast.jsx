import React from "react";
import { Link } from "react-router"; // 
import './WeatherForecast.css'

export default function WeatherForecast({ day, img, imgAlt, conditions, time, isVisible, onToggle, onRemove }) {
  return (
    <article className={`weather ${conditions}`}>
      // 
      <header className="weather-header" onClick={onToggle}>
        <Link to={`/day/${day}`} className="day-link">
          <h2>{day}</h2>
        </Link>
        <img src={img} alt={imgAlt} />
      </header>

      <div className={`details ${isVisible ? 'visible' : 'hidden'}`}>
        <p><span>conditions:</span> {conditions}</p>
        <p><span>time:</span> {time}</p>
      </div>

      <button className="remove-btn" onClick={onRemove}>Remove</button>
    </article>
  );
}
