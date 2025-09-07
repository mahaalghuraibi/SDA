<h1>
  <span class="headline">Intro to JavaScript</span>
  <span class="subhead">Weak vs Strong Typed Languages</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand the fundamental difference between weakly-typed and strongly-typed programming languages, with examples from JavaScript and Python.

*Weakly-typed* languages such as JavaScript allow implicit conversions between types, which can lead to interesting results. For example:

```js
const num = 7;
const sentence = `A week is ${num} days.`;
console.log(sentence);
// Prints: A week is 7 days.
```

From the above, we can see that JavaScript will happily automatically convert the number 7 into a string so that it can be concatenated with the rest of the sentence. That same code in a *strongly-typed* language would not function. For example, in Python:

```python
num = 7
sentence = "A week is " + num + " days."
# Error! A string and an int cannot be concatenated!
```

To make this valid code, the `num` must be explicitly converted into a string before it can be concatenated with the other strings surrounding it:

```python
num = 7
sentence = "A week is " + str(num) + " days." 
# This works!
print(sentence) 
# Prints: A week is 7 days.
```

> 🧠 There is a newer language called TypeScript you might hear about - this language is a superset of JavaScript and adds static and strong typing to JavaScript. Many developers agree that these type-safety features make code less error-prone and are worth the extra effort to code.

> 📚 In a *weakly-typed* language, conversions between unrelated data types occur implicitly. Conversions between unrelated data types must be explicitly made in a *strongly-typed* language.
