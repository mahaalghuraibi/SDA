<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Many to many relationships: Using join tables!

## Introduction

In this lab you will be writing queries to gain insight into our movies database. The `movies_db_lab` consists of four tables. You are already familiar with the `movies` and the `directors` tables. The two new tables are the `users` and the `users_movies` tables.

- The `users` table simply holds user records. These records only store a `name` string of a user. 
- The `users_movies` table represents a many to many relationship between the users table and the movies table. These types of tables are sometimes referred to as "join tables". 

The naming of the table ("`users_movies`") might sound strange, but it is a common naming convention you will certainly come across. This is just a concatenation of the two table names that it is joining. 

Sometimes, the join table represents an idea that lends itself to a better name. In our case, we could have named the table `favorites` or something like that. But it's good to see and get used to this naming convention also.

## Instructions

Solve each clue in the `questions.sql` file in your starter code repo.

Run the SQL file in the terminal as you solve each clue: `psql -f questions.sql`

## Setup
1. First make sure your database has been created:
   1. `createdb movies_joins_lab`
   2. If you receive an error like: `ERROR:  database "movies_joins_lab" already exists` then you are good to go ✅  
2. Let's seed the `movies_joins_lab` database with data...
   1. `psql -f movies_joins_lab.sql`
3. Start `psql` and connect to the new database called `movies_joins_lab`:
   1. `psql -d movies_joins_lab` 
4. Create your SQL queries in the `questions.sql` file.
5. Run your `questions.sql` file with: `psql -f questions.sql` or `\i questions.sql` in psql shell to see the results.
6. Exit the `psql` shell with: `\q`.