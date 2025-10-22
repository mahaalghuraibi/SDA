import "./App.css";
import { Routes, Route, Link, Navigate, useLocation } from "react-router-dom";
import HomePage from "../HomePage";
import AboutPage from "../AboutPage";
import NoteIndexPage from "../NoteIndexPage";
import NoteDetailPage from "../NoteDetailPage";
import NoteFormPage from "../NoteFormPage";
import ReactionIndexPage from "../ReactionIndexPage";
import ReactionDetailPage from "../ReactionDetailPage";
import ReactionFormPage from "../ReactionFormPage";
import headerLogo from "../../assets/images/today-s-mood-277365833.webp";

export default function App() {
  const location = useLocation();
  const routes = ["about", "notes", "reactions", "home"]; 
  const mainCSS = routes.filter(r => location.pathname.includes(r) ? r : "").join(" ");

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
            <li><Link to="/about">About</Link></li>
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/notes">All Notes</Link></li>
            <li><Link to="/notes/new">Add Note</Link></li>
            <li><Link to="/reactions/new">Add Reaction</Link></li>
            <li><Link to="/reactions">All Reactions</Link></li>
          </ul>
        </nav>
      </header>

      <main className={mainCSS}>
        <Routes>
          <Route path="/home" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/notes" element={<NoteIndexPage />} />
          <Route path="/notes/:id" element={<NoteDetailPage />} />
          <Route path="/notes/new" element={<NoteFormPage createNote={true} />} />
          <Route path="/notes/edit/:id" element={<NoteFormPage editNote={true} />} />
          <Route path="/notes/confirm_delete/:id" element={<NoteFormPage deleteNote={true} />} />
          <Route path="/reactions" element={<ReactionIndexPage />} />
          <Route path="/reactions/:id" element={<ReactionDetailPage />} />
          <Route path="/reactions/new" element={<ReactionFormPage createReaction={true} />} />
          <Route path="/reactions/edit/:id" element={<ReactionFormPage editReaction={true} />} />
          <Route path="/reactions/confirm_delete/:id" element={<ReactionFormPage deleteReaction={true} />} />
          <Route path="/*" element={<Navigate to="/home" />} />
        </Routes>
      </main>
    </>
  );
}

