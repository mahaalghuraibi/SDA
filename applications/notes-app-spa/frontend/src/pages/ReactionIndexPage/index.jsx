import "./styles.css";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import * as reactionAPI from "../../utilities/reactions-api";

export default function ReactionIndexPage() {
  const [allReactions, setAllReactions] = useState([]);

  useEffect(() => {
    async function getAll() {
      try {
        const data = await reactionAPI.index();
        setAllReactions(data);
      } catch (err) {
        console.log(err);
        setAllReactions([]);
      }
    }
    getAll();
  }, []);

  return (
    <>
      <section className="page-header">
        <h1>All Reactions</h1>
        <div className="emoji-strip" aria-hidden></div>
      </section>

      <section className="reaction-index-card-container">
        {allReactions.map(r => (
          <div key={r.id} className="reaction-index-card">
            <Link to={`/reactions/${r.id}`}>
              <div className="reaction-index-card-content">
                <h2 className="emoji">{r.emoji}</h2>
              </div>
            </Link>
          </div>
        ))}
        {allReactions.length === 0 && (
          <p className="empty">No reactions yet — add one!</p>
        )}
      </section>
    </>
  );
}
