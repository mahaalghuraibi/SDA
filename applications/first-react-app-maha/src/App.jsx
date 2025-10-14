import { useState } from "react";
import "./App.css";

const App = () => {
  const [theme, setTheme] = useState("light");

  
  const [info, setInfo] = useState({
    firstName: "Maha",
    lastName: "Alghuraibi",
    age: 25,
    hasPets: false
  });

  return (
    <div className={theme}>
      <p>
        my name is {info.firstName} {info.lastName}, i am {info.age} years old.
      </p>

      <div>
        <button onClick={() => setTheme("light")}>light mode ☀️</button>
        <button onClick={() => setTheme("dark")}>dark mode 🌙</button>
        <button onClick={() => setTheme("neon")}>neon mode 💚</button>
        <button onClick={() => setTheme("night")}>night mode 🌌</button>
      </div>
    </div>
  );
};

export default App;
