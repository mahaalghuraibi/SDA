<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# REACT LABS
Each react lab will build on the previous lab by adding to the same application that you will build in your `SDA-Ghazal/applications/react_labs`. We will do this for two reasons...

1. React applications can take up quite a bit of space on your computers and take time to build from the ground up.

2. You are more likely to build on one idea than you are to continuously create new applications over and over again. best to get the experience of continuing to build on one idea and seeing how code can be organized to help make projects easier to build and expand upon.

## About

Welcome to Reactville, a constantly evolving virtual metropolis. Let's build this digital town together, one component at a time.

![Reactville Skyline](./assets/Reactville.png)

Reactville Weather Station is at the heart of the town, keeping everyone informed about the ever-changing weather. They're in need of a tech upgrade and have called on you to develop their new 5-Day Weather Forecast App. 

## First React Lab

Today, your job is to build a weather forecast page that **re-uses a single component** to display multiple days' worth of weather forecasts.

## Setup

In this lab, you'll have two components: 
- `src/App.jsx` 
- `src/components/WeatherForecast/WeatherForecast.jsx`. 
  
  
The `App` component will act as our root, while the `WeatherForecast` component will be used within `src/App.jsx` to dynamically generate a list of forecasts.

Your app should adhere to the following component hierarchy diagram:

![Component hierarchy diagram](./assets/chd-core.png)

> 💡 When content is dynamically generated, we only include the re-used component **once** in a component hierarchy diagram.

## Starter code

First, we'll need some weather data. Copy the following `weatherForecasts` array into your `src/App.jsx` file:

```jsx
const weatherForecasts = [
  {
    day: 'Mon',
    img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/day.svg',
    imgAlt: 'sun icon',
    conditions: 'sunny',
    time: 'Morning',
  },
  {
    day: 'Tue',
    img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/night.svg',
    imgAlt: 'moon icon',
    conditions: 'clear',
    time: 'Night',
  },
  {
    day: 'Wed',
    img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/stormy.svg',
    imgAlt: 'clouds with lightning icon',
    conditions: 'stormy',
    time: 'All Day',
  },
  {
    day: 'Thu',
    img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/cloudy-day.svg',
    imgAlt: 'sun overcast by clouds icon',
    conditions: 'overcast',
    time: 'Evening',
  },
  {
    day: 'Fri',
    img: 'https://pages.git.generalassemb.ly/modular-curriculum-all-courses/react-components-lab/assets/cloudy-night.svg',
    imgAlt: 'moon overcast by clouds icon',
    conditions: 'cloudy',
    time: 'Night',
  },
];
```

## `App.jsx` starter code

At the `App.jsx` level, add a `<section>` tag that will surround all of the `WeatherForecast` elements. We'll need it for the CSS.

```jsx
  <>
    <h1>Local Weather</h1>
    <section>
        // Weather data here 
    </section>
  </>
```
## WeatherForecast.jsx (component)

App.jsx is considered to be a "page" level component. The component itself is entire page. Individual components are meant to be used within individual pages and potentially reused on multiple other pages. Generally speaking a `pages` folder will hold all pages and a separate `components` folder will hold all other components.

- Create a new folder under `src/` that is titled `components` 
- Create another folder inside components to hold the `WeatherForecast` component. 
- Create the actual `WeatherForecast.jsx` component.
- final: `components/WeatherForecast/WeatherForecast.jsx`

- Each instance of the `WeatherForecast` component should have the JSX equivalent of the following HTML structure...
- create your new component and add this in the return statement:

```html
<div className="weather">
  <h2>Day of the Week</h2>
  <img src="" alt="" />
  <p><span>conditions: </span>current weather conditions</p>
  <p><span>time: </span>time of day</p>
</div>
```

## WeatherForecast starter CSS

- Create a `WeatherForecast.css` file in the same directory as the `WeatherForecast.jsx` file (`./components`). 
- Import the CSS file at the top off `WeatherForecast.jsx`: `import './WeatherForecast.css';`
- Add the following style rules to it:

```css
section {
  display: flex;
}

section.weather {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid #ccc;
  flex: 1;
  padding: 10px;
  text-align: center;
}

.weather span {
  font-weight: bold;
}
```

## Display the weather data:

Your final task is to figure out, using today's lesson, how to **map** through each of the weather items in the `weatherForecasts` array, pass the information (props) into the `WeatherForecast.jsx` component, and display the weather data in App.jsx