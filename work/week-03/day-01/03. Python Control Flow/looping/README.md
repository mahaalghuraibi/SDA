# ![Python for JavaScript Developers - Control Flow - Looping](./assets/hero.png)

**Learning objective:** By the end of this lesson, students will be able to implement control flow with loops in Python.

## The `for` statement

Python's `for` statement is not designed like the one you first used in JavaScript:

```javascript
// A JavaScript for loop
for (let i = 0; i < 10; i++) {
  // do something ten times
}
```

Instead, the Python `for` loop always iterates over the items in a ***sequence*** (an ordered collection of items), similar to JavaScript's `for...in` and `for...of` loops. Here's how Python's `for` loop is used to loop through a ***list*** (Python's version of a JavaScript array):

```python
names = ["Emily", "Jack", "Sophia", "Ethan"]

for name in names:
    print(name)
```

The JavaScript equivalent would be this:

```javascript
let names = ["Emily", "Jack", "Sophia", "Ethan"];

for (name of names) {
  console.log(name);
}
```

## The `while` loop

Python also has a `while` loop construct that will continue to iterate **while a given condition is truthy**.

Let's look at the syntax:

```python
num = 1

while num <= 10:
    print(num)
    # prints the numbers 1 through 10
    num += 1
```

`while` loops are great for when you don't know how many times you will need to iterate - for example if you want to continue getting input from a user until a specific condition is met.

> 🚨 Beware of infinite loops! When using while loops, it's important to ensure that the condition will change to a falsy value so that the loop eventually exits.

## The `break` and `continue` statements

Like in JavaScript, the `break` statement in Python is used to exit `for` and `while` loops immediately.

In `for` and `while` loops, the `continue` statement will end the current iteration of a loop and continue to the next iteration as long as the condition of the loop is still truthy or there are still items to iterate through.

Here's an example:

```python
things = ["computer", "g-g-ghost", "chair", "spider", "desk"]

for thing in things:
    if thing == "g-g-ghost":
        print("Oh, that's just my ghost friend, carry on.")
        continue
    elif thing == "spider":
        print("Nope. Burn it down, no more.")
        break
    print(f"There is a {thing} in the room.")
```

## 🎓 You Do

Wrap the code you wrote in the previous branching exercise in a `while` loop. This should cause it to continue prompting the user for a color. The loop should end when the word `quit` is entered.
