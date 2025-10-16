import { Routes, Route, Link, useNavigate, useLocation } from "react-router-dom";
import { useState } from "react";
import LandingPage from "../LandingPage/index.jsx";
import GiphyDetailPage from "../GiphyDetailPage/GiphyDetailPage.jsx";
import "./App.css";

export default function App(){
  const [query, setQuery] = useState("");
  const navigate = useNavigate();
  const location = useLocation();

  function handleSearch(e){
    e.preventDefault();
    const q = query.trim();
    if(!q){
      if(location.pathname !== "/") navigate("/");
      else window.dispatchEvent(new CustomEvent("app:search", { detail: "" }));
      return;
    }
    if(location.pathname === "/"){
      window.dispatchEvent(new CustomEvent("app:search", { detail: q }));
    }else{
      navigate(`/?q=${encodeURIComponent(q)}`);
    }
  }

  return (
    <div className="container">
      <header className="header">
        <Link to="/"><h1>React Giphy Searcher</h1></Link>
        <span className="spacer" />
        <form onSubmit={handleSearch} className="searchbar">
          <input
            type="text"
            placeholder="Search GIFs…"
            value={query}
            onChange={(e)=>setQuery(e.target.value)}
            aria-label="Search GIFs"
          />
          <button type="submit">Search</button>
        </form>
      </header>

      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/giphy/:id" element={<GiphyDetailPage />} />
        <Route path="*" element={<p style={{padding:24}}>Not Found</p>} />
      </Routes>
    </div>
  );
}
