# ![Python for JavaScript Developers - Intro to Python - Data Types](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to check for and convert between Python data types.

## Data types in Python

Python is a true object-oriented programming language.

Every piece of data in Python is an object that's an instance of a *class*.

> 📚 A *class* is a blueprint for creating objects. This means that a string object will have different attributes and methods than an integer object because the string was created from a different blueprint than the integer.

### Checking the data type (class) of an object

We use the `type()` function to obtain the class used to instantiate the data:

```python
print(type("hello"))
# prints: <class 'str'>
```

Python's data types are similar to those available in JavaScript; there are just more of them. Above you can see an example of a string in Python, which is an instance of the `str` class.

Strings can be enclosed in double quotes or single quotes. Use either, but try to stick with one or the other.

### Integer numbers (`<class 'int'>`)

Unlike JavaScript, Python distinguishes between integers (whole numbers) and floating-point numbers (numbers with decimals).

When we don't follow a number literal with a decimal point, it is assumed to be an integer:

```python
print(type(25))
# prints: <class 'int'>
```

### Floating-point numbers (`<class 'float'>`)

Numbers with a decimal point are stored in variables as floating-point numbers - commonly called floats.

```python
print(type(3.14159))
# prints: <class 'float'>
```

Note that all it takes for an integer to become a float is the presence of a decimal, even if there's nothing after it:

```python
print(type(25.))
# prints: <class 'float'>
```

### Booleans (`<class 'bool'>`)

Named after George Boole, these are the logical data types often used in conditional expressions.

Just like in JavaScript, we have `true` and `false`, but they are capitalized in Python:

```python
print(type(True))
# prints: <class 'bool'>
```

You must start them with capital letters in Python, or they will not reflect the boolean values:

```python
print(type(true))
# NameError: name 'true' is not defined. Did you mean: 'True'?
```

### Nothingness (`<class 'NoneType'>`)

Similar to how JavaScript has the `null` value to represent nothingness, Python has `None`:

```python
print(type(None))
# prints: `<class 'NoneType'>`
```

The value `None` in Python, with a capital N, provides the same meaning as `null` in JavaScript.

### Other types

There are many other types. Refer to [Python's built-in types documentation](https://docs.python.org/3/library/stdtypes.html) for a comprehensive list and to see the attributes and methods available to all of them.

## Converting between data types

JavaScript attempts to automatically convert data types for us when necessary. This is known as implicit type coercion. This means JavaScript can automatically change one data type to another during operations, like when combining strings and numbers.

```javascript
let numTacos = 25;
let msg = "There are " + numTacos + " tacos.";
// msg is the string: "There are 25 tacos."
```

In this example, `numTacos` is a number, but when we concatenate it with strings, JavaScript implicitly converts `numTacos` into a string to create a single string.

However, in Python we cannot do this - there is no type coercion. With few exceptions, variables must be the same type to perform an operation on them. This does not work:

```python
num_tacos = 25
msg = "There are " + num_tacos + " tacos."
# TypeError: can only concatenate str (not "int") to str
```

Luckily, doing math operations between integers and floats is allowed, but not much else.

When the time comes to convert one data type into another, Python provides us with several global functions or predefined classes to do so:

```python
str(item)        # Converts `item` to a string
int(item, base)  # Converts `item` to an integer with the provided `base`
float(item)      # Converts `item` to a floating-point number
hex(int)         # Converts `int` to a hexadecimal string
oct(int)         # Converts `int` to an octal string
tuple(item)      # Converts `item` to a tuple
list(item)       # Converts `item` to a list
dict(item)       # Converts `item` to a dictionary
```
