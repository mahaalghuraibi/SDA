<h1>
  <span class="headline">Intro to SQL Lab</span>
  <span class="subhead">Exercise</span>
</h1>

# Carmen Sandiego
<img src="https://i.imgur.com/XDYV74g.jpeg" alt="Carmen Sandiego Banner" width="100%" />

## Instructions

Solve each clue in the `clues.sql` file in your starter code repo.

Run the SQL file in the terminal as you solve each clue: `psql -f questions.sql`

## Setup
1. First make sure your database has been created:
   1. `createdb world`
   2. If you receive an error like: `createdb: error: database creation failed: ERROR:  database "world" already exists` then you are good to go ✅  
2. Let's seed the `world` database with data...
   1. `psql -f world.sql`
3. Start `psql` and connect to the new database called `world`:
   1. `psql -d world` 
4. Create your SQL queries in the `clues.sql` file.
5. Run your `clues.sql` file with: `psql -f questions.sql` or `\i questions.sql` in psql shell to see the results.
6. Exit the `psql` shell with: `\q`.