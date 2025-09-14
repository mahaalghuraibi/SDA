# ![Python for JavaScript Developers - Intro to Python - Performing Operations](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to perform basic mathematical operations in Python.

## Math operations

Python has the normal math operators that you are used to from JavaScript:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulo (remainder) (`%`)
- Exponentiation (`**`)

All work as you would expect. However, there are a few special operations worth mentioning.

### Integer division

By default, when you divide two numbers (whether they are ints, floats, or a combination of the two), the result is a float, even if there is no remainder:

```python
result = 4 / 2
print(result)
# prints: 2.0
print(type(result))
# prints: <class 'float'>
```

You're able to force the result of division to an integer by using `//` instead of `/`:

```python
result = 4 // 2
print(result)
# prints: 2 because the decimal ".0" is truncated
```

This will always round down - everything after the decimal is removed, similar to using the `Math.floor()` method in JavaScript.

### Shortcut Assignment Operators

As we saw in JavaScript, reassigning the result of an operation on a variable to the same variable is common. It is so common that several shortcut operators exist to make these types of operations easier to write.

Python has the same operators:

```python
# this line of code:
num = num + 1
# can be written with this shortcut operator:
num += 1

# it also works for any of the other math operations:
num = num / 5
# can be rewritten like this:
num /= 5

# and this line:
num = num * 3
# can be written as this:
num *= 3
# and so on with the other operators
```

> ⚠️ A couple of our favorite operators in JavaScript, increment (++) and decrement (--), do not exist in Python. Use += 1 and -= 1 instead.
