# ![Python Functions - Parameters and Arguments](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to declare a function with parameters and call a function using arguments.

## Parameters

Just like in JavaScript, **parameters** are the placeholders for passing input to a function.

```python
# text is a parameter
def print_banner(text):
    print("=======================")
    print(text)
    print("=======================")
```

## Arguments

Also like JavaScript, the values/expressions passed in to a function when calling it are known as **arguments**:

```python
# "hello, world" is an arugment
print_banner("hello, world")
```

However, unlike JavaScript, Python requires that the correct number of arguments be provided when calling a function. For example if you try to call print_banner without any arguments now:

```python
print_banner()

# generates the following error:
# TypeError: print_banner() missing 1 required positional arguments: 'text'
```

## Accepting a varying number of arguments

In JavaScript, we accomplished this using *rest parameters*:

```javascript
const sum = (...nums) => {
  total = 0;

  nums.forEach((num) => {
    total += num;
  });

  return total;
};


console.log(sum(1, 5, 10));
// prints: 16
```

### Python's `*` Parameter Specifier (`args`)

Using the `*` ("star") specifier in a parameter list allows us to pass in a varying number of **positional** arguments into a function:

```python
def sum(*args):
    print(type(args))
    # prints: <class 'tuple'>
    total = 0
    
    for arg in args:
        total += arg

    return total

print(sum(1, 5, 10))
# prints: 16
```

The identifier used with `*`, for example, `args` as we used above, can technically be anything. However the convention is to use `args`.

Always use the `*args` parameter **after** any **required** positional parameters. For example:

```python
def sum(greeting, *args):
    print(greeting)
    # prints: Hello, friend
    total = 0
    
    for arg in args:
        total += arg

    return total

print(sum("Hello, friend", 1, 5, 10))
```
