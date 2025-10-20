import "./styles.css";
import { useState, useEffect } from "react";
import { useParams } from "react-router";
import skaterCat from "../../assets/images/sk8r-boi-cat.svg";
import * as catAPI from "../../utilities/cat-api";


export default function CatDetailPage() {
    const [catDetail, setCatDetail] = useState(null);
    const { id } = useParams();

    useEffect(() => { 
        async function getAndSetDetail() {
            try {
                console.log("Enter use effect")
              const cat = await catAPI.show(id);
                setCatDetail(cat);
            } catch (err) {
                console.log(err);
                setCatDetail(null);
            }
        }
        if (id) getAndSetDetail()
    }, [id])

    if (!catDetail) return <h3>Your cat details will display soon</h3>

    return (
        <section className="detail-cat-container">
          <div className="detail-cat-img">
            <img src={skaterCat} alt="A skater boy cat" />
          </div>
          <div className="cat-details">
            <h1>{ catDetail.name }</h1>
            <h2>{ catDetail.age > 0 
                  ? `A ${catDetail.age} year old ${catDetail.breed}` 
                  : `A ${catDetail.breed} kitten.`} 
            </h2>
            <p>{ catDetail.description }</p>
          </div>
        </section>
    )
}