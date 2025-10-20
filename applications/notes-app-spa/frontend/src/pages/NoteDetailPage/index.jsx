import "./styles.css";
import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg";
import * as noteAPI from "../../utilities/notes-api";

export default function NoteDetailPage() {
  const [noteDetail, setNoteDetail] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    async function getAndSetDetail() {
      try {
        const note = await noteAPI.show(id);
        setNoteDetail(note);
      } catch (err) {
        console.log(err);
      }
    }
    if (id) getAndSetDetail();
  }, [id]);

  if (!noteDetail) return <h3>Your note details will display soon...</h3>;

  return (
    <section className="detail-note-container">
      <div className="detail-note-img">
        <img src={moodImg} alt="Mood note" />
      </div>
      <div className="note-details">
        <h1>{noteDetail.title}</h1>
        <p>{noteDetail.content}</p>
        <p><small>{new Date(noteDetail.created_at).toLocaleDateString("en-GB")}</small></p>
      </div>

      <div className="note-actions">
        <Link to={`/notes/edit/${noteDetail.id}`} className="btn warn">Edit</Link>
        <Link to={`/notes/confirm_delete/${noteDetail.id}`} className="btn danger">Delete</Link>
      </div>
    </section>
  );
}
