<h1>
  <span class="headline">Intro to JavaScript Arrays</span>
  <span class="subhead">Concepts</span>
</h1>

**Learning Objective:** By the end of this lesson, the learner will be able to explain the fundamental properties of arrays in JavaScript, including their dynamic size, versatility in holding various data types, and their role as an ordered collection for storing multiple values.

## What are arrays?

Think of arrays in JavaScript like a bookshelf full of books. Each book on the shelf is an element of the array. Books placed on it have an order - there is a first and last book, and every book between has a specific location on the shelf.

[Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) can contain zero or more items called *elements* (not to be confused with HTML elements). These elements are stored in a specific order. 

Each element in an array can hold any data type - strings, numbers, objects, functions, or even other arrays. This sets JavaScript apart from many other programming languages. However, just because you can doesn't necessarily mean that you should - as we work with arrays, we will typically want them to contain a single type of data.

In JavaScript, arrays can grow and shrink in size dynamically. You can add to them without being concerned about their capacity.

Although it's common to refer to an array as its own data type, they are technically a subtype of the `Object` type. This means arrays are technically objects in JavaScript.

> 📚 An *element* in an array is an individual item stored at a specific position within an array. 

## Why use arrays?

Arrays are typically the data structure of choice for holding an ordered list of data. Imagine you wanted to record the high temperature in your location every day for a year. Without arrays, you would need to create a separate variable for every new piece of data. Instead we can store all that temperature data in a single container because we have arrays.

Collecting that data in a single container has other benefits. Because all the high-temperature data you've collected is held in one place, it's easier to carry out operations on that data. For example, finding the average high temperature or even the hottest or coldest day of the year.

As demonstrated by the example above, the real-world problems you'll solve often involve collections of things. Arrays provide a natural way to model those collections in code.

> 📚 An *array* is a collection of elements stored in a specific order. Think of an array as a list or a container holding multiple values.
