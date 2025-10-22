import { Link } from "react-router-dom";

export default function DisplayNoteReactions({ reaction, submitFunction, formAction }) {
  return (
    <div className="reaction-container" style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 10 }}>
      <div className="reaction-info" style={{ display: "flex", alignItems: "center", gap: 10 }}>
        <span style={{ fontSize: 28 }}>{reaction.emoji}</span>
        <Link to={`/reactions/${reaction.id}`} className="btn secondary" style={{ padding: "2px 8px" }}>
          View
        </Link>
      </div>
      <form onSubmit={(evt) => submitFunction(evt, reaction.id)} style={{ marginLeft: "auto" }}>
        <button type="submit" className="btn submit">{formAction}</button>
      </form>
    </div>
  );
}
