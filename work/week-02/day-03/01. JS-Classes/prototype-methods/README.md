<h1>
  <span class="headline">Intro to JavaScript Classes</span>
  <span class="subhead">Prototype Methods</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able utilize prototype methods in JavaScript classes.

## Class methods

Two types of methods can be added to a class - [Prototype methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#methods) and [Static methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#static_methods_and_fields).

1. **Prototype methods** are available on an instance of the class (object) - this is why they are called `instance methods` in other OOP languages. `forEach` is an example of a prototype method on an array:

```javascript
const nums = [1, 2, 3, 4, 5];
nums.forEach(num => console.log(num));
```

2. **Static methods** are called on the class itself and are not available on instances. These are typically used to implement behavior that doesn't pertain to a specific instance.

[Array.isArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) is an example of a static method on `Array`:

```js
const nums = [1, 2, 3, 4, 5];
console.log(Array.isArray(nums)); // true
```

## Defining prototype methods in a class

Let's add a prototype method called `start` to our `Car` class:

```javascript
class Car {
  // The constructor will always be called
  constructor(make, model, color) {
    this.make = make;
    this.model = model;
    this.color = color;
    this.isRunning = false;
  }
  start() {
    this.isRunning = true;
    console.log('Running!');
  }
};
```

> 🧠 Class methods are not separated by a comma or any other character.

Notice the usage of the `this` keyword in our `start` method. It is being used outside of the constructor in this scenario.

In our `start` method, the `this` keyword refers to the current object instance. When defining methods in a class, we don't know the names of the future instances. Because we don't know the name of the object being created ahead of time, we cannot specify its name within the `start` method. Even if we knew the object's name, it wouldn't be very useful because our `start` method would only work with that single object! `this` allows the method to function correctly in the context of a specific object instance.

If we define an object directly, we can reference the object by its name within its methods:

```javascript
const myFirstCar = {
  make: 'Toyota',
  model: 'Corolla',
  color: 'black',
  isRunning: false,
  start: function() {
    // Referencing the object by its name:
    myFirstCar.isRunning = true;
    console.log('Running!');
  },
};
```

Here, we use `myFirstCar.isRunning` because we're certain of the object's name. However, in class based instances, the object's name isn't predetermined, so we use `this` to dynamically reference whichever instance is calling the method. `this` will always point to the current object.

## 🎓 You Do

### Add another instance method.

1. Define a `stop` method in the `Car` class.

2. The `stop` method should set the `isRunning` property to `false` and log `"Stopped!"` to the console.


### Define another class.

1. Pick something like our car example above that would make sense to instantiate. You can pick anything you'd like, but we'll use `Airplane` as an example. Remember that the class name should be uppercase and singular.
2. Code the class' `constructor` method so that it creates at least two properties.
3. Add at least two methods to the class. At least one of the methods you write should interact with one or multiple of the properties you created above. As you write your methods you might think of more properties you could add to the constructor - if you do, add them!
4. Create a couple of new instances of the class you've built.