<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Property Shorthand Syntax</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to utilize ES6 Property Shorthand syntax to succinctly assign variables as object properties when the property names match the variable names.

It's a common scenario to want to pass the values of variables as properties in an object, especially when the property names match the variable names. Let's explore this with a simple and practical example.

Suppose we have details of a book, and we want to create an object that stores these details:

```javascript
const title = "To Kill a Mockingbird";
const author = "Harper Lee";
const yearPublished = 1960;

const book = {
  title: title,
  author: author,
  yearPublished: yearPublished
};

console.log(book);

// Output: 
// { 
//   title: "To Kill a Mockingbird", 
//   author: "Harper Lee", 
//   yearPublished: 1960 
// }
```
In this example, we are manually assigning each variable to a property in the book object, even though the property names are the same as the variable names.

Thanks to ES6's Property Shorthand syntax, we can simplify this by omitting the property names when they match the variable names:

```javascript
const title = "To Kill a Mockingbird";
const author = "Harper Lee";
const yearPublished = 1960;

const book = {
  title,
  author,
  yearPublished
};

console.log(book);

// Output: 
// { 
//   title: "To Kill a Mockingbird", 
//   author: "Harper Lee", 
//   yearPublished: 1960 
// }
```

If the property name is the same as the variable name, you can use the shorthand syntax. This means you can just write the variable name once, and JavaScript will understand that you want to create a property with that name and assign it the value of the variable.

Using ES6 Property Shorthand syntax makes your code more concise and easier to read. This can be especially helpful when creating objects with many properties.