<h1>
  <span class="headline">Intro to JavaScript</span>
  <span class="subhead">Template Literals</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to combine strings using template literals in JavaScript.

## Combining strings

We can use string interpolation with template literals to combine strings with one another .

Template literals are a special type of string written using the backtick character: `` ` ``. The key to type the backtick character is above the `Tab` key and to the left of the `1` key. The `greeting` string below is written as a template literal. 

```js
let username = 'friend';
let greeting = `Hello,`;
```

So what makes these so special? Template literals allow us to combine strings and place them anywhere we want in the template literal. Change the value that is assigned to `greeting`:

```js
let greeting = `Hello, ${username}.`;
```

As you can see above we use this special syntax `${}` inside of the template literal. Then, add a variable name inside of the `{}`. What happens when we log the greeting?

```js
console.log(greeting);
// Prints: Hello, friend.
```

Anything that resolves to a single value (an expression) can be used inside the `${}`.

As an additional note, template literals can span multiple lines. For example:

```js
let longString = `Hello, and welcome to the application!
Get started by logging in below!
We're happy to have you.`;
```

Attempting this with a normal string will cause an error.

## 🎓 You Do

Make use of template literals by sending a greeting to a friend!

Create two variables, `myName` and `friendName`. Assign both to different strings. Then, write a short message to your friend using a template literal that uses both variables inside of it.
