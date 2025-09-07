<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Iterating Through Properties</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to iterate through the properties of JavaScript objects using for...in loops and ES2017 methods (Object.keys, Object.values, Object.entries).

Let' imagine we have an object with details about a student:

```js
const student = {
  name: 'Ashley',
  email: 'student@email.com',
  enrolled: true,
}
```

Sometimes we need to iterate over an object’s properties. We can iterate over the keys of the properties using a `for...in` loop:

```javascript
for (let key in student) {
  console.log(`The value of the ${key} property is ${student[key]}`)
}

// Output
// The value of the name property is 'Ashley'
// The value of the email property is 'student@email.com'
// The value of the enrolled property is true
```

Note that `for...in` loops include all properties in the *prototype chain* (inherited properties) - not just its own properties that live on the object itself. We’ll learn how objects can inherit properties soon.

There’s a couple of nifty ES2017 methods that can be used to iterate over an object’s **own** keys or values:

- [`Object.keys(obj)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
- [`Object.values(obj)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Object/values)
- [`Object.entries(obj)`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)

Each of those methods mentioned returns an array that we can iterate over, for example:

```javascript
Object.values(student).forEach(function(val) {
  console.log(val)
})

// Output
// 'Ashley'
// 'student@email.com'
// true
```

> 🧠 The ECMAScript specification does not dictate how properties should be ordered; however, all browsers currently iterate over them in the order they are defined/added. This means that unlike arrays, the order of properties in objects is not guaranteed. 