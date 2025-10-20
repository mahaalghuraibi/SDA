import "./styles.css";
import { useState, useEffect } from "react";
import moodImg from "../../assets/images/mood.jpg";
import todayImg from "../../assets/images/today-s-mood-277365833.webp";
import NoteIndexCard from "../../components/NoteIndexCard";
import * as noteAPI from "../../utilities/notes-api";

export default function NoteIndexPage() {
  const [allNotes, setAllNotes] = useState([]);

useEffect(() => {
  async function getAllNotes() {
    try {
      const noteData = await noteAPI.index();
      console.log(noteData);
      setAllNotes(noteData);    
    } catch (err) {
      console.log(err);
    }
  }
  getAllNotes();
}, []);


  const displayAllNotes = allNotes.map((n, i) => <NoteIndexCard key={i} note={n} />);

  return (
    <>
      <section className="page-header">
        <h1>Notes List</h1>
        <img src={moodImg} alt="Mood photo" />
        <img src={todayImg} alt="Today's mood photo" />
      </section>

      <section className="index-card-container">
        {displayAllNotes}
      </section>
    </>
  );
}
