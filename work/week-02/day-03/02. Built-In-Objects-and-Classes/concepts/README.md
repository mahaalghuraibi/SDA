<h1>
  <span class="headline">JavaScript's Built in Objects and Classes</span>
  <span class="subhead">Concepts</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to understand how built-in classes and objects differ in JavaScript.

## Built-in classes and objects

When it comes to built-in classes and objects in JavaScript, the practical differences between the two can be a bit confusing.

### Classes

In JavaScript, *classes* function as a blueprint to generate or "construct" objects. It defines the properties and methods that the objects created from this class will have. For instance, if you have a `Car` class, it might define properties like `color` and `make`, and methods like `drive()` or `brake()`.

### Objects

When you create a new *object* from a class, you are essentially using that class's blueprint to build the object. Each object created from the class will have the properties and methods defined in the class. For example, if you create a new object from the `Car` class, that new car will have its own `color`, `make`, and the ability to perform actions like `drive()`.

### Prototypes

In JavaScript, objects have something called a *prototype*. A prototype is an object from which other objects inherit properties and methods. This is a core part of JavaScript's prototype-based inheritance system. For instance, when you create an `array` in JavaScript, it inherits properties like `length` and methods like `.join()` from the `Array` prototype. 

This is why, for example, a new array that you just created has access to a `length` property, or can use the `.join()` method:

```js
const anArray = [1,2,3,4,5];
console.log(anArray.length); // 5
console.log(anArray.join(‘’)); // 12345
```
All arrays will inherit properties from the `Array` object, which has a number of built-in properties and methods that make working with arrays easier.

### Classes and objects are similar but not the same

Simply put, in JavaScript, whether working with built-in *classes* or built-in *objects*, the end result is similar. The object or class is globally available to reference, and the resulting object will have predefined properties and methods associated with it. 

JavaScript has a number of built-in objects. Some work purely as objects while others allow for a class-like constructor syntax as well.

This module is not designed to be an exhaustive lesson on all of them, or to dive too deeply into *how* exactly they are available to us. Rather, the intention is to explore some of the common globally available classes and objects, and empower you to start using them in your own code.

