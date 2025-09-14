# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Exception Handling

## Objectives

*After this lesson, students will be able to:*

- Describe what an exception is
- Find errors and debug code
- Handle multiple exception during the runtime

### What are exceptions?

There may be times when, while executing a Python program, an issue arises that prevents the program from executing at all, or if it does execute, the program generates unexpected output or behaves abnormally. This type of error is caused by `syntax errors`, `runtime errors`, or `logical errors` in the code.<br/><br/>

In Python, exceptions are errors that get triggered automatically. There is however the possibility that exceptions can be forcedly triggered and handled through the code of the program. As part of this lesson, we will learn about how to handle exceptions in Python programs.<br/><br/>

The first error that programmers (even experienced ones) are confronted with is when the code has incorrect syntax, meaning that the code instructions are not correctly formatted.<br/><br/>

Consider this example of a syntax error:

```text
>>> for i in range(10)
  File “<stdin>”, line 1
    for i in range(10)
                      ^
SyntaxError: invalid syntax
```

In the case of the `for` declaration, there is an error that occurs due to the fact that there is no colon at the end of the statement. As you can see, this is an example of an exception being thrown. It is important to remember that `SyntaxError` is an error that not only informs the programmer that there is an error with the syntax of the code, but also prints the line where the error occurred with an arrow that indicates where the error is located in that line.

### Types of exceptions

There are various exceptions in Python that are derived (inherited) from a base class called the `Exception` class. Exceptions are a significant part of Python, and they come with a number of built-in features.<br/>

As per Python's [documentation](https://docs.python.org/3/library/exceptions.html), the following is a list of the built-in exceptions and what they mean.

| Exception |   Cause  |
|-----------|----------|
| AssertionError       | Raised when assert statement fails |
| AttributeError       | Raised when attribute assignment or reference fails |
| EOFError             | Raised when the input() function hits end-of-file condition |
| FileNotFoundError    | Raised when a requested file / directory doesn’t exist |
| FloatingPointError   | Raised when a floating point operation fails |
| GeneratorExit        | Raised when a generator's close() method is called |
| ImportError          | Raised when the imported module is not found |
| IndexError           | Raised when index of a sequence is out of range |
| KeyError             | Raised when a key is not found in a dictionary |
| KeyboardInterrupt    | Raised when the user hits interrupt key (Ctrl+C or delete) |
| MemoryError          | Raised when an operation runs out of memory |
| NameError            | Raised when a variable is not found in local or global scope |
| NotImplementedError  | Raised by abstract methods|
| OSError              | Raised when system operation causes system-related error|
| OverflowError        | Raised when result of an arithmetic operation is too large to be represented|
| ReferenceError       | Raised when a weak reference proxy is used to access a garbage collected referent|
| RuntimeError         | Raised when an error does not fall under any other category|
| StopIteration        | Raised by next() function to indicate no further items to iterate|
| SyntaxError          | Raised by parser when syntax error is encountered|
| IndentationError     | Raised when there is incorrect indentation|
| TabError             | Raised when indentation consists of inconsistent tabs and spaces|
| SystemError          | Raised when interpreter detects internal error|
| SystemExit           | Raised by sys.exit() function|
| TypeError            | Raised when a function or operation is applied to an object of incorrect type|
| UnboundLocalError    | Raised when a reference is made to a local variable where no value has been bound to that variable |
| UnicodeError         | Raised when a Unicode-related encoding or decoding error occurs|
| UnicodeEncodeError   | Raised when a Unicode-related error occurs during encoding |
| UnicodeDecodeError   | Raised when a Unicode-related error occurs during decoding |
| UnicodeTranslateError| Raised when a Unicode-related error occurs during translating |
| ValueError           | Raised when a function gets argument of correct type but improper value |
| ZeroDivisionError    | Raised when second operand of division or modulo operation is zero | 

As shown in the table above, every time an exception occurs and an exception error is raised in the interpreter, the execution of a program is halted.<br/><br/>

You can use the `try` keyword to catch exceptions thrown by the code, and when an exception occurs, you can use the `except` keyword to provide code to handle the error when it occurs.

### Process of handling exception

When an error occurs, Python interpreter creates an object called the **_exception object_**. This object contains information about the error like its type, file name and position in the program where the error has occurred.<br/><br/>

The object is handed over to the runtime system so that it can find an appropriate code to handle this particular exception. This process of creating an **exception object** and handing it over to the runtime system is called ** throwing** an exception. It is important to note that when an exception occurs while executing a particular program statement, the control jumps to an exception handler, abandoning execution of the remaining program statements.<br/><br/>

The runtime system searches the entire program for a block of code, called the _exception handler_ that can handle the raised exception. It first searches for the method in which the error has occurred and the exception has been raised. If not found, then it searches the method from which this method (in which exception was raised) was called. This hierarchical search in reverse order continues till the exception handler is found. This entire list of methods is known as _call stack_.
<br/><br/>

When a suitable handler is found in the call stack, it is executed by the runtime process. This process of executing a suitable handler is known as catching the exception. If the runtime system is not able to find an appropriate exception after searching all the methods in the call stack, then the program execution stops.<br/><br/>

Note: A programmer can also create custom exceptions to suit one’s requirements. These are called _user-defined exceptions_. We will learn how to handle exceptions in the next section.

### Catching exceptions using `try` and `except`

An exception is said to be caught when a code that is designed to handle a particular exception is executed. Exceptions, if any, are caught in the try block and handled in the except block. While writing or debugging a program, a user might doubt an exception to occur in a particular part of the code. Such suspicious lines of codes are put inside a `try` block.<br/><br/>

**Every `try` block is followed by an `except` block**. The appropriate code to handle each of the possible exceptions (in the code inside the try block) are written inside the except clause.<br/><br/>

- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `else` block lets you execute code when there is no error.
- The `finally` block lets you execute code, regardless of the result of the `try` and `except` blocks.

While executing the program, if an exception is encountered, further execution of the code inside the `try` block is stopped and the control is transferred to the `except` block. The syntax of `try` … `except` clause is as follows:

```text
try:
    [program statements where exceptions might occur]
except [exception-name]:
    [code for exception handling if the exception-name error is encountered]
```

Consider the Program 1-2 given below:

```python
import sys

file_object = open("/user/ecommerce/data.csv", "r")
```

Based on the analysis of the above code, which type of error is likely going to occur during the execution of the code as a result of analyzing its structure?

<details>
  <summary>Answer</summary>

```text
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    file_object = open("/user/ecommerce/data.csv", "r")
FileNotFoundError: [Errno 2] No such file or directory: '/user/ecommerce/data.csv'    
```

</details>

<hr>

```python
a = 5
b = 0
print(a / b)
```

Based on the analysis of the above code, which type of error is likely going to occur during the execution of the code as a result of analyzing its structure?

<details>
  <summary>Answer</summary>

```text
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print (a/b)
ZeroDivisionError: division by zero
```
</details>

You can catch the exception by putting your code in the `try` block and your error handling code for each exception in the `exception` block as shown here:

```python
import sys

try:
    file_object = open("/user/ecommerce/data.csv", "r")
except FileNotFoundError:
    print("Cannot load the file")
```

Sometimes, a single piece of code might be suspected to have more than one type of error. For handling such situations, we can have multiple `except` blocks for a single `try` block as shown below.

```python
try:
    file_object = open("/user/ecommerce/data.txt", "r")
    data = file_object.read()
    print(data)
except IOError:
    print("file cannot be opened")
except ValueError:
    print("function receives an argument that has the right type but an invalid value")
except EOFError:
    print("When the input reaches the end of a file and no more data can be read")
print("rest of the program")
```

### The `else` and `finally` clause

There are several other components of exception handling and that are the `else` and `finally` clauses.

We have already been able to use `try` and `except` statements, which are used to catch errors. Let's now look at the `else` and `finally` statements as well.

The `else` clause is used to execute code when the program does not raise an exception. It is also better to use the `else` clause than to add additional code to the `try` clause. This is because it avoids unintentionally catching an exception that wasn't raised by the code being protected by the `try`/`except` statements.

Consider the example:

```python
while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a valid number!")
    else:
        print("%s squared is %s" % (x, x ** 2))
```

**The `finally` clause** : This clause is meant to define **clean-up actions** that must be **performed regardless of whether an exception was raised or not**. A `finally` clause must always be executed before leaving the `try`/`except` statement, whether an exception has occurred or not. This is usually used to clean up, like to close an open file.<br/><br/>

Let's include the `finally` clause in our example:

```python
count = 0

while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a valid number!")
    else:
        print("%s squared is %s" % (x, x ** 2))
    finally:
        print("Ran %s time(s)" % count)
```

### Creating custom exception

In Python, users can define custom exceptions by creating a new class. This exception class has to be derived, either directly or indirectly, from the built-in Exception class. Most of the built-in exceptions are also derived from this class.

`error.py`

```python
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

```

`demo.py`

```python
from errors import ValueTooLargeError, ValueTooSmallError

# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

```

### Summary

- Syntax errors or parsing errors are detected when
  we have not followed the rules of the particular
  programming language while writing a program.
- When syntax error is encountered, Python displays
  the name of the error and a small description
  about the error.
- The execution of the program will start only after
  the syntax error is rectified.
- An exception is a Python object that represents
  an error.
- Syntax errors are also handled as exceptions.
- The exception needs to be handled by the
  programmer so that the program does not
  terminate abruptly.
- When an exception occurs during execution
  of a program and there is a built-in exception
  defined for that, the error message written in that
  exception is displayed. The programmer then has
  to take appropriate action and handle it.
- Some of the commonly occurring built-in
  exceptions are `SyntaxError`, `ValueError`,
  `IOError`, `KeyboardInterrupt`, `ImportError`,
  `EOFError`, `ZeroDivisionError`, `IndexError`,
  `NameError`, `IndentationError`, `TypeError`,and
  `OverFlowerror`.
- An exception is said to be caught when a code
  that is designed to handle a particular exception
  is executed.
- An exception is caught in the try block and
  handles in except block.

### Exercise

- When are the following built-in exceptions raised? Give
  examples to support your answers.
    - `ImportError`
    - `IOError`
    - `NameError`
    - `ZeroDivisionError`
- Define the following:
    - Exception Handling
    - Throwing an exception
    - Catching an exception

Consider the code given below and fill in the blanks.

```python
print(" Learning Exceptions...")
try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))
    quotient = (num1 / num2)
    print("Both the numbers entered were correct")
except _____________:  # to enter only integers
    print(" Please enter only numbers")
except ____________:  # Denominator should not be zero
    print(" Number 2 should not be zero")
else:
    print(" Great .. you are a good programmer")
    print(" JOB OVER... GO GET SOME REST")
```
  
### Further Reading

This section provides more resources on the topic if you are looking to go deeper.
  
- [What is exception handling?](https://www.techtarget.com/searchsoftwarequality/definition/error-handling)
- [The Python Exception Class Hierarchy](https://blog.airbrake.io/blog/python/class-hierarchy)
- [Python Exceptions are Exceptional - and so much more than error handling!](http://conquerprogramming.com/blog/3-Exceptions.html)
