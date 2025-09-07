<h1>
  <span class="headline">JavaScript's Built in Objects and Classes</span>
  <span class="subhead">Built in Classes</span>
</h1>

**Learning objective:** By the end of this lesson, learners will be able to differentiate between built-in `objects` and `classes` in JavaScript, specifically demonstrating the ability to use the `Date` class to create and manipulate date objects.

## Built-In Classes

The JavaScript `Math` object contains a lot of useful methods and values that we can reference. We don't characterize the `Math` object as a class though, because we cannot use it to *instantiate* or create new objects. This makes sense because we don't need new math *objects* to use its helpful properties. We have all the functionality we need baked into `Math`. We can just use this object directly.

```js
let randomNumber = Math.random()
```

In this example, what we want is a random number, not an object. So when would we need to instantiate new objects? 

> 📚 To *instantiate* means to create a new instance of an object from a class. It's like using a recipe (class) to bake a cake (object).

### The `Date` class

Let's take a look at one of JavaScript's [built-in classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects) now.

A great example of a common built-in class, is the JS [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) class. There are many reasons for creating different instances of `Date` objects (*for example, birthdays, anniversaries, dates and times for timecards, dates for to do lists, calendar events, etc.*).

What sets the `Date` *class* apart from the `Math` *object*, is that unlike `Math.random()` which returns a `number`, utilizing the `Date` class returns a new date `object` - complete with its own methods and properties.

Let's utilize JavaScript's `Date` class to instantiate a new date object using a string:

```js
const birthday = new Date("2023-05-31");
```

Our new date *object* is stored in the variable, `birthday`. And because it is an object created by the `Date` class, it will have its own set of methods and properties *inherited* from its parent. 

> 📚 Inheritance is when an object gets properties and methods passed down from its class.

These properties are also known as ***instance methods***. Let's take our new `birthday` object for a test drive.

### Instance methods

The JavaScript `Date` class provides a variety of instance methods that are extremely useful for handling and manipulating dates.

For reference:

```js
const birthday = new Date("2023-05-31");
```

[getFullYear()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear) - Returns the year of the specified date according to local time.

```js
let year = birthday.getFullYear();
console.log(year) // 2023
```

[getDate()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate) - Returns the day of the month (1-31) for the specified date.

```js
let day = birthday.getDate();
console.log(day)  // 31
```

[getTime()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime) - Returns the numeric value corresponding to the time for the specified date according to universal time.


```js
let time = birthday.getTime();
console.log(time); // 1685491200000
```

> Why the strange number? The `getTime()` method returns the number of milliseconds for this date since the *epoch*, which is defined as the midnight at the beginning of January 1, 1970, UTC. This format, though a bit confusing, is used frequently in code because of how exact it is. 

All of these helpful instance methods (and more) are attached to our new date object right out of the box. 


### Static (class) methods

There are also methods we can call on the `Date` class itself and these are called ***static methods***.

Above, we created a `Date` object using a specific date entered as a parameter. Let's say we instead wanted to create a `Date` object that reflects ***"right now"***, like when someone clicks the `submit` button on a form. To capture that exact submission time, we can use the `Date` class's [`.now()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now) method.

This method is called on the `Date` class directly: 

```js
let now = Date.now() 
console.log(now) // 1703121829554
```

Now, because the values of `birthday.getTime()` and `Date.now()` are numbers of the same format, we can actually compare them to see if one date may precede the other.

```js
if (birthday.getTime() < Date.now()) {
    console.log("Happy belated birthday!")
}
```
