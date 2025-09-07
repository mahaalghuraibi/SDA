<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead">Expanding on <code>forEach()</code></span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to optimize the use of the forEach() method by implementing named functions, managing scope within the callback function, and understanding the limitations on terminating the loop.

## Using named functions with `forEach()`

Most of the time, you'll provide an anonymous callback function to the `forEach()` method. However, you can also provide a named function. This can be useful when carrying the same generic action on multiple arrays.

```js
const logElements = (element) => {
  console.log(element);
};

movies.forEach(logElements);
books.forEach(logElements);
```

## `forEach()` and function declarations

Here's an example of the syntax to use function declaration as an anonymous callback function:

```js
movies.forEach(function (movie) {
  console.log(movie);
});
```

## Working with data in a `forEach()` loop

Note that variables created in the callback function of a `forEach()` loop have function scope. If you want to retain any information between the different iterations, you must consider that scope. Here's an example:

```js
const numsToSum = [2, 4, 6]

numsToSum.forEach((num) => {
  let sum = 0;
  sum = sum + num;
  // sum will not be retained between iterations and will not 
  // be available outside of the callback function
});

console.log(sum);
// sum will be undefined
```

Do this instead:

```js
const numsToSum = [2, 4, 6];
let sum = 0 ;

numsToSum.forEach((num) => {
  sum = sum + num;
  // sum will not be retained between iterations and will not 
  // be available outside of the callback function
});

console.log(sum);
// sum will be 12
```

## Stopping the execution of a `forEach()` loop

Do not terminate `forEach()` loops early. Doing so would break the otherwise clear intentions of the `forEach()` method. If you need to do this, use another tool, such as the `for...of` loop, which you can break out of if necessary. See the `break and continue` Lesson for more.
