<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead"><code>do...while</code></span>
</h1>

**Learning objective:** Students will understand the concept of `do...while` loops in JavaScript, how they differ from `while` loops, and when to use them for iterative tasks.

`do`...`while` loops are very similar to `while` loops, except they force the code block to execute at least once, regardless of the condition being truthy or falsy. 

```javascript
let num = 120;

do {
  console.log(`${num} is even`);
  num += 2;
} while (num <= 10);
```

The code inside the `do...while` loop will execute once, even though `120` is not less than or equal to `10`.
