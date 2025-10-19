import './App.css'
import { Routes, Route, Link } from 'react-router';
import HeaderLogo from "../../assets/images/header-logo.svg"
import HomePage from '../HomePage/HomePage';
import AboutPage from '../AboutPage/AboutPage';

function App() {

  return (<>
    <header>
      <div className="header-logo-container">
        <Link to="/"><img src={HeaderLogo} alt="The Cat Collector Logo" /></Link>
      </div>
      <nav>
        <ul>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>
    </header>
    <main>
      <Routes>
        <Route path="/about" element={<AboutPage />} />
        <Route path="/*" element={<HomePage />} />
      </Routes>
    </main>
  </>)
}

export default App
