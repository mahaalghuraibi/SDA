# ![Intro to SQL - Modifying and Deleting Data](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to modify and delete data in a database.

## Modifying or updating data

We have seen how to insert data into a table, but what if we need to update existing data? The `UPDATE` command is used to modify existing data in a table. The syntax for the `UPDATE` command is as follows:

```sql
UPDATE table_name 
SET column1 = value1, column2 = value2, ... 
WHERE condition;
```

- `UPDATE table_name` tells SQL which table you want to update.
- `SET column1 = value1, column2 = value2, ...` specifies the columns that should be updated and their new values.
- `WHERE condition` determines which records in the table should be updated. Without this condition, all records in the table would be updated.

Let's say we want to update the genre of the band `The Beatles` to `Rock and Roll`. We can use the `UPDATE` command to do this:

```sql
UPDATE bands SET genre = 'Rock and Roll' WHERE name = 'The Beatles';
```

> 🚨 The `WHERE` clause is used to filter the rows that will be updated. If you omit the `WHERE` clause, all rows in the table will be updated.

We can also update multiple columns at once. Let's say we want to update the genre of the band `The Rolling Stones` to `Rock and Roll` and the genre of the band `The Who` to `Rock and Blues`. We can do both back to back.

```sql
UPDATE bands SET genre = 'Rock and Roll' WHERE name = 'The Rolling Stones';
UPDATE bands SET genre = 'Rock and Blues' WHERE name = 'The Who';
```

## Deleting data

The `DELETE` command allows you to remove one or more rows from a table based on a specific condition. This is useful for cleaning up data or removing unnecessary records.

The basic syntax for the `DELETE` command is straightforward:

```sql
DELETE FROM table_name WHERE condition;
```

- `DELETE FROM table_name` instructs SQL to remove data from the specified table.
- `WHERE condition` specifies which rows should be deleted. If this condition is not included, all rows in the table will be deleted, which is rarely intended and could lead to data loss.

Let's say we want to delete the musician `Roger Daltrey` from the `musicians` table. We can use the `DELETE` command to do this:

```sql
DELETE FROM musicians WHERE name = 'Roger Daltrey';
```

This command deletes only the row where the name column matches 'Roger Daltrey'.

### Caution

Always use the `WHERE` clause with care when deleting data. Accidentally omitting this clause will result in all records being deleted from the table, which could be catastrophic if not intended.
