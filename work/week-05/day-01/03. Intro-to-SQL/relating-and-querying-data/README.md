# ![Intro to SQL - Relating and Querying Data](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to understand and implement one-to-many relationships in SQL databases, apply conditional logic with the `WHERE` clause to refine their data retrieval, and effectively use the `JOIN` command to query related data across tables.

## One to Many Relationships in SQL

We currently have a `bands` table that stores information about different bands. These bands can have many musicians. This relationship is known as a **one-to-many** relationship. We can think through this relationship as:

![One-to-many](./assets/music-bands-musicians.png)

**One *band* has many *musicians*, and**

**One *musician* belongs to a *band***

To represent this relationship in our database, we must create a new table called `musicians` that will store information about different musicians. The `musicians` table will have a ***foreign key*** referencing the `bands` table.

We will use the structure for our `musicians` table:

| Column Name | Data Type | Constraints          |
| ----------- | --------- | -------------------- |
| id          | SERIAL    | PRIMARY KEY          |
| band_id     | INTEGER   | REFERENCES bands(id) |
| name        | VARCHAR   | NOT NULL             |
| age         | INTEGER   | NOT NULL             |
| sings       | BOOLEAN   |                      |
| dances      | BOOLEAN   |                      |

To create the `musicians` table, we will use the `CREATE TABLE` command:

```sql
CREATE TABLE musicians (
  id SERIAL PRIMARY KEY,
  band_id INTEGER REFERENCES bands(id),
  name VARCHAR NOT NULL,
  age INTEGER NOT NULL,
  sings BOOLEAN,
  dances BOOLEAN
);
```

Let's insert the musicians for the bands we have in the `bands` table:

```sql
-- Insert musicians for The Beatles
INSERT INTO musicians (band_id, name, age, sings, dances) 
VALUES 
(1, 'John Lennon', 40, null, FALSE),
(1, 'Paul McCartney', 39, TRUE, FALSE),
(1, 'George Harrison', 38, TRUE, null),
(1, 'Ringo Starr', 41, FALSE, TRUE);

-- Insert musicians for The Rolling Stones
INSERT INTO musicians (band_id, name, age, sings, dances) 
VALUES 
(2, 'Mick Jagger', 38, TRUE, null),
(2, 'Keith Richards', 39, TRUE, FALSE),
(2, 'Charlie Watts', 40, null, FALSE),
(2, 'Ronnie Wood', 41, TRUE, TRUE);

-- Insert musicians for The Who
INSERT INTO musicians (band_id, name, age, sings, dances) 
VALUES 
(3, 'Roger Daltrey', 38, TRUE, TRUE),
(3, 'Pete Townshend', 39, null, FALSE),
(3, 'John Entwistle', 40, TRUE, FALSE),
(3, 'Keith Moon', 41, null, TRUE);
```

> 🧠 The `null` value represents unknown or missing data. Since the `sings` and `dances` columns are `BOOLEAN` data types without any constraints, we can represent the data using `TRUE`, `FALSE`, or `null`.

## Querying data from `musicians`

After learning the basics of the `SELECT` command and exploring how it can retrieve data from a database, we'll now focus on a powerful feature used to refine queries: the `WHERE` clause.

The `WHERE` clause is essential for filtering query results. It allows you to specify conditions that the data must meet to be included in the output. This makes your queries more precise and the data more manageable.

Here is the basic syntax for using the `WHERE` clause in an SQL query:

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

This syntax tells the database to select only those rows from the specified table where the condition holds true.

Let's query the musicians that sing:

```sql
SELECT name FROM musicians WHERE sings = TRUE;
```

This query will return the names of all musicians who sing. The condition sings = TRUE filters out any rows where sings is not true, ensuring that only singers are included in the results.

You should see the musicians that sing displayed in the terminal.

You can also use various operators in the condition, such as:

- `=`: Equal to
- `<>` or `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to
- `BETWEEN`: Between an inclusive range
- `LIKE`: Search for a pattern
- `IN`: Matches any of a list of values
- `IS NULL`: Checks for `NULL` values
- `AND`: Combines multiple conditions
- `OR`: Returns rows that meet either condition
- `NOT`: Negates a condition

Let's see some of these operators in action:

```sql
-- Query musicians who are older than 40
SELECT name FROM musicians WHERE age > 40;

-- Query musicians that are younger than or equal to 40
SELECT name FROM musicians WHERE age <= 40;

-- Query musicians that are between the ages of 38 and 40
SELECT name FROM musicians WHERE age BETWEEN 38 AND 40;

-- Query musicians that have a name that starts with 'J'
SELECT name FROM musicians WHERE name LIKE 'J%';

-- Query musicians that are in The Beatles or The Rolling Stones
SELECT name FROM musicians WHERE band_id IN (1, 2);

-- Query musicians that do not sing
SELECT name FROM musicians WHERE sings IS NULL;

-- Query musicians who are older than 40 and do dance
SELECT name FROM musicians WHERE age > 40 AND dances = TRUE;

-- Query musicians that are younger than or equal to 40 or sing
SELECT name FROM musicians WHERE age <= 40 OR sings = TRUE;

-- Query musicians that are not older than 40
SELECT name FROM musicians WHERE NOT age > 40;
```

> The `WHERE` clause is a powerful tool that allows you to filter the data returned based on a condition. To create complex queries, you can combine multiple conditions using the `AND`, `OR`, and `NOT` operators.

## Querying Related Data

As our database contains information spread across the `bands` and `musicians` tables, we can use the `JOIN` command to combine data from these tables based on their relationships. This is useful when you need to gather comprehensive information from multiple tables that are linked by a common column.

The `JOIN` command merges rows from two or more tables, creating a set where each combination of rows from the linked tables meets the conditions specified in the `ON` clause.

### Syntax of the JOIN command

Here's the general syntax for performing a join:

```sql
SELECT table1.column1, table2.column2, ...
FROM table1
JOIN table2 ON table1.column = table2.column;
```

This syntax directs the database to fetch data from two tables by matching the values in the specified columns from each table.

For example, we can find out which `musicians` belong to which `bands` by linking the `musicians` table with the `bands` table via the band `ID`s.

Let's query the musicians and the bands they belong to:

```sql
SELECT bands.name AS band, musicians.name AS musician
FROM bands
JOIN musicians ON bands.id = musicians.band_id;
```

This query selects the name of the band and the musician from the `bands` and `musicians` tables. It then joins the tables on the `bands.id` and `musicians.band_id` fields, meaning it will match musicians with the bands they are part of.

You should now see the musicians and the bands they belong to displayed in the terminal.

## Types of JOINs

The `JOIN` command is a powerful tool that combines related data from multiple tables. You can use different types of joins, such as:

- **`INNER JOIN`**: This is the default `JOIN`, returning rows only when a match is found in both tables.
- **`LEFT JOIN` (or `LEFT OUTER JOIN`)**: Returns all rows from the left table and the matched rows from the right table; if there is no match, the result is `NULL` on the side of the right table.
- **`RIGHT JOIN` (or `RIGHT OUTER JOIN`)**: Returns all rows from the right table and the matched rows from the left table; if there is no match, the result is `NULL` on the side of the left table.
- **`FULL JOIN` (or `FULL OUTER JOIN`)**: Returns rows when there is a match in at least one of the tables. If there is no match, the result is `NULL` for the unmatched side of either table.

Each of these `JOIN` types can be used depending on the specific requirements of your query and the relationships between your tables.
