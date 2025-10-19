import { use } from "react";
import "./App.css";
import {useState} from "react"

const App = () => {
  const [woroud, setWoroud] = useState([
    "sunflower", "daisy", "rose", "tulips", "lilies"
  ])
  
  const [themeMode, setThemeMode] = useState("light");
  // before refactor 
  // const [isDarkMode, setIsDarkMode] = useState(false);

  // Any valid javascript data type can be stored in a hook variable
  const [bool, setBool] = useState(false)
  const [num, setNum] = useState(null)
  const [obj, setObj] = useState({})

  // you do: Define a state variable that stores an object, and render its properties
  const [info, setInfo] = useState({
    firstName: "Khalid",
    lastName: "Al Duwayssan",
    hasPets: false,
    age: 18
  })

  // Before refactor
  // const handleLightMode = () => {
  //   setIsDarkMode(false)
  // }
  // const handleDarkMode = () => {
  //   setIsDarkMode(true)
  // }

  // after refactor
  const handleChangeTheme = (themeValue) => {
    setThemeMode(themeValue)
  }

  // updating complex state: arrays
  const addFlower = (flower) => {
    setWoroud([flower, ...woroud])
  }

  // updating complex state: objects
  const updateInfo = () => {
    setInfo({
      ...info,
      address: "Riyadh"
    })
  }


  return (
    <body className={themeMode}>
      <h1>
        The MVP is {info.firstName} {info.lastName}, he is {info.age}{" "}and{" "}
        {info.hasPets ? "has a pet." : " has no pets."}
      </h1>
      <div>
        {/* <button onClick={handleLightMode}>light mode</button> */}
        {/* <button onClick={() => setIsDarkMode(false)}>light mode</button>
        <button onClick={() => setIsDarkMode(true)}>dark mode</button> */}
        {/* <button onClick={handleDarkMode}>dark mode</button> */}

        {/* After refactor and todo */}
        {/* <button onClick={() => handleChangeTheme("dark")}>dark mode</button>
        <button onClick={() => handleChangeTheme("light")}>light mode</button>
        <button onClick={() => handleChangeTheme("neon")}>neon mode</button>
        <button onClick={() => handleChangeTheme("night")}>night mode</button> */}

        <div>
          {
            woroud.map((flower) => (
              <p>{flower}</p>
            ))
          }
        </div>

        <button onClick={() => addFlower("lavender")}>Add Flower</button>
      </div>
    </body>
  );
};

export default App;
