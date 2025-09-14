# ![Python for JavaScript Developers - Control Flow - Ternary Expressions](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to create Ternary expressions in Python.

## Ternary expressions

In JavaScript, we used the ternary expression to return one of two values concisely, depending on the result of evaluating a conditional expression. For example:

```javascript
// With a ternary expression
let timeOfDay = 9
let morning = timeOfDay < 12 ? true : false;

// Without a ternary expression
let timeOfDay = 9
let morning;
if (timeOfDay < 12) {
  morning = true;
} else {
  morning = false;
}
```

Python does not have a dedicated ternary operator. Instead, Python uses a modified syntax of `if`/`else`, which results in a ternary expression instead of a control flow construct.

The Python ternary expression equivalent to the JavaScript example above is:

```python
time_of_day = 9
morning = True if time_of_day < 12 else False
print(morning)
# prints: True
```
