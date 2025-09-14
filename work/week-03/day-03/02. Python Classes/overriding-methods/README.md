# ![Python for JavaScript Developers - Python Classes - Overriding Methods](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to override methods in a class.

## Overriding methods

Previously, when we used `print(ruby)` to print the `ruby` object, we got an unfriendly output similar to `<__main__.Dog object at 0x1031c0f90>`.

We can change this behavior by overriding the `__str__()` method that the print function calls automatically to obtain the string to print out.

Let's modify the `Dog` class to override the `__str__()` method:

```python
class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} says woof!')

    def __str__(self):
        return f'The dog named {self.name} is {self.age} years old.'
```

Try it out:

```python
ruby = Dog('Ruby', 3)

print(ruby)
# prints: The dog named Ruby is 3 years old.
```

Data and variables in Python have attributes and methods based on their data type.

For example, here's how you can see the attributes and methods associated with a list object:

```python
# Create a list
nums = [1, 2, 3]
# Use the dir() function to list all attributes and methods of the list
print(dir(nums))
```

You might recognize methods like `append` and `pop` which are used to add and remove elements from the list, respectively.

Try this with the `ruby` object:

```python
print(dir(ruby))
```

Here, you can see the attributes and methods associated with the `ruby` object. Some like `__init__`, `age`, `bark`, and `name` will look familiar. There's a collection of magic methods that are all new to us though.

These methods exist on our `ruby` object by default, but they won't be used directly by us. For example, the `__init__()` method is called when an object is created, and `__str__()` is called when an object is converted to a string such as when we wrote `print(ruby)`.

Just because we don't call them directly doesn't mean we can't override their behavior though. Overriding the `__str__()` method is an example of *polymorphism*.

> 📚 *Polymorphism* is a principle in OOP that is literally defined as "having many forms". In OOP this means that instantiated objects are treated as instances of a class, rather than the actual class. They can be modified without also modifying the class.
>
> For example, our `Dog` class modified the default behavior of the `__str__()` method, but that default behavior still exists. If we created another class, the behavior of that class' `__str__()` method would be the default behavior.
