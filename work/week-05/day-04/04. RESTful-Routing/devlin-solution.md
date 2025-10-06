### Devlin Solution - RESTful Routing from ERD


<h2>Studios</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/studios</td><td>index</td><td>List all studios</td></tr>
    <tr><td>POST</td><td>/studios</td><td>create</td><td>Create a new studio</td></tr>
    <tr><td>GET</td><td>/studios/:id</td><td>show</td><td>Show details of a studio</td></tr>
    <tr><td>PUT/PATCH</td><td>/studios/:id</td><td>update</td><td>Update a studio</td></tr>
    <tr><td>DELETE</td><td>/studios/:id</td><td>destroy</td><td>Delete a studio</td></tr>
</table>

<h2>Movies</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/movies</td><td>index</td><td>List all movies</td></tr>
    <tr><td>POST</td><td>/movies</td><td>create</td><td>Create a new movie</td></tr>
    <tr><td>GET</td><td>/movies/:id</td><td>show</td><td>Show details of a movie</td></tr>
    <tr><td>PUT/PATCH</td><td>/movies/:id</td><td>update</td><td>Update a movie</td></tr>
    <tr><td>DELETE</td><td>/movies/:id</td><td>destroy</td><td>Delete a movie</td></tr>
</table>

<h2>New Movie</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>POST</td><td>/studios/:studio_id/movies</td><td>create</td><td>Create a new movie with relationship to studio.</td></tr>
</table>

<h2>Directors</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/directors</td><td>index</td><td>List all directors</td></tr>
    <tr><td>POST</td><td>/directors</td><td>create</td><td>Create a new director</td></tr>
    <tr><td>GET</td><td>/directors/:id</td><td>show</td><td>Show details about a director.</td></tr>
    <tr><td>PUT/PATCH</td><td>/directors/:id</td><td>update</td><td>Update a director entry</td></tr>
    <tr><td>DELETE</td><td>/directors/:id</td><td>destroy</td><td>Delete a director</td></tr>
</table>

<h2>Associate a Director to a Movie</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>PUT</td><td>/movies/:movie_id/directors/:directors_id</td><td>create</td><td>Create a new relationship between movie and director.</td></tr>
</table>

<h2>Casts</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>POST</td><td>/movies/:movie_id/casts</td><td>create</td><td>Create a new cast.</td></tr>
    <tr><td>GET</td><td>/casts/:id</td><td>show</td><td>Show details about a director.</td></tr>
    <tr><td>EDIT</td><td>/casts/:id/edit</td><td>show</td><td>Show the page to edit the details.</td></tr>
    <tr><td>PUT/PATCH</td><td>/casts/:id</td><td>update</td><td>Update a director entry</td></tr>
    <tr><td>DELETE</td><td>/casts/:id</td><td>destroy</td><td>Delete a director</td></tr>
</table>

<h2>Actors</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>GET</td><td>/actors</td><td>index</td><td>List all actors</td></tr>
    <tr><td>POST</td><td>/actors</td><td>create</td><td>Create a new director</td></tr>
    <tr><td>GET</td><td>/actors/:id</td><td>show</td><td>Show details about a director.</td></tr>
    <tr><td>PUT/PATCH</td><td>/actors/:id</td><td>update</td><td>Update a director entry</td></tr>
    <tr><td>DELETE</td><td>/actors/:id</td><td>destroy</td><td>Delete a director</td></tr>
</table>

<h2>Associate a Actors to a Cast</h2>
<table border="1">
    <tr><th>HTTP Verb</th><th>Path</th><th>Action</th><th>Description</th></tr>
    <tr><td>PUT</td><td>/casts/:cast_id/actors/:actors_id</td><td>create</td><td>Create a new relationship between an actor and cast.</td></tr>
</table>