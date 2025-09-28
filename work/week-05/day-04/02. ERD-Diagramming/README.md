<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Entity-Relationship Diagramming

An ERD is a visual representation of the data structure in a database. It helps model how entities (objects) relate to each other. 

- Entities: Represent objects or concepts (e.g., "Book", "Author", "Publisher").
- Attributes: Characteristics of entities (e.g., "title", "ISBN" for a Book).
- Relationships: Connections between entities (e.g., "Author writes Book").
- Cardinality: Defines how many instances of one entity relate to another (e.g., one Author can write many Books, but a Book can have multiple Authors).


Schema design refers to the actual implementation of a database's structure, defining how data is stored, organized, and related. It includes:

Tables (or Collections in NoSQL): Represent entities.
Columns (or Fields): Represent attributes.
Primary Keys: Unique identifiers for records.
Foreign Keys: References between tables to maintain relationships.
Indexes: Optimizations for faster queries.

### Types of relationships and ERD Diagramming

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

## Build an ERD from this RESTful Routing Table

We can use this [Visual Paradigm Online](https://online.visual-paradigm.com/diagrams/features/erd-tool/) website as a tool for building our own ERDs!

<h2>Bands</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/bands</td><td>index</td><td>List all bands</td></tr>
    <tr><td>POST</td><td>/bands</td><td>create</td><td>Create a new band</td></tr>
    <tr><td>GET</td><td>/bands/:id</td><td>show</td><td>Show details of a band</td></tr>
    <tr><td>PUT/PATCH</td><td>/bands/:id</td><td>update</td><td>Update a band</td></tr>
    <tr><td>DELETE</td><td>/bands/:id</td><td>destroy</td><td>Delete a band</td></tr>
</table>

<h2>Band Members</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/bands/:band_id/members</td><td>index</td><td>List all members of a band</td></tr>
    <tr><td>POST</td><td>/bands/:band_id/members</td><td>create</td><td>Add a member to a band</td></tr>
    <tr><td>GET</td><td>/bands/:band_id/members/:id</td><td>show</td><td>Show details of a band member</td></tr>
    <tr><td>PUT/PATCH</td><td>/bands/:band_id/members/:id</td><td>update</td><td>Update band member details</td></tr>
    <tr><td>DELETE</td><td>/bands/:band_id/members/:id</td><td>destroy</td><td>Remove a band member</td></tr>
</table>

<h2>Albums</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/albums</td><td>index</td><td>List all albums</td></tr>
    <tr><td>POST</td><td>/albums</td><td>create</td><td>Create a new album</td></tr>
    <tr><td>GET</td><td>/albums/:id</td><td>show</td><td>Show details of an album</td></tr>
    <tr><td>PUT/PATCH</td><td>/albums/:id</td><td>update</td><td>Update an album</td></tr>
    <tr><td>DELETE</td><td>/albums/:id</td><td>destroy</td><td>Delete an album</td></tr>
</table>

<h2>Songs</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/albums/:album_id/songs</td><td>index</td><td>List all songs in an album</td></tr>
    <tr><td>POST</td><td>/albums/:album_id/songs</td><td>create</td><td>Add a song to an album</td></tr>
    <tr><td>GET</td><td>/albums/:album_id/songs/:id</td><td>show</td><td>Show details of a song</td></tr>
    <tr><td>PUT/PATCH</td><td>/albums/:album_id/songs/:id</td><td>update</td><td>Update a song</td></tr>
    <tr><td>DELETE</td><td>/albums/:album_id/songs/:id</td><td>destroy</td><td>Delete a song</td></tr>
</table>

<h2>Concerts</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/concerts</td><td>index</td><td>List all concerts</td></tr>
    <tr><td>POST</td><td>/concerts</td><td>create</td><td>Create a new concert</td></tr>
    <tr><td>GET</td><td>/concerts/:id</td><td>show</td><td>Show details of a concert</td></tr>
    <tr><td>PUT/PATCH</td><td>/concerts/:id</td><td>update</td><td>Update a concert</td></tr>
    <tr><td>DELETE</td><td>/concerts/:id</td><td>destroy</td><td>Delete a concert</td></tr>
</table>

<h2>Music Venues</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/venues</td><td>index</td><td>List all music venues</td></tr>
    <tr><td>POST</td><td>/venues</td><td>create</td><td>Create a new venue</td></tr>
    <tr><td>GET</td><td>/venues/:id</td><td>show</td><td>Show details of a venue</td></tr>
    <tr><td>PUT/PATCH</td><td>/venues/:id</td><td>update</td><td>Update a venue</td></tr>
    <tr><td>DELETE</td><td>/venues/:id</td><td>destroy</td><td>Delete a venue</td></tr>
</table>
