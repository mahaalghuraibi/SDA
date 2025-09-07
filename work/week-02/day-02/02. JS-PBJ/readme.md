# JS Peanut Butter and Jelly!

## The idea
For this exercise, we'll be using most everything we've learned on JavaScript so far. Your task will to be create a program that will help a user build their favorite own peanut butter and jelly sandwhich! YUMMY!!<br/><br/>

In order to create this program you will use javascript variables, control flow, and scope to allow the user to make decisions on hwo they want to build their sandwhich. We highly suggest using pseudocode to break down the algorithm into little steps that will eventually lead up to a fully working sandwhich making algorithm!<br/><br/>

## How to Get User Input
To ask the user for input we can use the `prompt()` from a nodeJS package that we will give you access to. 

*Try this code out in your browser console...*
```js
// prompts user and stores value in the variable
let valueOfPrompt = prompt('Good morning! We would like to help you make a peanute butter and jelly sandwhich. First you need to choose what kind of bread you would like. Choose which number you would like: 1: white bread, 2: whole grain...')
// logs value stored
alert(`You choose ${valueOfPrompt}`)
```

`prompt()` will `return` whatever the user types into the dialog box.

**WE NEED TO INSTALL A PACKAGE THROUGH THE NODEJS PACKAGE MANAGER CALLED `prompt-sync`. This package is what will allow you to request and receive input from the user in the terminal.**

1. In this current folder: `work/week-02/day-02/02. JS-PBJ/readme.md` we will install the package with: `npm i prompt-sync`
2. That's it!

## Requirements
1. Write the pseudocode **first**
2. Offer multiple options at each point in the process. Type of bread, type of peanut butter, etc...
3. You must check that the user responds with a number for the option they want.
   1. Think about how this will be implemented before just writing code!!
   2. How can we make sure the input is a number (hint: research through google!!!)
   3. How can we make sure it is one of the options you presented them? What is the number is 65 and you only have 2 options?
4. Once the sandwhich is built, present (print) the sandwhich in the terminal for the user to see how their sandwhich came together.
5. Implement a while loop so the user will be prompted to make another sandwhich or quit the process.

## Example

```js
firstQuestion() /* don't forget to run the function defined below! */
function firstQuestion () {
  let sandwhich;
  let response = prompt('You are walking down the road and a hungry-looking dog comes up to you, sniffing for treats. You have a cracker wrapped in plastic in your pocket. Do you feed the cracker to the dog? (choose y or n)')

  if (response === 'y') {
    /*call secondQuestion function*/
  } else {
    /*call thirdQuestion function*/
  }

  console.log(sandwhich)
}
```

## Running your code
When you are ready you will run your code with this command: `node script.js`.<br/><br/>

Simply type that command in the terminal in the same location as the script.js file and hit enter.