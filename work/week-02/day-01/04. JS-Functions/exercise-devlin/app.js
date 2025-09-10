// FUNCTIONS

function printFullName(lastName, firstName) {
    // console.log(`Hi! My name is ${firstName}, ${lastName}`)
    return `Hi! My name is ${firstName}, ${lastName}`
}

// printFullName(234572387, "Devlin")

console.log("anything i want", 123, true, printFullName(234572387, "Devlin"))

function printOneThroughNum(num = 5, num2, num3, num4 = 200) {
    // for (let i = 1; i <= num; i++) {
    //     console.log(i)
    // }
    console.log(num)
    return num + num2 + num3 + num4
}


// console.log(printOneThroughNum(10, 12, 13))

// REST / SPREAD OPERATOR
function addNumbers(num1, ...params) {
    console.log(num1, params)
}

// addNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 112, 12, 23234234)

// NESTING FUNCTIONS
function testOne() {

    console.log("i am test function one")
    // console.log(newName)
    test2()

    function test2() {
        console.log("Hello I am test function two ")

    }

    // const newName = "DevlinB"
}
testOne()

// ARROW FUNCTIONS
function add2() {}

const add = function(numA, numB) {
  return numA + numB;
}

console.log(add(1, 2));

const add3 = (numA, numB) => {
  return numA + numB;
}

const emphasize = (str) => (`${str} ${str}!`)

console.log(emphasize('really'))



// EXERCISE
// • write function that:
//     •• accepts three parameters: name, birthdate, color
//     •• creates three variables: myName, myBirthdate, myFavColor
//     •• if name is the same:	console.log(“We have the same name!”) else: “Hi (person’s name)”
//     •• if birthdate is the same:	console.log(“We have the same birthdate!”) else: “What a special birthday!”
//     •• if color is the same:	console.log(“I like (color) too!”) else: “(color) is a beautiful color!”
//     •• call the function to test your function works!
//     •• console.log() whatever you return from the return statement!
