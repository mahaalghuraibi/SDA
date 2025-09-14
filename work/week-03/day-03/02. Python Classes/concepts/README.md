# ![Python for JavaScript Developers - Python Classes - Concepts](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will understand the basic principles of object-oriented programming in Python, including the creation and manipulation of classes and objects.

## Object-oriented programming (OOP)

Object-oriented programming (OOP) is a programming paradigm that uses objects to design applications and computer programs. These objects represent real-world entities, encapsulating related properties (attributes) and behaviors (methods). Python is an object-oriented programming language, and this concept is central to writing Python code.

## The four key principles of OOP

### Encapsulation

Encapsulation is about keeping the data and behavior that manipulates that data under one roof within a class. This not only organizes the data and methods into manageable parts but can also protect the data by hiding it from outside interference, which can prevent misuse or errors.

### Inheritance

Inheritance allows a new class to receive or inherit attributes and methods from an existing class. This enables you to eliminate redundant code and extend the functionality of existing classes.

### Polymorphism and abstraction

While key to OOP, polymorphism and abstraction are more advanced concepts that are best learned after you've developed a deeper understanding of encapsulation and inheritance. We'll save these topics for another time.

## Classes

Classes enable us to implement the key principles of OOP in our applications.

At their most basic, classes are templates for creating objects. These new objects are called *instances* of that class. They specify what attributes and methods the objects will have.

A class defines characteristics (properties) and actions (methods) common to a group of objects. For instance, a `Car` class might specify properties like `make`, `model`, and `color` and a method like `drive()`. When we create individual cars (instances) from this class, each car inherits these properties and methods, allowing us to assign specific values (for example, a red Honda Civic) and perform actions (driving the car).

> 🧠 Classes offer a straightforward and efficient way to create reusable parts of an application.

![A Car class and its instances. The class has make, model, and color properties, which has been used to make 3 cars - an orange Ford Bronco, a red Honda Civic, and a blue BMW i4.](./assets/car-class-and-instances.png)

> 📚 An *instance* is an object produced by a class, containing all the properties and behaviors defined by that class.

In Python, the concept that everything is treated as an object is fundamental. This means that every entity, whether it's a data structure or a user-defined data type, has attributes (properties) and behaviors (methods) defined by its class. A class in Python acts as a blueprint for creating objects (instances).

Building these classes yourself is a powerful way to grasp object-oriented programming (OOP) principles. As you work more with classes, you'll see how encapsulation protects the data within an object and how inheritance lets you extend and customize existing code.

## Why use classes?

In Python, dictionaries can be created using dictionary literal syntax, so why are classes necessary?

Continuing from our car example above, imagine we are building an application for a car dealership. We want to track their inventory of cars and make modifications over time. When we build the application, we can't possibly know the make, model, and color of every car the dealership will ever sell.

Without classes, we would have to add a new dictionary literal in the application's code every time the dealership buys a new car. A more efficient approach can be taken with classes. We can construct a `Car` class that defines a car's basic structure and behaviors. In this example, every instance of a car has a `make`, `model`, and `color` and can be driven with the `drive()` method.

Going further, developers use classes to implement the four principles of OOP in applications, enabling more robust, modular, and reusable code.
