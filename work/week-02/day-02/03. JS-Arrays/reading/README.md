<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead">Reading</span>
</h1>

**Learning objective:** By the end of this lesson, the learner will be able to accurately retrieve elements from an array using both an index and the length property.

## Accessing elements at any position in an array

Array elements are accessed using square bracket notation along with the element's __index__ (position) within the array.

```js
const movies = ['Barbie', 'Interstellar', 'Get Out'];

const firstMovie = movies[0];
// firstMovie is 'Barbie'
```

Note that indexes are integers where `0` is used to access the first element. Each consecutive element has its index incremented by one.

> 📚 An *index* is a numerical value that represents the position of an element within an array.

> 🧠 Remember that array indexes start from 0 for the first element. This "zero-based" indexing convention is used in programming to align with memory offset principles.

## The `length` property

The [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length) property on an array can be used to quickly see how many elements an array contains. For example:

```js
console.log(movies.length);
// `3` is logged to the console
```

Given the code above, the number 3 is printed to the console because the `movies` array contains 3 elements.

### Using `length` to access the last element of an array

To access the last element of an array, you can utilize the `length` property.

```js
const lastMovie = movies[movies.length - 1];
// lastMovie is 'Get Out'
```

This works because the code `movies.length - 1` will resolve to the number 2, and the item held in the 2 index of the `movies` array is `'Get Out'`.

> ❓ Assuming the below code, what will the value of the variable `color` be?
>
> ```js
> const colors = ['red', 'green', 'blue'];
> let color = colors[1];
> ```
