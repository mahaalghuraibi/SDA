// ---------------- Part 1: Random ----------------

// GRAB THE BUTTON ELEMENT FROM THE DOM
const randomBtn = document.getElementById("getRandomGiphyButton");
const imgEl = document.getElementById("giphyImageTag");
const titleEl = document.getElementById("giphyTitleDiv");

// ADD A CLICK EVENT LISTENER
randomBtn.addEventListener("click", GET);

// INSIDE THE EVENT HANDLER, MAKE A FETCH GET REQUEST TO THE giphyRandomApiUrl ENDPOINT
const giphyRandomEndpoint =
  "https://api.giphy.com/v1/gifs/random?api_key=2041494ca782403cb6055682a7943c75&rating=G";

async function GET() {
  const res = await fetch(giphyRandomEndpoint);
  const json = await res.json();

  // IN THE .THEN METHOD, PARSE THE JSON RESPONSE OBJECT AND FIND THE image_url key
  // CHANGE THE SRC ATTRIBUTE ON THE IMG TAG TO THE image_url KEY
  imgEl.src = json.data.images.original.url;

  // CHANGE THE INNER TEXT OF THE giphyTitleDiv TO THE title KEY
  titleEl.textContent = json.data.title;
}



// ---------------- Part 2: Trending ----------------

// GRAB THE BUTTON ELEMENT FROM THE DOM
const trendingBtn = document.getElementById("getTrendingGiphyButton");
const resultsEl = document.getElementById("searchGifs");

// ADD A CLICK EVENT LISTENER
trendingBtn.addEventListener("click", GETTrending);

// INSIDE THE EVENT HANDLER, MAKE A FETCH GET REQUEST TO THE giphyTrendingEndpoint
const giphyTrendingEndpoint =
  "https://api.giphy.com/v1/gifs/trending?api_key=2041494ca782403cb6055682a7943c75&rating=G";

async function GETTrending() {
  const res = await fetch(giphyTrendingEndpoint);
  const json = await res.json();

  // CLEAR OLD RESULTS
  resultsEl.innerHTML = "";

  // LOOP THROUGH THE DATA ARRAY AND DISPLAY EACH GIF
  json.data.forEach((gif) => {
    const card = document.createElement("div");
    card.innerHTML = `
      <img src="${gif.images.original.url}" alt="">
      <p>${gif.title}</p>
    `;
    resultsEl.appendChild(card);
  });
}



// ---------------- Part 3: Search ----------------

// GRAB THE BUTTON AND INPUT ELEMENTS FROM THE DOM
const searchBtn = document.getElementById("getSearchGiphyButton");
const searchInput = document.querySelector("input[name='user-input']");

// ADD A CLICK EVENT LISTENER
searchBtn.addEventListener("click", GETSearch);

// INSIDE THE EVENT HANDLER, MAKE A FETCH GET REQUEST TO THE giphySearchEndpoint
async function GETSearch() {
  const keyword = searchInput.value.trim();
  if (!keyword) return;

  const url = `https://api.giphy.com/v1/gifs/search?api_key=2041494ca782403cb6055682a7943c75&q=${encodeURIComponent(
    keyword
  )}&limit=10&rating=G`;

  const res = await fetch(url);
  const json = await res.json();

  // CLEAR OLD RESULTS
  resultsEl.innerHTML = "";

  // LOOP THROUGH THE DATA ARRAY AND DISPLAY EACH GIF
  json.data.forEach((gif) => {
    const card = document.createElement("div");
    card.innerHTML = `
      <img src="${gif.images.original.url}" alt="">
      <p>${gif.title}</p>
    `;
    resultsEl.appendChild(card);
  });
}

