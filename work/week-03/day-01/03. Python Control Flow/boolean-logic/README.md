# ![Python for JavaScript Developers - Control Flow - Boolean Logic](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to implement conditional expressions in Python.

## Conditional expressions in Python

Control flow can typically be described as different code paths executing according to the evaluation of **conditional expressions**.

In other words, if the **conditional expression** evaluates to a truthy value, do something, optionally, do something else.

Let's review some of the logic and fundamentals of conditional expressions.

### Boolean values

Python has two logical boolean values: `True` and `False`.

Most logical operations result in one of these two values. They work the same as in JavaScript but are always written with a starting capital letter in Python.

## Equality operators

Equality operators are used to compare whether two values are equal.

- `==` - equal to
- `!=` - not equal to

There's only one type of equality operator in Python: `==`, which is the same as `===` in JavaScript.

### Examples

Check out the following examples:

```python
print(7 == 7)
# prints: True
# 7 is equal to 7

print(7 == "7")
# prints: False 
# 7 is an integer, and "7" is a string

print(7 != 7)
# prints: False
# 7 is equal to 7

print(7 != "7")
# prints: True 
# 7 is an integer, and "7" is a string; therefore, they cannot be equal
```

Execute the `control_flow.py` file with this command:

```bash
python3 control_flow.py
```

## Comparison operators

Python has all the same comparison operators as JavaScript:

- `<` - less than
- `>` - greater than
- `<=` - less than or equal
- `>=` - greater than or equal

### Examples

Let's try the following examples together. Use the `print()` function to print each  result in your console.

```python
print(8 > 8)
# prints: False 
# 8 is not greater than 8

print(8 >= 8)
# prints: True 
# 8 is greater than or equal to 8 (equal)

print(8 < 8)
# prints: False 
# 8 is not less than 8
```

## Logical operators

Logical operators we used in JavaScript work the same way in Python, except Python uses English words instead of symbols:

- `or` is the same as `||`
- `and` is the same as `&&`

Because they behave identically to their JavaScript counterparts, they always return either the ***first*** or the ***second*** operand as follows:

- `or` - Returns the first truthy operand, or the last operand.
- `and` - Returns the first falsy operand, or the last operand.

Python stops evaluating as soon as the result of the operation is determined.

### Examples

Let's try the following examples together. Use the `print()` function to print each result in your console. Remember that 0 is falsy and non-empty strings are truthy.

```python
# or
# returns the first truthy operand, or the last operand

print(True or False)
# prints: True

print(False or True)
# prints: True

print(False or False)
# prints: False

print('hello' or 0)
# prints: 'hello'

print(0 or 'hello')
# prints: 'hello'

print('hello' or 'tacos')
# prints: 'hello'

# and
# returns the first falsy operand, or the last operand

print(True and False)
# prints: False

print(False and True)
# prints: False

print('hello' and 0)
# prints: 0

print(0 and 'hello')
# prints: 0

print('hello' and 'tacos')
# prints: 'tacos'

```

Like in JavaScript, more than two conditions may be evaluated at a time. For example:

```python
# or
# returns the first truthy operand, or the last operand

print(True or True or True)
# prints: True

print(True or True or False)
# prints: True

# and
# returns the first falsy operand, or the last operand

print(True and True and True)
# prints: True

print(True and True and False)
# prints: False
```

You can also mix-and-match `and` and `or`:

```python
print(False or True and True)
# prints: True
```

> ⚠️ Be careful evaluating more than two items at a time, it can make code more difficult to read.

## The `not` operator

Just like the not operator in JavaScript (`!`), the `not` operator in Python flips a truthy expression to a boolean value of `False`, and a falsy expression to a boolean value of `True`.

### Examples

```python
print(not False)
# prints: True

print(not 'hello')
# prints: False
```
