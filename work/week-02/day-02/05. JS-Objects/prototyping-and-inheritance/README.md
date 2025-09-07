<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Prototyping and Inheritance</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand the concept of prototyping and inheritance in JavaScript, enabling them to comprehend how built-in methods are accessible in different data types.

Thus far, we've made use of a wide range of string and array methods in our code. These are methods that are built into the [object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes) for each of these types. 

To understand how we're able to access these methods, it's important to understand that, in JavaScript, anything that is not a primitive value (string, number, bigint, boolean, undefined, symbol, or null) is an object. 

**Prototypes** are how JavaScript objects inherit features from one another. Every object in JavaScript has a built-in property called its prototype, and this prototype itself is an object so it has its own prototype as well (it's prototypes all the way down!)

This creates a chain of prototypes. Whenever you access a method on an object (for example, an array), the JavaScript engine searches up this chain to try and find the method. This allows a newly created array to make use of array methods like `.join()`. It is inheriting these methods from the `Array.prototype` object. 

```javascript
const myArray = [1, 2, 3, 4, 5]

myArray.join(' - ') // returns: 1 - 2 - 3 - 4 - 5
```

> 🧠 You may have noticed that methods on MDN always have a title syntax like 'Array.prototype.forEach', rather than the 'array.forEach()' syntax that we use to invoke these methods. As we've learned, the forEach method is actually a property of the prototype object on the top level Array object we are inheriting from. Since invoking a method on an array will automatically search for that method up the chain, we can omit the 'Array.prototype' whenever accessing an array method. 

<br>

So, what about the primitive values? We learned earlier that these are not objects, so why can we still call methods on strings, for instance?

Under the hood, the JavaScript engine converts any primitive value to the equivalent type object, which is why strings, despite not being objects, can inherit string methods like `.split()`, `length`, etc. JavaScript essentially treats a string like `'hello'` as a string object instance, which has its own prototypes and methods associated with it. 

Prototyping and inheritance are the mechanisms by which, almost like magic, we are able to access a number of pre-written methods to help us perform typical tasks with the various types of data we encounter in JavaScript!