# ![Python for JavaScript Developers - Intro to Python - Working with Strings](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to write multiline strings, perform string interpolation, and use string methods to work with string types in Python.

## Working with strings

Python has strings for holding text, just like JavaScript:

```python
my_string = "A double-quoted string"
your_string = 'A single quoted string'
```

You can also create multiline strings by using a triple quote (single or double):

```python
multiline_string = '''This is my string that
                      goes on multiple lines
                      for whatever reason'''
```

### Concatenating strings

One or more strings can be combined into a single string in the same way we do it in JavaScript by using the `+` operator:

```python
little_string = "bad"
medium_string = "super"
long_string = medium_string + little_string
print(long_string)
# prints: superbad
```

### String interpolation using f-Strings

You might recall using string template literals in JavaScript, which allow embedding expressions in strings using backticks and `${}`.

Python's approach is similar but has a key difference: you must prefix the string with an `f` to indicate it's an f-string (formatted string literal).

```python
state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
print(message)
# prints: Hawaii was the last state to join the U.S. in 1959.
```

When the `f` is placed directly before a string's opening quote (single or double), it makes a formatted string or ***f-string*** for short.

Once we do this, we can put expressions into curly braces to include the result of the expressions in the final string.

## Useful string methods

Like JavaScript, Python has several string methods we can use for string manipulation.

Some are familiar, like `split()`, but others have different names:

```python
print("ace of spades".split(" "))
# prints: ['ace', 'of', 'spades']

# however, this won't work:
print("abcd".split(""))
# ValueError: empty separator

# instead, use the list() function like this:
print(list("abcd"))
# prints: ['a', 'b', 'c', 'd']

# get the index of a substring:
print("abcd".index("c"))    
# prints: 2
# this method raises an error if the substring is not found:
print("abcd".index("e"))
# ValueError: substring not found

# .find() is similar to .index() but returns -1 if the substring is not found
# this behavior may be preferable to raising an error:
print("abcd".find("e"))
# prints: -1

print("boo".upper())
# prints: 'BOO'

print("WHY???".lower())
# prints: 'why???'

print("Then I went to the store I like".replace("I", "you"))
# prints: 'Then you went to the store you like'
```

Want to know if a string contains a substring? You don't even need a method for that! You can use the `in` operator to quickly find out if one string appears in another.

```python
print("eggs" in "green eggs and ham")
# prints: True
```

Use the built-in global `len()` function on a string to find its length.

```python
print(len("Tacos"))
# prints: 5
```

### More string methods

It might be hard to believe but the above methods represent only a small fraction of the string methods available in Python. For more, check out the [Python docs covering string methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
