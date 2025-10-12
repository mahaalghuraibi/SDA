<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# REACT LABS
Each react lab will build on the previous lab by adding to the same application that you will build in your `SDA-Ghazal/applications/react_labs`. We will do this for two reasons...

1. React applications can take up quite a bit of space on your computers and take time to build from the ground up.

2. You are more likely to build on one idea than you are to continuously create new applications over and over again. best to get the experience of continuing to build on one idea and seeing how code can be organized to help make projects easier to build and expand upon.

## About

Welcome to Reactville, a constantly evolving virtual metropolis. Let's build this digital town together, one component at a time.

![Reactville Skyline](./assets/Reactville.png)

Reactville Weather Station is at the heart of the town, keeping everyone informed about the ever-changing weather. They're in need of a tech upgrade and have called on you to develop their new 5-Day Weather Forecast App. 

## React Router Lab

Welcome to the React Router Lab! In this lab, we'll upgrade our application to allow for client side routing! A huge step! This allows to be able to navigate to specific pages in our application and ultimately be able to add activities to the specific forecast day that we are currently looking it.

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

Our goal for this exercise is to implement client side routing using react router and then be able to add / remove activities from a daily forecast. 

### Story =>
The user has asked us to provide a way to add activities to a daily forecast so they can plan activities for that day. We previously lifted our state from our `Activities.jsx` component. Now we need to update the application to allow for client side routing and then add functionality to be able to add activities to out forecast.


Your job is to:

- Implement client side routing to be able to access a page for one daily forecast.
- Implement functionality to allow the user to add activities to that day's forecast so the User can plan their day with fun activities.