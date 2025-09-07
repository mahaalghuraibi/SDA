<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead"><code>break</code> and <code>continue</code></span>
</h1>

**Learning objective:** By the end of this lesson, the learner will be able to implement the `break` and `continue` statements in JavaScript to control the flow of loops based on specific conditions.

## `break`

The `break` statement lets you exit a loop early, dependent upon a condition.

```js
// assuming `movies` is ['Barbie', 'Arrival', 'Get Out', 'Coco']
for (let movie of movies) {
  if (movie === 'Get Out') break;
  console.log(movie);
}
```
This results in the following output: 

```text
Barbie
Arrival
```

Thanks to the [break](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break) statement, the loop exits early when it encounters `'Get Out'`. The `for...of` statement provides extra control when iterating, like this ability to exit early easily.

## `continue`

The `continue` statement is very similar to the `break` statement, only it doesn't stop execution of the loop entirely, and instead only ends the ***current iteration*** of the loop. Let's add a `continue` to the code above. 

```js
for (let movie of movies) {
  console.log("Another iteration");
  if (movie === 'Barbie') continue;
  if (movie === 'Get Out') break;
  console.log(movie);
}
```

Here's the output:

```text
Another iteration
Another iteration
Arrival
Another iteration
```

Here we can see that the movie `'Barbie'` is never printed to the console, but the loop picks back up from the start of the next iteration.
