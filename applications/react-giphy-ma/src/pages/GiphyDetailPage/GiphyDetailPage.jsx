import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import * as giphyAPI from "../../utilities/giphy.js";
import "./styles.css";

export default function GiphyDetailPage(){
  const { id } = useParams();
  const [gif, setGif] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(()=>{
    async function load(){
      setLoading(true); setError("");
      try{
        const data = await giphyAPI.getGifById(id);
        setGif(data.data);
      }catch(e){
        setError(e.message || "Failed to load GIF");
      }finally{
        setLoading(false);
      }
    }
    load();
  },[id]);

  if(loading) return <div className="detail-container">Loading…</div>;
  if(error)   return <div className="detail-container error">{error}</div>;
  if(!gif)    return <div className="detail-container">No data.</div>;

  const user = gif.user || {};
  const creator = user.display_name || user.username || gif.username || "Unknown";
  const src = (gif.images?.original || gif.images?.downsized)?.url;

  return (
    <div className="detail-container">
      <p><Link to="/">← Back</Link></p>
      <div className="detail-card">
        <img className="detail-image" src={src} alt={gif.title} />
        <div className="detail-meta">
          <h2>{gif.title || "Untitled GIF"}</h2>
          <p><strong>Creator:</strong> {creator}</p>
          {user.profile_url && (
            <p><strong>Profile:</strong> <a href={user.profile_url} target="_blank" rel="noreferrer">{user.profile_url}</a></p>
          )}
          {gif.source && (
            <p><strong>Source:</strong> <a href={gif.source} target="_blank" rel="noreferrer">{gif.source}</a></p>
          )}
          <p><strong>Rating:</strong> {gif.rating?.toUpperCase?.() || "N/A"}</p>
          <p><strong>ID:</strong> {gif.id}</p>
        </div>
      </div>
    </div>
  );
}
