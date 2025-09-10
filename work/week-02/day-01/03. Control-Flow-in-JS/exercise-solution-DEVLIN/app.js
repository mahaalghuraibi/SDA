
// console.log(Boolean(""))
// console.log(Boolean("test"))

// if ("test" && 1) {
//     console.log("this if statement is truthy");
// }

// if ("test" || null && "test 2") {
//     console.log("this if statement is truthy line 10");
// }

// if ("12" === 12) {
//     console.log("these are both the number 12 line 14") 
//     // this will not print
// }

// if ("12" == 12) {
//     console.log("these are both the number 12 line 19") 
//     // this will print
// }

// if (12 >= 12) console.log("yes, the number is less than 12 on line 23")

// const numOne = 3;
// const numTwo = 3; 
// if (numOne <= numTwo) {
//     console.log("num one is greater or equal")
// } else if (numOne === numTwo) {
//     console.log("these numbers are equal")
// } else {
//     console.log("num one is less than or equal to num two")
// }

const numThree = 20;
const numFour = 10; 
let answer = null;
if (numThree <= numFour) {
    console.log("num one is greater or equal")
    answer = numThree;
    if (numThree === 7) {
        console.log("the number is 7")
    }
} else if (numThree === numFour) {
    console.log("these numbers are equal")
} else {
    answer = numFour;
    console.log("num one is less than or equal to num two")
}

console.log(answer)

// TERNARY
const answerTwo = numThree >= numFour ? "yes it is greater" : "no it is not greater"
console.log(answerTwo)

// LOOPING
// if () {}
const num1 = 5
const num2 = 60;
for (let i = num1; i <= num2; i += 5) {
    console.log(i)
    if (i % 5 === 0) console.log("i is a divider of 5")
}

// console.log(17 % 3)

// • write the code that:
//     •• prints the numbers from 1 to 100. 
//     •• For multiples of 3, print "Fizz"
//     •• For multiples of 5, print "Buzz". 
//     •• For numbers which are multiples of both 3 and 5, print "FizzBuzz".

for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) console.log("FizzBuzz") 
    else if (i % 3 === 0) console.log("Fizz");
    else if (i % 5 === 0) console.log("Buzz");
    else console.log(i);
}

let test = true;
let num = 1
while (test) {
    console.log("While loop still running")
    if (num === 19) test = false;
    num += 1;
}

console.log(`While loop complete!! =? ${num}`)