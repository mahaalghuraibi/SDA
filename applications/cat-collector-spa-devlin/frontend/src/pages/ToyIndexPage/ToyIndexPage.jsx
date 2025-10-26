import "./styles.css"
import { useEffect, useState } from "react"
import { Link } from "react-router";
import string from "../../assets/images/string.svg";
import mouse from "../../assets/images/mouse.svg";
import post from "../../assets/images/post.svg";
import fish from "../../assets/images/fish.svg";
import * as toyAPI from "../../utilities/toy-api";
import { closest } from 'color-2-name';

export default function ToyIndexPage() {
    const [allToys, setAllToys] = useState([])

    useEffect(() => {
        async function getAllToys() {
            try {
                const allToysData = await toyAPI.index();
                setAllToys(allToysData);
            } catch (err) {
                console.log(err)
            }
        }
        getAllToys()
    }, [])

    return (<>
        <section className="page-header">
            <h1>All Cat Toys</h1>
            <img src={string} alt="A ball of string" />
            <img src={mouse} alt="A mouse" />
            <img src={post} alt="A scratching post" />
            <img src={fish} alt="A fishy toy." />
        </section>
        <section>
            {allToys.map(toy => (
                <div key={toy.id} className="toy-index-card" style={{  borderColor: toy.color }}>
                    <div className="toy-index-card-bg" style={{  backgroundColor: toy.color }}></div>
                    <Link to={`/toys/${toy.id}`}>
                        <div className="toy-index-card-content">
                            <h2>{toy.name}</h2>
                            <p>A {closest(toy.color).name}</p>
                        </div>
                    </Link>
                </div>
            ))}
        </section>
    </>)
}
