<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead">Manipulation</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to update existing array elements and utilize methods like `push()` and `pop()` to add or remove elements at the start or end of an array.

## Updating existing elements in an array

Just like we access elements in an array using square bracket notation, we can also use this same syntax to update an element in a specific position:

```js
// recall that movies is ['Barbie', 'Interstellar', 'Get Out']

// let's update the 2nd movie (index of 1)
movies[1] = 'Arrival';
// movies is now ['Barbie', 'Arrival', 'Get Out']
```

Wait though, wasn't `movies` defined using `const`? How are we able to modify its contents? 

When we made `movies`, we told JavaScript not to let us change what `movies` points at (a specific array). It is not, however, saying that the contents of that array cannot be *mutated* (altered). In short, if we try doing something like the examples below, we'll get a `TypeError`:

```js
// attempting to change the movies constant to a string
movies = 'Barbie and Arrival';
// attempting to change the movies constant to a different array (even if the contents of that array are identical)
movies = ['Barbie', 'Arrival', 'Get Out'];
```

But when we change the contents of the existing array, everything checks out fine!

> 📚 *Mutation* is the modification of the content of a data structure or variable. This contrasts with *immutability*, where data cannot be changed once created.

## Adding or removing elements at the start or end of an array

Don't worry; we'll eventually get to adding (and removing) elements anywhere in an array!

### `push()`

We can add one or more elements to the **end** of an array using the [`push()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push) method:

```js
movies.push('Parasite', 'Dune');
// movies is ['Barbie', 'Arrival', 'Get Out', 'Parasite', 'Dune']
```

Imagine a stack of books on a table. The `push()` method is like adding a book or books to the top of the stack. 

### `pop()`

We can remove a single element from the **end** of an array using the [`pop()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop) method:

```js
movies.pop();
// movies is ['Barbie', 'Arrival', 'Get Out', 'Parasite"]
```

`pop()` doesn’t take any arguments and returns the element that was removed from the array:

```js
const removedMovie = movies.pop();
// movies is ['Barbie', 'Arrival', 'Get Out']
// removedMovie is 'Parasite'
```

`pop()` is like removing a single book from the top of the stack of books. It also allows us to do something with the book we removed if we want.

### You Do

Add a movie of your choice to the end of the array!

Can't think of a movie? If you need a suggestion, I'll be adding **Coco**.
