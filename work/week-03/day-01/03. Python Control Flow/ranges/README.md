# ![Python for JavaScript Developers - Control Flow - Ranges](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to identify and use ranges in Python.

## Purpose of ranges

Python ***ranges*** are a sequence type, similar to a list.

The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in `for` loops.

Ranges have their own class (type): `range`.

## Basic syntax

Ranges can only be created by invoking the `range()` class:

```python
for num in range(5):
    print(num)
    # prints the integers: 0, 1, 2, 3, 4
```

By default, the sequence starts at `0` and goes up to, but does not include, the integer passed in.

Ranges can also generate more complex sequences when passed a ***start*** and a ***step***:

```python
for even in range(4, 12, 2):
    print(even)
    # prints the integers: 4, 6, 8, 10
```

The ***start*** (the first argument above - `4`) indicates the starting integer.

The ***step*** (the last argument above - `2`) is an integer added to the current value after each iteration to determine the next value.

When not passed in, the start value defaults to `0`, and the step defaults to `1`.

Ranges can also be used to create lists:

```python
nums = list(range(10))
print(nums)
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Negative step

If the step is a negative integer, the sequence counts down:

```python
for num in range(5, 0, -1):
    print(num)
    # prints the integers: 5, 4, 3, 2, 1
```

## More on ranges

For more detail on ranges, check out the [Python docs](https://docs.python.org/3/tutorial/controlflow.html#the-range-function).
