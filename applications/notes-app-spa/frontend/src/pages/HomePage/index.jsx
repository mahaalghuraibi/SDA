import "./styles.css";
import moodImg from "../../assets/images/mood.jpg";
import logoType from "../../assets/images/today-s-mood-277365833.webp";

export default function HomePage() {
  return (
    <section className="logo-container">
      <div className="home-mood-container">
        <img src={moodImg} alt="Mood Notes Main" />
      </div>
      <img src={logoType} alt="Text reads: Mood Notes" />
    </section>
  );
}
