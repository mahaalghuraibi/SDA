import "./Navigation.css";
import { Link } from "react-router";
import { useState } from "react";

export default function Navigation({ searchGIFs }) {
    const [formData, setFormData] = useState("")

    return (
        <nav className="nav-container">
            <form onSubmit={(evt) => searchGIFs(evt, formData, setFormData)}>
                <input value={formData} type="text" placeholder="search" onChange={(evt) => setFormData(evt.target.value)}/>
            </form>
            <Link to="*">Landing Page</Link>
        </nav>
    )
}