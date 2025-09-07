<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Truthy, Falsy, and Logical Operators</span>
</h1>

**Learning objective:** By the end of this lesson, students will gain a deep understanding of the power and versatility of logical operators `||` (OR) and `&&` (AND) in JavaScript, and how to use them effectively for conditional logic and default value assignments.

The logical operators `||` and `&&` are more powerful than meets the eye.

The logical `||` (OR) operator evaluates expressions and returns the first truthy operand it encounters. If all operands are falsy, it returns the last falsy operand:

```javascript
'hello' || 'goodbye' // evaluates to 'hello'
0 || null            // evaluates to null
```

In the first example, `'hello'` is truthy, so the result is `'hello'`. In the second example, both `0` and `null` are falsy, so it returns the last falsy operand, which is `null`.

The power of `||` lies in its ability to provide default values. For instance:

```JS
const username = getUsername() || 'Guest';

```

In this code, if `getUsername()` returns a truthy value (e.g., a username string), it will be assigned to `username`. However, if `getUsername()` returns a falsy value (e.g., null or undefined), the default value `'Guest'` will be assigned.



The logical `&&` (AND) operator evaluates expressions and returns the first falsy operand it encounters. If all operands are truthy, it returns the last truthy operand:

```javascript
'hello' && 'goodbye' // evaluates to 'goodbye'
0 && null            // evaluates to 0
```

In the first example, `'hello'` is truthy, so it moves on to the next operand and returns `'goodbye'`. In the second example, `0` is falsy, so it returns `0`.

The `&&` operator is often used for conditional execution. For example:


```JS
userIsLoggedIn && performLogout();
```

In this code, `performLogout()` will only be called if `userIsLoggedIn` is truthy, preventing unnecessary function calls.


Logical operators `||` and `&&` are not just for combining conditions, they also offer concise ways to handle default values and control flow based on truthiness and falsiness. Understanding how they work can significantly improve the clarity and efficiency of your JavaScript code!