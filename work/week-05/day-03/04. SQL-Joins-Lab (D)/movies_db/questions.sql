-- Test query!!
SELECT * FROM users;

-- 1. List all the movie titles and their corresponding directors.
SELECT m.title, d.name
FROM movies m
JOIN directors d ON m.director_id = d.director_id;

-- 2. Select the movie title and user name for all of the "favorites"
SELECT m.title, u.name
FROM users_movies um
JOIN users  u ON um.user_id  = u.user_id
JOIN movies m ON um.movie_id = m.movie_id;

-- 3. List the movies with the number of favorites they have.
SELECT m.title, COUNT(um.user_id) AS favorite_count
FROM movies m
LEFT JOIN users_movies um ON um.movie_id = m.movie_id
GROUP BY m.movie_id, m.title
ORDER BY favorite_count DESC, m.title;

-- 4. Directors + number of favorites for all their movies (desc)
SELECT d.name, COUNT(um.user_id) AS favorite_count
FROM directors d
JOIN movies m        ON m.director_id = d.director_id
LEFT JOIN users_movies um ON um.movie_id   = m.movie_id
GROUP BY d.director_id, d.name
ORDER BY favorite_count DESC, d.name;

-- 5. user name + director name + favorite count per (user, director)
SELECT u.name AS user_name,
       d.name AS director_name,
       COUNT(*) AS favorite_count
FROM users_movies um
JOIN users     u ON um.user_id  = u.user_id
JOIN movies    m ON um.movie_id = m.movie_id
JOIN directors d ON m.director_id = d.director_id
GROUP BY u.user_id, u.name, d.director_id, d.name
ORDER BY u.name, director_name;
