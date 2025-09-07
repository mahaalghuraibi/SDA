<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Getters and Setters</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to implement and use getters and setters in JavaScript objects, understanding their role in data access and modification within object properties.


In JavaScript, `getters` and `setters` are special functions that provide a way to get and set the values of an object's properties. They offer more control over how properties are accessed and modified.

Simply put: 
[`getter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get) and [`setter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set) properties allow you to treat methods like regular properties that you can access without invoking and set using the assignment operator (=).

## Getters
- A getter is used to access the value of an object's property.
- It's defined using the get keyword.
- A getter does not take any arguments and is ***used like a property, not a function call***.


```JS
const person = {
  firstName: 'John',
  lastName: 'Doe',
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
};

// used like a property, not a function call
console.log(person.fullName); // 'John Doe'

```

## Setters
- A setter is used to set the value of an object's property.
- It's defined using the set keyword.
- A setter ***takes a single argument and is used to assign a value***.

```JS
const person = {
  firstName: 'John',
  lastName: 'Doe',
  set fullName(value) {
    [this.firstName, this.lastName] = value.split(' ');
  }
};

// takes a single argument and is used to assign a value
person.fullName = 'Jane Smith';
console.log(person.firstName); // 'Jane'
console.log(person.lastName); // 'Smith'
```