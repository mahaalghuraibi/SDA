<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Students</td><td>GET</td><td>/students</td><td>No</td></tr>
    <tr><td>Students</td><td>GET</td><td>/students/{id}</td><td>No</td></tr>
    <tr><td>Students</td><td>POST</td><td>/students</td><td>Yes</td></tr>
    <tr><td>Students</td><td>PUT</td><td>/students/{id}</td><td>Yes</td></tr>
    <tr><td>Students</td><td>DELETE</td><td>/students/{id}</td><td>No</td></tr>
  </tbody>
</table>

<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Addresses</td><td>GET</td><td>/addresses</td><td>No</td></tr>
    <tr><td>Addresses</td><td>GET</td><td>/addresses/{id}</td><td>No</td></tr>
    <tr><td>Addresses</td><td>POST</td><td>/students/{student_id}/address</td><td>Yes</td></tr>
    <tr><td>Addresses</td><td>PUT</td><td>/addresses/{id}</td><td>Yes</td></tr>
    <tr><td>Addresses</td><td>DELETE</td><td>/addresses/{id}</td><td>No</td></tr>
  </tbody>
</table>

<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Instructors</td><td>GET</td><td>/instructors</td><td>No</td></tr>
    <tr><td>Instructors</td><td>GET</td><td>/instructors/{id}</td><td>No</td></tr>
    <tr><td>Instructors</td><td>POST</td><td>/instructors</td><td>Yes</td></tr>
    <tr><td>Instructors</td><td>PUT</td><td>/instructors/{id}</td><td>Yes</td></tr>
    <tr><td>Instructors</td><td>DELETE</td><td>/instructors/{id}</td><td>No</td></tr>
  </tbody>
</table>

<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Courses</td><td>GET</td><td>/courses</td><td>No</td></tr>
    <tr><td>Courses</td><td>GET</td><td>/courses/{id}</td><td>No</td></tr>
    <tr><td>Courses</td><td>POST</td><td>/courses</td><td>Yes</td></tr>
    <tr><td>Courses</td><td>PUT</td><td>/courses/{id}</td><td>Yes</td></tr>
    <tr><td>Courses</td><td>DELETE</td><td>/courses/{id}</td><td>No</td></tr>
  </tbody>
</table>

<h2>Courses Relations</h2>
<table border="1" width="100%">
  <thead>
    <tr>
      <th>HTTP method</th>
      <th>Path</th>
      <th>Action</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PUT</td>
      <td>/courses/{course_id}/students/{student_id}</td>
      <td>enroll</td>
      <td>enroll specific student in specific course.</td>
    </tr>
    <tr>
      <td>DELETE</td>
      <td>/courses/{course_id}/students/{student_id}</td>
      <td>remove</td>
      <td>remove specific student from specific course.</td>
    </tr>
    <tr>
      <td>PUT</td>
      <td>/courses/{course_id}/instructors/{instructor_id}</td>
      <td>enroll</td>
      <td>enroll specific instructor in specific course.</td>
    </tr>
    <tr>
      <td>DELETE</td>
      <td>/courses/{course_id}/instructors/{instructor_id}</td>
      <td>remove</td>
      <td>remove specific instructor from specific course.</td>
    </tr>
  </tbody>
</table>
