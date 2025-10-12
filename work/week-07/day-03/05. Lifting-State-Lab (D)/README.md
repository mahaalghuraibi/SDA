<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# REACT LABS
Each react lab will build on the previous lab by adding to the same application that you will build in your `SDA-Ghazal/applications/react_labs`. We will do this for two reasons...

1. React applications can take up quite a bit of space on your computers and take time to build from the ground up.

2. You are more likely to build on one idea than you are to continuously create new applications over and over again. best to get the experience of continuing to build on one idea and seeing how code can be organized to help make projects easier to build and expand upon.

## About

Welcome to Reactville, a constantly evolving virtual metropolis. Let's build this digital town together, one component at a time.

![Reactville Skyline](./assets/Reactville.png)

Reactville Weather Station is at the heart of the town, keeping everyone informed about the ever-changing weather. They're in need of a tech upgrade and have called on you to develop their new 5-Day Weather Forecast App. 

## React State Lifting State

Welcome to the React Lifting State Lab! In this lab, we'll more your state from a child component to a parent component (called lifting) so that the state can be shared between parallel components. The point is to make it so that state remains the same throughout the application and can be used in different locations throughout your application.

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

Our goal for this exercise is to implement the ability to share state amongst components and ultimately add some of that state to another piece of state. 

### Story =>
The user has asked us to provide a way to add activities to a daily forecast so they can plan activities for that day. The first step in doing this will be to "lift" the activities state from out activities component to a the parent component called `App.jsx`. Later, in the next lab, we will make it so that an activity can be added to a specific daily forecast.


Your job is to:

- Move the activities state from `Activities.jsx` to `App.jsx`.
- Pass the state and state updatign functions to the Activities compponent so the functionality remains intact.

