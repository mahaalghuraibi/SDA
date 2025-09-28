# ![Intro to SQL - Inserting and Selecting Data](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to insert data into a table and query data from a table.

## Inserting Data

We now have a database and table established, but it's empty! We can add a single row or multiple rows into a table using the `INSERT INTO` command. The syntax for the `INSERT INTO` command is as follows:

```postgres
INSERT INTO table_name (column1, column2, ...) 
VALUES 
(value1, value2, ...)[, (value1, value2, ...), ...];
```

Let's add some bands to the `bands` table:

> 🚨 Notice our use of the single quote (`'`) character below - this is required to indicate the use of a string in SQL!

```postgres
-- Insert a single row
INSERT INTO bands (name, genre) 
VALUES 
('The Beatles', 'Rock');

-- Insert multiple rows
INSERT INTO bands (name, genre) 
VALUES 
('The Rolling Stones', 'Rock'), 
('The Who', 'Rock');
```

> 🧠 Note: We are not specifying the `id` column when inserting data into the `bands` table. Since the `id` column is a `SERIAL` data type, PostgreSQL will automatically increment the value each time a new row is inserted.

## Selecting Data

Now that we have data in our `bands` table, we can use the `SELECT` command to query the data. The syntax for the `SELECT` command is as follows:

```postgres
SELECT column1, column2, ... FROM table_name;
```

Let's query all the data from the `bands` table:

```postgres
SELECT * FROM bands;
```

> 🧠 The `*` is a wildcard character that selects all columns from the table. If you only want to select specific columns, you can replace the `*` with the column names you want to select.

You should see the data you inserted into the `bands` table in the terminal.

### Selecting data with SELECT *clauses*

The `SELECT` command is foundational in SQL for retrieving data from databases. To make your queries more precise and efficient, you can use several standard clauses with `SELECT`:

- `WHERE`: Filters the returned rows based on a condition.
- `ORDER BY`: Sorts the returned rows based on a column.
- `LIMIT`: Limits the number of returned rows.
- `COUNT`: Returns the number of returned rows.

Let's look at how these clauses are used in real SQL queries:

```postgres
-- Query bands where the genre is 'Rock'
SELECT name FROM bands WHERE genre = 'Rock';

-- Query bands sorted by name in ascending order
SELECT genre FROM bands ORDER BY name ASC;

-- Query the first two bands
SELECT * FROM bands LIMIT 2;

-- Count the number of bands
SELECT COUNT(*) FROM bands;
```

While the `SELECT` command might seem straightforward, its power becomes apparent when dealing with larger databases. With the right clauses, `SELECT` can help you efficiently query vast amounts of data, extract meaningful insights, and perform complex data manipulations.
