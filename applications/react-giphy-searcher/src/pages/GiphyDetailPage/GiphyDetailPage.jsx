import { useEffect, useState } from 'react';
import { useParams } from "react-router";
import "./styles.css";

export default function GiphyDetailPage({ trendingGifs }) {
    const [gifDetail, setGifDetail] = useState(null);
    const { id } = useParams();

    useEffect(() => { 
        const gifData = trendingGifs.find(gif => gif.id === id);
        setGifDetail(gifData);
    }, [id]) 

    if (!gifDetail) return <h3>Your gif details will display soon</h3>

    return (
        <div className="giphy-detail-container">
            <h1>{gifDetail.title}</h1>
            <img src={gifDetail.images.downsized_large.url} alt={gifDetail.alt_text} />
            <div className="giphy-details">
                <h5>Upload Date: </h5>
                <h5>{gifDetail.import_datetime}</h5>
                <h5>Rating: </h5>
                <h5>{gifDetail.rating}</h5>
                <h5>Source: </h5>
                <h5>{gifDetail.source}</h5>
            </div>
        </div>
    )
}