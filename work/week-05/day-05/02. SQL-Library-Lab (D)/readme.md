<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Library DB

## Instructions

Solve each prompt in the following two `.sql` files:
* [Basic Queries](basic_queries.sql) - SELECT, INSERT, UPDATE, DELETE
* [Advanced Queries](advanced_queries.sql) - JOINS

Run the `.sql` file in the terminal as you solve each clue: 
- `psql -f basic_queries.sql`
- `psql -f advanced_queries.sql`

## Setup
1. First make sure your database has been created:
   1. `createdb library`
   2. If you receive an error like: `createdb: error: database creation failed: ERROR:  database "library" already exists` then you are good to go ✅  
2. Let's seed the `library` database with data...
   1. `psql -f seed.sql`
3. Start `psql` and connect to the new database called `library`:
   1. `psql -d library` 
4. Create and run your SQL queries in the files mentioned above.
5. Exit the `psql` shell with: `\q`.
