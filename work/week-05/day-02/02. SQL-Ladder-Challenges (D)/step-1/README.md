<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

## Instructions

Solve each clue in the `questions.sql` file in your starter code repo.

Run the SQL file in the terminal as you solve each clue: `psql -f questions.sql`

## Setup
1. First make sure your database has been created:
   1. `createdb ladder`
   2. If you receive an error like: `ERROR:  database "ladder" already exists` then you are good to go ✅  
2. Let's seed the `ladder` database with data...
   1. `psql -f ladder.sql`
3. Start `psql` and connect to the new database called `ladder`:
   1. `psql -d ladder` 
4. Create your SQL queries in the `questions.sql` file.
5. Run your `questions.sql` file with: `psql -f questions.sql` or `\i questions.sql` in psql shell to see the results.
6. Exit the `psql` shell with: `\q`.