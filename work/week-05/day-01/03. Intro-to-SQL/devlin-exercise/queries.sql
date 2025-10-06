-- \c music \\ also works
\connect music

-- SELECT * FROM bands;

-- SELECT name FROM bands;

-- SELECT * FROM bands
-- LIMIT 2;

-- SELECT * FROM bands
-- WHERE name = 'The Beatles';

-- SELECT name, genre FROM bands
-- WHERE id = 3;

-- \echo "Hello World";

 SELECT * FROM bands;

 UPDATE bands
 SET genre = 'rthgerthgidrhtgrthg'
 WHERE id = 1;

SELECT * FROM bands;

UPDATE bands
SET genre = 'disco';

SELECT * FROM bands;

DELETE from bands
WHERE name = 'The Who';

DELETE from bands
WHERE id = 1;

SELECT * FROM bands;