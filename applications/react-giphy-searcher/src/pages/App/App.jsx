import './App.css'
import { useState, useEffect } from 'react'
import { Route, Routes } from 'react-router';
import GiphyDetailPage from '../GiphyDetailPage/GiphyDetailPage';
import LandingPage from '../LandingPage/LandingPage';
import * as giphyAPI from "../../utilities/giphy"
import Navigation from '../../components/Navigation/Navigation';

function App() {
  const [trendingGifs, setTrendingGifs] = useState([]);

  useEffect(function () {
    async function getTrendingGifs() {
      const data = await giphyAPI.getTrendingGifs()
      setTrendingGifs(data.data)
    }
    getTrendingGifs()
  }, [])

  async function searchGIFs(evt, searchText, setSearchText) {
    evt.preventDefault()
    const searchResults = await giphyAPI.searchGifs(searchText);
    console.log(searchResults.data)
    setTrendingGifs(searchResults.data)
    setSearchText("")

  }

  return (<div>
    <Navigation searchGIFs={searchGIFs} />
    <Routes>
      <Route path="/*" element={<LandingPage trendingGifs={trendingGifs} />} />
      <Route path="/giphy/:id" element={<GiphyDetailPage trendingGifs={trendingGifs} />} />
    </Routes>
  </div>);
}

export default App
