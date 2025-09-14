# ![Python for JavaScript Developers - Python Classes - Class vs. Instance Members](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to compare and contrast class and instance members in Python.

## Class vs. instance members

In Python, attributes and methods (members) are categorized into two types based on whether they belong to instances of the class or the class itself:

- **Instance Attributes and Methods**: These are linked to **individual instances** of a class. Each object created from the class has its own copy of instance attributes. For example, in a `Dog` class, each `dog` object might have its own `name` and `age` attributes.
- **Class Attributes and Methods**: These belong to the **class** as a whole, not to any individual instance. All instances of the class share the same class attributes. This means that if one instance changes a class attribute, the change is reflected across all other instances. These are intended to be accessed on the class only, not an instance (although accessing them on the instance is technically possible).

To demonstrate class attributes, let's add a `next_id` class attribute to the `Dog` class that can be used to assign an `id` to each dog instance:

```python
class Dog():
    next_id = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        # assign the current value of `next_id` to this instance
        self.id = Dog.next_id
        # increment the class attribute `next_id` so the next dog gets a new ID
        Dog.next_id += 1

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'Dog #{self.id} named {self.name} is {self.age} years old.'
```

Note how the `Dog.next_id` class attribute is being accessed within the `__init__` method.

> 💡 Note: Technically, instances can also access class members via `self` because Python will look for a member on the class if it's not found on the instance.

Let's check that it worked:

```python
harry = Dog('Harry', 2)

print(harry)

maggie = Dog('Maggie')

print(maggie)
```

Cool, now let's see how class methods are created by adding a `get_total_dogs` method.

Add this to the bottom of the `Dog` class:

```python
    def __str__(self):
        return f'Dog #{self.id} named {self.name} is {self.age} years old.'

# new code below

    @classmethod
    def get_total_dogs(cls):
        # cls represents the Dog class
        return cls.next_id - 1
```

There are only two differences when defining a class method:

1. The `@classmethod` *decorator*.
2. The naming convention of the first parameter is to use `cls` instead of `self`.

> 💡 Decorators in programming are used to implement metaprogramming (when a program has knowledge or manipulates itself). In Python, [decorators](https://www.programiz.com/python-programming/decorator) are used to modify the behavior of a function or class.

Let's test out the new class method:

```python
spot = Dog('Spot', 2)
diogee = Dog('Diogee')

# class methods are called on the class, not an instance
print(Dog.get_total_dogs()) 
# prints: an integer representing however many dogs you've created!
```
