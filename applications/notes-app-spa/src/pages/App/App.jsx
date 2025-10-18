import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import HomePage from "../HomePage";   
import AboutPage from "../AboutPage"; 
import headerLogo from "../../assets/images/today-s-mood-277365833.webp";

export default function App() {
  return (
    <>
      <header className="header">
        <div className="header-logo-container">
          <Link to="/">
            <img src={headerLogo} alt="Notes App Logo" />
          </Link>
        </div>

        <nav className="nav">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/about">About</Link></li>
          </ul>
        </nav>
      </header>

      <main className="main">
        <Routes>
          <Route path="/*" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </main>
    </>
  );
}
