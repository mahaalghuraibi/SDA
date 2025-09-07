<h1>
  <span class="headline">Intro to JavaScript Classes</span>
  <span class="subhead">Extending Built-in Classes</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand how extend JavaScript's built-in classes

## Extending JavaScript's built-in classes

It's possible to use `extends` to subclass JavaScript's built-in classes.

For example, it would be nice to have a `last` property on arrays that returns the last element of the array:

```js
class MyArray extends Array {
  get last() {
    return this[this.length - 1];
  }
}
```

You then would need to instantiate the `MyArray` class to create the specialized array:

```js
const nums = new MyArray(1, 2, 3, 4, 5);
console.log(nums.last); //-> 5
```

All other array properties and methods are available due to inheritance!

Learn more about prototypal inheritance and the prototype chain [here in the docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain).
