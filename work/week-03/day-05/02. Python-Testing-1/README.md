# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Unit Testing - Part 1

## Objectives

*After this lesson, students will be able to:*

- Explain what unit testing is and why it is important
- Organize the project structure for the purpose of unit testing
- Make use of assert statements
- Write & run unit test

### What is Unit Testing?

A unit test is a kind of test that aims to cover the application's functionality at the most *basic level possible*. It is very **imperative** to **test every single unit of code**, usually a function or a method, in isolation. This is in order to determine if it will perform as expected under certain circumstances. As soon as you break testing down to this level, you can be confident that each part of the application will behave as expected.<br/>

You'll be able to include edge cases where the unexpected happens, and will be prepared to handle them accordingly.<br/>

To put it another way, a unit test is a piece of code which imports parts of the code with the business logic and executes that logic, asserting multiple scenarios with the idea of guaranteeing certain conditions. There are some traits that unit tests must have, such as:<br/><br/>

- `Isolation`:In order to ensure that unit tests are completely independent of any external agents, they have to focus solely on the business logic that needs to be tested. In order to take advantage of this feature, they do not use a database, they do not execute HTTP requests, and so forth. In order to achieve isolation, the tests must also be independent among themselves: they must be able to run in any order and without being dependent on anything that might have happened previously.
- `Performance`: It is essential that unit tests run as quickly as possible. It is intended to run these programs multiple times, repeatedly in order to obtain the best results.
- `Repeatability`: As far as the software is concerned, unit tests must be able to objectively assess the status of the software in a deterministic manner. This means that the test results should be able to be repeated by the same tester again and again. Whenever a unit test fails, the test must keep failing until the code is fixed, as this is how unit tests assess the status of the code. If a test passes and no changes are made to the code, then the test should be expected to pass in the future. It is critical that your tests are not flaky or random in any way.
- `Self-validating`: In order for a unit test to produce a result, it must be executed. The process of completing the form should not require any additional steps; It is much easier to interpret the unit test (much less manual intervention is required).

### What Should You Test?

One of the most common questions that many developers ask, especially when they are just starting out, is what should test first? It is a legitimate question, and it is also one that is interesting, because the applications that are being built today are often vast and have many complexities to them. As you know, unit testing makes it a lot easier to do this task. This is because the whole idea of unit testing is to focus only on the **smallest components** of your code. _Instead, it is to try to think about how to test the entire application you are putting together_. In order to check that your code works as expected, you should always think about the kind of tests you will be writing before you start writing any code. You will be able to gain a lot of experience as you write more and more unit tests. You will be able to understand what works and what may cause problems later on.<br/><br/>

## Python Modules, Packages, and `__init__.py`

When structuring your project(s), you can follow some clear standards to make your application's code more accessible to other Python developers. These simple rules are easy to apply and result in a uniform structure to make it easy to find the test and code files you need.<br/><br/>

As projects grow, it is our responsiblity as engineers to organize our code and subdivide our code into smaller groups of code that are easier to follow.

1. **Modules**
- A **module** is just a Python file (`.py`) that contains code — functions, classes, or variables. We describe these files as modules so that we conceptualize them as files that we can access from other files with the idea that they are part of a bigger system or "package". 

2. **Packages**
- A **package** is a directory (folder) that contains **modules** or even other packages.
- To tell Python "this folder is a package," it must contain a special file named **`__init__.py`**.

Example structure:

```
my_project/
    my_package/
        __init__.py
        math_utils.py
        string_utils.py
```

3. **Role of `__init__.py`**
- It makes the folder **importable as a package**.
- Without it Python does not recognize the folder as a package.
- `__init__.py` is **good practice** because it allows you to:
  - **Initialize package-level variables**
  - **Control what gets imported** when someone does `from my_package import *`
  - **Re-export functions/classes** for convenience

## Unit Test Structure
Using our python packaging and modular system we can build a test directory where we can group together all of the testing we might want for our application. 

Generally speaking:

- Unit tests should be placed under a `test/unit` directory at the top level of your project folder.
- All folders within the application's code should be mirrored by test folders under `test/unit`, which will have the unit tests for each file in them. For example, `app/data` should have a mirrored folder of `test/unit/app/data`.
- All unit test files should mirror the name of the file they are testing, with `_test` the suffix. For example, `app/data/data_interface.py` should have a test file of `test/unit/app/data/data_interface_test.py`.

```text
.
├── README.md
├── src
├── __init__.py
├── add.py
└── test
    ├── __init__.py
    └── unit
        ├── __init__.py
        ├── test_add.py
        ├── test_module01.py
        ├── test_module02.py
        ├── test_module03.py
        └── test_module05.py
```

Let's test the packaging system works!...

### Using `unittest`

An example of a unit test program using a small calculator is considered to be one of the classic examples of unit testing. Let's build our folder structure / file system and set ourselves up to create some test files to test with.

#### Example 1

We will create an `add.py` file (module) inside of the `/src` folder and a `test_add.py` file (module) inside of `/test/unit/test_add.py` so that we can run a test! Contents below!

```python
# src/add.py

def addition(x, y):
    """Simple addition function"""
    return x + y

```

```python
# test/unit/test_add.py

import unittest

from src import add


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.addition(1, 5), 6)

if __name__ == '__main__':
    unittest.main()
```

**`if __name__ == '__main__':` is a Python conditional that checks whether the file is being run **directly** (as a script) rather than being imported as a module.**

`unittest.main()` is a function that:

- Discovers all `unittest.TestCase` subclasses in the file.
- Finds all methods whose names start with `test_`.
- Executes these test methods.
- Prints a summary of the results to the console.

Together:

```python
if __name__ == '__main__':
    unittest.main()
```

#### Code explanation:-

- We imported the `unittest` module and `add`.
- Created a class inheriting from `unittest.TestCase()`.
- Then we defined our test for the addition function. You must note that the method/function must start with `test_.`
- As a final step, we have used the `assertEqual` statement in order to verify equality.

To run a single test module, in this case `test_add.py`: First of all, make sure you are in the root directory of the project.

```text
(venv) Sureshs-MBP:python-unit-testing-1 suresh$ ls
README.md       src             test

```

- Run the following command in order to run the test: `python3 -m unittest test.unit.test_add`
- This is the result that you should see when you run the program:

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```

There is a list of assert statements available on [this page](https://docs.python.org/3/library/unittest.html#assert-methods) that you can use as per your requirements. Below is a list of some of the most common assert statements.

| Method                      | Checks for               |
|-----------------------------|--------------------------|
| `assertEqual(a, b)`         | a `==` b                 |
| `assertNotEqual(a, b)`      | a `!=` b                 |
| `assertTrue(x)`             | `bool(x)` `is` `True`    |
| `assertFalse(x)`            | `bool(x)` `is` `False`   |
| `assertIs(a, b)`            | a `is` b                 |
| `assertIsNot(a, b)`         | a `is` `not` b           |
| `assertIsNone(x)`           | x `is` `None`            |
| `assertIsNotNone(x)`        | x `is` `not` `None`      |
| `assertIn(a, b)`            | a `in` b                 |
| `assertNotIn(a, b)`         | a `not` `in` b           |
| `assertIsInstance(a, b)`    | `isinstance(a, b)`       |
| `assertNotIsInstance(a, b)` | `not` `isinstance(a, b)` |

#### Example 2

```python
# test/unit/test_module01.py
import unittest


class TestClass01(unittest.TestCase):
    def test_case_01(self):
        my_name_str = "Suresh Sigera "
        my_int = 1000
        self.assertTrue(isinstance(my_name_str, str))
        self.assertTrue(isinstance(my_int, int))

    def test_case_02(self):
        my_pi = 3.14
        self.assertFalse(isinstance(my_pi, int))


if __name__ == '__main__':
    unittest.main()

```

- In the code above, the `import unittest` statement imports the unittest module. `TestClass01` is the test class. It is subclassed from the [TestCase](https://docs.python.org/3/library/unittest.html) class in the unittest module.
- The class methods `test_case01()` and `test_case02(`) are test methods, as their names start with test_ (Later in the lesson, you will learn about the guidelines and naming conventions that should be followed when writing tests).
- The `assertTrue()` and `assertFalse()` methods are assertion methods which check if the argument passed to them is `True` or `False`, respectively.
- If the argument meets the `assert` condition, the test case passes; otherwise, it fails. `unittest.main()` is the test runner. We will explore more assert methods in detail later.<br/><br/>

Run the following command in order to run the test: `python3 -m unittest test.unit.test_module01 -v`<br/>
Since verbosity is disabled by default, the `-v` option will give you more detailed information about the test.

```text
(venv) Sureshs-MBP:unit suresh$ python3 -m unittest test.unit.test_module01 -v
test_case_01 (__main__.TestClass01) ... ok
test_case_02 (__main__.TestClass01) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

For a list of all the command-line options, use the following command `python3 –m unittest -h`

- `-h`, --help Show this message
- `-v`, --verbose Verbose output
- `-q`, --quiet Minimal output
- `-f`, --failfast Stop on first failure
- `-c`, --catch Catch control-C and display results
- `-b`, --buffer Buffer stdout and stderr during test runs

### Order of Execution of the Test Methods

```python
# test/unit/test_module02.py

import unittest
import inspect

debug = True


class TestClass02(unittest.TestCase):
    def test_case02(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])


if __name__ == '__main__':
    unittest.main(verbosity=2)

```

It is important to note that no matter which order the test methods were listed in the code, the test methods ran in alphabetical order. Using `inspect.stack()[0][3]`, you can print out the name of the test method that is currently running. When debugging, you can use it to see which methods are executed in which order in the test class.<br/><br/>

**How does it work?**

- `inspect.stack()` returns a list with frame records.
- The fourth element of the frame record (`inspect.stack()[0][3]`) is the function name.

```text
(venv) Sureshs-MBP:unit suresh$ python3 -m unittest test.unit.test_module01 -v
test_case01 (__main__.TestClass02) ... 
Running Test Method : test_case01
ok
test_case02 (__main__.TestClass02) ... 
Running Test Method : test_case02
ok

```

### Test Fixtures

A fixture is a set of resources needed for a test to be performed. Suppose, for example, that you are writing several tests about the same class, and each of those tests needs an instance of that class for testing purposes in order to run. Database connections and temporary files are other test fixtures that are often used. Many people would argue that the use of external resources makes these tests not "unit tests", but they can still be useful tests even if they are not "unit tests". It is pertinent to note that `TestCase` includes a hook that allows you to configure and clean up any fixtures that your tests may require. In order to **_configure_** the fixtures, you will need to override the `setUp()` method. In order to clean up, you need to override `tearDown()` to do so.

```python
# test/unit/test_module05.py

import unittest


class TestClass06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """called once, before any test"""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """called once, after all tests, if setUpClass successful"""
        print("In tearDownClass()...")

    def setUp(self):
        """called multiple times, before every test method"""
        print("\nIn setUp()...")

    def tearDown(self):
        """called multiple times, after every test method"""
        print("In tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case01()")

    def test_case02(self):
        self.assertFalse("python".isupper())
        print("In test_case02()")


if __name__ == '__main__':
    unittest.main()

```

- The `setUpModule()` and `tearDownModule()` methods are the module-level fixtures.
- `setUpModule()` method is executed before any method in the test `module.tearDownModule()` is executed after all methods in the test module.
- `setUpClass()` and `tearDownClass()` are class-level fixtures. `setUpClass()` is executed before any method in the test class. `tearDownClass()` is executed after all methods in the test class.

```python
# src/employee.py

class Employee:
    """Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'


if __name__ == '__main__':
    employee = Employee("Suresh", "Sigera")
    print(employee.fullname)

```

Now, whenever we create an instance of an employee with the first and last name, it will create the email and full name of the employee automatically. This is because we enter the first and last names. As well, the employee's full name and email address should be changed whenever the first or last name of the employee is changed.

```python
# test/unit/employee.py

import unittest
from src.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('saral', 'gyaan')
        emp_2 = Employee('udit', 'vashisht')
        self.assertEqual(emp_1.email, 'saralgyaan@email.com')
        self.assertEqual(emp_2.email, 'uditvashisht@email.com')

        emp_1.first = "first"
        emp_2.first = "second"

        self.assertEqual(emp_1.email, 'firstgyaan@email.com')
        self.assertEqual(emp_2.email, 'secondvashisht@email.com')

    def test_fullname(self):
        emp_1 = Employee('saral', 'gyaan')
        emp_2 = Employee('udit', 'vashisht')
        self.assertEqual(emp_1.fullname, 'Saral Gyaan')
        self.assertEqual(emp_2.fullname, 'Udit Vashisht')

        emp_1.first = "first"
        emp_2.first = "second"

        self.assertEqual(emp_1.fullname, 'First Gyaan')
        self.assertEqual(emp_2.fullname, 'Second Vashisht')


if __name__ == '__main__':
    unittest.main()

```

Running this will give the following output:-

```text
(venv) Sureshs-MBP:python-unit-testing-1 suresh$ python3 -m unittest test.unit.test_employee
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

```

The above test violates the **_DRY convention_** as we create instances of the individual for each test, and therefore we are creating instances of the individual for each test. We can overcome this problem by using the `setUp` and `tearDown` methods in our code and modifying the code accordingly. It is not strictly necessary that we pass the tearDown method. This is because it is only useful when testing involves the creation of files, databases, etc., and we want to be able to clean them up at the end of the test and start over. It will be helpful if we add the `print()` function to our tests so that we can illustrate how it works more clearly.

```python
# test/unit/employee.py

import unittest
from src.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("Setting up!")
        self.emp_1 = Employee('saral', 'gyaan')
        self.emp_2 = Employee('udit', 'vashisht')

    def tearDown(self):
        print("Tearing down!\n")

    def test_email(self):
        print("Testing email.")
        self.assertEqual(self.emp_1.email, 'saralgyaan@email.com')
        self.assertEqual(self.emp_2.email, 'uditvashisht@email.com')

        self.emp_1.first = "first"
        self.emp_2.first = "second"

        self.assertEqual(self.emp_1.email, 'firstgyaan@email.com')
        self.assertEqual(self.emp_2.email, 'secondvashisht@email.com')

    def test_fullname(self):
        print("Testing Full Name.")
        self.assertEqual(self.emp_1.fullname, 'Saral Gyaan')
        self.assertEqual(self.emp_2.fullname, 'Udit Vashisht')

        self.emp_1.first = "first"
        self.emp_2.first = "second"

        self.assertEqual(self.emp_1.fullname, 'First Gyaan')
        self.assertEqual(self.emp_2.fullname, 'Second Vashisht')


if __name__ == '__main__':
    unittest.main()
```

Output:-

```text
(venv) Sureshs-MBP:python-unit-testing-1 suresh$ python3 -m unittest test.unit.test_employee
Setting up!
Testing email.
Tearing down!

.Setting up!
Testing Full Name.
Tearing down!

.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

```

The output shows that the `setUp` method is called before all tests, and the `tearDown` method is called after all tests. This could be useful if you are running multiple tests.

Some of the use-cases might require that some code be run before the unit tests are run as well as some code to be run after the unit tests are run so that some code is run before and after the unit tests are run. In such a scenario, you can use two `class` methods named `setUpClass` and `tearDownClass`.

### Ignoring broken tests

There are times when a test is known to fail, but we do not want the test suite to report that failure to the user. The reason for this may be that a broken or unfinished feature already has tests written. However, we aren't focusing on improving it right now in order to fix it. There are many reasons why this occurs. The most common reason is that a certain feature does not exist on a specific platform, Python version, or in an advanced version of a certain library. As a Python user, it is possible to use a few decorators to mark tests with the expectation that they will fail. This can enable you to skip them if conditions are known to occur.<br/>

These decorators are as follows:

- `expectedFailure()`
- `skip(reason)`
- `skipIf(condition, reason)`
- `skipUnless(condition, reason)`

The `skip` method goes one step further and doesn't even bother to run the test. In order to skip the test, it expects only one string argument describing the reason why it was omitted. The other two decorators accept two arguments, one a Boolean expression that indicates whether or not the test should be run, and a similar description. In use, these three decorators might be applied as they are in the following code:

```python
import unittest
import sys


class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 4, "broken on 3.4")
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(
        sys.platform.startswith("linux"), "broken unless on linux"
    )
    def test_skip_unless(self):
        self.assertEqual(False, True)


if __name__ == "__main__":
    unittest.main()
```

Running this using `python3 -m unittest test.unit.test_skip -v` will give the following output:-

```text
test_fails (test.unit.test_skip.SkipTests) ... expected failure
test_skip (test.unit.test_skip.SkipTests) ... skipped 'Test is useless'
test_skip_if (test.unit.test_skip.SkipTests) ... FAIL
test_skip_unless (test.unit.test_skip.SkipTests) ... skipped 'broken unless on linux'

======================================================================
FAIL: test_skip_if (test.unit.test_skip.SkipTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/suresh/Documents/ga/abbott/python-unit-testing-1/test/unit/test_skip.py", line 16, in test_skip_if
    self.assertEqual(False, True)
AssertionError: False != True

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=1, skipped=2, expected failures=1)
```

The `x` on the first line indicates an expected failure; the two `s` characters represent skipped tests, and the `F`
indicates a real failure, since the conditional to `skipUnless` was True on my system.

### Further Reading

This section provides more resources on the topic if you are looking to go deeper.

- [unittest](https://docs.python.org/3/library/unittest.html) module (and the list
  of [assert](https://docs.python.org/3/library/unittest.html#assert-methods) methods)
- [TestCase](https://docs.python.org/3/library/unittest.html)
- [Inspect](https://docs.python.org/3/library/inspect.html)
