-- "\connect world" will allow us to connect to the database
-- "\x" this will format the information being printed in the console to make it easier.. try it without if you want!
-- !!We're counting on you, gumshoe. Find out where she's headed, send us the info, and we'll be sure to meet her at the gates with bells on!!
\connect world  
\x on         
\echo "SQL QUERIES!"

-- START FINDING CARMEN! --
-- Clue #1 (where): Carmen is at it again and we know she is not in 'South America', 'Europe' or 'Asia'! 
-- Let's find which countries she could be:
-- Write SQL query here


-- Clue #2 (sort / limit): We just received news that Carmen is in the most populated country out of the previous list above.
-- Write SQL query here


-- Clue #3 (group by, count, having): Carmen is on the move! She has now moved to one of the countries with the greatest number of different languages spoken.
-- Write SQL query here


-- Clue #4 (subqueries / nesting): Carmen is definitely in one of the countries with more than 10 languages. We are hearing it is the most populated one so that she can blend in!
-- Write SQL query here


-- Clue #5 (matching strings): Oh no, she pulled a switch. She is headed to the city with a name similar to her's and ha the highest population.
-- Write SQL query here


-- Clue #6 (join, group, string match): We've got her! We just received a tip that Carmen is in the city where they speak italian, with a population over one million, is located in South America, and has 'elo' in the name!
-- Write SQL query here