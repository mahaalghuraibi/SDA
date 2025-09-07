<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Pixart 

For this assignment you'll be creating a Javascript painting app.
<br>
Use the starter code and commit after each step of the exercise.
<br>

## Instructions

[Here is a Codepen on how to capture user input from a form](https://codepen.io/marcwright/pen/MWbZRvo?editors=1011)

### 1. Get color setting working

* When I click the "Set Color" button, it should change the color of the "brush" box to the color I specify in the input field.
* You can use `document.querySelector` (or another document method) to select the element, then add an event listener.

> **HINT:** You will notice that the page refreshes whenever you click the button. You need to prevent this from happening using a method you have not used before. Google "javascript event prevent default".

<br>
:red_circle: **Commit.**
<br>

### 2. Enable enter key to change color

* The same thing should happen when I press the enter key from inside the input field

<br>
:red_circle: **Commit.**
<br>

### 3. Make the squares

* Create 20 divs of the "square" class and append them to the body
* **Hint**: use `.appendChild()`

<br>
:red_circle: **Commit.**
<br>

### 4. Clicking a square should change its color to green

* Add functionality so that when I click on each "square", it changes the color of that individual square to "green"
* **Hint**: either add the event listener while creating the squares, or listen for events on the `body` element

<br>
:red_circle: **Commit.**
<br>

### 5. Clicking a square makes it be the selected color

* Modify your code so that when I click on each "square", it changes to the color I set using my input instead of "green" every time.

<br>
:red_circle: **Commit.**
<br>

### 6. Scale it appropriately.

* Modify the CSS so that the "square" class has a height and width of 10px and a margin of 0.
* Modify your code so that you are creating 8000 divs instead of 20.
* Change the event that changes your box colors from 'click' to 'mouseover'
* Paint a picture!

<br>
:red_circle: **Commit.**
<br>

# Hungry for more :interrobang:

### 7. Enable lifting of "brush"/"pen".

Make it so that clicking the canvas "turns off" and "turns on" the paintbrush.  Have there be an indicator that says "Paintbrush on" when it's on and "Paintbrush off" when it's off.  Changing colors should not change whether the paintbrush is off or on.

<br>
:red_circle: **Commit.**
<br>

### 8. Color History

Add a color swatch. You should have 3 boxes with the most recent 3 colors used. When you click on each of those boxes, it should set the current brush color back to that color.

<br>
:red_circle: **Commit.**
<br>
