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
import string from "../../assets/images/string.svg";
import mouse from "../../assets/images/mouse.svg";
import fish from "../../assets/images/fish.svg";
import DisplayCatToys from "../../components/DisplayCatToys/DisplayCatToys";

const MEALS = {
  B: "Breakfast",
  L: "Lunch",
  D: "Dinner",
};

export default function CatDetailPage() {
  const [catDetail, setCatDetail] = useState(null);
  const [catFeedings, setCatFeedings] = useState([]);
  const [toysCatHas, setToysCatHas] = useState([]);
  const [toysCatDoesntHave, setToysCatDoesntHave] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    async function getAndSetDetail() {
      const catDetailData = await catAPI.show(id);
      setCatDetail(catDetailData.cat);
      setCatFeedings(catDetailData.feedings);
      setToysCatHas(catDetailData.toysCatHas);
      setToysCatDoesntHave(catDetailData.toysCatDoesntHave);
    }
    if (id) getAndSetDetail();
  }, [id]);

  async function addPhoto(catId, formData) {
    try {
      const updatedCat = await catAPI.addPhoto(catId, formData);
      setCatDetail(updatedCat);
    } catch (err) {
      setCatDetail({ ...catDetail });
    }
  }

  async function handleAddToy(evt, toyId) {
    try {
      evt.preventDefault();
      const toyData = await catAPI.addToyToCat(catDetail.id, toyId);
      setToysCatHas(toyData.toysCatHas);
      setToysCatDoesntHave(toyData.toysCatDoesntHave);
    } catch (err) {
      setToysCatHas([...toysCatHas]);
      setToysCatDoesntHave([...toysCatDoesntHave]);
    }
  }

  async function handleRemoveToy(evt, toyId) {
    try {
      evt.preventDefault();
      const toyData = await catAPI.removeToyFromCat(catDetail.id, toyId);
      setToysCatHas(toyData.toysCatHas);
      setToysCatDoesntHave(toyData.toysCatDoesntHave);
    } catch (err) {
      setToysCatHas([...toysCatHas]);
      setToysCatDoesntHave([...toysCatDoesntHave]);
    }
  }

  if (!catDetail) return <h3>Your cat details will display soon</h3>;

  const catToys = toysCatHas.map((toy) => (
    <DisplayCatToys
      key={toy.id}
      toy={toy}
      submitFunction={handleRemoveToy}
      formAction="Take Toy"
    />
  ));

  const availableToys = toysCatDoesntHave.map((toy) => (
    <DisplayCatToys
      key={toy.id}
      toy={toy}
      submitFunction={handleAddToy}
      formAction="Give Toy"
    />
  ));

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

          <h3>{catDetail.name}'s Toys</h3>
          <div className="subsection-content">
            {toysCatHas.length > 0 ? (
              catToys
            ) : (
              <p className="no-toys">{catDetail.name} doesn't have any toys!</p>
            )}
          </div>

          <h3>Available Toys</h3>
          <div className="subsection-content">
            {availableToys.length > 0 ? (
              availableToys
            ) : (
              <p className="all-toys">{catDetail.name} already has all the available toys 🥳</p>
            )}
          </div>
        </section>
      </div>
    </>
  );
}
