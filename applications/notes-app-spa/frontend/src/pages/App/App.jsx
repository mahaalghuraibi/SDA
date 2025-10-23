import "./App.css";
import { Routes, Route, Link, Navigate, useLocation } from "react-router-dom";
import { useState, useEffect } from "react";  
import HomePage from "../HomePage";
import AboutPage from "../AboutPage";
import { getUser } from "../../utilities/users-api";
import NoteIndexPage from "../NoteIndexPage";
import NoteDetailPage from "../NoteDetailPage";
import NoteFormPage from "../NoteFormPage";
import ReactionIndexPage from "../ReactionIndexPage";
import ReactionDetailPage from "../ReactionDetailPage";
import ReactionFormPage from "../ReactionFormPage";
import headerLogo from "../../assets/images/today-s-mood-277365833.webp";
import SignupPage from "../SignupPage/SignupPage";
import Navbar from "../../components/Navbar/Navbar";

export default function App() {
  const [user, setUser] = useState(null);
  const location = useLocation();
  const routes = ["about", "notes", "reactions", "home"]; 
  const mainCSS = routes.filter(r => (location.pathname.includes(r) ? r : "")).join(" ");

  useEffect(() => {
    async function checkUser() {
      const foundUser = await getUser();
      setUser(foundUser);
    }
    checkUser();
  }, []);

  return (
    <>
      <header>
        <div className={`${mainCSS} header-logo-container`}>
          <Link to="/">
            <img src={headerLogo} alt="Mood Notes Logo" />
          </Link>
        </div>
        <nav className="nav">
          <ul>
            <Navbar user={user} setUser={setUser} />
          </ul>
        </nav>
      </header>

      <main className={mainCSS}>
        <Routes>
          {user ? (
            <>
              <Route path="/home" element={<HomePage user={user} setUser={setUser} />} />
              <Route path="/about" element={<AboutPage />} />
              <Route path="/notes" element={<NoteIndexPage />} />
              <Route path="/notes/new" element={<NoteFormPage createNote={true} />} />
              <Route path="/notes/edit/:id" element={<NoteFormPage editNote={true} />} />
              <Route path="/notes/confirm_delete/:id" element={<NoteFormPage deleteNote={true} />} />
              <Route path="/notes/:id" element={<NoteDetailPage />} />
              <Route path="/reactions" element={<ReactionIndexPage />} />
              <Route path="/reactions/new" element={<ReactionFormPage createReaction={true} />} />
              <Route path="/reactions/edit/:id" element={<ReactionFormPage editReaction={true} />} />
              <Route path="/reactions/confirm_delete/:id" element={<ReactionFormPage deleteReaction={true} />} />
              <Route path="/reactions/:id" element={<ReactionDetailPage />} />
              <Route path="/*" element={<Navigate to="/home" />} />
            </>
          ) : (
            <>
              <Route path="/home" element={<HomePage user={user} setUser={setUser} />} />
              <Route path="/about" element={<AboutPage />} />
              <Route path="/signup" element={<SignupPage setUser={setUser} />} />
              <Route path="/*" element={<Navigate to="/home" />} />
            </>
          )}
        </Routes>
      </main>
    </>
  );
}
