import "./styles.css";
import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg";
import * as noteAPI from "../../utilities/notes-api";
import * as moodchecksAPI from "../../utilities/moodchecks-api";
import MoodCheckForm from "../../components/Forms/MoodCheckForm";
import AddPhotoForm from "../../components/Forms/AddPhotoForm";
import * as reactionsAPI from "../../utilities/reactions-api";
import DisplayNoteReactions from "../../components/DisplayNoteReactions";
import * as notesAPI from "../../utilities/notes-api";

const PERIODS = { M: "Morning", A: "Afternoon", N: "Night" };

export default function NoteDetailPage() {
  const [noteDetail, setNoteDetail] = useState(null);
  const [moodChecks, setMoodChecks] = useState([]);
  const [allReactions, setAllReactions] = useState([]);
  const [reactionsNoteHas, setReactionsNoteHas] = useState([]);
  const [reactionsNoteDoesntHave, setReactionsNoteDoesntHave] = useState([]);

  const { id } = useParams();

  useEffect(() => {
    async function getAndSetDetail() {
      try {
        const res = await noteAPI.show(id);
        const normalizedNote = res?.note ?? res;
        setNoteDetail(normalizedNote);

        setReactionsNoteHas(res?.reactionsNoteHas ?? []);
        setReactionsNoteDoesntHave(res?.reactionsNoteDoesntHave ?? []);

        const checks = await moodchecksAPI.noteMoodChecks(id);
        setMoodChecks(checks);

        const reactions = await reactionsAPI.index();
        setAllReactions(reactions);
      } catch (err) {
        console.log(err);
      }
    }
    if (id) getAndSetDetail();
  }, [id]);

  async function addPhoto(noteId, formData) {
    try {
      const updated = await noteAPI.addPhoto(noteId, formData);
      setNoteDetail(updated?.note ?? updated);
    } catch (err) {
      console.log(err);
      setNoteDetail({ ...noteDetail });
    }
  }

  async function handleAddReaction(evt, reactionId) {
    try {
      evt.preventDefault();
      const data = await notesAPI.addReactionToNote(noteDetail.id, reactionId);
      setReactionsNoteHas(data.reactionsNoteHas ?? []);
      setReactionsNoteDoesntHave(data.reactionsNoteDoesntHave ?? []);
    } catch (err) {
      console.log(err);
    }
  }

  async function handleRemoveReaction(evt, reactionId) {
    try {
      evt.preventDefault();
      const data = await notesAPI.removeReactionFromNote(noteDetail.id, reactionId);
      setReactionsNoteHas(data.reactionsNoteHas ?? []);
      setReactionsNoteDoesntHave(data.reactionsNoteDoesntHave ?? []);
    } catch (err) {
      console.log(err);
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

        <section className="reactions">
          <div className="subsection-title" style={{ marginTop: 24 }}>
            <h2>Reactions</h2>
            <span style={{ marginLeft: 8 }}>💜 😄 👍 😢 🔥 🙌</span>
          </div>

          <h3>Available Reactions</h3>
          <div className="subsection-content">
            {allReactions.map((r) => (
              <div
                key={r.id}
                className="reaction-container"
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 12,
                  marginBottom: 10,
                }}
              >
                <div
                  className="reaction-info"
                  style={{ display: "flex", alignItems: "center", gap: 10 }}
                >
                  <span style={{ fontSize: 28 }}>{r.emoji}</span>
                  <Link
                    to={`/reactions/${r.id}`}
                    className="btn secondary"
                    style={{ padding: "2px 8px" }}
                  >
                    View
                  </Link>
                </div>
              </div>
            ))}
            {allReactions.length === 0 && <p>No reactions yet.</p>}
          </div>
        </section>

        <section className="reactions">
          <div className="subsection-title" style={{ marginTop: 24 }}>
            <h2>Reactions on this note</h2>
          </div>

          <h3>Current Reactions</h3>
          <div className="subsection-content">
            {reactionsNoteHas.length > 0 ? (
              reactionsNoteHas.map((r) => (
                <DisplayNoteReactions
                  key={r.id}
                  reaction={r}
                  submitFunction={handleRemoveReaction}
                  formAction="Remove"
                />
              ))
            ) : (
              <p>No reactions yet on this note.</p>
            )}
          </div>

          <h3 style={{ marginTop: 16 }}>Available to Add</h3>
          <div className="subsection-content">
            {reactionsNoteDoesntHave.length > 0 ? (
              reactionsNoteDoesntHave.map((r) => (
                <DisplayNoteReactions
                  key={r.id}
                  reaction={r}
                  submitFunction={handleAddReaction}
                  formAction="Add"
                />
              ))
            ) : (
              <p>All reactions already added 🎉</p>
            )}
          </div>
        </section>
      </div>
    </section>
  );
}
