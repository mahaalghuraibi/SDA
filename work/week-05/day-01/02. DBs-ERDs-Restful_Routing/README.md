<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

<img src="https://i.imgur.com/EItmcVX.jpeg" width="750px">
<br/><br/>

<div align="center">
<h1>Databases, ERD Diagrams, and Restful Routing</h1>
</div>

## Road Map

- What is a Database?
- Relational vs. Non-Relational Databases
- Data Modeling
- ERD Diagramming
- RESTful Routing

## What is a Database? Why do we need one?

You just setup a brand new account on the latest social media craze. You're excited for your beautiful profile and it took you over an hour to get everything exactly how you wanted. You say 'hi' to friends, share some photos, make a new post, and feel amazing.

You wake up the next morning and excitedly log back in to see how many, likes, comments, etc. and its ALL GONE!

**What happened?**

There was no way to persist the information... so computer scientists created databases.

**Databases** are a way to organize and save, or persist, data. Without databases banks can't electronically remember who you are, social media can't track how many likes you've received, and nobody would be able to receive any emails or text messages. The world would not be anywhere near as productive, connected, and advanced as we are.

As far back as the 1950's/60's computer scientists starting developing file systems that would allow for persistence of data. However, the systems were unstructred, inconsistent, and lacked the ability to increase data redundancy. 

In 1970 a computer scientist named Edgar F. Codd came up with a solution by organizing data in tables called relations. It was until 1979 that a relational database became commercially available by the company, Oracle. For years this style of database grew in popularity due to their speed, accuracy, and organizational abilities. They have remained that way since their inception.

Meanwhile, in the background, NoSQL databases have existed since 1966 (via IBM) due to NASA's requirement for handling large amounts of data for the Apollo missions. Even though this approach to data management has existed for this long, it wasn't until the 2000's that it became publically popular. The reason being the NoSQL style of database is capable of handling massive amounts of unstructured or semi-structured data while also scaling horizontally across servers and being more flexible. With the internet boom, this was great for developers looking to develop quickly. 

So let's take a look at some of the most popular databases that are still in use and then dig in to comparing SQL to NoSQL databases.

There are lots of different database systems - check out [this site](http://db-engines.com/en/ranking) that tracks the popularity of different database systems.

As you can see, **Relational Database Management Systems (RDMS)** are by far the most popular - they've been around since the 1960s. They are more commonly referred to as **SQL Databases** because they are designed and accessed using **Structured Query Language**.

However, you'll also see that **MongoDB** is by far the most popular **NoSQL** database system. (created in 2009).

There are several varieties of NoSQL databases. MongoDB is of the **document-based** variety because it stores and retrieves _documents_.

## NoSQL vs. Relational SQL Databases

### Terminology

<img src="https://i.imgur.com/XdV3hSs.png" style="width:900px">

As diagramed above, there is a one-to-one mapping of the key concepts of a database.

Either a SQL database or MongoDB can be used for most applications.

However, in general:

- **Relational Databases** are preferred in mission-critical financial applications such as banking, stock trading, etc., due to their strength of handling [transactions](https://en.wikipedia.org/wiki/Database_transaction). They are not very good however on handling data that can't be strictly organized into tables of structured columns because they have a strict **schema** (structure) they must adhere to.

- **NoSQL** is preferred for storing vast amounts of unstructured data, such as in social-media type applications.  MongoDB is also a great choice when prototyping applications because it is **schema-less** and more adaptable to change.

What do these differences look like in real time?

<img src="https://imgur.com/hlIPXMO.jpeg" style="width:900px">

<br/><br/>
# OR IN A MORE CONCRETE EXAMPLE:


<table border="1">
    <tr>
        <th>Feature</th>
        <th>SQL (Relational Databases)</th>
        <th>NoSQL (Non-Relational Databases)</th>
    </tr>
    <tr>
        <td>Image</td>
        <td><img src="https://i.imgur.com/1Wog5Tk.png" style="width:350px"></td>
        <td><img src="https://i.imgur.com/flGcVfu.jpeg" style="width:350px"></td>
    </tr>
    <tr>
        <td><strong>Data Structure</strong></td>
        <td>Structured data stored in tables with predefined schemas.</td>
        <td>Flexible data models (document, key-value, column, or graph-based).</td>
    </tr>
    <tr>
        <td><strong>Scalability</strong></td>
        <td>Vertically scalable (scale up by adding more CPU, RAM).</td>
        <td>Horizontally scalable (scale out by adding more servers).</td>
    </tr>
    <tr>
        <td><strong>Performance</strong></td>
        <td>Optimized for complex queries, joins, and transactions.</td>
        <td>Faster for big data and real-time applications.</td>
    </tr>
    <tr>
        <td><strong>Query Language</strong></td>
        <td>Uses SQL (Structured Query Language) for standardized queries.</td>
        <td>Uses different query methods (e.g., JSON-based, key-value lookups).</td>
    </tr>
    <tr>
        <td><strong>Data Consistency</strong></td>
        <td>Follows ACID properties, ensuring strong consistency.</td>
        <td>Uses eventual consistency, trading off strict ACID compliance.</td>
    </tr>
    <tr>
        <td><strong>Use Cases</strong></td>
        <td>Ideal for transactional applications, banking, and structured data.</td>
        <td>Best for big data, real-time analytics, social networks, and IoT.</td>
    </tr>
    <tr>
        <td><strong>Flexibility</strong></td>
        <td>Rigid schema, requiring schema changes for modifications.</td>
        <td>Schema-less, allowing dynamic and evolving data structures.</td>
    </tr>
    <tr>
        <td><strong>Joins and Relationships</strong></td>
        <td>Supports complex relationships with foreign keys and joins.</td>
        <td>Generally avoids joins, using denormalization for speed.</td>
    </tr>
    <tr>
        <td><strong>Maintenance</strong></td>
        <td>Requires careful schema design and database tuning.</td>
        <td>Easier to modify and evolve with application changes.</td>
    </tr>
    <tr>
        <td><strong>Examples</strong></td>
        <td>MySQL, PostgreSQL, SQL Server, Oracle.</td>
        <td>MongoDB, Cassandra, Redis, DynamoDB.</td>
    </tr>
</table>


## What is Data Modeling

**Data modeling** is the process of structuring and organizing data to define how it will be stored, managed, and used in a database. It involves creating diagrams, schemas, and rules to represent relationships between different data elements, ensuring consistency, efficiency, and accuracy in data storage and retrieval.

### Core Concepts
Thinking back to our two main database types, each has its own version of the core concepts below. A database will hold a table/collection, the table/collection will hold rows/documents/entities, and each document will hold attributes/properties. 

Do the rows/documents/entities sound like anything we have worked with before when we mention that they have properties?

<table border="1">
    <tr>
        <th>Concept</th>
        <th>Description</th>
        <th>Purpose</th>
    </tr>
    <tr>
        <td><strong>Entity</strong></td>
        <td>An object or thing in the database (e.g., User, Product, Order).</td>
        <td>Represents real-world data objects.</td>
    </tr>
    <tr>
        <td><strong>Attribute</strong></td>
        <td>A property or characteristic of an entity (e.g., User has Name, Email).</td>
        <td>Stores meaningful details about an entity.</td>
    </tr>
    <tr>
        <td><strong>Primary Key (PK)</strong></td>
        <td>A unique identifier for each record in a table (e.g., UserID).</td>
        <td>Ensures each record is uniquely identifiable.</td>
    </tr>
    <tr>
        <td><strong>Foreign Key (FK)</strong></td>
        <td>An attribute in one table that refers to the primary key in another table.</td>
        <td>Establishes relationships between entities.</td>
    </tr>
    <tr>
        <td><strong>Relationship</strong></td>
        <td>A connection between two entities (e.g., Users place Orders).</td>
        <td>Defines how entities interact with each other.</td>
    </tr>
    <tr>
        <td><strong>Cardinality</strong></td>
        <td>Defines the number of relationships between entities (e.g., One-to-Many, Many-to-Many).</td>
        <td>Determines how records are linked across tables.</td>
    </tr>
    <tr>
        <td><strong>Normalization</strong></td>
        <td>The process of organizing data to reduce redundancy.</td>
        <td>Improves data consistency and storage efficiency.</td>
    </tr>
    <tr>
        <td><strong>Denormalization</strong></td>
        <td>The process of combining tables to improve performance.</td>
        <td>Enhances query speed at the cost of some redundancy.</td>
    </tr>
    <tr>
        <td><strong>Index</strong></td>
        <td>A data structure that improves the speed of data retrieval.</td>
        <td>Boosts query performance and search efficiency.</td>
    </tr>
    <tr>
        <td><strong>Schema</strong></td>
        <td>The blueprint of a database, defining tables, fields, and relationships.</td>
        <td>Provides a structured framework for data storage.</td>
    </tr>
    <tr>
        <td><strong>Constraints</strong></td>
        <td>Rules applied to database fields (e.g., NOT NULL, UNIQUE, CHECK).</td>
        <td>Ensures data validity and integrity.</td>
    </tr>
</table>

## Creating Relationships

What do we mean by creating realationships? Let's have a discussion about real world relationships and how we can emulate those relationships through data modeling.

How do recognize or distinguish from one person vs another person? What is **unique** to each person regardless of whether we know them or not? 

### Unique IDs

<table border="1">
    <tr>
        <th>Identifier</th>
        <th>Document Type</th>
        <th>Region/Country</th>
        <th>Purpose</th>
    </tr>
    <tr>
        <td><strong>ISBN (International Standard Book Number)</strong></td>
        <td>Books</td>
        <td>Worldwide</td>
        <td>Uniquely identifies books and their editions.</td>
    </tr>
    <tr>
        <td><strong>ISSN (International Standard Serial Number)</strong></td>
        <td>Magazines, Journals, Newspapers</td>
        <td>Worldwide</td>
        <td>Identifies periodicals and serial publications.</td>
    </tr>
    <tr>
        <td><strong>DOI (Digital Object Identifier)</strong></td>
        <td>Academic Papers, Research Articles</td>
        <td>Worldwide</td>
        <td>Identifies scholarly and research documents.</td>
    </tr>
    <tr>
        <td><strong>Library of Congress Control Number (LCCN)</strong></td>
        <td>Books, Library Records</td>
        <td>United States</td>
        <td>Used by the U.S. Library of Congress for cataloging books.</td>
    </tr>
    <tr>
        <td><strong>OCLC Number</strong></td>
        <td>Library Catalog Records</td>
        <td>Worldwide</td>
        <td>Identifies records in the WorldCat library catalog system.</td>
    </tr>
    <tr>
        <td><strong>Patent Number</strong></td>
        <td>Patents</td>
        <td>Worldwide</td>
        <td>Identifies registered patents for inventions.</td>
    </tr>
    <tr>
        <td><strong>National ID Number</strong></td>
        <td>Identification Cards</td>
        <td>Country-Specific</td>
        <td>Used for personal identification and government records.</td>
    </tr>
    <tr>
        <td><strong>Passport Number</strong></td>
        <td>Passports</td>
        <td>Worldwide</td>
        <td>Unique identifier for international travel documents.</td>
    </tr>
    <tr>
        <td><strong>Social Security Number (SSN)</strong></td>
        <td>Government Identification</td>
        <td>United States</td>
        <td>Used for tax, employment, and social benefits.</td>
    </tr>
    <tr>
        <td><strong>Driver’s License Number</strong></td>
        <td>Driver’s Licenses</td>
        <td>Country-Specific</td>
        <td>Identifies individuals authorized to drive.</td>
    </tr>
    <tr>
        <td><strong>Vehicle Identification Number (VIN)</strong></td>
        <td>Vehicles</td>
        <td>Worldwide</td>
        <td>Uniquely identifies motor vehicles.</td>
    </tr>
    <tr>
        <td><strong>Tax Identification Number (TIN)</strong></td>
        <td>Tax Records</td>
        <td>Country-Specific</td>
        <td>Used for tax reporting and government revenue tracking.</td>
    </tr>
    <tr>
        <td><strong>International Standard Music Number (ISMN)</strong></td>
        <td>Music Scores</td>
        <td>Worldwide</td>
        <td>Identifies printed music publications.</td>
    </tr>
    <tr>
        <td><strong>International Article Number (EAN/UPC)</strong></td>
        <td>Product Barcodes</td>
        <td>Worldwide</td>
        <td>Identifies consumer goods and retail products.</td>
    </tr>
    <tr>
        <td><strong>International Standard Recording Code (ISRC)</strong></td>
        <td>Audio Recordings</td>
        <td>Worldwide</td>
        <td>Uniquely identifies music recordings.</td>
    </tr>
    <tr>
        <td><strong>Clinical Trial Number</strong></td>
        <td>Medical Research Documents</td>
        <td>Worldwide</td>
        <td>Identifies registered clinical trials.</td>
    </tr>
    <tr>
        <td><strong>International Treaty Serial Number</strong></td>
        <td>Government Treaties</td>
        <td>Worldwide</td>
        <td>Identifies international treaties and agreements.</td>
    </tr>
</table>

## Putting these ideas to use;

Somehow we need to be able to generate these relationships in the digital world using this unique id concept. The way we do this is through storing these id's on another table's field to show that there is a relationship between these two entitites.

### For example:

If I have a profile on facebook and I decide to make a new post, each of these concepts is it's own model. In order to show the relationship between the two models, I will store my **PROFILE_id** in the **POST** model/entity. This way when I query my database of posts for all posts that contain that ID, it can return all posts related to me specifically and not ALL of the posts that exist.

What are other types of relationships we can emulate from the real world to the digital world?

### Types of relationships and ERD Diagramming

The three core relationships we will cover are called "one-to-one", "one-to-many", and "many-to-many". Our goal here is to discuss, conceptually, how to recognize the relaionship types and then be able to show those relationships in a diagram form so we can express it in a visual aid for others to understand.

#### One to One
A one-to-one relationship means that the each entitity only has one direct relationship to the other entity. An example of this in the real world would be the Earth only having ONE Moon, the solar system having only ONE Sun, or a country having one national flag. You can implicitly set the model relationships, meaning, you decide within your project if a user only gets one email to sign up with for that account. 

**ERD Diagram showing one-to-one:**<br/>
The standard showing this is: "-----"<br/><br/>
<img src="https://i.imgur.com/5MVdbbK.png" style="width:350px">

#### One to Many
A one-to-many relationship means that one entity can be related to several of the other entities. A real world relationship would be a music venue having many concerts or a user having many posts. Once again, you can implicitly set what relationships you want. It depends on how you construct your database and the way those relationships are created.

**ERD Diagram showing one-to-many:**<br/>
The standard showing this is: "-----<"<br/><br/>
<img src="https://i.imgur.com/nKc0Wgy.png" style="width:350px">

#### One to Many to Many
A many-to-many relationship means that each entity can be related to multiple other entities of the other entity. That's a tongue twister! Consider a concept like a books can have many authors and many authors can create many books. OR movies can have many actors and many actors can belong to many movies. 

**ERD Diagram showing one-to-many:**<br/>
The standard showing this is: ">-----<"<br/><br/>
<img src="https://i.imgur.com/H7SAlDt.png" style="width:350px">

### Final Notes on Relationships and Diagramming

These diagrams help explain to an engineer the models they should expect to find in a project, and the relationships they will expect to find in a project. It then explains how the database will be setup and all the fields / properties you should epxect to see on the model. Once we move through the basics of using SQL, we will work towards showing how to create these relationships and reinforce these concepts so you can put them to use.
<br/><br/>

# RESTful Routing
Lastly, we need to have a way to generate these relationships through code. If you remember, we previously discussed CRUD. 

- (C) Create, 
- (R) Read, 
- (U) Update,
- (D) Delete,

We also discussed HTTP Methods to connect specific verbs (methods) to running specific code. We now need to show how to be more specific by matching the **http method** to a specific **path** so we can then ensure that we run the code we want to execute.

RESTful routing is one of many ways to approach organizing code in your server. There are certainly other options, it just happens to be one of the most popular and quite easy to use. So we will learn it!

The architural pattern itself was not introduced until the year 2000 via Roy Fielding who felt there was an easier approach to web development and organization to code. Since it's creation it has become increasingly more popular over time and today, is considered a standard.

## RESTful Routing Explained:

RESTful routing stands for Representational State Transfer and uses our resources (entities in our database) as the focal point of how to organize our code. If you haven't heard this phrase yet, "Data is the single source of truth", is a popular phrase within the software / tech community. It means that we use our hard coded data to make and inform decisions throughout our applications. 

#### For example:
If I need to decide whether or not to display a person's age on web page, what if the data we have stored on the profile doesn't include the age?

```javascript
// using react example
export default function DisplayProfile({ profile })
	
	return (
		<div>
			{profile.name ? <h3>{profile.name}<h3/> : "" }
			{profile.age ? <h3>{profile.age}<h3/> : "" }
		<div/>
	)
```

The example above uses the data to decide what to display. We can make these decisions constantly throughout our applications. The point is we can also use our data to make decisions on how to organize, architect, design our servers. In this case we refer to our data as **RESOURCES** in our application. A **RESOURCE** is the same concept as a **MODEL** (which defines how to store data in the database). From we use our resources to generate the paths for matching to code in our servers.<br/><br/>

## RESTful Routes to CRUD Mapping

> Example resource: **posts**

HTTP Method<br>(Verb) | Path/Endpoint/URI  | CRUD Operation | Typical<br>Controller Action | Has Data<br>Payload
-----------|------------------|------------------|:---:|:---:
GET     | /posts          | Read all _posts_ | index | No
GET     | /posts/:id      | Read a specific _post_ | show | No
POST    | /posts          | Create a new _post_ | create | Yes
PUT     | /posts/:id      | Update specified _post_  | update | Yes
DELETE  | /posts/:id      | Delete specified _post_ | delete | No

# Additional Common Non-RESTful (CRUD-less) Routes

HTTP Method<br>(Verb) | Path/Endpoint/URI  | Purpose | Typical<br>Controller Action |Has Data<br>Payload
-----------|------------------|------------------|:---:|:---:
GET     | /posts/new          | Return view (form) to add a new _post_ | new | No
GET     | /posts/:id/edit     | Return view (form) to edit a _post_ | edit | No

# Routing for Related Resources (One:Many & Many:Many Relationships)

HTTP Method<br>(Verb) | Path/Endpoint/URI  | CRUD Operation<br>or Purpose | Note
-----------|------------------|------------------|:---:
GET     | /posts/:id/comments | Read all _comments_ for a _post_ | No payload
GET     | /comments/:id | Read one _comment_ for a _post_ | "Shallow" route / No payload
GET     | /posts/:id/comments/new | n/a (Non-RESTful) | OPTIONALLY display a dedicated form used to create a nested resource
POST     | /posts/:id/comments | Create a _comment_ for a _post_ (1:M) | Needs Payload
PUT     | /comments/:id      | Update specified _comment_  | "Shallow" route / Needs payload
DELETE  | /comments/:id      | Delete specified _comment_ | "Shallow" route / No payload
POST     | /posts/:postId/blogs/:blogId | Associate a _post_ with a _blog_ (M:M) | No payload
POST     | /posts/:postId/blogs | Associate a _post_ with a _blog_ (M:M) | id of blog included in payload vs endpoint