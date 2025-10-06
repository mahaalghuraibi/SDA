# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Exception Handling Lab

| Title                         | Type   | Duration | Author               |
|-------------------------------|--------|----------|-----------------------
| Python Exception Handling     | Lab    | 2:00     | Suresh Melvin Sigera |

You are getting ready to write an interactive Python calculator in this lab.

We assume that the user input will be a formula consisting of a number, a logical operator (at least `+` and `-`), and
another number, separated by whitespace (e.g. `1 + 1`). As a first step, split the user input using `str.split()`, and
make sure that the resulting list is valid by checking:

- Raising a `FormulaError`, which is a **custom exception**, if there aren't three elements in the input.
- To convert the **first** and **third** inputs to floats, use `float_value = float(str_value)`. In the case of
  a `ValueError`
  occurring, instead of raising a `ValueError`, raise a `FormulaError` instead.
- If the second input is not `+` or `-`, again raise a `FormulaError`.

If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input,
and so on, until the **user enters quit**.

An interaction could look like this:

```text
>>> 
1 + 1
2.0
>>> 
2 + 1
3.0
>>> 
0 + 0
0.0
>>> 
quit
```

## How to submit homework

- Step 1. Complete your work in a file called `calculator.py`
- Step 2. Add, Commit, Push.
