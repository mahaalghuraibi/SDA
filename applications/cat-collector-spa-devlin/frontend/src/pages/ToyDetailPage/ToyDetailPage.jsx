import "./styles.css"
import { useState, useEffect } from "react";
import { useParams, Link } from "react-router";
import { closest } from "color-2-name";
import * as toyAPI from "../../utilities/toy-api";

export default function ToyDetailPage() {
    const [toyDetail, setToyDetail] = useState(null)
    const { id } = useParams();

    useEffect(() => {
        async function getToyDetail() {
            try {
                const toyData = await toyAPI.detail(id);
                console.log(toyData, "toy detail page 13");
                setToyDetail(toyData);
            } catch (err) {
                console.log(err);
            }
        }
        if (id) getToyDetail()
    }, [id])


    if (!toyDetail) return <h1>Toy Detail Coming Soon!</h1>
    return (<>
        <div className="toy-detail-card" style={{ borderColor: toyDetail.color }}>
            <div className="toy-detail-card-bg" style={{ backgroundColor: toyDetail.color }}></div>
            <div className="toy-detail-card-content">
                <h2>{toyDetail.name}</h2>
                <p>A {closest(toyDetail.color).name} toy</p>
            </div>
        </div>
        <div className="toy-actions">
            <Link to={`/toys/edit/${toyDetail.id}`} className="btn warn">Edit</Link>
            <Link to={`/toys/confirm_delete/${toyDetail.id}`} className="btn danger">Delete</Link>
        </div>
    </>)
}
