# ![Python for JavaScript Developers - Python Classes - Instantiating Objects](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to create a class and instantiate objects from it.

## Instantiating objects from classes

In programming, classes are the blueprints for objects. They define the properties and behaviors the objects will have, but they are not objects themselves. To create objects from classes, we use the term *instantiate*.

> 🧠 The proper way to express this concept is to say, "I am *instantiating* an object from this class." It is incorrect to say, "I am instantiating a class by creating this object." this is a common misconception. Objects are instantiated, not classes.

By defining the `Dog` class, we now know the structure each pooch will have!

Let's *instantiate* a new dog object:

```python
ruby = Dog('Ruby', 3)

print(ruby)
# prints: something like <__main__.Dog object at 0x1031c0f90>

# print the `name` and `age` attributes of the ruby object
print(ruby.name, ruby.age)
# prints: Ruby 3

# invoke the ruby object's bark instance method
ruby.bark()
# prints: Ruby says woof!
```

> 💡 Recall that Python dictionaries use square bracket notation to access and set the value of an item. Objects instantiated by our Python classes use dot notation instead.

Let's try out the default parameter for a new dog's age:

```python
# don't pass a second argument
liam = Dog('Liam')

print(liam.name, liam.age)
# prints: Liam 0
```
