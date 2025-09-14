# ![Python Functions - kwargs](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to distinguish between args and kwargs and better know when to use them.

## Keyword arguments - kwargs

`kwargs` stands for ***keyword arguments***. This is a different style of passing arguments that isn't possible in JavaScript.

These are arguments that have a name. You can provide as many as you like to a function when you call it.

As we've seen, we can pass positional arguments to a function:

```python
def make_employee(role):
    print(role)
    # prints: CEO

    employee = {"role": role}
    return employee

print(make_employee("CEO"))
# prints: { 'role': 'CEO' }
```

But we can pass keyword arguments to a function as well:

```python
def make_employee(role):
    print(role)
    # prints: CEO

    employee = {"role": role}
    return employee

print(make_employee(role="CEO"))
# prints: { 'role': 'CEO' }
```

Because `role` is the parameter's name, we can assign `"CEO"` to `role` when we pass it into the `make_employee` function. That value will be matched to the `role` parameter because it has the same name.

This can make passing arguments to a function more readable, and is a common practice in many Python frameworks.

## Python's `**` parameter specifier (`**kwargs`)

If you'd like to access a varying number of keyword arguments, use `**kwargs` at the ***end of the parameter list***. This is similar to how we passed an arbitrary number of positional arguments with `*args`.

Just like with `args`, `kwargs` could technically be anything but is named `kwargs` by convention - what matters is the `**`.

Let's define and call a function that uses `**kwargs`:

```python
def make_employee(role, **kwargs):
    print(kwargs)
    # prints: {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
    print(type(kwargs))
    # prints: <class 'dict'>
    # kwargs is a dictionary - you can use it anywhere you'd use one:
    employee = {"role": role, "name": kwargs}
    return employee

print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }
```

`kwargs` arguments are not positional! You can provide them in any order, but they must come after any positional arguments.

As you can see above, in a function, kwargs can be accessed by its name - `kwargs`. `kwargs` is a dictionary, meaning you can treat it as such. For example, you could iterate through it using the `values()` method:

```python
def make_employee(role, **kwargs):
    username = ""
    for name in kwargs.values():
        username += name

    employee = {"role": role, "username": username}
    return employee

print(make_employee("CEO", first="Sam", middle="Harris", last="Altman"))
```

## Combining `kwargs` and keyword arguments

We can combine these ideas in the same function:

```python
print(make_employee(role="CEO", first="Sam", middle="Harris", last="Altman"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }
```

We can even provide the `role` out of order if we want:

```python
print(make_employee(first="Sam", middle="Harris", last="Altman", role="CEO"))
# prints: {
#     'role': 'CEO',
#     'name': {'first': 'Sam', 'middle': 'Harris', 'last': 'Altman'}
# }
```

Note when we do this, `role` is not added to the `kwargs` dictionary - it is matched directly with its positional parameter.

### Combining argument types

Required positional, optional positional (`*args`), and keyword (`**kwargs`) arguments can all be used simultaneously.

But note that order is important! Check out this example:

```python
def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args:')
    for arg in args:
        print(' ', arg)
    print('**kwargs:')
    for keyword, value in kwargs.items():
        print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')
```

Which results in this output:

```plaintext
Positional params: A, B
*args:
  1
  2
  3
**kwargs:
  color: purple
  shape: circle
```
