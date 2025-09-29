--\connect music

--select * from bands;

--select name from bands
--LIMIT 2;

--select name 

\connect music

SELECT * FROM bands;

UPDATE bands
SET genre = 'asdf'
WHERE id = 1;

SELECT * FROM bands;

DELETE FROM bands
WHERE name = 'Amr Diab Band';

DELETE FROM bands
WHERE id = 3;


SELECT * FROM bands;
