import "./styles.css";
import catCollectorCat from "../../assets/images/splash.svg";
import logoType from "../../assets/images/logotype.svg";

export default function HomePage() {
  return (
    <section className="logo-container">
      <div className="home-cat-container">
        <img src={catCollectorCat} alt="The Cat Collector Cat" />
      </div>
      <img src={logoType} alt="Text reads: Cat Collector" />
    </section>
  )
}