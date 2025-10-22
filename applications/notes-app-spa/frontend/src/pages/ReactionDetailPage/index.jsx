import "./styles.css";
import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import * as reactionAPI from "../../utilities/reactions-api";

export default function ReactionDetailPage() {
  const [reactionDetail, setReactionDetail] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    async function getAndSetDetail() {
      try {
        const reaction = await reactionAPI.show(id);
        setReactionDetail(reaction);
      } catch (err) {
        console.log(err);
        setReactionDetail(null);
      }
    }
    getAndSetDetail();
  }, [id]);

  if (!reactionDetail) return <h3>Your reaction details will display soon </h3>;

  return (
    <>
      <div className="reaction-detail-card">
        <div className="reaction-detail-card-bg"></div>
        <div className="reaction-detail-card-content">
          <h2>{reactionDetail.emoji}</h2>
        </div>
      </div>
      <div className="reaction-actions">
        <Link to={`/reactions/edit/${reactionDetail.id}`} className="btn warn">
          Edit
        </Link>
        <Link
          to={`/reactions/confirm_delete/${reactionDetail.id}`}
          className="btn danger"
        >
          Delete
        </Link>
      </div>
    </>
  );
}
