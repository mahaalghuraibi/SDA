<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Branching</span>
</h1>

**Learning objective:** By the end of this lesson, students will be proficient in using JavaScript's `if...else` statements for conditional logic in programming.

## Branching

Branching is a type of control flow that allows for different code paths to be executed based on specific conditions.

### `if`

***Single Path***

To execute a statement or statements conditionally, use the `if` statement. Conditional expressions must be surrounded by parenthesis.

The `if` statement checks a condition – it's like asking a yes-or-no question. If the answer is 'yes' (which in coding terms means the condition is `true`), then the code inside the `if` block will run. If the answer is 'no' (`false`), the code inside the block will be skipped.

```js
const val = 1;

// Ask: Is val exactly equal to 1?
if (val === 1) {
  console.log('This code runs because val is 1');
}
// Since val is 1, the answer is 'yes', so the code inside the if block runs.
```

### `if...else`

***Dual Paths***

When using an `if...else` statement, the code inside the `if` block will be executed if the condition evaluates to `true`. If the condition evaluates to `false`, then the code inside the `else` block will be executed. 

Think of `if...else` like a fork in the road. If the condition in the if part is true, take the first path. Otherwise, take the else path.

```js
const val = 2;

// If path
if (val === 1) {
  console.log('val is one');
// Else path
} else {
  console.log('val is not one');
  // Since val is not 1, the else path is taken, printing 'val is not one'.
}
```
Check out the **Ternary Operator** for another way to write short dual path branches.

### `if...else if...else`

***Three or more paths***

If you have three or more code paths, use `if` with as many `else if` statements as necessary and optionally a final `else`.

When you have several conditions to check, think of `if...else if...else` like multiple doors to choose from. Only one door can be entered, based on which condition is true.

```js
const val = 3;

if (val === 1) {
  console.log('val is one');
} else if (val === 2) {
  console.log('val is two');
} else if (val === 3) {
  console.log('val is three');
} else {
  console.log('not one, two, or three');
}

// val is 3, so 'val is three' will be printed.
```

## 🎓 You Do

First, declare and initialize a variable named `color`.

Then, write a branching statement that console.logs the following based upon the value of `color`: 

- If the value is `green`, log `'Go'`
- If the value is `yellow`, log `'Slow'`
- If the value is `red`, log `'Stop'`
- If the value is anything else, log `'Whatever'`

Manipulate the value of `color` to ensure you're able to log all of the above values.
