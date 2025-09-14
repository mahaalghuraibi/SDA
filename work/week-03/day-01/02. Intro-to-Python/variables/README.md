# ![Python for JavaScript Developers - Intro to Python - Variables](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to define and reassign Python variables.

## Python variables

Variables in Python hold the data an app needs when it runs, much like they do in JavaScript.

### Declaring

Here is how we declare a variable in Python:

```python
num = 15
```

Notice the lack of `let` or `const` keywords. In Python, we only need to decide on a variable's name and the value we want to assign to it. There is no way to define a constant variable in Python, but there are conventions to help us communicate that a variable should be a constant, which we'll cover soon.

You cannot declare a variable without assigning to it:

```python
movie
# returns: NameError: name 'movie' is not defined
# this is illegal syntax that cannot be used
```

This is because there is no `undefined` data type in Python.

### Naming convention

Variables are case sensitive - `num` and `Num` would be two different variables.

When you have a variable name with multiple words, the convention is to **snake_case** the identifier:

```python
# in Python, we use snake_case
my_number = 10
```

### Reassigning variables

We can freely assign a new value to a variable after it has been declared:

```python
my_number = 15
print(my_number)
# prints: 15
my_number = -4
print(my_number)
# prints: -4
```

Reassignment replaces the current value, and the previous value is lost, just like in JavaScript.

### Constants

While Python doesn't have a way to declare constants, the convention is to declare any variable you'd like to be known as a constant in `SCREAMING_SNAKE_CASE`.

```python
MY_FAVORITE_NUMBER = 5
```

> ⚠️ This convention does not prevent reassignment. It only communicates that the variable is not intended to be reassigned.
