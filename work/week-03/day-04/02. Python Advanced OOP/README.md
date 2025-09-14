# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Advanced OOP

## Objectives

*After this lesson, students will be able to:*

- Using special method attributes
- Making an object behave like a list
- Subclassing built-in types
- Understanding meta-classes
- Creating abstract base classes

### Object-oriented concepts

When it comes to creating a new piece of software, many developers become overwhelmed when they first start out. There is so much to learn and s many things to explore Consider the following:

- Infrastructure
- Platform software
- Architecture
- Design patterns
- The programming language
- Frameworks

In the context of object-oriented programming, objects are often referred to as "**nouns**" and the actions that determine their behavior are referred to as "**verbs**". A verb is commonly implemented as a method, which means that it is systematically coupled to the object that is being used to perform the action.<br/><br/>

Note : Programming in nouns and verbs is all about the encapsulation. It’s grouping properties (nouns) and methods (verbs) into a single cohesive unit (Object). The tricky part, it seems, is to decide what are the properties and methods to group together. Reducing this to nouns and verbs makes this much simpler.<br/><br/>

These are all terms you will hear when talking about Object-Oriented Programming:

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

There are a number of terms you are likely to hear when discussing Object-Oriented Programming that you should be aware of:<br/><br/>

| Term                 | Description |
|-----------------     |-------------|
| Class                | Factory of objects: encapsulating data and behavior |
| Instance             | A particular object of a class: a specific circle |
| Object               | Any value (in Python anyway). It also is the generic term for any class.|
| Attribute            | Something that belongs to an object (or class) |
| Method               | A function that belongs to a class or an instance of a class.|
| Encapsulation        | The grouping of data and function related to the same object |
| Data Protection      | The concept that data can be “private” or hidden. Python does not strictly support this. | 
| Class Instance Attrs | Attributes can be attached to a class or they can be attached to only that instance |
| Subclassing          | A class that “inherits” the attributes / methods of its “parent” class. |
| Overriding Methods   | The subclass inherits the methods of its parent class, or replace them. |
| Operator Overloading | Operators like +, -. *, etc. can be redefined in a class to have a new purpose. |
| Polymorphism         | Allowing instances of multiple classes to be used in the same way, but w/ their own meaning. |

### What is a special method attribute?

This is a special method attribute, as its name implies, and it refers to an attribute of a Python class that has a
unique meaning for Python. It’s defined as a method but isn’t intended to be used directly as such. A special method is usually not directly invoked; instead, it is called automatically by Python in response to a demand made on an object belonging to that class, once the object has been created.

Perhaps the simplest example of this is the `__str__` special method attribute. The `__str__` method attribute of a
class is invoked as soon as an instance of that class is used, and when Python requires a user-readable string
representation for that instance, the `__str__` method attribute of that class will be invoked, and its value will be used to represent that instance.

```python
# src/student.py
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


suresh = Student("Suresh", "Sigera")
print(suresh)

```

If you run the code above, you will see the following output:-

```text
<__main__.Student object at 0x104777730>
```

Let's add `__str__` method

```python
# src/student.py
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Full name: {self.first_name} {self.last_name}"


suresh = Student("Suresh", "Sigera")
print(suresh)

```

If you run the code above, you will see the following output:-

```text
Full name: Suresh Sigera
```

In spite of the fact that none of our code has explicitly invoked the `__str__` special method attribute, the attribute has nevertheless been used by Python, which knows that the str attribute (if present) defines a method to convert objects into user-readable strings in the event it is present. In some cases, these special methods can also be referred to as magic methods or dunder methods. You may want to keep in mind that special methods begin and end with double underscores.<br/><br/>

Use the `dir()` function to see the number of magic methods inherited by a class. For example, the following lists all the attributes and methods defined in the `Student` class.

```python
print(dir(Student))
```

As a result of running the code above, you will see the following output:-

```text
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__
gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__
reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

```

### `__add__()` method

One of the magic methods in Python is the `__add()__` method, which is one of the magic methods that returns a new
object (third), which is the result of adding the other two objects together. It implements the addition operator "**+**" in Python.

For example, the `__add__` method is a magic method which gets called when we add two numbers using the `+` operator.<br/><br/>

Consider the following example.

```text
Sureshs-MBP:python-advanced-oop suresh$ python3
Python 3.10.6 (main, Aug 30 2022, 05:12:36) [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> num + 5
15
>>> num.__add__(5)
15
>>> 
```

When you do `num+10`, as you can see, the + operator invokes the `__add__(10)` method when the + operator is used.
Alternatively, you can also call `num.__add__(5)` directly, which will give you the same result as calling `num.__add__(5)`. The only problem is, as we mentioned a moment ago, magic methods cannot be directly invoked, but rather, they should be invoked internally, through other methods or actions.<br/><br/>

The following example illustrates how a class called distance is defined with two instance attributes - feet and inches. In order to add these two distance objects to the list, it is desired to execute the addition using the overloading `+` operator.

```python
# src/distance.py

class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = Distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __str__(self):
        return 'ft:' + str(self.ft) + ' in:' + str(self.inch)


d1 = Distance(3, 10)
d2 = Distance(4, 4)
print("d1= {} d2={}".format(d1, d2))
d3 = d1 + d2
print(d3)

```

### `__ge__()` method

The following method is added in the distance class to overload the `>=` operator.

```python
# src/distance.py

class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = Distance()
        temp.ft = self.ft + x.ft
        temp.inch = self.inch + x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
            return temp

    def __ge__(self, x):
        val1 = self.ft * 12 + self.inch
        val2 = x.ft * 12 + x.inch
        if val1 >= val2:
            return True
        else:
            return False

    def __str__(self):
        return 'ft:' + str(self.ft) + ' in:' + str(self.inch)


d1 = Distance(3, 10)
d2 = Distance(4, 4)
print("d1= {} d2={}".format(d1, d2))
d3 = d1 + d2
print(d3)
print(d1 >= d2)

```

Run the above Python script to verify the overloaded operation of the `+` operator.

### Python - Public, Protected, Private Members

Classical object-oriented languages, such as C++ and Java, restrict access to class resources by means of public,
private, and protected keywords. A private member of a class is denied access by the environment outside the class to its members. In order to handle them, you can only do so within a class.

#### Public members

It is imperative to keep in mind that public members (generally methods declared in a class) can be accessed by anyone outside of the class. In order to invoke a public method, an object of the same class must be invoked. In this way, the principle of data encapsulation is ensured by the arrangement of private instance variables and public methods.<br/><br/>

```python
# src/student.py

class Student:
    schoolName = 'General Assembly'  # class attribute, this variable shared among all the objects

    def __init__(self, name, age):
        self.name = name  # public instance attribute
        self.age = age  # public instance attribute
```

Note: Class variables are defined within the class construction. Because they are owned by the class itself, class
variables are shared by all instances of the class. They therefore will generally have the same value for every instance unless you are using the class variable to initialize a variable.

#### Private members

It is imperative to note that Python does not have any mechanism that effectively limits access to any instance variable or method. To emulate the behavior of private access specifiers, Python prescribes a convention that begins the name of a variable/method with a single or double underscore before it. This produces the same effect as a private access specifier.

```python
# src/student.py

class Student:
    __school_name = 'General Assembly'

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__salary = age  # private instance attribute

    def __display(self):  # private method
        print('This is private method.')


student = Student("Suresh", 22)
print(student.__school_name)
print(student.__name)
print(student.__display)

```

As a result of running the code above, you will see the following output:-

```text
Traceback (most recent call last):
  File "/Users/suresh/Documents/ga/abbott/python-advanced-oop/student.py", line 13, in <module>
    print(student.__school_name)
AttributeError: 'Student' object has no attribute '__school_name'
```

### instance, class, and static methods

Methods are functions defined inside the body of a class. They are used to perform operations with the attributes of our objects. Methods are essential in encapsulation concept of the OOP paradigm. This is essential in dividing
responsibilities in programming, especially in large applications. You can basically think of methods as functions acting on an Object that take the Object itself into account through its self argument.

**Instance methods**

An instance method is able to access and modify various aspects of an object's state in a single call. If we use instance variables inside a method, such methods are called instance methods. The `self` parameter must be included in the method in order to refer to the current object in the program.

```python
# src/student.py

class Student:
    __school_name = 'General Assembly'

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__age = age  # private instance attribute

    # instance method
    def get_name(self):  # private method
        return f"{self.__name}"


student = Student("Suresh", 22)
print(student.get_name())


```

**Class methods**

A class state can be accessed or modified using this method. As far as method implementation is concerned, if we are only using class variables in the implementation, then such a method should be declared as a class method. It is imperative to note that the class method has a `cls` parameter which refers to the class itself.

```python
# src/student.py

from datetime import date


class Student:
    __school_name = 'General Assembly'

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__age = age  # private instance attribute

    # instance method
    def get_name(self):  # private method
        return f"{self.__name}"

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.__name + "'s age is: " + str(self.__age))


student = Student("Suresh", 22)
print(student.get_name())
joy = Student.calculate_age("Joy", 1995)
joy.show()

```

- In the above example, we created two objects, one using the constructor and the second using the `calculate_age()`
  method.
- The constructor takes two arguments `name` and `age`. On the other hand, class method takes `cls`, `name`,
  and `birth_year` and returns a class instance which nothing but a new object.
- The `@classmethod` decorator is used for `converting calculate_age()` method to a class method.
- The `calculate_age()` method takes `Student` class (`cls`) as a first parameter and returns constructor by calling
  `Student(name, date.today().year - birthYear)`, which is equivalent to `Student(name, age)`.

As a result of running the code above, you will see the following output:-

```text
Suresh
Joy's age is: 27
```

**Static methods**

Generally, a static method is defined as a general utility method that performs a task in an isolated manner. In this method, there is no use of instance or class variables, because this static method does not take any parameters, such as `self` and `cls`, inside of it.

```python
# src/employee.py

class Employee:

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)


kelly = Employee('Kelly', 12000, 'ABC Project')
jessa = Employee('Jessa', 7000, 'XYZ Project')

# false
# because separate copy of instance method is created for each object
print(kelly.work is jessa.work)

# True
# because only one copy is created
# kelly and jess objects share the same methods
print(kelly.gather_requirement is jessa.gather_requirement)

# True
print(kelly.gather_requirement is Employee.gather_requirement)

```

Note: There are limited uses for static methods because they do not have access to the attributes of an object (instance variables) and the attributes of a class (class variables). Nevertheless, they can be very useful when it comes to converting from one type to another, which is one of their most useful uses.

### Inheritance (IS-A) vs. Composition (HAS-A) Relationship

As we discussed earlier, inheritance is a mechanism that is used to allow us to take all of the properties of one class and apply them to our own. It is the parent class (also referred to as the base class) from which the attributes and functions are derived. There is a term known as a child class, which refers to a class that uses the properties of another class (also known as a derived class). The term "Is-A Relation" is another name for the concept of inheritance.<br/><br/>

As an example, Suresh is a full time student, or car is a vehicle.

As the name suggests, composition (HAS-A) simply refers to referencing other objects within an instance variable through a reference to them. As an example, a Maruti has an engine, or a house has a bathroom.

```python
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return f"Annual salary ${(self.pay * 12) + self.bonus}"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"my name is {self.name}"


class FullTimeEmployee(Person):
    def __init__(self, name, age, sal):
        self.name = name
        self.sal = sal
        super().__init__(name=name, age=age)

    def total_sal(self):
        return self.sal.annual_salary()


salary = Salary(10000, 1500)
suresh = FullTimeEmployee('Suresh', 25, salary)
print(suresh)
print(suresh.total_sal())

```

### Further Reading

This section provides more resources on the topic if you are looking to go deeper.

- [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/)