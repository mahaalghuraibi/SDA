const prompt = require('prompt-sync')();
// - DO YOU WANT A PB&J SANDWICH?
//     - YES -> BUILD A SANDWICH
//     - NO  -> END PROGRAM
const sandwichRes = prompt("DO YOU WANT A PB&J SANDWICH?!"); 
if (sandwichRes === "YES") peanutButterAndJellySandwhich()
else console.log("Thank you - Have a nice day!");
return

function peanutButterAndJellySandwhich() {
    // - SAVE NUMBER OF SANDWICHES
    let numOfSandwich = null;
    // - SAVE KIND OF BREAD
    let kindOfBread = null;
    // - SAVE THE FLAVOR OF JELLY
    let kindOfJelly = null;
    // - SAVE KIND OF PEANUT BUTTER
    let kindOfPnutButter = null;
    // - SAVE CUT IN HALF
    let cutChoice = null;
    // - SAVE WANT THE CRUST
    let crust = null;
    
    while(typeof numOfSandwich !== "number" || isNaN(numOfSandwich)) {
        // - HOW MANY SANDWICHES DO YOU WANT?
        numOfSandwich = parseInt(prompt("HOW MANY SANDWICHES DO YOU WANT?!"));
        if(typeof numOfSandwich !== "number" || isNaN(numOfSandwich)) console.log("Please provide a real number.")
    }
    
    // - WHAT KIND OF BREAD WOULD YOU LIKE?
    const breadOptions = { 1: "White Bread", 2: "Wheat Bread", 3: "Multi-Grain Bread" }
    while(!(kindOfBread in breadOptions)) {
        kindOfBread = prompt("Which bread would you like?\n1: White Bread\n2: Wheat Bread\n3: Multi-Grain Bread").trim(); 
        if (!(kindOfBread in breadOptions)) console.log("Please choose a valid option.");
    }

    // - WHAT FLAVOR OF JELLY WOULD YOU LIKE?
    const jellyOptions = { 1: "Cherry", 2: "Strawberry", 3: "Raspberry" }
    while(!(kindOfJelly in jellyOptions )) {
        kindOfJelly = prompt("Which jelly would you like?\n1: Cherry\n2: Strawberry\n3: Raspberry").trim();; 
        if (!(kindOfJelly in jellyOptions)) console.log("Please choose a valid option.");
    }
    
    // - WHAT KIND OF PEANUT BUTTER
    const pnutButterOptions = { 1: "Crunchy", 2: "Smooth", 3: "Honey" }
    while(!(kindOfPnutButter in pnutButterOptions)) {
        kindOfPnutButter = prompt("Which peanut butter would you like?\n1: Crunchy\n2: Smooth\n3: Honey").trim();; 
        if (!(kindOfPnutButter in pnutButterOptions)) console.log("Please choose a valid option.");
    }
    
    // - WOULD YOU LIKE IT CUT IN HALF?
    const cutOptions = { 1: "In Half", 2: "In Quarters", 3: "Whole" }
    while(!(cutChoice in cutOptions)) {
        cutChoice = prompt("How would you like your bread cut?\n1: In Half\n2: In Quarters\n3: Whole").trim();; 
        if (!(cutChoice in cutOptions)) console.log("Please choose a valid option.");
    }
    
    // - DO YOU WANT THE CRUST?
    const crustOptions = { 1: "No Crust", 2: "With Crust" }
    while(!(crust in crustOptions)) {
        crust = prompt("Do you like crust?\n1: No crust\n2: With Crust").trim();
        if (!(crust in crustOptions)) console.log("Please choose a valid option.");
    }

    // - DISPLAY SANDWICH / ENJOY
    console.log(`Thank you for ordering a sandwich.\nThis is what your sandwich will include:\nYou have a ${pnutButterOptions[kindOfPnutButter]} Peanut Butter Sandwich\nwith ${jellyOptions[kindOfJelly]} jelly, ${crustOptions[crust].toLowerCase()},\n${ cutChoice === 3 ? " not cut." : `and cut ${cutOptions[cutChoice].toLowerCase()}` } `)

}


/* PSEUDOCODE HERE */
/*

- DO YOU WANT A PB&J SANDWICH?
    - YES -> BUILD A SANDWICH
    - NO  -> END PROGRAM

- HOW MANY SANDWICHES DO YOU WANT?
    - STORE NUMBER OF SANDWICHES
- WHAT KIND OF BREAD WOULD YOU LIKE?
    - SAVE KIND OF BREAD
- WHAT FLAVOR OF JELLY WOULD YOU LIKE?
    - SAVE THE FLAVOR OF JELLY
- WHAT KIND OF PEANUT BUTTER
    - SAVE KIND OF PEANUT BUTTER
- WOULD YOU LIKE IT CUT IN HALF?
    - SAVE CUT IN HALF
- DO YOU WANT THE CRUST?
    - SAVE WANT THE CRUST
- DISPLAY SANDWICH / ENJOY
- END PROGRAM




*/
