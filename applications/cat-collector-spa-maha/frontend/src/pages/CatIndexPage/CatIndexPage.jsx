import "./styles.css"
import coolCat from "../../assets/images/cool-cat.svg";
import happyCat from "../../assets/images/happy-cat.svg";
import teacupCat from "../../assets/images/teacup-cat.svg";
import catInBox from "../../assets/images/cat-in-box.svg";
import { useEffect, useState } from "react";
import CatIndexCard from "../../components/CatIndexCard";
import * as catAPI from "../../utilities/cat-api";


export default function CatIndexPage() {
    const [allCats, setAllCats] = useState([]);
//    {name: 'Lolo', breed: 'tabby', description: 'Kinda rude.', age: 3},
//     {name: 'Sachi', breed: 'tortoiseshell', description: 'Looks like a turtle.', age: 0},
//     {name: 'Fancy', breed: 'bombay', description: 'Happy fluff ball.', age: 4},
//    {name: 'Bonk', breed: 'selkirk rex', description: 'Meows loudly.', age: 6},

    const displayAllCats = allCats?.map((c, idx) => (
        <CatIndexCard key={idx} cat={c} />
    ))

 useEffect(function(){
    async function getAllCats() {
        const allCatData = await catAPI.index()
        console.log(allCatData , 'line-25 CatIndexPage')
        setAllCats(allCatData)
    }
    if (allCats.length === 0)
        getAllCats()
 },[])


    return (<>
        <section className="page-header">
            <h1>Cat List</h1>
            <img src={coolCat} alt="A cool cat" />
            <img src={happyCat} alt="A happy cat" />
            <img src={teacupCat} alt="A cat in a teacup" />
            <img src={catInBox} alt="A cat in a box" />
        </section>
        <section className="index-card-container">
            {displayAllCats}
        </section>
    </>)
}