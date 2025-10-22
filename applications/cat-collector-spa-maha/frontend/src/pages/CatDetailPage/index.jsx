import "./styles.css";
import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import * as catAPI from "../../utilities/cat-api";
import skaterCat from "../../assets/images/sk8r-boi-cat.svg";
import catCone from "../../assets/images/cat-cone.svg";
import catOniGirl from "../../assets/images/cat-onigiri.svg";
import kittyKabob from "../../assets/images/kitty-kabob.svg";
import FeedingForm from "../../components/Forms/FeedingForm";
import AddPhotoForm from "../../components/Forms/AddPhotoForm";
import * as feedingsAPI from "../../utilities/feedings-api";
import string from "../../assets/images/string.svg";
import mouse from "../../assets/images/mouse.svg";
import fish from "../../assets/images/fish.svg";
import * as toysAPI from "../../utilities/toy-api";

const MEALS = {
  B: "Breakfast",
  L: "Lunch",
  D: "Dinner",
};

export default function CatDetailPage() {
  const [catDetail, setCatDetail] = useState(null);
  const [catFeedings, setCatFeedings] = useState([]);
  const [allToys, setAllToys] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    async function getAndSetDetail() {
      const cat = await catAPI.detail(id);
      const feedings = await feedingsAPI.catFeedings(id);
      const toys = await toysAPI.index();
      setCatDetail(cat);
      setCatFeedings(feedings);
      setAllToys(toys);
    }
    if (id) getAndSetDetail();
  }, [id]);

  async function addPhoto(catId, formData) {
    try {
      const updatedCat = await catAPI.addPhoto(catId, formData);
      setCatDetail(updatedCat);
    } catch (err) {
      console.log(err);
      setCatDetail({ ...catDetail });
    }
  }

  async function handleAddToy(toyId) {}
  async function handleRemoveToy(toyId) {}

  if (!catDetail) return <h3>Your cat details will display soon</h3>;

  return (
    <>
      <section className="detail-cat-container">
        <div className="cat-img">
          {catDetail.photo?.url ? (
            <img
              src={catDetail.photo.url}
              alt={`A photo of ${catDetail.name}`}
              className="usr-img"
            />
          ) : (
            <img src={skaterCat} alt="A skater boy cat" />
          )}
        </div>

        <div className="cat-details">
          <h1>{catDetail.name}</h1>
          <h2>
            {catDetail.age > 0
              ? `A ${catDetail.age} year old ${catDetail.breed}`
              : `A ${catDetail.breed} kitten.`}
          </h2>
          <p>{catDetail.description}</p>

          <div className="cat-actions">
            <Link to={`/cats/edit/${catDetail.id}`} className="btn warn">
              Edit
            </Link>
            <Link
              to={`/cats/confirm_delete/${catDetail.id}`}
              className="btn danger"
            >
              Delete
            </Link>
          </div>
        </div>

        <section>
          <AddPhotoForm cat={catDetail} addPhoto={addPhoto} />
        </section>
      </section>

      <div className="feedings-toy-container">
        <section className="feedings">
          <div className="subsection-title">
            <h2>Feedings</h2>
            <img src={catCone} alt="An ice cream cone cat" />
            <img src={catOniGirl} alt="A cat as onigiri" />
            <img src={kittyKabob} alt="A kabob of kittens" />
          </div>

          <h3>Add a Feeding</h3>
          <FeedingForm
            catDetail={catDetail}
            catFeedings={catFeedings}
            setCatFeedings={setCatFeedings}
          />

          {catFeedings.length > 0 ? (
            <>
              <h3>Past Feedings</h3>
              <table>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Meal</th>
                  </tr>
                </thead>
                <tbody>
                  {catFeedings.map((meal, ind) => (
                    <tr key={ind}>
                      <td>{meal.date}</td>
                      <td>{MEALS[meal.meal]}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </>
          ) : (
            <div className="subsection-content">
              <p>⚠️ {catDetail.name} has not been fed!</p>
            </div>
          )}
        </section>

        <section className="toys">
          <div className="subsection-title">
            <h2>Toys</h2>
            <img src={string} alt="A ball of string" />
            <img src={mouse} alt="A mouse" />
            <img src={fish} alt="A fishy toy" />
          </div>
          <h3>Available Toys</h3>
          <div className="subsection-content">
            {allToys.map((toy) => (
              <div key={toy.id} className="toy-container">
                <div className="toy-info">
                  <div
                    className="color-block"
                    style={{ backgroundColor: toy.color }}
                  ></div>
                  <Link to={`/toys/${toy.id}`}>
                    <p>A {toy.color} {toy.name}</p>
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </>
  );
}
