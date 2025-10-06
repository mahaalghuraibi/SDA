<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

## Next Level SQL Queries
Basic queries are great for simple lookups, but most real world questions need more. Advanced querying let's us combine filters, group data, and nest results so we can spot patterns, compare groups, and answer complex questions that a single condition can’t handle. It’s how we move from just finding data to truly analyzing it."


### 1. WHERE clause:

One of the most basic and important to use. The purpose of this function is to match specific conditions.

- Let's find all countries **IN** South America.

**WHERE** with matching what you **DO WANT**
```sql
SELECT name, population, region FROM countries
WHERE region = 'South America';
```

- Let's find all countries **NOT IN** Europe or Asia.
**WHERE** with matching what you DO **NOT** WANT
```sql
SELECT name, continent
FROM country
WHERE continent NOT IN ('Europe', 'Asia')
```

### 2. Sorting and Ranking

Many times you may need the option to **SORT** items or **LIMIT** the number of items that are returned from that database. Is it efficient to retrieve ALL of the items from the databae if we only need to return the first 100?

- Let's find which country in South America has the smallest population..

```sql
SELECT name, population FROM countries
WHERE region = 'South America'
ORDER BY population ASC
LIMIT 10;
```

- `ASC`  -> 0, 1, 2, 3, 4, 5
- `DESC` -> 5, 4, 3, 2, 1, 0

### 3. GROUP BY, AGGREGATION, COUNTING

We often times run into calculations where we need to know **how much** or **how many** items we have in relation to the specific characteristics we are wanting to match. The `group by`, `count()` and `having count()` operators can support us in making this possible.

- `GROUP BY` = organize items into buckets.
- `COUNT`    = **how many** clues each suspect has.
- `HAVING`   = keep only items that meet specific group-level conditions.
- `SUM`, `AVG`, `MIN`, `MAX` = perform math on the items

The **GROUP BY** clause is used to organize rows into groups that share the same value in one or more columns. Once the rows are grouped, you can use aggregate functions (like `COUNT`, ) to perform calculations on each group.

Think of it like this:

-- **Without GROUP BY**: you’re looking at every individual row.

-- **With GROUP BY**: you’re saying “put rows with the same value together, then calculate something about the group on that column”

-- What COUNT(*) means

- The * in COUNT(*) does not mean “all columns to display.”
- It means: count every row in the result set, regardless of which columns you select based on the GROUP BY phrase.

- Basic Grouping
```sql
SELECT language, COUNT(*) FROM countrylanguages
GROUP BY language;
```

- With an `ALIAS` (also known as)
```sql
SELECT language, COUNT(*) AS num_languages
FROM countrylanguages
GROUP BY language
```

- **Make more specific** - ONLY items that equal a specific count(s)
```sql
SELECT language, COUNT(*) AS num_languages
FROM countrylanguages
GROUP BY language
HAVING COUNT(*) = 10 
-- OR
-- HAVING COUNT(*) <> 10 (does not equal) 
-- HAVING COUNT(*) != 10 (does not equal) 
```

OR

```sql
SELECT language, COUNT(*) AS num_languages
FROM countrylanguages
GROUP BY countrycode
HAVING COUNT(*) IN (1, 2, 3);
```

### 4. Subqueries and Nesting:
There will also be many times where we will need nested querying so that we can make an initial query based on another query. Because we do not have variables, we are unable to store information. So we will have to NEST instead...

```sql
SELECT name
FROM countries
WHERE code IN (
    SELECT countrycode
    FROM countrylanguages
    WHERE language = 'Italian'
);
```


### 5. String Comparison
We might also want to build queries so that we can match specific strings. Built into SQL is the ability to match strings using specialty characters and we also have access to `regular expressions`. Regular expressions are a way of matching complicated strings to ensure that the pattern is exactly as you expect it to be. For example: ensuring that a password is a specific length or has specific characters / formatting. Phone numbers, emails, etc..

Ex: [Regular Expressions Website](https://regexr.com/)
Ex: [Javascript RegEx](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet)

For now we will check out `LIKE` and `ILIKE` and a few operators to use with them...

- `LIKE` / `ILIKE` are what we call wildcards.
- `LIKE` = cAsE SeNSiTive
- `ILIKE` = case insensitive
- `%` = any number of characters _before_ **OR** _after_.
- `_` = exactly _one_ character.
- `~` = allows for matching a regular expression:
 
```sql
- WHERE name ~ '^A.*a$'; -- <-- regular expression
```

- Let's find cities whose names start with “San” (like San Francisco, San José).
- 
```sql
SELECT name, countrycode FROM cities
WHERE name ILIKE 'San%';
```

### 6. **Final Mission: Complex Multi-Step Query**
Let's combine several of the items that we have done today! 

We can join together two of the tables from the Carmen San Diego `world` database, and work to find a more complicated / nested item so that we can finally find Carmen San Diego!

<!-- ex: JOIN table2 ON table1.column = table2.column; -->
```sql
SELECT * from countries
JOIN countrylanguages ON countries.code = countrylanguages.countrycode
WHERE 
```


