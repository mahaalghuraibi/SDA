<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# REACT LABS
Each react lab will build on the previous lab by adding to the same application that you will build in your `SDA-Ghazal/applications/react_labs`. We will do this for two reasons...

1. React applications can take up quite a bit of space on your computers and take time to build from the ground up.

2. You are more likely to build on one idea than you are to continuously create new applications over and over again. best to get the experience of continuing to build on one idea and seeing how code can be organized to help make projects easier to build and expand upon.

## About

Welcome to Reactville, a constantly evolving virtual metropolis. Let's build this digital town together, one component at a time.

![Reactville Skyline](./assets/Reactville.png)

Reactville Weather Station is at the heart of the town, keeping everyone informed about the ever-changing weather. They're in need of a tech upgrade and have called on you to develop their new 5-Day Weather Forecast App. 

## React State Controlled Forms

Welcome to the React Controlled Forms Lab! In this lab, we'll interact with state to better understand how to manage it in a React application. Your task is to update your lab to use state management so that react will update the DOM based on changes in your application's state. 

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

Our goal for this exercise is to implement the ability to accept user input / data and display that data accordingly. We will do so by allowing users to generate a list of activities they may want to be able to do. Ultimately we will update the user interface (UI) so that we can navigate to an individual forecast page and add activities from our list of activities to the state of the specific forecast, and be able to display them! Woohooo!

### Story =>
The user has asked us to provide a way to create a list of activities they may want to do on any day. Ultimately they want to be able to add an activity to a day based on the forecast they are seeing for that day. Before we get to that point, we need to provide a way to view the list and create / add new acitivities to the list...


Your job is to:

- Add two sections to the page to display:
  - The activities that have been added / already exist in our list of acitvities
  - A form to add new acitivities
- Add CSS to keep the UI clean / organized

**HINTS**
- Think about how to structure your application to add your new form component to add new activities. 
- Think about how you will display this information? Where will it sit on the page?

