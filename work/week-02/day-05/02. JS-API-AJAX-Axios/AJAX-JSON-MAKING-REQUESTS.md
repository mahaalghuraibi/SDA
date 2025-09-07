<img src="https://i.imgur.com/PE14J3Y.jpg">

# 🌐 AJAX, JSON, and Making Requests

Now that you understand **HTTP requests**, let’s look at how we can send and receive data in the browser using **AJAX** and **JSON**.

## 🔹 What is AJAX?
- **AJAX** stands for **Asynchronous JavaScript and XML**.
- Despite the name, today we mostly use **JSON instead of XML**.
- AJAX allows web pages to:
  - Send and receive data **without refreshing the page**.
  - Communicate with a server **asynchronously** in the background.


## 🔹 How AJAX Works
1. JavaScript makes an HTTP request (GET, POST, etc.) to a server.
2. The server processes the request and sends back a response (often JSON).
3. JavaScript updates the page dynamically with the response data.


## 🔹 What is JSON?
- **JSON** stands for **JavaScript Object Notation**.
- It is a lightweight format for storing and exchanging data.
- JSON is based on JavaScript object syntax but is language-independent.
- Data is represented as **key-value pairs**.

### Example JSON:
```json
{
  "name": "Alice",
  "age": 25,
  "isStudent": true,
  "courses": ["Math", "Science", "History"]
}
```

### Key Points:
- Keys must be in **double quotes**.
- Values can be:
  - Strings
  - Numbers
  - Booleans
  - Arrays
  - Objects
- JSON is often used in **APIs** to send data between client and server.

## API
Where does all of this information come from? From a server using their API (application programming interface). As developers / future full stack developers, we will design our own application programming interfaces that are hosted on a server and we will use RESTful APIs to accept requests and respond with JSON so that we can deliver content to the clients requesting our data...

Let's check out a few example API's:

- [Dog API](https://dog.ceo/dog-api/)
- [Star Wars API](https://swapi.co/)
- [Pokemon API](https://pokeapi.co/)
- [Game of Thrones API](https://anapioficeandfire.com/)

We can add a [chrome extension](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en) to make JSON easier to read.


## Request Types
- method
    - GET
    - POST
    - DELETE
    - PATCH/PUT
- url
    - https://swapi.co/api/people/1
    - https://pokeapi.co/api/v2/pokemon/2
- data (optional)
- [RESPONSE CODES](https://www.restapitutorial.com/httpstatuscodes)
- 

## Making Requests and Asynchronous Programming
The modern way to do AJAX in JavaScript is with the **Fetch API**. This fetch request is built into nodeJS version 18+ and all modern browsers. We can use it to make requests across the internet to get information from different servers. An example request will provide the url or address we would like to make a request to and an options object that can provide more detailed information if we need to make requests other than type `"GET"`. Today we will not need any other request types. We just want to learn the basics.

### What is Asynchronous Programming?
Asynchronous programming is a way of writing code that allows tasks to run **without blocking** the execution of other tasks. Instead of waiting for one task to finish before starting the next, asynchronous code can continue running while certain operations (like fetching data from an API, reading a file, or querying a database) complete in the background.

This is especially important in JavaScript because it runs on a **single-threaded event loop**. If one task blocks the thread (like a slow API call), the entire program would freeze until it finishes — unless we handle it asynchronously.

### Synchronous vs. Asynchronous

- **Synchronous (blocking)**  
  Tasks are executed one after another. Each task waits for the previous one to complete.  
  ```js
  console.log("Task 1");
  console.log("Task 2");
  console.log("Task 3");
  // Output: Task 1 → Task 2 → Task 3
  ```

- **Asynchronous (non-blocking)**  
  Some tasks are delegated (to the browser or Node.js APIs) and handled in the background. Once they are done, they notify the main thread.  
  ```js
  console.log("Task 1");
  setTimeout(() => console.log("Task 2 (delayed)"), 1000);
  console.log("Task 3");
  // Output: Task 1 → Task 3 → Task 2 (after ~1s)
  ```

### Promises

A **Promise** is a JavaScript object that represents the result of an asynchronous operation.  
It acts as a placeholder for a value that will be available **now**, **later**, or **never**.

---

### States of a Promise
A Promise can be in one of three states:

1. **Pending** → The initial state, operation not completed yet.
2. **Fulfilled** → The operation completed successfully, and the promise has a resulting value.
3. **Rejected** → The operation failed, and the promise has a reason (error).

Once a promise is **fulfilled** or **rejected**, it is considered **settled** and cannot change state.

---

### Creating a Promise w/ .then()
```js
// Make an AJAX request to get data
  fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => response.json())   // parse JSON
    .then(data => { console.log(data) }) // use the JSON data
    .catch(error => console.error('Error:', error));
    .finally(console.log("Made it to the end"))
```



### ASYNC AWAIT
**`async/await`** is a modern JavaScript syntax for handling asynchronous operations more **readably and cleanly** than chaining `.then()` and `.catch()` on Promises.  
- `async` functions always **return a Promise**.  
- `await` pauses the execution of the `async` function until the awaited Promise resolves or rejects.  
- It allows you to write asynchronous code that **looks synchronous**, making it easier to read, debug, and maintain.

---

#### History
- Introduced in **ECMAScript 2017 (ES8)**, finalized in **June 2017**.  
- Before `async/await`, asynchronous code relied on **callbacks** or **Promise chains**.  
- `async/await` is syntactic sugar over Promises; it does **not** change how asynchronous operations work internally.  
- Supported in **Node.js 8+** and all modern browsers.

---

#### Why It Makes a Difference
1. **Improves readability** – avoids deeply nested `.then()` chains (callback hell).  
2. **Simplifies error handling** – use standard `try/catch/finally` blocks.  
3. **Makes sequential logic easier** – you can `await` multiple asynchronous calls in order.  
4. **Keeps code maintainable** – easier to understand flow of asynchronous operations.

#### Complete Example with Try / Catch / Finally

```js
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
    console.log("Fetched data:", data);
    return data; // Optional return
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    console.log("Fetch attempt finished (success or failure).");
  }
}
```
---

## Why Use Promises?
- They handle asynchronous operations more cleanly than callbacks.
- They prevent "callback hell".
- They provide centralized error handling with `.catch()`.
- They support chaining multiple async steps with `.then()`.

---

## Key Methods
- **`.then(onFulfilled)`** → Handles the resolved value.
- **`.catch(onRejected)`** → Handles errors or rejection.
- **`.finally(onSettled)`** → Runs regardless of success or failure.
- **`Promise.all([...])`** → Runs multiple promises in parallel, waits for all.
- **`Promise.allSettled([...])`** → Waits for all promises to finish, no matter the outcome.

## EXERCISE
Take a look at the `./exercise` folder where we can find a `readme.md` to follow and some starter code so that we can make requests in real time and handle the responses!