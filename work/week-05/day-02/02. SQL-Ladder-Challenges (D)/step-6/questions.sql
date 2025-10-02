-- this will allow us to connect to the database
-- this will format the information being printed in the console to make it easier.. try it without if you want!
\connect ladder  
\x on 

-- 6.1 List all the scientists' names, their projects' names,
SELECT
  s.name AS scientist_name,
  p.name AS project_name,
  p.hours AS project_hours  
FROM Scientists s
JOIN AssignedTo a ON a.scientist = s.ssn
JOIN Projects   p ON a.project   = p.code
ORDER BY p.name, s.name;

-- and the hours worked by that scientist on each project,
-- in alphabetical order of project name, then scientist name.
-- 6.2 Select the project names which are not assigned yet
SELECT p.name
FROM Projects p
LEFT JOIN AssignedTo a ON a.project = p.code
WHERE a.project IS NULL
ORDER BY p.name;