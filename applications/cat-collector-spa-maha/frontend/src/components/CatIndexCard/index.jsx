import "./styles.css";
import skaterCat from "../../assets/images/sk8r-boi-cat.svg";
import { Link } from "react-router";

export default function CatIndexCard({ cat }) {

    return (
      <div className="cat-index-card">
          <Link to={`/cats/${cat.id}`}>
              <div className="cat-index-card-content">
                  <img src={skaterCat} alt="A skater boy cat" />
                  <h2>{cat.name}</h2>
                  <p>{cat.age > 0 ? `A ${cat.age} year old ${cat.breed}` : `A ${cat.breed} kitten.`}</p>
                  <p><small>{cat.description}</small></p>
              </div>
          </Link>
      </div>
    )
}