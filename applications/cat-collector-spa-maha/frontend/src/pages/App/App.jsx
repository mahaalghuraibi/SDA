import './App.css'
import { Route, Routes, Link } from 'react-router';
import headerLogo from "../../assets/images/header-logo.svg";
import HomePage from '../HomePage';
import AboutPage from '../AboutPage';
import CatIndexPage from '../CatIndexPage/CatIndexPage';
import { useLocation, Navigate } from 'react-router';
import CatDetailPage from "../CatDetailPage";
import CatFormPage from '../CatFormPage';

function App() {
  const routes = ["about", "cats", "home"]
  const mainCSS = routes.filter(r => location.pathname.includes(r) ? r : "").join(" ")


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
            <li><Link to="/cats">All Cats</Link></li>
            <li><Link to="/cats/new">Create New Cat</Link></li>


          </ul>
        </nav>
      </header>
      <main className={mainCSS}>
        <Routes>
          <Route path="/home" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/cats" element={<CatIndexPage />} />
          <Route path="/*" element={<Navigate to="/home" />} />
          <Route path="/cats/:id" element={<CatDetailPage />} />
          <Route path="/cats/new" element={<CatFormPage />} />


        </Routes>



      </main>





    </>)
}

export default App