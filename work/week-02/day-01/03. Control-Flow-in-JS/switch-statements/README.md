<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead"><code>switch</code> Statements</span>
</h1>

**Learning objective:** Students will learn how to effectively use the switch statement in JavaScript to handle multiple conditional cases, improving code readability and maintainability.

Look into using the `switch` statement instead of `if`...`else` if you have more than three code paths, and your conditionals always check the same variable.

Here’s the documentation for the [switch statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch).

As an example, the following `if...else if...else` statement: 

```javascript
const seasonCheck = 'winter';

if (seasonCheck === 'summer') {
  console.log("It's summer!");
} else if (seasonCheck === 'fall') {
  console.log("It's fall now!");
} else if (seasonCheck === 'winter') {
  console.log('Brrr!');
} else if (seasonCheck === 'spring') {
  console.log("It's spring!");
} else {
  console.log('Invalid season');
}
```

Can also be expressed using `switch` as: 

```javascript
const seasonCheck = 'winter';

switch (seasonCheck) {
  case 'summer':
    console.log("It's summer!");
    break;
  case 'fall':
    console.log("It's fall now!");
    break;
  case 'winter':
    console.log('Brrr!');
    break;
  case 'spring':
    console.log("It's spring!");
    break;
  default:
    console.log('Invalid season');
}
```

## Fall-through

```javascript
switch (seasonCheck) {
  case 'summer':
    console.log("It's summer!");
    break;
  case 'autumn':
  case 'fall':
    console.log("It's fall now!");
    break;
  case 'winter':
    console.log('Brrr!');
    break;
  case 'spring':
    console.log("It's spring!");
    break;
  default:
    console.log('Invalid season');
}
```

The `break` statement is used within a `switch` statement's body to break out of execution early. 

If `break` is omitted, then execution moves on to the next `case`, regardless of if it matches the expression. 

In this example, `seasonCheck` could equal 'autumn' OR 'fall' and fall-through would ensure that "It's fall now!" would be logged in both instances. 
