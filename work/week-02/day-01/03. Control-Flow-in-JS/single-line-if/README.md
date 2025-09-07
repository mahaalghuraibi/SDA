<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Single Line <code>if</code></span>
</h1>

**Learning objective:** Understand and effectively use single-line `if` statements in JavaScript for concise conditional execution of a single statement.

## Single-line if statements

When you have a simple condition that requires only a single action, JavaScript allows you to write if statements in a more concise way. This is known as a single-line if statement. In this structure, curly braces are omitted, and the action is written directly after the condition.

```javascript
if (val === 1) console.log('This code will run only if val equals 1');
```

### When to use

Single-line if statements are best used for simple operations to keep your code clean and readable. They're particularly useful in scenarios like setting a variable, logging a message, or executing a simple function based on a condition.

### Limitations

**Only one statement:** The single-line if only allows for one statement to be executed. If you have multiple actions that depend on the condition, you'll need to use the standard if statement with curly braces.

**Readability:** While it can make the code more concise, it can sometimes reduce readability, especially in complex codebases. Use this form judiciously and always prioritize clarity.