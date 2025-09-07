<h1>
  <span class="headline">JavaScript Control Flow</span>
  <span class="subhead">Boolean Logic</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to use comparison operators to compare values in code. 

In coding, just as in everyday decision-making, we often need to compare values to decide what action to take. This process in programming is similar to comparing numbers or quantities in everyday life. For instance, you might compare prices while shopping to decide which item is more affordable.

To perform these comparisons in code, we use special symbols known as *operators*. 

> 📚 An operator in programming is a symbol that tells the computer to perform a specific mathematical, relational, or logical operation. The items we compare using these operators are called operands. Operands can be direct values (like numbers) or variables that represent values.

For example, consider the statement `10 is greater than 5`. In mathematics, this is expressed as `10 > 5`.Here, `10` and `5` are the operands, and the symbol `>` is the operator that performs the comparison between them.

## Equality operators

**Equality operators** are the tools we use to compare whether two values are equal. These values can be variables, literal values (like numbers or strings), and more. In JavaScript, there are two primary equality comparison operators:

- `===` - Strict Equality (Best Practice)
- `==` - Loose Equality (Performs Type Conversion)

The strict equality operator, often referred to as 'triple equals,' compares the values of both the left and right operands and returns `true` if they are not only equal in value, but also of the same data type.

If the values have different types, then the operator returns `false`. 

```javascript
3 === 3   // true
3 === 4   // false
3 === '3' // false 
```

In loose equality: `3 == '3'` is true because, with loose equality, `3` (a number) is considered equal to `'3'` (a string)."

```js
3 == '3' // true, but dangerous
```

Strict equality `===` avoids confusion and errors in code by ensuring that not only the values are equal but also their types. For example, treating the number `0` and the string `'0'` as the same could lead to unexpected results.

We'll always use strict equality as a best practice.

## Relational operators

JavaScript also has a host of relational operators: 

- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal to
- `>=` - Greater than or equal to

```javascript
3 < 4       // true
3 > 4       // false
10 >= 5 + 5 // true
```

In a gaming app, you might use relational operators to check if a player's score is greater than a certain threshold to level up: `playerScore > 1000`.

## Logical operators

In JavaScript, you often encounter situations where you need to make decisions based on the truthiness or falsiness of values. This is where logical operators `||` (OR) and `&&` (AND) come into play. They not only allow you to check conditions but also provide some powerful behaviors that can make your code more concise and expressive.

> The logical operators `||` and `&&` help evaluate multiple conditions simultaneously.

The logical OR (`||`) operator evaluates multiple conditions. If any of the conditions evaluate to `true`, then the operator resolves to `true`. Here are some examples:

```javascript
true  || true   // true
true  || false  // true
false || false  // false

'sandwich' === 'sandwich' || 2 === 2 // true
'hotdog' === 'sandwich'   || 2 === 2 // true
'hotdog' === 'sandwich'   || 4 === 5 // false
```

More than two conditions may be evaluated at a time. For example:

```js
true  || true  || true  // true
true  || true  || false // true
true  || false || false // true
false || false || false // false
```

The logical AND (`&&`) operator also evaluates multiple conditions. Every condition must evaluate to `true` for the operator to resolve to `true`. Using the same examples as above, and only changing the operator:

```javascript
true && true   // true
true && false  // false
false && false // false

'sandwich' === 'sandwich' && 2 === 2 // true
'hotdog' === 'sandwich' && 2 === 2   // false
'hotdog' === 'sandwich' && 4 === 5   // false
```

Imagine setting an alarm. You only want the alarm to ring if it's a weekday AND the time is 7:00 AM. This could be represented as:

```js
isWeekday && isSevenAm
```

Again, more than two conditions may be evaluated at a time. For example:

```js
true && true && true    // true
true && true && false   // false
true && false && false  // false
false && false && false // false
```

## The not operator

The not (`!`) operator, also known as the bang operator, flips a `true` expression to the boolean value of `false`, and vice-versa. For example: 

```javascript
!false  // true
!true   // false
```

When used in conjunction with the equality operators, the syntax looks like this: 

- `!==` - Strict Inequality

```javascript
3 !== 4   // true, 3 isn't equal to 4
3 !== 3   // false, 3 is equal to 3
```