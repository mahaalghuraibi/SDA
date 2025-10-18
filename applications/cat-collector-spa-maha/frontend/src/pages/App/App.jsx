import './App.css'
import { Route, Routes, Link } from 'react-router';
import headerLogo from "../../assets/images/header-logo.svg";
import HomePage from '../HomePage';
import AboutPage from '../AboutPage';


function App() {

  return (
    <>
      <header>
        <div className="header-logo-container">
          <a href="/">
            <img src={headerLogo} alt="The Cat Collector Logo" />
          </a>
        </div>
        <nav>
          <ul>
            <li><Link to="/about">About</Link></li>
          </ul>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/*" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>



      </main>





    </>)
}

export default App