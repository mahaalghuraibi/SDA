\connect sakila_pg;
\x off
------------------------------------------------



--1 Get the name, last name, email, and address of all customers located in the city ‘Santiago de los Caballeros’.

SELECT 
  c.first_name, 
  c.last_name, 
  c.email, 
  a.address
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city = 'Santiago de los Caballeros';

-- 2 Get the film title, description, release year, rating, special features, and genre (category) for all movies in the 'Sci-Fi' category.

SELECT
  f.title,
  f.description,
  f.release_year,
  f.rating,
  f.special_features,
  c.name AS category
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Sci-Fi';

-- 3 Get the actor ID, actor name, film title, description, and release year for all movies featuring the actress ‘WHOOPI’.

SELECT
  a.actor_id,
  a.first_name || ' ' || a.last_name AS actor_name,
  f.title,
  f.description,
  f.release_year
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE a.first_name ILIKE 'WHOOPI%' OR a.last_name ILIKE 'WHOOPI%'
ORDER BY f.title;

-- 4 Get the name, last name, email, and address of all customers from store_id = 1 who live in cities with IDs 1, 42, 312, and 459.

