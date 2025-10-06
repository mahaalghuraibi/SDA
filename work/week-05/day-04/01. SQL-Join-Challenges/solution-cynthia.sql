-- film title, description, release year, rating, and special feature
-- SELECT title, description, release_year, rating, special_features FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- WHERE rating = 'PG-13'
-- AND special_features @> ARRAY['Trailers']
-- AND actor_id = 23;

-- Get the film_id, title, actor_id, and actor name for all actors who participated in film_id = 157.
-- SELECT film.film_id, title, actor.actor_id, first_name FROM actor
-- JOIN film_actor ON actor.actor_id = film_actor.actor_id
-- JOIN film ON film.film_id = film_actor.film_id
-- WHERE film_actor.film_id = 157;

-- Get the film title, description, release year, rating, special features, 
-- and genre for all 'Horror' movies with a rental_rate of 0.99.
SELECT title, description, release_year, rating, special_features, name as genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE name = 'Horror' AND rental_rate = 0.99;
