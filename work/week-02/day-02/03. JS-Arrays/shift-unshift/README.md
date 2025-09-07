<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead"><code>shift()</code> and <code>unshift()</code></span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to add and remove elements at the beginning of an array using the unshift() and shift() methods.

### `unshift()`

Just like `push()`, [`unshift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift) allows us to add one or multiple items to an array, this time at the start of the array.

```js
movies.unshift('Dune', 'John Wick');
// movies is ['Dune', 'John Wick', 'Barbie', 'Arrival', 'Get Out', 'Coco']
```

Here, we've added two items to the array by passing multiple arguments to the method.


### `shift()`

We can also remove from the **front** of an array with [`shift()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift):

```js
movies.shift();
// movies is ['John Wick', 'Barbie', 'Arrival', 'Get Out', 'Coco']
```

`shift()` removes only one element at a time and don’t take any arguments. These methods both return the element that was removed from the array:

```js
const removedMovie = movies.shift();
// movies is ['Barbie', 'Arrival', 'Get Out', 'Coco']
// removedMovie is 'John Wick'
```

### Remembering the `push()`, `pop()`, `unshift()`, and `shift()` methods.

Here's a way to help you remember the functions of all of these methods:

The methods with longer names ***add*** to an array.
`unshift() -> [...] <- push()`

The methods with shorter names ***remove*** elements from an array.
`shift() <- [...] -> pop()`

Don't get too caught up in remembering things like this though; MDN, Google, and AI assistants are there to help you remember the things you might get turned around on or forget.
