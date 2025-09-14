# ![Python for JavaScript Developers - Control Flow - If...Else](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to use `if...else` statements to implement control flow in Python.

## Indentation

Before we practice more control flow, it's essential to know that ***Python uses indentation to define blocks of code*** - not curly braces.

In JavaScript, we used indentation for readability purposes; however, proper indentation is mandatory in Python!

## Branching with the `if` statement

Like in JavaScript, we can run one of several code paths depending upon the result of conditional expression(s).

Single path `if` statement:

```python
floor = "sticky"
walls = "clean"

# notice the colon ':' after the conditional expression
# it indicates the start of the if block
if floor == "sticky":
    print("Clean the floor! It's sticky!")
    # this is where you would add more lines of code related to the condition
    # each line must be indented to be part of the 'if' block

# unindented code indicates that we have returned to normal code execution
print("This will always print, it's not inside of an if block!")

# parentheses are not required around the conditional expression
if walls == "sticky":
    print("Clean the walls! They're sticky!")
```

> 🧠 A quick note on code style - we follow the [PEP8 Style Guide for Python Code](https://peps.python.org/pep-0008/) as closely as possible for all our work in Python. In this convention we use 4-space indentation.

Dual path `if...else` statement:

```python
val = 3

# if path
if val == 1:
    print('val is one')
# else path
else:
    print('val is not one')
    # prints: val is not one
    # since val is not 1, the else path is taken
```

Multi-path `if...elif...else` statement:

```python
val = 3

if val == 1:
    print('val is one')
elif val == 2:
    print('val is two')
elif val == 3:
    print('val is three')
    # prints: val is three
    # since val is 3, this elif path is taken
else:
    print('not one, two, or three')
```

The `elif` is not a typo! It is Python's syntax for `else if`

`else` is always optional, just like it is in JavaScript.

> 🧠 Note: There is no switch construct in Python.

## 🎓 You Do

In your **`control_flow.py`** file, add the following code that accepts text input from the user:

```python
color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')
```

Below that code, write an `if...elif...else` statement that prints out one of the following messages:

- If `green` is entered, print the message `Go!`
- If `yellow` is entered, print the message `Slow Down!`
- If `red` is entered, print the message `Stop!`
- If anything else is entered, print the message `Bogus!`

Use the following command to run this code in your terminal:

```bash
python3 control_flow.py
```
