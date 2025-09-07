<h1>
  <span class="headline">JavaScript Scope</span>
  <span class="subhead">Global Scope</span>
</h1>

**Learning Objective**: By the end of this lesson, students will be able to define what global scope means in JavaScript, list its specific features, and apply guidelines when using global variables to reduce programming errors.

## Global scope

Global scope in JavaScript refers to the outermost scope where variables and functions are accessible throughout the entire codebase. In other words, variables and functions declared in the **global scope** can be accessed and modified by any part of the code. This makes global variables powerful but also risky, as their values can be changed from any scope, potentially leading to unintended side effects or bugs.

Any variable declared outside a function or block will live in the global scope.

Taking our previous example and moving `mainDish` to the global scope allows it to be used anywhere.

```js
let mainDish;

const chooseDinner = () => {
  let isHungry = true;

  if (isHungry) {
    // We are able to modify the global mainDish variable
    mainDish = 'meatloaf';
  } else {
    mainDish = 'corn';
  }
  // Note how variables in the global scope can be modified anywhere!

  console.log(`Dinner tonight is ${mainDish}`);
  // Prints: 'Dinner tonight is Meatloaf'
}

chooseDinner();

// Because mainDish was declared in the global scope, it is available.
console.log(mainDish);
// Prints: 'meatloaf'
```

## Global scope as a metaphor

Scope is a tough concept, especially when you're new to coding. To help you further understand, here's an example to illustrate the idea of scope:

Imagine that you are in a library. The entire library is the **global scope**. You can access anything in the library from anywhere in the library.

Now imagine that you go to the children's section. The children's section is a **local scope**. You can access anything in the children's section from inside the children's section, but you cannot access anything outside of the children's section unless you go outside the children's section, thereby re-entering **global scope**.

For example, if you want to get a book from the non-fiction section, you have to leave the children's section and go to the non-fiction section.
