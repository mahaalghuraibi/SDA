<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

<img src="https://i.imgur.com/PE14J3Y.jpg">
<br><br>

# Intro to **Full-Stack Development**

Full-stack development refers to the practice of building both the front-end (client-side) and back-end (server-side) of a web application. A **full-stack developer** is someone proficient in working with both ends of the technology stack, meaning they can build an entire application from start to finish.

What are some examples of full-stack web applications?

## **Key Components of Full-Stack Development**  

### **1. Front-End (Client-Side) Development:**  
- Deals with what users see and interact with in a web browser.  
- **Technologies:**  
  - **HTML** (Structure)  
  - **CSS** (Styling)  
  - **JavaScript** (Functionality)  
  - **Front-end frameworks/libraries:** React, Angular, Vue.js  

### **2. Back-End (Server-Side) Development:**  
- Handles the logic, database operations, and user authentication.  
- **Technologies:**  
  - **Programming languages:** Node.js, **Python**, Java, PHP, Ruby, C#  
  - **Frameworks:** Express.js, **Django**, Flask, Spring Boot, Laravel  
  - **Databases:** SQL (MySQL, PostgreSQL), NoSQL (MongoDB, Firebase)  
  - **Authentication & APIs:** JWT, OAuth, GraphQL, REST APIs  

### **3. Database Management:**  
- Storing, retrieving, and managing data.  
- **Relational Databases:** MySQL, PostgreSQL  
- **NoSQL Databases:** MongoDB, Firebase  

### **4. DevOps & Deployment:**  
- Setting up and managing servers, CI/CD, cloud hosting.  
- **Technologies:** Docker, Kubernetes, AWS, Firebase, Vercel, Netlify  

### **5. In this course we will work with:**
<img src="https://i.imgur.com/GuogOfX.png" style="width:200px; height:200px">
<img src="https://i.imgur.com/MjX4aD7.png" style="max-width:200px; max-height:200px">
<br/><br/>


<h1> Core Concepts</h1>

## Client/Server Architecture

<img src="https://i.imgur.com/clxiqnO.png" style="width:80%">

- The terms **client** and **server** can refer to both a **physical device** (computer, tablet, phone, etc.) but can also refer to a **software process**. For example:
	- Database software such as PostgreSQL and web servers like Apache are examples of software processes behaving as servers.
	- Browser software such as Chrome or Firefox are examples of software clients.

- Physical **servers** connected to the Internet are also referred to as **hosts**.

- Web developers usually think of a "web browser" when they hear "client".

- Note that during development, your computer will plays the role of BOTH client and web server.

## HTTP

### What is HTTP?

- **Hypertext Transfer Protocol (HTTP)** is an application-level network protocol that powers the communications across the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web), more commonly referred to as just **the Web**.

- **HTTP is fundamental to web development** - regardless of which back-end or front-end web technology/framework is used.

- When a user interacts with an amazing **web application** we developed, it's **HTTP** that informs the **web application** what the **browser** wants and it's **HTTP** that delivers the goods from the server back to the browser. For example, when the user browses to our app:

	<img src="https://i.imgur.com/JDFHoZl.png" style="width:80%">

- When the response is received by the client, that request/response cycle has ended and there will be no further HTTP communications unless another request is sent by the client.

- HTTP itself does not maintain any information regarding previous requests between client and server - this makes HTTP a _stateless_ protocol. However, it is possible to remember "state" using cookies or by sending data in the request's body (data payload).

### Making HTTP Requests

- Let's open a new tab in Chrome, open DevTools, and click on the _Network_ tab where we can inspect HTTP requests and responses.

- Now let's browse to General Assembly's site by typing **generalassemb.ly** in the address bar...

- Wow! Each one of those lines represents a separate HTTP request made to a server!  Find the line in the left-side pane with **generalassemb.ly** and click on it:

	<img src="https://i.imgur.com/fuED3VM.png" style="width:80%">

- In the pane on the right you will find all of the information about a particular HTTP request. Select the _Headers_ tab and explore!:

	<img src="https://i.imgur.com/44W3zEE.png" style="width:80%">

### Anatomy of HTTP Request/Response Messages

- The following diagrams an HTTP Request and Response Message: 

	<img src="https://i.imgur.com/kCuWuw7.png">

- Notice they both have a **Start Line** followed by **Headers**, an **Empty line**, and finally the **Body** of the message.
	
### The Status Code of the Response

- The [status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) in the first line of the response message informs us how the request/response went.

- It is always a three-digit number that falls within the following ranges/categories:
	- 1xx Informational
	- 2xx Success
	- 3xx Redirection
	- 4xx Client Error
	- 5xx Server Error

- Most HTTP responses will have a _status code_ of `200`, which means _OK_. You also might be familiar with the _status code_ of `404` - _Not Found_.

### The Body of the Message

- The **Body** contains the data being sent to the server (if any) and the data being returned by the server

- The **Content-Type** header is a [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) and helps the browser determine what to do with the data being sent in the **body** of the HTTP response. For example:
	- **text/html**: The browser will parse the **body** as HTML and, depending on how the HTTP request was initiated, usually **replace** the browser window's content with the newly received HTML.
	- **image/png**

- Although the HTTP protocol is text-based, the content in the body can be binary, for example, images are typically transferred in a binary format.

### THE Two Key Components of an HTTP Request 

- We saw earlier that every HTTP request message begins with a request-line like this:

	```
	GET /puppies HTTP/1.1
	```

- **The two key components of any HTTP request are**:
	- The **HTTP method** (`GET` in the example above), and
	- The _request target_, which developers refer to as the **path**, **endpoint**, or the **URL** (although more accurately is a **URI**)

- The reason these are the key components are because most web frameworks use them to match routes defined on the server (more on routes in a bit).

### HTTP Methods

- [HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), are used to indicate the desired **action** to be performed for a given resource (specified by the URL) on the server.

- The fact that they indicate **action** is why they are also at times called **HTTP Verbs**.

- We'll be using the following HTTP Methods when we start defining our application's routes: 

	| HTTP Method (Verb) | Desired Action on Server |
	|:-:|:-:|
	| `GET` | The GET method requests a representation of the specified resource (URL). Requests using GET should only retrieve data. |
	| `POST` | The POST method is used to create a resource on the server. |
	| `PUT` | The PUT method is used to update a resource on the server. |
	| `DELETE` | The DELETE method deletes the specified resource. |

### URL

- **URL** stands for **Uniform Resource Locator**.

- It informs the server of what resource the client wants to GET. create (POST), DELETE, etc.

- Here's the complete anatomy of a URL:

	<img src="https://i.imgur.com/w1igQx0.png" style="display:inline-clock;width:80%">

- Developers often refer to just the **path** (incorrectly) as a URL.

### Ways to Send HTTP Requests From the Browser

- These are ways that a browser can send an HTTP Request:

	| Action | HTTP Method(s) Possible |
	|---|---|
	| Using the _address bar_ | GET |
	| User submits an HTML form | POST, GET (used for searches) |
	| User clicks a link | GET |
	| Using JavaScript | All Methods can be sent using [AJAX](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX)|

Until we get to Unit 4, our apps will rely on the user clicking links and submitting forms to interact with the app - that's it!

### Ways to Send HTTP Requests Without Using the Browser

- There are plenty of developer tools that enable us to issue HTTP requests to servers without using a browser.

- One tool we use later in the course is [Postman](https://www.getpostman.com/).

- If you prefer to use a command-line tool, our computers already have a tool called [cURL](https://en.wikipedia.org/wiki/CURL).

### How HTTP Requests Run Code on the Server

- As full-stack web developers, we'll create front-ends that display in the browser.

- As a user interacts with the app by clicking links and submitting forms, they will cause HTTP requests to be sent to our back-end web application.

- In our web app on the back-end, we will create **routes** that listen for these requests from the front-end, and...

- Those **routes** will map HTTP requests to our back-end **code**!

- As an example, you want your app to add a new user to your database when they sign up...

<img src="https://i.imgur.com/ltB5IYA.png">

1. The user submits the sign up form.

2. An HTTP request message with the form's data in the request body leaves the browser.

3. The HTTP request is received by the web app's routing and, in this case, would match the route defined to match a `POST /users` (**HTTP Method** & **Path**) HTTP request.

4. The purpose of a defined route is to map an HTTP request to code which is typically a function defined in the "controller" module.  The controller function would perform any necessary data operations, etc.

5. The controller function ultimately responds with an HTTP Response which can either:
    - Containing an HTML page in the message body (in the case of a GET request)
    - Or, with a Status Code of 302 (Redirect), make the browser issue a new GET request.
<br/><br/>

# ORMs, MPAs, Web Frameworks:

We've covered the basics of what full-stack development includes. Recognizing that html, css, and javascript make our front-end come alive and that the backend (server) requires a programming language and a database to help us get a server up, running, and ready to respond to requests with data that are able to persist. While this is enough, we do have access to functionality that can make our lives easier.

What might I be talking about?

If I were to ask you to create a server, would you know how to do this? If we know that hundreds of websites have already been created, shouldn't that mean that the boilerplate code has already been written to setup a server without having to write the basics every single time?

What about interacting with a SQL database? Would you want to have to write the SQL code evey single time, or would you want access to functionality that allows us to develop more quickly?

Thankfully these technologies exist and developers overtime have given us access to their software that allows to expedite these processes.

## Web Frameworks

The first such technology we will discuss is called a **web framework**. A web framework is a collection of pre-written code, libraries, and tools that help developers build web applications efficiently. It provides a structured way to handle common tasks such as routing, database interactions, authentication, and API development, reducing the need to write everything from scratch. 

Like I've said many many times before -> "developers are lazy". When I say this I don't actually mean they are lazy individuals, what I do mean is that we are looking for the quickest, most efficient way to do our jobs and not write any code that we do not need to write. We do out best to keep things **DRY (Don’t Repeat Yourself)** and we also try our best to **KISS (Keep It Simple, Stupid)**.

The packages, libraries, and pre-built technologies that we can work with help us to KISS and keep things DRY.

In this course we will specificlly be working with a **web framework** called **Django**, which we will discuss in depth this afternoon!

## ORMs - Object Relational Mappers

<img src="https://i.imgur.com/MHZhLw2.jpg">

At some point most web applications interact with a database. Can you imagine writing SQL queries for every single database request? What if there were a library that existed that allowed you to do something like 

- `db.create(new_item)` instead of... 

- `INSERT INTO table_name (column1, column2, column3,etc)
VALUES (value1, value2, value3, etc);`

Far easier and more efficient (YAY, ABSTRACTION!) -> This is the power of using ORMs!

An ORM (Object-Relational Mapper) is a programming tool or library that allows developers to interact with a relational database using object-oriented programming instead of writing raw SQL queries.

An ORM maps database tables to classes, rows to objects, and columns to attributes, allowing you to work with databases in a more intuitive and structured way.

While there are many ORM libraries out there, we will be working with Django's built in ORM to accept our information / requests and write the queries for us to interact with our postgresql database. 

## MPA - Multi-Page Application

An MPA (Multi-Page Application) is a type of web application where each interaction or request results in a new page being loaded from the server. Unlike SPAs (Single-Page Applications), MPAs reload the entire page when navigating between different sections of the site.

How MPAs Work
The browser requests a new HTML page from the server.
The server processes the request, retrieves data, and sends back a fully rendered HTML page.
When a user clicks a link, a new request is sent, and a full page reload occurs.

<br/>
<img src="https://dz2cdn1.dzone.com/storage/temp/13596577-traditional-and-spa.jpg">

<br/><br/>

We will be creating an two examples of each of these application types in this cohort. One we will do together, and the second you will build in your own by following the example we do in class. 

The first type, **multi-page application**, will be created using **HTML, Django, DjangoORM, & PostgreSQL** to deliver individual HTML pages to the front end, based on requests from the front end. 

The second type, **single-page application** will use **React, (DRF) Django Rest Framework + ORM, postgreSQL** to deliver a single html page to the front end while responding to additional requests with JSON (javascript object notation) to deliver data directly to React and react will dynamically update information accordingly. We will do the same application again, "Cat Collector", as a guided walk-through together and then you will once again build your own version. 

**HINT** -> the capstone project is essentially the exact same concept as doing the (SPA) version of Cat Collector a third time... we are setting you up for success so you can also make an effort to try more advanced functionlity on your own!