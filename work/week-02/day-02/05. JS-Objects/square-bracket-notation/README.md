<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Square Bracket Notation</span>
</h1>


**Learning objective:** By the end of this lesson, students will be able to use square bracket notation for dynamically accessing, adding, updating, and deleting properties in JavaScript objects.

We've covered dot notation as the primary way to engage with object properties. The other way to access, add, update, and delete properties is by using **square bracket notation**. We use *square bracket notation* instead of *dot notation* when we’re writing code where we don’t know which property needs to be accessed. In other words, we use *square brackets* to access properties *dynamically* during runtime.

*Square bracket notation* has the following syntax:
```javascript
someObject[anyJSExpression]
```

The `anyJSExpression` can be anything that evaluates to a single “value” - even function calls!

Let’s explore this idea with an example: 

Given an array of strings (`voteArr`), let's dynamically create and return an object with two properties.

One property will count how many instances of `'yes'` appear in the array, while another will count how many instances of `'no'` appear in the array.

So, for example, if the array has the string of `'yes'` appear in it four times and the string `'no'` appear in it six times, the output would be: `{ yes: 4, no: 6 }`.

First, we will solve this problem by using dot notation which will not be dynamic. Then we’ll solve it *again* using square bracket notation so that you can see the benefits of using square bracket notation and how square bracket notation can save us a lot of effort and help solve potential problems.

Let’s start with our data:

```javascript
const voteArr = ['yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no']
```

and then stub up a function called `voteTallyDot` that accepts an array as its only argument. Go ahead and also set up a console log. Inside it call the `voteTallyDot` function and pass in the `voteArr`.

```javascript
function voteTallyDot(arr) {

}

console.log(voteTallyDot(voteArr));
```

Next, we will create an object to accumulate vote tallies into and assign it to a const variable named `tally`. Since the `tally` variable is what will eventually hold all our data, that's what we will return out of the function.

```javascript
function voteTallyDot(arr) {
  const tally = { yes: 0, no: 0 };
	
  return tally;
}
```

<br>

With our function fully stubbed up, we need to loop through the array passed to the function. On each iteration, we will assign the element we are iterating over into a constant called `vote`.

```javascript
function voteTallyDot(arr) {
  const tally = { yes: 0, no: 0 };
  for (let i = 0; i < arr.length; i++) {
    const vote = arr[i];
  }
  return tally;
}
```

Our next step is to look at what `vote` is to branch off our functionality. Looking at our `voteArr`, we can determine that `vote` can be either `'yes'` or `'no'`, so that is what our conditionals will look for.

```javascript
function voteTallyDot(arr) {
  const tally = { yes: 0, no: 0 };
  for (let i = 0; i < arr.length; i++) {
    const vote = arr[i];
    if (vote === 'yes') {
      // We have a yes vote!
    } else if (vote === 'no') {
      // We have a no vote! 
    }
  }
  return tally;
}
```

<br>

We’re getting close to the end. Next, we need to look on the `tally` object for a key that matches what’s held in vote. 

```javascript
function voteTallyDot(arr) {
  const tally = { yes: 0, no: 0 };
  for (let i = 0; i < arr.length; i++) {
    const vote = arr[i];
    if (vote === 'yes') {
      tally.yes = tally.yes + 1;
    } else if (vote === 'no') {
      tally.no = tally.no + 1;
    }
  }
  return tally;
}
```

If we run our code now, we can see that our output should be `{ yes: 4, no: 6 }`,  which is correct!

<br>

So this works, yay! But what if we want to expand this function to accept an array that can have values in addition to the `'yes'` or `'no'` we have already? That will mean another block with more code that does almost the same thing. What if we don’t know what the votes can be ahead of time? In that case, the best we could do is add a catch-all `else` at the end that would catch whatever isn’t a `'yes'` or a `'no'`. 

So, the moral of this story: this could quickly spiral out of control and become a huge pain to maintain. Enter square bracket notation. 

Go ahead and create a new function called `voteTallySquare` and have it take in an array as its only argument. Then, inside a console log, call the `voteTallySquare` function and pass in the `voteArr`.

```javascript
function voteTallySquare(arr) {

}

console.log(voteTallySquare(voteArr));
```

We’ll skip right to the good stuff by duplicating some previous work we’ve already done into our new function. This code is the same as above, so we’re not going to dive into it again here.


```javascript
function voteTallySquare(arr) {
  const tally = {};
  for (let i = 0; i < arr.length; i++) {
    const vote = arr[i];
  }
  return tally;
}
```

And now it’s time for square bracket notation! We’re going to start by seeing if the `tally` object has a `vote` defined on it. Remember, in this case, `vote` will hold a value of either `'yes'` or `'no'`. 

```javascript
function voteTallySquare(arr) {
  const tally = {};
  for (let i = 0; i < arr.length; i++) {
    const vote = arr[i];
    if (tally[vote]) {
			// property exists on the tally object
    } else {
			// property doesn't exist on the tally object
    }
  }
  return tally
}
```

Like we did above, when a property is `undefined` on the `tally` object, we will define it by setting its value to `1`. When a property has already been defined, we will increment its value by `1`.

```javascript
function voteTallySquare(arr) {
  const tally = {};
  for (let i = 0; i < arr.length; i++) {
    const vote = arr[i];
    if (tally[vote]) {
      tally[vote] = tally[vote] + 1;
    } else {
      tally[vote] = 1;
    }
  }
  return tally;
}
```

If we run our code now, we can see that our output should be `{ yes: 4, no: 6 }`, which is correct!

Look how much less code we had to write to accomplish the same thing! We also solved a few problems we had with our solution that utilized dot notation - this function can take in an array with any number of different values in it, and we don’t even need to know what those values are ahead of time.