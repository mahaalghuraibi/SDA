<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead"><code>join()</code></span>
</h1>

## `join()` example

The array [`join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join) method combines all of the string elements in an array and returns a single string:

```js
// as a reminder, movies is ['Barbie', 'Arrival', 'Get Out', 'Coco']
let movieString = movies.join();
// movieString is 'Barbie,Arrival,Get Out,Coco'
```
	
As you can see, by default, the movie strings were separated by a comma. However, we can pass `join()` whatever string we want to use as the separator:

```js
movieString = movies.join(' -- ');
// movieString is 'Barbie -- Arrival -- Get Out -- Coco'
```
