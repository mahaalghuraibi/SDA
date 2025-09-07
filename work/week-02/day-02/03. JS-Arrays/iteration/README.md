<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead">Iteration</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to use both `for` and `for...of` loops to iterate through arrays and manipulate each element.

> 📚 *Iteration* is the process of repeatedly executing a set of instructions or looping through a collection of items (like an array or string) one by one until a specific condition is met or until no more items are left to process.

## Using a `for` loop

A standard `for` loop can iterate through an array. Initialize the loop with `idx` set to `0` - the index of the first element. End iteration at the index of the last element:

```js
// as a reminder, movies is ['Barbie', 'Arrival', 'Get Out', 'Coco']

for (let idx = 0; idx < movies.length; idx++) {
  console.log(movies[idx]);
}
```

Inside the loop, `idx` serves as the index to retrieve elements from the `movies` array. It increments by 1 after the code inside of the `{ }` has been executed until the condition statement (`idx < movies.length`) is no longer true.

We use the `length` property of `movies` to ensure that this loop is dynamic to the size of the array - as elements are added or removed, this same loop will still function.

For our `['Barbie', 'Arrival', 'Get Out', 'Coco']` array, this will result in the following output:

```text
Barbie
Arrival
Get Out
Coco
```

This loop doesn't do much, but we could do anything we want to inside the `for` loop. Let's number each item.

```js
for (let idx = 0; idx < movies.length; idx++) {
  console.log(`${idx + 1}. ${movies[idx]}`);
}
```

For the same array, this will be the result:

```text
1. Barbie
2. Arrival
3. Get Out
4. Coco
```

## Using a `for...of` loop

The traditional `for` statement can be used to iterate over an array in an *imperative* way - meaning we provide each step the computer should take to carry out an action. The [`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) statement is a *declarative* approach that provides a more concise way to iterate over arrays (and other iterable structures like strings):

```js
for (let movie of movies) {
  console.log(movie);
}
```

And here's the result:

```text
Barbie
Arrival
Get Out
Coco
```

> 📚 When using *imperative* programming, you instruct the computer how to achieve a specific outcome step by step. When using *declarative* programming, you tell the computer the desired outcome, omitting the finer details. A mnemonic may be helpful to remember this:
> - ***I***mperative programming requires ***i***nstructions to carry out a task.
> - ***D***eclarative programming is a ***d***ecree unconcerned with how the result happens, just that it does.

A `for...of` loop has couple of extra unique features in addition to this more declarative approach.

> ⚠️ JavaScript also provides a `for...in` loop. It's designed mainly for iterating over an object's properties rather than array items. Be sure you're using the correct loop for your needs.
