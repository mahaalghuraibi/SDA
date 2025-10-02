-- this will allow us to connect to the database
-- this will format the information being printed in the console to make it easier.. try it without if you want!
\connect ladder  
\x on

-- 4.1 Select the title of all movies.
SELECT title
FROM Movies;
-- 4.2 Show all the distinct ratings in the database.
SELECT DISTINCT rating
FROM Movies;
-- 4.3  Show all unrated movies.
SELECT *
FROM Movies
WHERE rating IS NULL OR rating = '';
-- 4.4 Select all movie theaters that are not currently showing a movie.
SELECT *
FROM MovieTheaters
WHERE movie IS NULL;

-- 4.5 Select all data from all movie theaters 
SELECT *
FROM MovieTheaters
LEFT JOIN Movies
  ON MovieTheaters.movie = Movies.code;
-- and, additionally, the data from the movie that is being shown in the theater (if one is being shown).
-- 4.6 Select all data from all movies and, if that movie is being shown in a theater, show the data from the theater.
SELECT *
FROM Movies
LEFT JOIN MovieTheaters
  ON MovieTheaters.movie = Movies.code;
-- 4.7 Show the titles of movies not currently being shown in any theaters.
SELECT m.title
FROM Movies m
LEFT JOIN MovieTheaters t ON t.movie = m.code
WHERE t.movie IS NULL;
-- 4.8 Add the unrated movie "One, Two, Three".
INSERT INTO Movies (code, title, rating)
VALUES (8, 'One, Two, Three', NULL);

-- 4.9 Set the rating of all unrated movies to "G".
UPDATE Movies
SET rating = 'G'
WHERE rating IS NULL OR rating = '';

-- 4.10 Remove movie theaters projecting movies rated "NC-17".
DELETE FROM MovieTheaters
WHERE movie IN (
  SELECT code FROM Movies WHERE rating = 'NC-17'
);
