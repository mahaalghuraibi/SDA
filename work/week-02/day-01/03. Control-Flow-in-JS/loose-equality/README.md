<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Loose Equality</span>
</h1>

**Learning objective:** Students will understand the concept of the loose equality operator (double equals) in JavaScript, its behavior regarding type conversion, and why it's generally recommended to use strict equality (triple equals) instead.

The loose equality operator (commonly called 'double equals') will perform a type conversion (if needed) when it compares its left and right operands: 

```js
3 == '3'  // true
```

In the above example, JavaScript will [coerce](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion) the string `'3'` into the number `3`. Then, JavaScript will perform a strict equality check now that the types are the same:

```js
3 === 3
```

`3` is strictly equal to `3`, so this returns `true`.

Typically, it is best to avoid using the double equals operator - we will rarely be in a position where the type of our data is irrelevant or interchangeable. Use strict equality/triple equals as best practice!
