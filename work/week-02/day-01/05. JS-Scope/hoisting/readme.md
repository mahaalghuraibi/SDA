````markdown
# JavaScript Hoisting Guide

## What is Hoisting?

In JavaScript, **hoisting** is a behavior where variable and function **declarations** are moved to the top of their containing scope **before the code is executed**.  
With `let` and `const`, declarations are hoisted, but they cannot be accessed before they are initialized. This period is called the **Temporal Dead Zone (TDZ)**.

### Why is it Beneficial?

Hoisting is a core JavaScript behavior that moves **declarations** to the top of their scope before code execution. Understanding it provides several practical benefits:

---

#### 1. Flexible Function Placement

- Function **declarations** are fully hoisted.  
- You can call functions **before they are defined** in the code, allowing more flexible and readable organization.

```javascript
greet() // Works even though greet is defined later

function greet() {
    console.log("Hello!")
}
```

---

#### 2. Encourages Proper Code Organization

- Hoisting makes it clear that **declarations are lifted**, encouraging developers to **declare variables and functions at the top of their scope**.  
- This improves code readability and reduces surprises.

```javascript
let total = calculateTotal(5, 10)

function calculateTotal(a, b) {
    return a + b
}
```

---

#### 3. Highlights the Temporal Dead Zone (TDZ)

- `let` and `const` are hoisted but cannot be accessed before initialization.  
- Understanding this prevents **ReferenceErrors** and subtle bugs.

```javascript
console.log(x) // ReferenceError
let x = 5
```

---

#### 4. Helps Debug and Understand Code Execution

- Knowing what is hoisted clarifies **why certain variables or functions work before their declaration** and why others don’t.  
- This improves debugging skills and understanding of JavaScript's execution model.

---

## Hoisting with `let` and `const`

- `let` and `const` are hoisted to the top of their block scope, but trying to access them before the declaration line will throw a **ReferenceError**.  
- Always declare `let` and `const` variables before using them.

```javascript
console.log(a) // ReferenceError
let a = 10

console.log(b) // ReferenceError
const b = 20
```

---

## Hoisting with Function Declarations

- Traditional function declarations are **fully hoisted**.  
- You can call them **before their declaration** in the code.

```javascript
greet() // "Hello!"

function greet() {
    console.log("Hello!")
}
```

---

## Hoisting with Function Expressions

- Function expressions are assigned to variables.  
- Only the variable declaration is hoisted (not the function assignment).  
- Accessing the function before assignment will throw a **ReferenceError** with `let`/`const`.

```javascript
sayHi() // ReferenceError
const sayHi = function() {
    console.log("Hi!")
}
```

---

## Hoisting with Arrow Functions

- Arrow functions are a type of function expression.  
- Like regular function expressions, the variable is hoisted, but the function assignment is not.  
- Accessing it before initialization will throw a **ReferenceError**.

```javascript
sayHello() // ReferenceError
const sayHello = () => {
    console.log("Hello!")
}
```

---

## Key Takeaways

- `let` and `const` declarations are hoisted but cannot be accessed before initialization (TDZ).  
- Function declarations are fully hoisted and can be called before they appear in the code.  
- Function expressions and arrow functions behave like `let`/`const` variables: only the variable is hoisted, not the assignment.  
- Always declare your variables and functions **before using them** to avoid ReferenceErrors and improve code readability.

---

## Visual Example

Original code:

```javascript
console.log(x) // ReferenceError
let x = 5

console.log(add(2,3)) // 5
function add(a,b) {
    return a + b
}

console.log(subtract(5,2)) // ReferenceError
const subtract = (a,b) => a - b
```

What JavaScript actually sees (hoisted version conceptually):

```javascript
// let x and const subtract are hoisted but in TDZ
let x
const subtract

// function add is fully hoisted
function add(a,b) {
    return a + b
}

console.log(x) // ReferenceError
x = 5

console.log(add(2,3)) // 5

console.log(subtract(5,2)) // ReferenceError
subtract = (a,b) => a - b
```
