<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack React / Django REST Framework Application / Cat Colletor

Today we start our journey of building a full stack web application using React on the front end and Django Rest Framework on the backend. This process will unfold over the course of several days / parts and will combine the tools we learned this week (react) along with a fresh approach to developing a Django server with a slightly different framework. The overall concept is the exact same as our previous Cat Collector, but with a few small changes. 

## Part 1 - REACT / Frontend SETUP

## Setup

1. `npm create vite@latest first-react-app-lab`
2. `Select a framework:` => `React`
3. `Select a variant` => `Javascript`
4. `Use rolldown-vite (Experimental)?:` => `No`
5. `Install with npm and start now?:` => `Yes`
6. Navigate to `localhost:5173` (check app is running)
7. `ctrl+c` => terminate running application
8. `cd project-name`
9. `npm i -D @types/react @types/react-dom` (helps with intellisense / autocomplete!)
10. `npm i react-router` - Install ReactRouter...


11.  Setup React Router
   - importing `BrowserRouter` in our entry file, (`src/main.jsx`). 
   - `BrowserRouter` is a component in React Router that enables navigation. 
   - Add the following to `src/main.jsx`:

```jsx
import { BrowserRouter } from 'react-router';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
```

12. **Clean Up `App.jsx`**

Open the `App.jsx` file in the `src` directory and replace its contents with the following:

`src/App.jsx`
```jsx
import './App.css'

function App() {
  return (
    <h1>Welcome to Cat Collector SPA!</h1>
  );
}

export default App;
```

13. Run the development server

- `npm run dev`

You should see that `Vite` is available on port number 5173:

```plaintext
localhost:5173
``` 

10.  That's it!