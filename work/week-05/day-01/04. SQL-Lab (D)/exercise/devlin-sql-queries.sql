-- "\connect world" will allow us to connect to the database
-- "\x" this will format the information being printed in the console to make it easier.. try it without if you want!
-- !!We're counting on you, gumshoe. Find out where she's headed, send us the info, and we'll be sure to meet her at the gates with bells on!!
-- \connect world  
\x off       
\echo "SQL QUERIES!"

-- START FINDING CARMEN! --
-- Clue #1 (where): Carmen is at it again and we know she is not in 'South America', 'Europe' or 'Asia'! 
-- Let's find which countries she could be:
-- Write SQL query here

-- SELECT name, population, region FROM countries
-- WHERE region = 'South America';

-- SELECT name, population, region FROM countries
-- WHERE region NOT IN ('South America', 'Asia', 'Europe')
-- LIMIT 10;


-- Clue #2 (sort / limit): We just received news that Carmen is in the most populated country out of the previous list above.
-- Write SQL query here

-- SELECT name, population FROM countries
-- WHERE region = 'South America'
-- ORDER BY population ASC
-- LIMIT 10;

-- SELECT name, population FROM countries
-- WHERE name IN ('Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Albania', 'Andorra', 'Netherlands', 'Antilles', 'United Arab Emirates', 'Armenia', 'American Samoa')
-- ORDER BY population DESC
-- LIMIT 1;
 

-- Clue #3 (group by, count, having): Carmen is on the move! She has now moved to one of the countries with the greatest number of different languages spoken.
-- Write SQL query here

-- SELECT language, COUNT(*) FROM countrylanguages
-- GROUP BY language
-- ORDER BY count(*) DESC;

-- SELECT countrycode, COUNT(*) from countrylanguages
-- GROUP BY countrycode
-- ORDER BY COUNT(*) DESC;

-- Clue #4 (subqueries / nesting): Carmen is definitely in one of the countries with more than 10 languages. We are hearing it is the most populated one so that she can blend in!
-- Write SQL query here

-- SELECT name FROM countries
-- WHERE code IN (
--     SELECT countrycode
--     FROM countrylanguages
--     WHERE language = 'Italian'
-- );

-- SELECT name, population FROM countries
-- WHERE code IN (
--     SELECT countrycode FROM countrylanguages
--     GROUP BY countrycode
--     HAVING COUNT(*) BETWEEN 4 AND 8
--     -- ORDER BY COUNT(*) DESC
-- )
-- ORDER BY population DESC
-- LIMIT 1;


-- Clue #5 (matching strings): Oh no, she pulled a switch. She is headed to the city with a name similar to her's and ha the highest population.
-- Write SQL query here

SELECT name, countrycode, population FROM cities
WHERE name ILIKE 'San%'
ORDER BY population DESC
LIMIT 1;


-- Clue #6 (join, group, string match): We've got her! We just received a tip that Carmen is in the city where they speak italian, with a population over one million, is located in South America, and has 'elo' in the name!
-- Write SQL query here
--  South America, and has 'elo' 
SELECT cities.name AS cityName, countries.name, cities.population AS City_Population, countries.region, lang.language from countries
JOIN countrylanguages lang ON countries.code = lang.countrycode
JOIN cities ON countries.code = cities.countrycode
WHERE lang.language = 'Italian'
AND cities.population > 2000000
AND countries.region = 'South America'
AND cities.name ILIKE '%elo%';
