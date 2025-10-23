import "./styles.css";
import coolCat from "../../assets/images/cool-cat.svg";
import happyCat from "../../assets/images/happy-cat.svg";
import teacupCat from "../../assets/images/teacup-cat.svg";
import catInBox from "../../assets/images/cat-in-box.svg";
import { useEffect, useState } from "react";
import CatIndexCard from "../../components/CatIndexCard";
import * as catAPI from "../../utilities/cat-api";

export default function CatIndexPage() {
  const [allCats, setAllCats] = useState([]);

  const displayAllCats = allCats.map((c) => (
    <CatIndexCard key={c.id} cat={c} />
  ));

  useEffect(function () {
    async function getAllCats() {
      const allCatData = await catAPI.index();
      console.log(allCatData, "line-25 CatIndexPage");
      setAllCats(allCatData);
    }
    getAllCats();
  }, []);

  return (
    <>
      <section className="page-header">
        <h1>Cat List</h1>
        <img src={coolCat} alt="A cool cat" />
        <img src={happyCat} alt="A happy cat" />
        <img src={teacupCat} alt="A cat in a teacup" />
        <img src={catInBox} alt="A cat in a box" />
      </section>

      <section className="index-card-container">{displayAllCats}</section>
    </>
  );
}
