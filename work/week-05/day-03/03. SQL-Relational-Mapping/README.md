# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Relational Models

### Learning Objectives

*After this lesson, students will be able to:*

- Create one-to-one, one-to-many, and many-to-many relationships in SQL.
- Determine when each type of relationship is most useful for certain data sets.

## Introduction

As we discussed earlier, what makes SQL databases relational is that each table is "related" to other tables in some way. This model organizes data into one or more tables (or "relations") of columns and rows, using a unique key to identify each row. Rows are also called **records** or **tuples**. Columns are also called **attributes**.

### Relational Mapping

Relationships happen when we start seeing multiple occurrences of duplicative information, or when one object needs to "connect" to another object.

There are three ways in which one table can be linked to another. Each is used in particular scenarios. We'll look at all three and their implementations.

-----

## One-to-One

The first way of linking tables is called a **one-to-one** relationship. It's not frequently used, but it's important to know about this option.

In real-world applications, `address` is created as a separate table linked to `students`. We say that each student can have only one address and each address is linked to a unique student. In such a case, we say that `Student` and  `Address` have a one-to-one relationship.

### Code-Along

Let's create a one-to-one relationship between a student and their address in a different table...

## SETUP

1. Enter our psql shell: `psql` or `psql -U postgres`
2. Create our `students` database with: `CREATE DATABASE students`
3. Connect to students database: `\c students`
4. Let's create our student table:
```sql
CREATE TABLE students (
	student_id SERIAL PRIMARY Key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	age INT
);
```

5. Let's add some initial value to work with:
```sql
INSERT INTO students VALUES 
(default, 'Jack', 'Sparrow', 45), 
(default, 'Albus', 'Dumbledore', 121), 
(default, 'Tom', 'Cruise', 61), 
(default, 'Annie', 'Potts', 51), 
(default, 'Christina', 'Aguilara', 28); 
```

6. let's check: `select * from students`
   1. we'll see all our students and updated ids auto incremented.

7. Create the `address` table with a few necessary attributes:

```sql
CREATE TABLE address (
	address_id SERIAL PRIMARY Key,
	street VARCHAR(150),
	city VARCHAR(50),
	state VARCHAR(10)
);
```

8. Let's view our tables in `students` db: `\dt`

### Creating a relationship

Now, to create a relationship between these two tables, we'll have to add a new column in the `students` table that will eventually store the reference to the `address` record for that student. 

We'll use `ALTER` to add a new column; the `ALTER` keyword is used to change the description of the existing table. Our query will look like this:

```sql
ALTER TABLE students ADD COLUMN student_address_id INT;
```

#### confirm column names: `\d students`
-> will show the column details for the specific table.

RECAP: 

- We're adding a new column of the integer data type, named `student_address_id` , to our `students` table.
- Once the column is added, we can add a foreign key constraint to this column so that `student_address_id` in `students` table will have the reference to the data in the `address` table.
- A **foreign key** is a key used to link two tables together. It's a field (or collection of fields) in one table that refers to the primary key in another table.


In the `psql` prompt, we'll again `ALTER` the `students` table to create this constraint:

```sql
ALTER TABLE students 
ADD CONSTRAINT fk_student_address 
FOREIGN KEY (student_address_id) 
REFERENCES address (address_id);
```

RECAP:

- With `ALTER TABLE students`, we're again altering the `students` table to a foreign key on one of its columns. 
  
- `fk_student_address` is just the name of the constraint, so we can give any name here. Think of it in terms of a variable in any programming language: It's just a placeholder.
  
- `FOREIGN KEY (student_address_id) REFERENCES address (address_id)`, we're declaring the column in the `students` table, which will be the foreign key (and what it will reference). 
  
- As mentioned before, this is the primary key for `address_id` of `address` table.

Let's run `\d students` to have one final look at the table.

```sql
generalassembly=# \d students;
                                             Table "public.students"
       Column       |         Type          | Collation | Nullable |                   Default                    
--------------------+-----------------------+-----------+----------+----------------------------------------------
 student_id         | integer               |           | not null | nextval('students_student_id_seq'::regclass)
 name               | text                  |           | not null | 
 age                | integer               |           | not null | 
 mobile             | character varying(50) |           |          | 
 student_address_id | integer               |           |          | 
Indexes:
    "students_pkey" PRIMARY KEY, btree (student_id)
    "fki_fk_student_address" btree (student_address_id)
Foreign-key constraints:
    "fk_students_address" FOREIGN KEY (student_address_id) REFERENCES address(address_id)
```

### Add addresses and create the relationship:

Let's add records in the `address` table for each student in the `students` table. Then, update the `students` table to associate the address.
	
```sql
INSERT INTO address VALUES 
(DEFAULT, '200 Horton Ave', 'Lynbrook', 'NY'),
(DEFAULT, '123 Webdev Dr', 'Boston', 'MA'),
(DEFAULT, '555 Five St', 'Fivetowns', 'CA'),
(DEFAULT, '2 OldForThis Ct', 'Fivetowns', 'OK');
(DEFAULT, '2416 Broadway St', 'Baton Rouge', 'LA');
```

#### let's update their foreign key fields to create the relationships

```sql
update students set student_address_id = 1 where first_name = 'Jack';
update students set student_address_id = 2 where student_id = 3;
update students set student_address_id = 3 where student_id = 4;
update students set student_address_id = 4 where student_id = 5;
```
	
#### Let's get our students and query their accompanying (matching) address information.

```sql
select * from students, address 
where address_id = student_address_id;
```

<br>

------

## One-to-Many

The [**one-to-many**](https://www.tech-recipes.com/rx/56738/one-to-one-one-to-many-table-relationships-in-sql-server) relationship is defined as a relationship between two tables where a row from one table can have multiple matching rows in another table. This relationship can be created using the primary key-foreign key relationship.	

You simply put the ID of the "one" resource in the "many," as shown above. This is called a **foreign key**, because it is the key (or ID) of an item in a different table. 

### Code-Along

In our example, we'll now create two new tables: `courses` and `instructors`. Let's first create the `courses` table, which will have at least two attributes: `course_code` and `course_name`.

```sql
CREATE TABLE courses (
	course_id SERIAL PRIMARY KEY,
	course_code VARCHAR(10),
	course_name VARCHAR(100)
);
```

While we're at it, let's put in some data:

```sql
INSERT INTO courses VALUES (DEFAULT, 'SEI', 'Software Engineering Immersive');
INSERT INTO courses VALUES (DEFAULT, 'DSI', 'Data Science Immersive');
```

```sql
generalassembly=# SELECT * FROM courses;
 course_id | course_code |          course_name           
-----------+-------------+--------------------------------
         1 | SEI         | Software Engineering Immersive
         2 | DSI         | Data Science Immersive
(2 rows)

```

We say that each course can be taught by multiple instructors, but only one instructor can teach a course at a time. Therefore, there is a one-to-many relationship between course and instructors.

Now, when we create the `instructors` table, we'll also add **referential integrity** to it, just as we did before:

```sql
CREATE TABLE instructors (
	instructor_id SERIAL PRIMARY KEY, 
	name VARCHAR(255) NOT NULL, 
	email VARCHAR(200) NOT NULL, 
	instructor_course_id INT REFERENCES courses(course_id) NOT NULL DEFAULT (0)
);
```

RECAP:

- We've created a new column, `instructor_course_id`, which is the foreign key referencing `course_id`, the primary key in the `Courses` table.
   
- An instructor should always be teaching a course; that's why we have put a `NOT NULL` constraint. 

- What if an instructor is not teaching any courses or is on hiatus at the moment? What do we do then? 
  
- One option is to delete the record, but this is definitely not the best one. The better option is to set the default value to `0`. Now, we'll know the total number of instructors we have and how many are currently teaching.

```psql
generalassembly=# \d instructors
                                                Table "public.instructors"
        Column        |          Type          | Collation | Nullable |                      Default                       
----------------------+------------------------+-----------+----------+----------------------------------------------------
 instructor_id        | integer                |           | not null | nextval('instructors_instructor_id_seq'::regclass)
 name                 | character varying(255) |           | not null | 
 email                | character varying(200) |           | not null | 
 instructor_course_id | integer                |           | not null | 0
Indexes:
    "instructors_pkey" PRIMARY KEY, btree (instructor_id)
Foreign-key constraints:
    "instructors_instructor_course_id_fkey" FOREIGN KEY (instructor_course_id) REFERENCES courses(course_id)

```

### Let's create some instructors!
In order to start building our one-to-many relationships we will need to have some instructors to work with. Copy / Paste / Run this code so we can generate the data.

```sql
INSERT INTO instructors VALUES 
(default, 'Jack Sparrow', 'black_pearl@pirates.com', 1), 
(default, 'Albus Dumbledore', 'headmaster@hogarts.com', 1), 
(default, 'Tom Cruise', 'maverick@top_gun.com', 2), 
(default, 'Annie Potts', 'who_you_gonna_call@ghostbusters.com', 2), 
(default, 'Christina Aguilara', 'beautiful@thevoice.com', 2); 
```

### Let's check to see we were able to make our relationships:

```sql
select * from instructors
where instructor_course_id = 2
```

Success! -> Now we move to Many-To-Many!

------

## Many-to-Many

Let's think about a high school situation where students have many courses and courses have many students. 

How do we do this? We _could_ attempt to use the previous approach (wrong) and put ALL of the student IDs associated with each course in each row of the `courses` table AND ALL of the course IDs associated with each student in each row on the `students` table. 

However, we'd just be putting arbitrary amounts of columns in our tables, and the end result is not pretty:

![](https://media.giphy.com/media/N9sfGVpuo4p56/giphy.gif)

Fortunately, the eggheads of computer science yesteryear came up with a beautiful, elegant solution: The **JOIN table**. 

### The JOIN Table

![](https://media.giphy.com/media/jDiUeDQpIkGIM/giphy.gif)

![](https://smehrozalam.files.wordpress.com/2010/06/erd-many-to-many-2.jpg)

We use a JOIN table! It's a table with the IDs of BOTH tables, thus connecting our data across databases! YAY!

A JOIN table might be JUST a JOIN table, meaning it might have nothing but the two IDs, or it might represent something bigger.

For example, the JOIN table above represents a real thing: **enrollment**! Enrollment might have some of its own properties, such as start and stop dates. Other times, the JOIN table might not really represent anything that has a real-life analogy, and it might not need to hold any data besides the IDs. 

### Code-Along

We already have `students` and `courses` tables in our database. We just have to create a JOIN table signifying the enrollment, just as we discussed in the example above. For now, we'll keep things simple and just have a column for `student_id` and a column for `course_id`. 

Let's create our JOIN table. We'll call it `student_course_enrollment`:

```sql
CREATE TABLE student_course_enrollment (
	enrollment_id SERIAL PRIMARY KEY,
	student_id INT REFERENCES students(student_id) NOT NULL,
	course_id INT REFERENCES courses(course_id) NOT NULL,
	UNIQUE (student_id, course_id)
);
```
#### Let's check: `\dt` will show our tables

### Let's chat about what we just did!

There's a lot happening in this `CREATE TABLE` query, so let's go over it.

First, we're creating a JOIN table with a primary key: `CREATE TABLE student_course_enrollment ( enrollment_id SERIAL PRIMARY KEY`.

Then, we're adding a `NOT NULL` constraint to both of our foreign keys. A student shouldn't be able to enroll without a course, and vice versa: `student_id INT REFERENCES students(student_id) NOT NULL, course_id INT REFERENCES courses(course_id) NOT NULL`.

Finally, a student should only enroll in a course once; that's why we made the combination of both `student_id` and `course_id` unique: `UNIQUE (student_id, course_id)`.

If you describe your table, you can see all of the constraints above.

```
generalassembly=# \d student_course_enrollment
                                     Table "public.student_course_enrollment"
    Column     |  Type   | Collation | Nullable |                             Default                              
---------------+---------+-----------+----------+------------------------------------------------------------------
 enrollment_id | integer |           | not null | nextval('student_course_enrollment_enrollment_id_seq'::regclass)
 student_id    | integer |           | not null | 
 course_id     | integer |           | not null | 
Indexes:
    "student_course_enrollment_pkey" PRIMARY KEY, btree (enrollment_id)
    "student_course_enrollment_student_id_course_id_key" UNIQUE CONSTRAINT, btree (student_id, course_id)
Foreign-key constraints:
    "student_course_enrollment_course_id_fkey" FOREIGN KEY (course_id) REFERENCES courses(course_id)
    "student_course_enrollment_student_id_fkey" FOREIGN KEY (student_id) REFERENCES students(student_id)
```

### You Do

The stage is set. You have courses you can offer; you have instructors ready to teach them; you also have interested students. Now is the time to start making some money. Using the JOIN table we just created, enroll students in the courses they're interested in.

Make sure your Captain Barbossa gets at least a few students enrolled in his course. Let us all strive for peace on campus.

- Let's create a relationship between the following:
- 

```sql
INSERT INTO student_course_enrollment VALUES 
(default, 1, 1),
(default, 2, 2),
(default, 3, 1),
(default, 3, 2),
(default, 4, 2),
(default, 4, 1),
(default, 5, 2);
```

## How can we query this information? let's see!

```sql
SELECT students.first_name, students.last_name, courses.course_name FROM students, courses
WHERE students.student_id = 4;
```

```sql
SELECT students.first_name, students.last_name, courses.course_name FROM students, courses
WHERE courses.course_id = 2;
```

```sql
SELECT students.first_name, students.last_name, students.student_address_id, address.street, address.city, address.state, courses.course_name FROM students, address, courses
where address_id = student_address_id
order by student_address_id;
```

