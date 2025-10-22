import "./App.css";
import { Route, Routes, Link, Navigate, useLocation } from "react-router-dom"; 
import headerLogo from "../../assets/images/header-logo.svg";

import HomePage from "../HomePage";
import AboutPage from "../AboutPage/AboutPage.jsx";
import CatIndexPage from "../CatIndexPage";
import CatDetailPage from "../CatDetailPage";
import CatFormPage from "../CatFormPage";

import ToyIndexPage from "../ToyIndexPage";
import ToyDetailPage from "../ToyDetailPage";
import ToyFormPage from "../ToyFormPage";

export default function App() {
  const location = useLocation();

  const routes = ["about", "cats", "toys"];
  const mainCSS = routes
    .filter((r) => (location.pathname.includes(r) ? r : ""))
    .join(" ");

  return (
    <>
      <header>
        <div className={`${mainCSS} header-logo-container`}>
          <Link to="/"> 
            <img src={headerLogo} alt="The Cat Collector Logo" />
          </Link>
        </div>
        <nav>
          <ul>
            <li><Link to="/about">About</Link></li>
            <li><Link to="/cats">All Cats</Link></li>
            <li><Link to="/cats/new">Create New Cat</Link></li>
            <li><Link to="/toys">All Toys</Link></li>
            <li><Link to="/toys/new">Add a Toy</Link></li>
          </ul>
        </nav>
      </header>

      <main className={mainCSS}>
        <Routes>
          <Route path="/" element={<HomePage />} />

          <Route path="/about" element={<AboutPage />} />
          <Route path="/cats" element={<CatIndexPage />} />
          <Route path="/cats/:id" element={<CatDetailPage />} />
          <Route path="/cats/new" element={<CatFormPage createCat={true} />} />
          <Route path="/cats/edit/:id" element={<CatFormPage editCat={true} />} />
          <Route path="/cats/confirm_delete/:id" element={<CatFormPage deleteCat={true} />} />

          <Route path="/toys" element={<ToyIndexPage />} />
          <Route path="/toys/:id" element={<ToyDetailPage />} />
          <Route path="/toys/new" element={<ToyFormPage createToy={true} />} />
          <Route path="/toys/edit/:id" element={<ToyFormPage editToy={true} />} />
          <Route path="/toys/confirm_delete/:id" element={<ToyFormPage deleteToy={true} />} />

          <Route path="/*" element={<Navigate to="/" />} />
        </Routes>
      </main>
    </>
  );
}
