<h1>
  <span class="headline">Intro to JavaScript Classes</span>
  <span class="subhead">Static Methods</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand the role of static methods in JavaScript classes.

## Static methods

Static methods are typically used to implement behavior that does not pertain to a particular instance. These are callable on the class itself - not on its instances. For example, we could design the `Car` class so that it tracks every car it creates. We could then write static methods that return how many cars have been created, search for them by their make, and more.

Here’s how to define a basic static method:

```javascript
class Car {
  // the constructor will always be called
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
  static about() {
    console.log('I\'m the Car class!');
  }
};
```

> 💡 Notice the use of the `static` keyword that prefaces the method's name.

Next, let's call upon the static `about` method:

```javascript
Car.about(); // I'm the Car class! 
```

If we attempt to call `about` on the `mySubaru` instance, we should get an error:

```javascript
mySubaru.about(); // Uncaught TypeError: mySubaru.about is not a function
```