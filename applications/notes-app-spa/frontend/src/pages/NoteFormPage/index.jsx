// frontend/src/pages/NoteFormPage/index.jsx
import "./styles.css";
import { useEffect, useState } from "react";
import { useNavigate, useParams, Link } from "react-router-dom";
import moodImg from "../../assets/images/mood.jpg";
import * as noteAPI from "../../utilities/notes-api";

export default function NoteFormPage({ createNote, editNote, deleteNote }) {
  const initialState = { title: "", content: "" };
  const [currNote, setCurrNote] = useState(null);
  const [formData, setFormData] = useState(initialState);
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    async function getAndSetDetail() {
      try {
        const note = await noteAPI.show(id);
        setCurrNote(note);
        setFormData({ title: note.title, content: note.content });
      } catch (err) {
        console.log(err);
        setCurrNote(null);
        setFormData(initialState);
      }
    }
    if ((editNote || deleteNote) && id) getAndSetDetail();
  }, [id]); // eslint-disable-line

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const saved =
        editNote
          ? await noteAPI.update(formData, currNote.id)
          : await noteAPI.create(formData);

      setFormData(initialState);
      navigate(`/notes/${saved.id}`);
    } catch (err) {
      console.log(err);
    }
  }

  async function handleDelete(e) {
    e.preventDefault();
    try {
      await noteAPI.deleteNote(currNote.id);
      setFormData(initialState);
      navigate("/notes");
    } catch (err) {
      console.log(err);
    }
  }

  if (deleteNote && !currNote) return <h1>Loading</h1>;
  if (deleteNote && currNote)
    return (
      <>
        <div className="page-header">
          <h1>Delete Note?</h1>
          <img src={moodImg} alt="Mood" />
        </div>
        <h2>Are you sure you want to delete “{currNote.title}”?</h2>
        <form onSubmit={handleDelete}>
          <Link to={`/notes/${currNote.id}`} className="btn secondary">Cancel</Link>
          <button type="submit" className="btn danger">Yes — Delete!</button>
        </form>
      </>
    );

  if (editNote && !currNote) return <h1>Loading</h1>;

  if (createNote || editNote)
    return (
      <>
        <div className="page-header">
          {editNote ? <h1>Edit “{currNote?.title}”</h1> : <h1>Add a Note</h1>}
          <img src={moodImg} alt="Mood" />
        </div>

        <form className="form-container" onSubmit={handleSubmit}>
          <table>
            <tbody>
              {!editNote && (
                <tr>
                  <th><label htmlFor="id_title">Title:</label></th>
                  <td>
                    <input
                      id="id_title"
                      name="title"
                      type="text"
                      maxLength="100"
                      required
                      value={formData.title}
                      onChange={handleChange}
                    />
                  </td>
                </tr>
              )}
              <tr>
                <th><label htmlFor="id_content">Content:</label></th>
                <td>
                  <textarea
                    id="id_content"
                    name="content"
                    rows="8"
                    maxLength="500"
                    required
                    value={formData.content}
                    onChange={handleChange}
                  />
                </td>
              </tr>
            </tbody>
          </table>
          <button type="submit" className="btn end submit">Submit!</button>
        </form>
      </>
    );

  return null;
}
