-- this will allow us to connect to the database
-- this will format the information being printed in the console to make it easier.. try it without if you want!
\connect ladder  
\x off


-- 2.1 Select the last name of all employees.
SELECT LastName
FROM Employees;

-- 2.2 Select the last name of all employees, without duplicates.
SELECT DISTINCT LastName
FROM Employees;

-- 2.3 Select all the data of employees whose last name is "Smith".
SELECT *
FROM Employees
WHERE LastName = 'Smith';

-- 2.4 Select all the data of employees whose last name is "Smith" or "Doe".
SELECT *
FROM Employees
WHERE LastName = 'Smith' or LastName= 'Doe'

-- 2.5 Select all the data of employees that work in department 14.
SELECT *
FROM Employees
WHERE Department = 14;

-- 2.6 Select all the data of employees that work in department 37 or department 77.
SELECT *
FROM Employees
WHERE Department IN (37, 77);

-- 2.7 Select all the data of employees whose last name begins with an "S".
SELECT *
FROM Employees
WHERE LastName LIKE 'S%';

-- 2.8 Select the sum of all the departments' budgets.
SELECT SUM(Budget)
FROM Departments;

-- 2.9 Select the number of employees in each department (show department code + count).
SELECT Department, COUNT(*) AS num_employees
FROM Employees
GROUP BY Department;

-- 2.10 Select all the data of employees, including each employee's department's data.
SELECT *
FROM Employees
JOIN Departments 
  ON Employees.Department = Departments.Code;

-- 2.11 Select the name and last name of each employee,
--      along with the name and budget of the employee's department.
SELECT Employees.Name, Employees.LastName, Departments.Name AS dept_name, Departments.Budget
FROM Employees
JOIN Departments
  ON Employees.Department = Departments.Code;

-- 2.12 Select the name and last name of employees working for departments with a budget > 60000.
SELECT Employees.Name, Employees.LastName
FROM Employees
JOIN Departments
  ON Employees.Department = Departments.Code
WHERE Departments.Budget > 60000;

-- 2.13 Select the departments with a budget larger than the average budget of all the departments.
SELECT *
FROM Departments
WHERE Budget > (SELECT AVG(Budget) FROM Departments);

-- 2.14 Select the names of departments with more than two employees.
SELECT Name
FROM Departments
WHERE Code IN (
  SELECT Department
  FROM Employees
  GROUP BY Department
  HAVING COUNT(*) > 2
);

-- 2.15 Very Important - employees in the department with the second lowest budget.
SELECT e.Name, e.LastName
FROM Employees e
WHERE e.Department = (
  SELECT Code
  FROM Departments
  ORDER BY Budget ASC
  LIMIT 1 OFFSET 1
);

-- 2.16 Add new department and employee.
-- Department: "Quality Assurance", budget 40000, code 11
INSERT INTO Departments (Code, Name, Budget)
VALUES (11, 'Quality Assurance', 40000);

-- Employee: "Mary Moore", SSN 847-21-9811, in department 11
INSERT INTO Employees (SSN, Name, LastName, Department)
VALUES (847219811, 'Mary', 'Moore', 11);

-- 2.17 Reduce the budget of all departments by 10%.
UPDATE Departments
SET Budget = Budget * 0.9;

-- 2.18 Reassign all employees from Research (77) to IT (14).
UPDATE Employees
SET Department = 14
WHERE Department = 77;

-- 2.19 Delete all employees in the IT department (code 14).
DELETE FROM Employees
WHERE Department = 14;

-- 2.20 Delete all employees who work in departments with budget >= 60000.
DELETE FROM Employees
WHERE Department IN (
  SELECT Code
  FROM Departments
  WHERE Budget >= 60000
);

-- 2.21 Delete all employees.
DELETE FROM Employees;

