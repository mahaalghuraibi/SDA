import "./styles.css";
import { Link } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg";

export default function NoteIndexCard({ note }) {
  return (
    <div className="note-index-card">
      <Link to={`/notes/${note.id}`}>
        <div className="note-index-card-content">
          <img src={moodImg} alt="Mood image" />
          <h2>{note.title}</h2>
          <p>{note.content}</p>
          <p>
            <small>{new Date(note.created_at).toLocaleDateString("en-GB")}</small>
          </p>
        </div>
      </Link>
    </div>
  );
}
