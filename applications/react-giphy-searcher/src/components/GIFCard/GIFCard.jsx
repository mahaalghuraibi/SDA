import { Link } from "react-router"
import "./GIFCard.css"

export default function GIFCard({ gif }) {
   return (
      <div className="gif-card">
         <img src={gif.images.downsized.url} />
         <h5>{gif.title}</h5>
         <Link to={`/giphy/${gif.id}`}>Details</Link>
      </div>
   )
}