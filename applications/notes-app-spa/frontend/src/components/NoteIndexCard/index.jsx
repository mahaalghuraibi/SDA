import "./styles.css";
import { Link } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg"; 

export default function NoteIndexCard({ note }) {
  return (
    <div className="note-index-card">
      <Link to={`/notes/${note.id}`}>
        <div className="note-index-card-content">
          {note.photo?.url ? (
            <img
              src={note.photo.url}
              alt={`Photo for ${note.title}`}
              className="usr-img"
            />
          ) : (
            <img src={moodImg} alt="Default mood" className="usr-img" />
          )}

          <h2>{note.title}</h2>
          <p><small>{note.content.slice(0, 100)}...</small></p>
        </div>
      </Link>
    </div>
  );
}
