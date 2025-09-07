<h1>
  <span class="headline">Intro to JavaScript Classes</span>
  <span class="subhead">Constructor Functions</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand how to use constructor functions in place of the `class` keyword.

## What are constructor functions?

Before classes arrived via ES2015, **constructor functions** were used in place of classes. They accomplished the same task with a now outdated syntax.

Code written today will most likely use the `class` keyword, but you may encounter older code using constructor functions.
 
Let's look at how the `Car` class can be written as a constructor function:

```js
function Car(make, model, color) {
  this.make = make;
  this.model = model;
  this.color = color;
  this.isRunning = false;  // default to false
};

Car.prototype.start = function() {
  this.isRunning = true;
  console.log('Running!');
};

// other prototype (instance) methods defined like above would go here
	
// Instantiation is identical
const car = new Car('Toyota', 'Camry', 'Green')
```

Static methods would be created directly on the constructor function:

```js
Car.about = function() {
  console.log('I\'m the Car class!');
};
```