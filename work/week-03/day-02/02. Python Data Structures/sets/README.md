# ![Python for JavaScript Developers - Python Data Structures - Sets](./assets/hero.png)

**Learning objective:** By the end of this lesson, learners will be able to understand the concept of sets in Python, differentiate them from other data structures, and demonstrate how to create and manipulate sets.

## Introduction to sets in Python

A ***set*** is an unordered collection of unique items called ***elements***. Unlike lists and tuples, sets do not allow duplicate elements. Sets are not indexed. Elements in a set can be added and removed but cannot be changed.

Sets are commonly used for mathematical operations like union, intersection, and difference. This makes them useful for tasks such as removing duplicates and finding common elements in multiple collections.

## Creating sets

There are two ways to define a set in Python - using curly braces (`{}`) or the `set()` function.

### Curly braces `{}`

Create a set from scratch using curly braces:

```python
integer_set = {1, 2, 3, 4, 5}
```

### The `set()` function

Or, more commonly, create a set from an iterable data type, like a list or tuple.

```python
another_int_set = set([5, 6, 7, 8, 9])

chips = ['potato', 'computer', 'fish and']

chips_set = set(chips)
```

## Operations on sets

Sets support various operations such as adding elements, removing elements, and performing mathematical set operations.

### Adding elements

In Python, you can add elements to a set using the `add()` method.

```python
# Adding elements to a set
chips_set.add('paint')
print(chips_set)
# prints: {'paint', 'fish and', 'potato', 'computer'}
# remember, sets are not ordered - your elements may print in a different order
```

### Removing elements

To remove elements from a set in Python, you can use the `remove()` method.

```python
# Removing elements from a set
chips_set.remove('fish and')
print(chips_set)
# prints: {'potato', 'paint', 'computer'}
# remember, sets are not ordered - your elements may print in a different order
```

### Mathematical operations

Sets can help performing more complex mathematical operations, such as discovering overlap between two collections of data - check out [this tutorial](https://realpython.com/python-sets/) from Real Python for more.
