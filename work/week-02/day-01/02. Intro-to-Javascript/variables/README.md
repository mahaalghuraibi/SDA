<h1>
  <span class="headline">Intro to JavaScript</span>
  <span class="subhead">Variables</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand the basics of JavaScript variables, including naming conventions and the difference between `let` and `const`.

## Concepts

The purpose of a [*variable*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#declarations) in programming is to hold or reference data. 

> 📚 A *variable* is a named container used to store and retrieve data used within a program.

We use the `let` or `const` (short for constant) keyword to declare a variable in JavaScript. These are special keywords known as *declarations*. The variable name or *identifier* follows the declaration.

> 📚 A *declaration* is used to indicate a variable is being created. An *identifier* is then used to identify a variable.  

```js
let favSnack;
// let is the declaration
// favSnack is the identifier
```

We can also assign a value to a variable at the time we declare it by using the `=` (assignment) operator:

```js
let name = 'Tony Stark';
```

and change its value later:

```js
name = 'Pepper Potts';
// note that we only declare a variable once
```

## Naming rules

In JavaScript, when naming variables, the convention is to name the identifiers using lowerCamelCase. Good examples are `numActivePlayers`, `tacoFlavor`, or `name`.

Identifiers in JS:

- Are case-sensitive
- Cannot begin with a number
- Can contain letters, digits, underscores, and dollar signs
- Cannot contain spaces
- Cannot be [reserved words or keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)

> ❓ Is car-3 a valid variable identifier?

## `let` and `const`

The difference between `let` and `const` is that a `const` variable cannot be re-assigned to - you can assign data to it once, and that's it:

```js
let x = 25;
x = 100; // no problem
const z = 25;
z = 100; // Uncaught TypeError: Assignment to constant variable
```
