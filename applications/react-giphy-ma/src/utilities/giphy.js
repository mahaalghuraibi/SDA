const API_KEY = import.meta.env.VITE_GIPHY_API_KEY;
const BASE = "https://api.giphy.com/v1/gifs";

function withKey(url){
  const joiner = url.includes("?") ? "&" : "?";
  return `${url}${joiner}api_key=${API_KEY}`;
}

export async function getTrendingGifs(limit = 24){
  const url = withKey(`${BASE}/trending?limit=${limit}`);
  const res = await fetch(url);
  if(res.ok) return res.json();
  throw new Error("Bad request (trending)");
}

export async function searchGifs(query, limit = 24){
  const url = withKey(`${BASE}/search?q=${encodeURIComponent(query)}&limit=${limit}`);
  const res = await fetch(url);
  if(res.ok) return res.json();
  throw new Error("Bad request (search)");
}

export async function getGifById(id){
  const url = withKey(`${BASE}/${id}`);
  const res = await fetch(url);
  if(res.ok) return res.json();
  throw new Error("Bad request (get by id)");
}
