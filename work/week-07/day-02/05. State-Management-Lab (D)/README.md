<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# REACT LABS
Each react lab will build on the previous lab by adding to the same application that you will build in your `SDA-Ghazal/applications/react_labs`. We will do this for two reasons...

1. React applications can take up quite a bit of space on your computers and take time to build from the ground up.

2. You are more likely to build on one idea than you are to continuously create new applications over and over again. best to get the experience of continuing to build on one idea and seeing how code can be organized to help make projects easier to build and expand upon.

## About

Welcome to Reactville, a constantly evolving virtual metropolis. Let's build this digital town together, one component at a time.

![Reactville Skyline](./assets/Reactville.png)

Reactville Weather Station is at the heart of the town, keeping everyone informed about the ever-changing weather. They're in need of a tech upgrade and have called on you to develop their new 5-Day Weather Forecast App. 

## React State Management

Welcome to the React State Management Lab! In this lab, we'll interact with state to better understand how to manage it in a React application. Your task is to update your lab to use state management so that react will update the DOM based on changes in your applications state. 

## Setup

Your `react_labs`, should already contain: 
- `src/App.jsx` 
- `src/components/WeatherForecast/WeatherForecast.jsx`. 
  

## Running the development server

To start the development server and view our app in the browser, we'll use the following command:

```bash
npm run dev
```

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
```

## Exercise

It is your job to update to implement the following functionality...

1. Move the initial weather state into a react useState hook so the UI will update based on changes.
2. Create a state that can make it possible to show / hide weather details when clicking on an individual weather item.
3. Remove a weather item when clicked on.
4. Add some conditional CSS based on the weather.


**HINTS!!!!**

- Use the "conditions" property from each daily forecast data to decide a css class to add based on that information. The condition property can literally be the CSS classname and adjust in the css accordinly!

- Use the ['visibility'](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility) property in CSS to adjust showing the conditions and time of the forecast properties of the day... Wrap the two properties in the div and use react useState to determine the correct class to set. Ask yourself where the state needs to be set in order to make toggling work for EVERY forecast.