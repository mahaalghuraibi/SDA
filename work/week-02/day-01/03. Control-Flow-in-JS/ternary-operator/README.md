<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Ternary Operator</span>
</h1>


**Learning objective:** Students will learn how to use the ternary operator in JavaScript to perform conditional actions and return values based on conditions.

The [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) is useful when you need to carry out one of two actions depending on a condition. Take this `if...else` branch as an example:

```js
const num = 100;

if (num > 5) {
  console.log('num is larger than 5');
} else {
  console.log('num is 5 or less');
}
```

We can use a ternary to accomplish this same task:

```js
num > 5 ? console.log('num is larger than 5') : console.log('num is 5 or less');
```

Note some syntax going on here: 

- `num > 5` is our condition.
- The condition is followed by a `?`.
- An expression to execute if the condition is true or truthy.
- A colon `:`.
- An expression to execute if the condition is false or falsy.

Note that we can only place expressions (code that evaluates to a single output) inside the ternary.

The ternary operator gets even better when you need to return one of two values depending upon a condition:

```javascript
let message = num > 5 ? 'num is larger than 5' : 'num is 5 or less';

console.log(message);
```

The above one line of code replaces this code:

```javascript
let message;

if (num > 5) {
  message = 'num is larger than 5';
} else {
  message = 'num is 5 or less';
}

console.log(message)
```
