# ![Intro to SQL - Setup](./assets/hero.png)

## Setup

In this lesson, you will use your Terminal application to create and interact with a PostgreSQL database. You will use the `psql` command line tool to interact with the database. Open your Terminal application and use the command `psql` to start the PostgreSQL command line tool:

1. Setup a folder: `mkdir intro-to-sql`
2. Setup a file: `queries.sql` 
3. Open a terminal from the new folder.
4. Start the postgresql shell using: `psql`...

You should see a prompt that looks similar to this:

```postgres
psql (16.2 (Homebrew))
Type "help" for help.

username=#
```

> The version number, `(16.2 (Homebrew))`, may be different on your machine. You are in the PostgreSQL command line tool if you can see your username followed by a `#`.

To close the PostgreSQL command line tool, type `\q` and press `Enter`:

```postgres
\q
```