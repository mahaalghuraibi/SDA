-- this will allow us to connect to the database
-- this will format the information being printed in the console to make it easier.. try it without if you want!
\connect ladder  
\x on

-- 5.1 Select the name of all the pieces.
SELECT name
FROM Pieces;
-- 5.2  Select all the providers' data.
SELECT *
FROM Providers;
-- 5.3 Obtain the average price of each piece (show only the piece code and the average price).
SELECT piece, AVG(price) AS avg_price
FROM Provides
GROUP BY piece;
-- 5.4  Obtain the names of all providers who supply piece 1.
SELECT DISTINCT p.name
FROM Providers p
JOIN Provides pr ON p.code = pr.provider
WHERE pr.piece = 1;


-- 5.5 Select the name of pieces provided by provider with code "HAL".
SELECT DISTINCT pi.name
FROM Pieces pi
JOIN Provides pr ON pi.code = pr.piece
WHERE pr.provider = 'HAL';
-- 5.6
-- ---------------------------------------------
-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Interesting and important one.
-- For each piece, find the most expensive offering of that piece and include the piece name, provider name, and price
-- (note that there could be two providers who supply the same piece at the most expensive price).
SELECT pi.name AS piece_name, pv.name AS provider_name, pr.price
FROM Provides pr
JOIN Pieces   pi ON pr.piece    = pi.code
JOIN Providers pv ON pr.provider = pv.code
JOIN (
  SELECT piece, MAX(price) AS max_price
  FROM Provides
  GROUP BY piece
) mx ON mx.piece = pr.piece AND mx.max_price = pr.price
ORDER BY pi.code, pv.code;
-- ---------------------------------------------
-- 5.7 Add an entry to the database to indicate that "Skellington Supplies" (code "TNBC") will provide sprockets (code "1") for 7 cents each.
DELETE FROM Provides
WHERE piece = 1 AND provider = 'TNBC';

INSERT INTO Provides (piece, provider, price)
VALUES (1, 'TNBC', 0.07);
-- 5.8 Increase all prices by one cent.
UPDATE Provides
SET price = price + 0.01;
-- 5.9 Update the database to reflect that "Susan Calvin Corp." (code "RBT") will not supply bolts (code 4).
DELETE FROM Provides
WHERE provider = 'RBT' AND piece = 4;
-- 5.10 Update the database to reflect that "Susan Calvin Corp." (code "RBT") will not supply any pieces
DELETE FROM Provides
WHERE provider = 'RBT';
-- (the provider should still remain in the database).