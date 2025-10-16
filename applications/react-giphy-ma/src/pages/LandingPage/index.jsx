import { useEffect, useMemo, useState } from "react";
import * as giphyAPI from "../../utilities/giphy.js";
import GIFCard from "../../components/GIFCard/GIFCard.jsx";
import "./styles.css";

export default function LandingPage(){
  const [gifs, setGifs]   = useState([]);
  const [title, setTitle] = useState("Trending GIFs");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const initialQuery = useMemo(()=>{
    const usp = new URLSearchParams(window.location.search);
    return (usp.get("q") || "").trim();
  },[]);

  useEffect(()=>{
    async function load(){
      setLoading(true); setError("");
      try{
        if(initialQuery){
          const data = await giphyAPI.searchGifs(initialQuery);
          setGifs(data.data || []);
          setTitle(`Results for: "${initialQuery}"`);
        }else{
          const data = await giphyAPI.getTrendingGifs();
          setGifs(data.data || []);
          setTitle("Trending GIFs");
        }
      }catch(e){
        setError(e.message || "Failed to load GIFs");
      }finally{
        setLoading(false);
      }
    }
    load();

    function onSearch(ev){ performSearch(ev.detail); }
    window.addEventListener("app:search", onSearch);
    return ()=> window.removeEventListener("app:search", onSearch);
  },[]);

  async function performSearch(term){
    setLoading(true); setError("");
    try{
      if(!term){
        const data = await giphyAPI.getTrendingGifs();
        setGifs(data.data || []);
        setTitle("Trending GIFs");
        return;
      }
      const data = await giphyAPI.searchGifs(term);
      setGifs(data.data || []);
      setTitle(`Results for: "${term}"`);
    }catch(e){
      setError(e.message || "Failed to search GIFs");
    }finally{
      setLoading(false);
    }
  }

  return (
    <>
      <div className="landing-header">
        <h3>{title}</h3>
        <span className="badge">{gifs.length} items</span>
      </div>

      {loading && <div className="placeholder">Loading…</div>}
      {error && <div className="error">{error}</div>}

      <div className="trending-gifs-container grid">
        {!loading && !error && gifs.map(gif=>(
          <GIFCard key={gif.id} gif={gif} />
        ))}
      </div>
    </>
  );
}
