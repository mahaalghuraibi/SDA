-- this will allow us to connect to the database
-- this will format the information being printed in the console to make it easier.. try it without if you want!
\connect ladder  
\x on  

-- 7.1 Who received a 1.5kg package?
SELECT DISTINCT Recipient
FROM Package
WHERE weight = 1.5;
-- The result is "Al Gore's Head".
-- 7.2 What is the total weight of all the packages that he sent?
SELECT SUM(p.weight) AS total_sent_weight
FROM package p
JOIN client c ON p.sender = c.accountnumber
WHERE c.name = 'Al Gores Head';
