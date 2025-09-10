console.log("Hello World")

const logoImgEl = document.querySelector("#logo")
console.dir(logoImgEl)

const logoIdEl = document.getElementById("logo");
console.dir(logoIdEl)

const aTagEls = document.getElementsByTagName("A")
console.dir(aTagEls);
const aTagElsArr = Array.from(aTagEls)

aTagElsArr.forEach(el => {
    console.dir(el);
    el.textContent = "TEST";
})

const cardElsClass = document.getElementsByClassName("card");
console.dir(cardElsClass)
const cardElsClassArr = Array.from(cardElsClass);
cardElsClassArr.forEach(card => {
    console.dir(card)
    card.style.backgroundColor = "red";
})

const movieCardElsClass = document.querySelectorAll(".movie-card-start")
console.dir(movieCardElsClass)

movieCardElsClass.forEach(movieCardEl => {
    // console.dir(movieCardEl, "line 30")
    movieCardEl.className = "movie-card-finish";
    // movieCardEl.classList.add("movie-card-finish")
    // movieCardEl.classList.remove("movie-card-start")
});

// movieCardElsClass.forEach(movieCardEl => {
//     movieCardEl.style.border = "3px solid yellow";
// });

document.querySelectorAll(".movie-card > img").forEach(el => {
    el.src = "https://intheposter.com/cdn/shop/products/so-this-is-30-in-the-poster-1.jpg?v=1733910582";
    // el.setAttribute("src", "https://intheposter.com/cdn/shop/products/so-this-is-30-in-the-poster-1.jpg?v=1733910582");
});

const newDivEl = document.createElement("DIV");
newDivEl.classList.add("movie-card-start");
const newImgEl = document.createElement("IMG");
newImgEl.setAttribute("src", "https://intheposter.com/cdn/shop/products/so-this-is-30-in-the-poster-1.jpg?v=1733910582");
newImgEl.setAttribute("alt", "movie-poster");
const newMovieDescEl = document.createElement("P");
newMovieDescEl.textContent = "Joker: Folie à Deux (2024) is a psychological musical thriller directed by Todd Phillips, serving as the sequel to the 2019 film Joker. The movie stars Joaquin Phoenix reprising his role as Arthur Fleck, alongside Lady Gaga as Harleen 'Lee' Quinzel. Set primarily within the confines of Arkham State Hospital, the film delves into themes of duality, shared delusion, and the blurred lines between reality and fantasy.";

newDivEl.appendChild(newImgEl);
newDivEl.appendChild(newMovieDescEl);
console.log(newDivEl)

document.getElementById("movies-grid").appendChild(newDivEl)
