import { Link } from "react-router-dom";
import "./GIFCard.css";

export default function GIFCard({ gif }){
  const img = gif.images?.downsized?.url || gif.images?.original?.url;
  return (
    <div className="gif-card">
      <img src={img} alt={gif.title} />
      <h5>{gif.title || "Untitled GIF"}</h5>
      <Link to={`/giphy/${gif.id}`}>Details</Link>
    </div>
  );
}
