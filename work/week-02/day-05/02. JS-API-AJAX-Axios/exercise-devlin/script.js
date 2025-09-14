const randomDogUrl = 'https://dog.ceo/api/breeds/image/random';
const listAllBreedsUrl = 'https://dog.ceo/api/breeds/list/all';


/*** CACHED ELEMENTS*****/
const dogImgEl = document.getElementById("dogImage");
const dogBreedSelectEl = document.getElementById("dogsSelectTag");
const randomDogBtnEl = document.getElementById('getRandomDogButton');



/*** EVENT LISTENERS *****/
dogBreedSelectEl.addEventListener("click", async (evt) => {
    try {
        // console.log("this event listener is working!", evt.target.value, Boolean(evt.target.value))
        if(!evt.target.value) return;
        // console.log("the value was truthy", evt.target.value)
        // const dogBreed = evt.target.value;
        // const dogBreedURL = `https://dog.ceo/api/breed/${dogBreed}/images`;
        const res = await fetch(`https://dog.ceo/api/breed/${evt.target.value}/images`);
        const data = await res.json();
        // console.log("Fetched data:", data.message[0]);
        dogImgEl.setAttribute("src", data.message[0]);
        dogImgEl.setAttribute("alt", evt.target.value);
    } catch (err) {
        console.log(err);
    }
})

randomDogBtnEl.addEventListener("click", async () => {
    try {
        console.log("tsting random dog evet listener")
        const res = await fetch(randomDogUrl);
        const data = await res.json();
        console.log("Fetched random dog data: ", data.message);
        dogImgEl.setAttribute("src", data.message);
        dogImgEl.setAttribute("alt", data.message.split("/")[4]);
    } catch (err) {
        console.log(err);
    }
})



// console.log("Task 1");
// console.log("Task 2");
// console.log("Task 3");
// // Output: Task 1 → Task 2 → Task 3

// console.log("Task 9");
// setTimeout(() => console.log("Task 10 (delayed)"), 1000);
// console.log("Task 11");
// Output: Task 1 → Task 3 → Task 2 (after ~1s)

// fetch('https://jsonplaceholder.typicode.com/users')
//     .then(response => response.json())   // parse JSON
//     .then(data => { console.log(data) }) // use the JSON data
//     .catch(error => console.error('Error:', error))
//     .finally(console.log("Made it to the end"));

const url = 'https://jsonplaceholder.typicode.com/users';
async function fetchData(url) {
  try {
    // Await the fetch request
    const response = await fetch(url);
    
    // Check if response is OK
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    // Await parsing the JSON body
    const data = await response.json();
    // console.log("Fetched data:", data);
    return data; // Optional return
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    console.log("Fetch attempt finished (success or failure).");
  }
}

// fetchData(url);

async function example() {
    try {

    } catch (err) {

    } finally {

    }
}

async function getAllDogs() {
    try {
        const response = await fetch(listAllBreedsUrl);
        // console.log(response)
        const data = await response.json();
        // console.log(data)
        const allDogBreeds = Object.keys(data.message);
        allDogBreeds.forEach(breed => {
            // create new option element
            const newOptionEl = document.createElement("OPTION");
            // set value attribute to breed name
            newOptionEl.setAttribute("value", breed);
            // set textContent to breed name
            newOptionEl.textContent = breed;
            // appendChild element to parent select element
            dogBreedSelectEl.appendChild(newOptionEl)
        })
    } catch (err) {

    }
}

getAllDogs();