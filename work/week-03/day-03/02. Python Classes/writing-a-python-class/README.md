# ![Python for JavaScript Developers - Python Classes - Writing a Python Class](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to write a Python class with instance methods and default parameters.

## Writing a `Dog` class

Let's define a `Dog` class to create new dogs from:

```python
class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')
```

> 💡 The naming convention for Python classes is UpperCamelCasing - just like in JavaScript.

### `__init__()`

When a new dog is created, Python ***automatically*** calls the `__init__()` method.

In Python, methods with names beginning and ending with double underscores `__` are known as ***dunder*** (double underscore) or ***magic*** methods. These are special methods that Python calls internally for certain operations. When referring to the `__init__()` method by name in conversation, it would be common to use the language ***dunder init***.

`__init__` is short for initialize, which is an appropriate name for a method used to initialize the new object's properties.

> ❓ What method in JavaScript classes performs the same thing?

Inside the `__init__()` method, we define the attributes that exist on instances of the class. Instances of the `Dog` class will have `name` and `age` attributes.

The `age = 0` in `__init__`'s parameter list is a ***default parameter***. If we don't give a dog an age when we create it by passing an argument in that position, then the dog's age will be 0 as specified by `= 0`.

`bark()` is an *instance method* in this Dog class.

> 📚 An *instance method* is a function defined inside a class that operates on instances of that class. Put another way, every object created from the `Dog` class will have a `bark()` method!

### `self`

You might recall using the `this` keyword in JavaScript. Every object-oriented programming language has a similar mechanism. This mechanism allows a method within an object to:

- Access other properties or methods in the same object.
- Use a single copy of a method in memory to interact with any number of object instances.

In Python, `self` functions similarly but with a key difference - `self` is not a keyword. Instead it's a parameter name, and it is called `self` by convention.

When defining methods on Python classes, such as `__init__()` or `bark()`, the first parameter is typically named `self`. This parameter refers to the instance on which the method is being called.
