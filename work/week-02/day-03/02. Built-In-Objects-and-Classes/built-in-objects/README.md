<h1>
  <span class="headline">JavaScript's Built in Objects and Classes</span>
  <span class="subhead">Built in Objects</span>
</h1>

**Learning objective:** By the end of this lesson, learners will be able to use and explain JavaScript's Math object, applying methods such as .random() and .floor(), and create functions for generating random integers.

## Built-In Objects

The [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math). object in JavaScript is very useful for different tasks that require mathematics. For example, when you need random numbers for things like making unique IDs or shuffling items in a list.

Math has many special functions. One important one is `.random()`. This function gives you a random number between 0 (including 0) and 1 (but not reaching 1):

```js
Math.random() // you might get a result like: 0.5570349614485068
```

Math also has functions that change numbers in specific ways. For example, `.floor()` makes a number smaller to the nearest whole number:

```js
let num = 1.21
Math.floor(num) // gives you 1
```
This method has a return value of the largest integer less than or equal to the value of `num`. In other words, it removes or *truncates* everything after the decimal.

When combined, you can see how the built-in Math object can dramatically shorten code and make life easier. Without having to code out either method, we can create a function that gets a random integer from a maximum value: 

```js
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
```

In addition to **methods**, the JavaScript Math object also contains certain values, such as PI:

```js
Math.PI // => 3.141592653589793
```

Now that we've taken a look at an example of a built-in Javascript object and refreshed ourselves on dot notation, let's take a look at a built-in class.
