import "./styles.css";
import GIFCard from "../../components/GIFCard/GIFCard";

export default function LandingPage({ trendingGifs }) {

    const trendingGifCards = trendingGifs.map(gif => (
        <GIFCard key={gif.id} gif={gif}/>
    ))

  return (
        <>
            <h3>Trending Gifs:</h3>
            <div className="trending-gifs-container">
                {trendingGifCards}
            </div>
        </>
    )
}
