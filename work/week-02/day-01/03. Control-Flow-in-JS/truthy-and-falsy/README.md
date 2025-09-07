<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Truthy and Falsy</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand the concept of `truthy` and `falsy` values in JavaScript.

## Truthy and Falsy

JavaScript has the primitive `boolean` values of `true` and `false`, but it also has the idea of ***truthy*** and ***falsy***. So what are truthy and falsy, and why don't we use `true` and `false` for everything?

**Understanding Truthy and Falsy**

Truthy and falsy are conceptual and attempt to treat non-boolean expressions as booleans (`true` or `false`) during runtime. This concept is especially useful in conditions like `if` statements, where you might want to check if a variable exists or has a meaningful value without explicitly comparing it to `true` or `false`.

**What is Falsy?**

Most things in JavaScript are truthy, so it's easier to remember what is falsy.

These two data types are always falsy:
  
- `null`: Represents the intentional absence of any object value.
- `undefined`: Indicates that a variable has not been assigned a value.

These four values are also falsy: 

- `false`: The boolean value of false.
- `0` (zero): The number zero.
- `NaN` (Not a Number): Indicates a value that is not a valid number.
- `''` (An empty string): Strings are falsy when they are empty. Note, a string with a value of a space (`' '`) is not empty and therefore is truthy.

**What is Truthy?**

Everything else is truthy! This means most objects, including arrays and functions, non-zero numbers, and non-empty strings, are considered true in a boolean context.

**Practical Use**

The concept of truthiness and falsyness in JavaScript is not just a theoretical idea, but it has very practical applications in coding, particularly in making your code more concise and readable.

### Simplifying Conditions

Truthy and falsy values allow us to write conditions that directly check the value itself, rather than writing out a full comparison. This makes the code cleaner and often easier to understand at a glance. 

### Be Cautious

However, it's essential to be cautious when using this feature. Misunderstanding the truthiness or falsiness of a value can lead to bugs, especially if you're not fully aware of the potential values a variable can hold.

### Example in Code

Consider the following example:

```javascript
let string = "truthy value";

// Here, 'if (string)' is checking if 'string' is not an empty string, null, undefined, false, 0, or NaN.
if (string) {
  // This block of code will run because 'string' contains a non-falsy value.
}
```

The above syntax is preferable to the following equivalent statement: 

```javascript
if (string !== "") {
  // this is a more lengthy way of trying to make the same check without 
  // relying on the inherent nature of truthy/falsy values in JavaScript
}
```
