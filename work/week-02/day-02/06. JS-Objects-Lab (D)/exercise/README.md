<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# JS Objects Lab

This lab provides an opportunity to practice defining, accessing, and manipulating objects and arrays. Don't hesitate to collaborate with your classmates when working through labs. If you get stuck during the lab, we recommend revisiting the lesson materials first. They're designed to provide you with the information and examples that will help you complete the exercises.

## SETUP
As you work through the following lab, copy and paste the following exercises into your `app.js` file. To check your work, run the file in your terminal using `node app.js`.<br/><br/>

You will notice that the files look slightly different this time. We have created two separate `.js` files to divide the Pokemon data and keep it separate from our exercise code. While the pokemon data is critical to run your code, it is not the primary focus of this lab, so detailed understanding at this stage is not required. You can ignore what is happening in the background for now.<br/><br/>

> If you are curious.. there is a line of code (`module.exports = pokemon;`) at the bottom of the `data.js` file. This line allows nodeJS to be able to 'export' data from that file and make the data accessible from another file. At the very top of the `app.js` file we see a line of code that says: `const pokemon = require('./data.js');` This is the code that allows us to access the data from the `data.js` file. For now.. just appreciate the syntax and ignore it otherwise.

**COPY AND PASTE EACH EXERCISE BELOW AND WORK TO SOLVE EACH ITEM**

### Exercise 1
Spend some time inspecting the `pokemon` array by running the following command:

```javascript
console.dir(pokemon, { maxArrayLength: null })
```

In this lab, we're using a method you might be unfamiliar with: `console.dir()`. We're using it here so that you can see all of the Pokemon in the console. Normally, both `console.dir()` and `console.log()` show only the first 100 items in an array. However, by using `{ maxArrayLength: null }` with `console.dir()`, we can display every item in the array. This specific option isn't available with `console.log()`, making `console.dir()` the necessary choice for the full visibility needed in this lab.

Take note of the shape of the data here. Each Pokemon object in the array has the following properties:

- Number: A number between 1 and 151.
- Name: A string representing the Pokémon's name.
- Type: A string indicating the Pokémon's type.
- HP (Hit Points): A numerical value representing the Pokémon's health.
- Starter: A boolean indicating whether the Pokémon is a starter.


There's some game-specific terminology here, if you're new to Pokémon, here's an explanation of the terms used in the game:

- **Number**: Each Pokémon has a unique number as its identifier.
- **Type**: This refers to a Pokémon's primary abilities. While Pokémon can have multiple types, we're focusing on their primary type here for simplicity.
- **Hit Points (HP)**: This is a measure of a Pokémon's health, expressed in a numerical value.
- **Starter Pokémon**: At the beginning of the game, players choose a starting Pokémon. In our data, starter Pokémon are marked with a starter property set to true. 

The starter Pokémon options are:
 - Pokémon 1: Bulbasaur
 - Pokémon 4: Charmander
 - Pokémon 7: Squirtle
 - Pokémon 25: Pikachu

When you've completed your inspection of the data, you can comment out the `console.dir()` method and use `console.log()` to log JUST the name of the Pokemon with the number 59 using the index of the Pokemon in the array. Feel free to uncomment the `console.dir()` as needed to help you complete the rest of the lab.

### Exercise 2

Next, add the following `console.log`:

Run the following:

```javascript
console.log(game)
```

Take a moment to familiarize yourself with the `game` object being logged. It has four properties: `party`, `gyms`, and `items`. All of these hold or will hold an array of objects.

As you move through the exercises:

- `game.party` will hold an array of Pokemon objects that will be retrieved from the `pokemon` array we reviewed in Exercise 1. These are Pokemon that you have caught!
- `game.gyms` holds an array of objects, each representing a gym (checkpoints placed throughout the game). Note the `completed` boolean property on each. This will be important later.
- `game.items` holds an array of objects, each representing an item in a player's inventory.

When you've completed your inspection of the data, you can comment out the console.log and move on to Exercise 3. Feel free to uncomment the console.log as needed to help you complete the rest of the lab.

### Exercise 3

```javascript
/*
Exercise 3
1. Add a new property to the `game` object. Let's call it "difficulty".
2. Choose a value for "difficulty" that you think fits the game. Ex: "Easy", "Med" or "Hard". How would you assign it?


Solve Exercise 3 here:
*/


```


### Exercise 4

```javascript
/*
Exercise 4
1. Select a starter Pokémon from the `pokemon` array. Remember, a starter Pokémon's `starter` property is true.
2. Add this Pokémon to the `game.party` array. Which array method will you use to add them?


Solve Exercise 4 here:
*/


```

### Exercise 5

```javascript
/*
Exercise 5
1. Choose three more Pokémon from the `pokemon` array and add them to your party.
2. Consider different attributes like 'type' or 'HP' for your selection. Which array method will you use to add them?


Solve Exercise 5 here:
*/



```

### Exercise 6

```javascript
/*
Exercise 6
1. Set the `completed` property to true for gyms with a difficulty below 3.
2. Think about how you'd loop through the `gyms` array to check and update the `completed` property.


Solve Exercise 6 here:
*/

```

### Exercise 7

```javascript
/*
Exercise 7
1. Evolve the starter Pokémon you added to your party earlier. Each starter Pokémon evolves into a specific one.
2. How would you replace the current starter Pokémon in your party with its evolved form?

Hint: 
  - Pokemon 1: Bulbasaur evolves into Pokemon 2: Ivysaur
  - Pokemon 4: Charmander evolves into Pokemon 5: Charmeleon
  - Pokemon 7: Squirtle evolves into Pokemon 8: Wartortle
  - Pokemon 25: Pikachu evolves into Pokemon 26: Raichu

More Hints: The existing starter Pokemon will be *replaced* in your party with the Pokemon it evolved into. When working with an array of objects, the splice() array method is ideal for replacing one element with another. 


Solve Exercise 7 here:
*/

```
Visit the MDN docs to learn more about the [splice() method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice).


### Exercise 8

```javascript
/*
Exercise 8
1. Print the name of each Pokémon in your party.
2. Consider using a loop or an array method to access each Pokémon's name.

Solve Exercise 8 here:
*/

```

### Exercise 9

```javascript
/*
Exercise 9
1. Can you print out all the starter Pokémon from the `pokemon` array?
2. Think about how you can identify a starter Pokémon and then log their names.


Solve Exercise 9 here:
*/
```

### Exercise 10

```javascript
/*
Exercise 10
Create a method called `catchPokemon` and add it to the `game` object. You should not need to edit the original game object directly. This method should:
  - Accept an object as a parameter called `pokemonObj`
  - Add the `pokemonObj` to the `game.party` array.
  - not return anything

After writing this method, call it and pass in a Pokemon object of your choice from the `pokemon` data to catch it.

Solve Exercise 10 here:
*/
```

### Exercise 11

```javascript
/*
Exercise 11
1. Copy the `catchPokemon` method that you just wrote above, and paste it below. Modify it so that it also decreases the number of pokeballs in your inventory each time you catch a Pokémon.
2. How will you find and update the quantity of pokeballs in the `game.items` array?

Tips:
For this exercise, it's okay to have a negative number of pokeballs.
After updating the method, call it and pass in a Pokemon object of your choice from the `pokemon` data to catch it.
Also, log the `game.items` array to confirm that the pokeball quantity is being decremented.

Solve Exercise 11 here:
*/


```

### Exercise 12

```javascript
/*
Exercise 12
1. Similar to Exercise 6, now complete gyms with a difficulty below 6. How will you approach this?
 (change the value of `complete` in the qualifying objects from false to true).

Solve Exercise 12 here:
*/


```

### Exercise 13

```javascript
/*
Exercise 13
1. Create a `gymStatus` method in `game` to tally completed and incomplete gyms.
2. How will you iterate through the `gyms` array and update the tally? Remember to log the final tally.

This method should:
  - Not accept any arguments.
  - Initially create a constant `gymTally`, which is an object that has two 
    properties: `completed` and `incomplete`, both of which are initially set to 0.
  - Iterate through the objects in the `game.gyms` array and update the 
    properties on `gymTally` as follows: 
    - `completed` should count how many gyms in the array have a value of `true` 
      for their `completed` property. 
    - `incomplete` should count how many gyms in the array have a value of 
      `false` for their `completed` property.
  - Log the value of `gymTally`.
  - The method should not return anything.

For example, if five gym objects have a value of `true` on their `completed` property and three gym objects have a value of `false` on their `completed` property, the logged value would be: `{ completed: 5, incomplete: 3 }`.

Solve Exercise 13 here:
*/
```

### Exercise 14

```javascript
/*
Exercise 14
1. Add a `partyCount` method to `game` that counts the number of Pokémon in your party.

This method should:
  - Not accept any arguments.
  - Count the number of Pokemon in the party.
  - return the found number of Pokemon in the party.

Solve Exercise 14 here:
*/
```

### Exercise 15

```javascript
/*
Exercise 15
1. Now, complete gyms with a difficulty below 8. Reflect on how this is similar to or different from the previous gym exercises.
(change the value of `complete` in the qualifying objects from false to true).

Solve Exercise 15 here:
*/
```

### Exercise 16

```javascript
/*
Exercise 16
1. Log the entire `game` object to the console. Take a moment to review the changes you've made throughout the exercises.


Solve Exercise 16 here:
*/

```

🎉  **YOU DID IT! TRY THE BONUS CONTENT BELOW...**  🎉
🎉  **YOU DO NOT NEED TO COMPLETE 17++**   🎉


### Exercise 17

For this exercise, you'll need to make use of a compare function to define the sort order of `.sort()`.

Check out the [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#comparefn) for more information and examples.

```javascript
/*
Exercise 17
1. Arrange the Pokémon in `game.party` by their HP. The one with the highest HP should come first.
2. You'll need to use the `.sort()` method. How does the compare function work in sorting numbers?


Solve Exercise 17 here:
*/
```

### Exercise 18

```javascript
/*
Exercise 18
Add a new property to the `game` object called `collection` and initialize its value to an empty array.

Copy the `catchPokemon` method you wrote in Exercise Twelve and paste it below. Modify it so that:
  - Ensure that no more than six Pokemon can be in the party at any time. 
    Excess Pokemon should be placed in the `game.collection` array.
  - It's up to you how to distribute Pokemon in a situation where more than six 
    would be placed into the `game.party` array.

Again, for this exercise, it's okay to have a negative number of pokeballs.

After updating the method, use it by calling it and passing in a pokemon object of your choice from the `pokemon` data to catch it.

Also, log the `game.items` array to confirm that the pokeball quantity is being decremented.

Solve Exercise 18 here:
*/
```

### Exercise 19

```javascript
/*
Exercise 19
Copy the `catchPokemon` method that you just wrote above, and paste it below. The time has come to make it so that we cannot catch a Pokemon when we do not have any pokeballs to catch it with. 

Modify the method so that if there are no pokeballs a message will be displayed that there are not enough pokeballs to catch the desired Pokemon.

Also, ensure that the Pokemon isn't added to the `game.party` or the `game.collection`.

Solve Exercise 19 here:
*/
```

### Exercise 20

```javascript
/*
Exercise 20
Copy the `catchPokemon` method that you just wrote above, and paste it below. Modify is so that you can just pass in the name of a Pokemon instead of an entire object, and the method will look up the Pokemon from the data set for you.

The string passed in should be allowed to be any case (for example, if the string 'PiKacHU' is passed to the function, it should match to 'Pikachu' in the data set). 

If there is not a match, then return a string noting that the selected Pokemon does not exist. Ensure you do not decrement the pokeball count if an invalid Pokemon name is passed in, and also ensure that the Pokemon isn't added to the `game.party` or the `game.collection`.

Solve Exercise 20 here:
*/
```

### Exercise 21

```javascript
/*
Exercise 21
Dynamically construct an object with the existing `pokemon` data sorted by the different pokemon types. The object will have this structure:

{
  grass: [
    { number: 1, name: 'Bulbasaur', type: 'grass', hp: 45, starter: true },
    { number: 2, name: 'Ivysaur', type: 'grass', hp: 60, starter: false },
    { number: 3, name: 'Venusaur', type: 'grass', hp: 80, starter: false },
    * more grass type Pokemon objects...
  ],
  fire: [
    { number: 4, name: 'Charmander', type: 'fire', hp: 39, starter: true },
    * more fire type Pokemon objects...
  ],
  water: [
    * water type Pokemon objects...
  ],
  * etc... until there is an array for every Pokemon type!
}

Log the object when it's constructed.

Solve Exercise 21 here:
*/
```

