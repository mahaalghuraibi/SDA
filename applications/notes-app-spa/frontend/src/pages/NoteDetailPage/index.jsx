import "./styles.css";
import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg";
import * as noteAPI from "../../utilities/notes-api";
import * as moodchecksAPI from "../../utilities/moodchecks-api";
import MoodCheckForm from "../../components/Forms/MoodCheckForm";
import AddPhotoForm from "../../components/Forms/AddPhotoForm";

const PERIODS = { M: "Morning", A: "Afternoon", N: "Night" };

export default function NoteDetailPage() {
  const [noteDetail, setNoteDetail] = useState(null);
  const [moodChecks, setMoodChecks] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    async function getAndSetDetail() {
      try {
        const note = await noteAPI.show(id);
        setNoteDetail(note);

        const checks = await moodchecksAPI.noteMoodChecks(id);
        setMoodChecks(checks);
      } catch (err) {
        console.log(err);
      }
    }
    if (id) getAndSetDetail();
  }, [id]);

  async function addPhoto(noteId, formData) {
    try {
      const updatedNote = await noteAPI.addPhoto(noteId, formData);
      setNoteDetail(updatedNote);
    } catch (err) {
      console.log(err);
      setNoteDetail({ ...noteDetail });
    }
  }

  if (!noteDetail) return <h3>Your note details will display soon...</h3>;

  return (
    <section className="detail-note-container">
      <div className="detail-note-img">
        {noteDetail.photo?.url ? (
          <img
            src={noteDetail.photo.url}
            alt={`A photo for ${noteDetail.title}`}
            className="usr-img"
          />
        ) : (
          <img src={moodImg} alt="Mood note" />
        )}
      </div>

      <div className="note-details">
        <h1>{noteDetail.title}</h1>
        <p>{noteDetail.content}</p>
        <p>
          <small>
            {noteDetail.created_at
              ? new Date(noteDetail.created_at).toLocaleDateString("en-GB")
              : "No date"}
          </small>
        </p>
        <div className="note-actions">
          <Link to={`/notes/edit/${noteDetail.id}`} className="btn warn">
            Edit
          </Link>
          <Link
            to={`/notes/confirm_delete/${noteDetail.id}`}
            className="btn danger"
          >
            Delete
          </Link>
        </div>
      </div>

      <section className="add-photo-section">
        <AddPhotoForm note={noteDetail} addPhoto={addPhoto} />
      </section>

      <div className="feedings-toy-container">
        <section className="feedings">
          <div className="subsection-title">
            <h2>Mood Checks</h2>
            <span style={{ marginLeft: 8 }}>🌅 🌤️ 🌙</span>
          </div>

          <h3>Add a Mood Check</h3>
          <MoodCheckForm
            noteDetail={noteDetail}
            moodChecks={moodChecks}
            setMoodChecks={setMoodChecks}
          />

          <h3>Past Mood Checks</h3>
          {moodChecks.length > 0 ? (
            <table>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Period</th>
                </tr>
              </thead>
              <tbody>
                {moodChecks.map((mc, idx) => (
                  <tr key={idx}>
                    <td>{mc.date}</td>
                    <td>{PERIODS[mc.period]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <div className="subsection-content">
              <p>
                ⚠️ No mood checks recorded for{" "}
                <strong>{noteDetail.title}</strong> yet!
              </p>
            </div>
          )}
        </section>
      </div>
    </section>
  );
}
