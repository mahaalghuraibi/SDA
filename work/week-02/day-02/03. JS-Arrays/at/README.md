<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead"><code>at()</code></span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to utilize the at() method to access array elements using both positive and negative indexes for more efficient code.

## The `at()` method

Unlike other programming languages, JavaScript does not support negative indexing using square bracket. Attempting to access an array element with a negative index will result in a value of `undefined`.

```js
movies[-1];  // undefined
```

In ES2022, the [`at()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at) method was added to the JavaScript spec. The `at()` method can directly access elements by their index. It's not that different from square bracket notation at first glance, except it does accept negative indexes! This can be used to access the last item in an array easily:

```js
// movies is ['Barbie', 'Arrival', 'Get Out', 'Coco']
const lastMovieAt = movies.at(-1);  
// lastMovieAt is 'Coco'
```

The `at()` method improves code readability, especially when executing complex array manipulations.
