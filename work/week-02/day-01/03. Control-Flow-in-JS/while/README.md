<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead"><code>while</code></span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to implement and differentiate between `for` and `while` loops, understanding the appropriate use of each, particularly when the number of iterations is unknown.

## while

The `while` loop is the go-to when the number of iterations is unknown.

Unlike a `for` loop, `while` loops only specify the `condition`: 

```javascript
while (/* condition */) {
  // statement block
}
```

We can refactor our previous `for` loop example to a `while` loop: 

```javascript
let number = 1;

while (number <= 10) {
  console.log(number);
  number++;
}
```

Where `x <= 10` is the `condition`. 

You'll notice that a `for` loop and a `while` loop work similarly, but where a `for` loop specifies all of the loop parameters up front, a `while` loop allows for more freedom in composition. This is perhaps why `while` loops are especially susceptible to causing infinite loops. 

For instance, it would be easy to forget to increment `number`: 
```javascript
let number = 1;

while (number <= 10) {
  console.log(number);
}
```

As written, `number` will never be larger than or equal to 10, so this `while` loop will run forever, endlessly logging the number 1 until the end of time (or, more likely, until your browser crashes). 

> 🧠 An infinite loop (or endless loop) is a sequence of code that will continue endlessly.
