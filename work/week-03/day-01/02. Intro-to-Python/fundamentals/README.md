# ![Python for JavaScript Developers - Intro to Python - Fundamentals](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to leave code comments and print data to the console.

## Comments

Single-line comments in Python start with the `#` character and continue to the end of the line.

```python
# This is a comment! Python will ignore it.
```

Everything on that line after the `#` is ignored when the code is evaluated, but you can place code to be executed before the `#` on the same line.

To make multiline comments, use three quotes (either as `"""` double quotes or `'''` single quotes) wrapped around your comments, or use the `#` character at the start of each line:

```python
"""
this is a
multiline comment
"""

'''
this is also a multiline comment
you can use either set of quotes
'''

# this is a
# multiline comment
```

Multiline comments are often used to document what a function or module does; therefore, they are sometimes referred to as ***docstrings***.

## Printing to the console

In Python, we use the `print()` function to print a message to the console.

```python
print("Hello, world!") # prints: Hello, world!
```

## Executing Python

Any Python script can be executed from the terminal using this command:

```bash
python3 <filename>.py
```

Replacing `<filename>` (including the `<` and the `>`) with the name of the python file you'd like to execute.

For example, to execute the `intro_to_python.py` file, use:

```bash
python3 intro_to_python.py
```

You should see the text you passed to the `print()` function printed to the console.
