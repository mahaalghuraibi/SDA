\connect movies_joins_lab;

-- Test query!!
SELECT * FROM users;

-- 1. List all the movie titles and their corresponding directors.
SELECT movies.title, directors.name
FROM movies
JOIN directors ON movies.director_id = directors.director_id;

-- 2. Select the movie title and user name for all of the "favorites"
SELECT movies.title, users.name
FROM users_movies
JOIN users  ON users_movies.user_id  = users.user_id
JOIN movies ON users_movies.movie_id = movies.movie_id;

-- 3. List the movies with the number of favorites they have.
SELECT movies.title, COUNT(users_movies.user_id) AS favorite_count
FROM movies
LEFT JOIN users_movies ON users_movies.movie_id = movies.movie_id
GROUP BY movies.movie_id, movies.title
ORDER BY favorite_count, movies.title;

-- 4. Directors + number of favorites for all their movies (desc)
SELECT directors.name, COUNT(users_movies.user_id) AS favorite_count
FROM directors
JOIN movies        ON movies.director_id = directors.director_id
LEFT JOIN users_movies ON users_movies.movie_id   = movies.movie_id
GROUP BY directors.director_id, directors.name
ORDER BY favorite_count DESC, directors.name;

-- 5. user name + director name + favorite count per (user, director)
SELECT users.name AS user_name,
       directors.name AS director_name,
       COUNT(*) AS favorite_count
FROM users_movies
JOIN users     ON users_movies.user_id  = users.user_id
JOIN movies    ON users_movies.movie_id = movies.movie_id
JOIN directors ON movies.director_id    = directors.director_id
GROUP BY users.user_id, users.name, directors.director_id, directors.name
ORDER BY users.name, directors.name;
