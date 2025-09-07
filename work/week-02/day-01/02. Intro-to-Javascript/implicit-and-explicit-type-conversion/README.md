<h1>
  <span class="headline">Intro to JavaScript</span>
  <span class="subhead">Implicit and Explicit Type Conversion</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand the concepts of implicit and explicit type conversion in JavaScript, when and why they occur, and how to perform explicit type conversion when needed.

## Type Conversion

JavaScript is very relaxed when it comes to data types. Contrary to non-dynamic languages, a variable can change its type.

```js
let num = 15; // I'm a number
num = 'Hey!'; // Now I'm a string!
```

## Beware of implicit conversion

**Implicit type conversion** is the process of automatically converting one data type to another. JavaScript performs implicit type conversion in various situations, such as when you perform arithmetic operations on values of different types.

JavaScript is friendly and tries to help us whenever it can. However, sometimes this help can backfire if we lack knowledge of these behaviors.

**Try adding a string to a number. What did JS do?**

Now try comparing a number and a string containing the same digits using the equality (`==`) comparison operator:

```js
13 == '13';
// true!
```

This is why we use the strict equality operator (`===`). It will not perform type conversion.

```js
13 === '13';
// false!
```

## Explicit type conversion

**Explicit type conversion** is the process of manually converting one data type to another. You can use the following methods to perform explicit type conversion:

To convert into strings: 

- using the `toString()` method

  ```js
  let numOne = 123.456;
  let strOne = numOne.toString(); // "123.456"
  ```

- using the `String()` method

  ```js
  let numTwo = 123.456;
  let strTwo = String(numTwo); // "123.456"
  ```

- using the `toFixed()` method

  ```js
  let numThree = 123.456;
  let strThree = numThree.toFixed(2); // "123.46"
  ```

  Note that we must specify the number of decimals we want inside the `()`'s.

To convert into numbers:

- using the `parseInt()` method 

  ```js
  let strFour = '1234.567';
  let numFour = parseInt(strFour); // 1234
  ```
  `parseInt()` rounds down to the nearest whole number. 

- using the `parseFloat()` method

  ```js
  let strFive = '1234.567';
  let numFive = parseFloat(strFive); // 1234.567
  ```

- using the `Number()` method

  ```js
  let strSix = '1234.567';
  let numSix = Number(strSix); // 1234.567
  ```

## When to use implicit and explicit type conversion

Implicit type conversion can be convenient but can lead to unexpected results. It's important to be aware of the situations in which JavaScript will perform implicit type conversion.

In general, it's best to use explicit type conversion when we need to be sure that a value is of a certain type. For example, if we're writing a function that expects a number value as a parameter, we should use the `Number()` function to convert the value to a number before using it in the function.
