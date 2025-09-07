function isAdult(age) {
    if (age >= 18) {
        return 'Adult';
    } else {
        return 'Minor';
    }
}
console.log('Exercise 2 Result:', isAdult(21));

function isCharAVowel(char) {
    const vowels = ['a','e','i','o','u'];
    if (vowels.includes(char.toLowerCase())) {
        return true;
    } else {
        return false;
    }
}
console.log('Exercise 3 Result (a):', isCharAVowel("a")); 

function generateEmail(name, domain ) {
    return name +'@' + domain;
}
console.log('Exercise 4 Result:', generateEmail("maha",'gmail.com'));

function greetUser(name, timeOfDay) {
    return "Good " + timeOfDay + ", " + name + "!";
}

console.log('Exercise 5 Result:', greetUser("maha", "morning"));

function maxOfThree(num1, num2, num3) {
    if (num1 >= num2 && num1 >= num3) {
        return num1;
    } else if (num2 >= num1 && num2 >= num3) {
        return num2;
    } else {
        return num3;
    }
}
console.log('Exercise 6 Result:', maxOfThree(5, 10, 8)); 

function calculateTip(billAmount, tipPercentage) {
    const tip = billAmount * (tipPercentage / 100);
    return tip;
}
console.log('Exercise 7 Result:', calculateTip(50, 20)); 

function convertTemperature(temperature, scale) {
    if (scale === "C") {
        return (temperature * 9/5) + 32;
    } else if (scale === "F") {
        return (temperature - 32) * 5/9;
    } else {
        return "Invalid scale"; 
    }
}
console.log('Exercise 8 Result:', convertTemperature(32, "C")); 

function basicCalculator(num1, num2, operation) {
    if (operation === "add") {
        return num1 + num2;
    } else if (operation === "subtract") {
        return num1 - num2;
    } else if (operation === "multiply") {
        return num1 * num2;
    } else if (operation === "divide") {
        return num1 / num2;
    } else {
        return "Invalid operation";
    }
}

console.log('Exercise 9 Result:', basicCalculator(7, 5, "add"));      

function calculateGrade(score) {
    if (score >= 90) {
        return "A";
    } else if (score >= 80) {
        return "B";
    } else if (score >= 70) {
        return "C";
    } else if (score >= 60) {
        return "D";
    } else {
        return "F";
    }
}

console.log('Exercise 10 Result:', calculateGrade(70));  

function createUsername(firstName, lastName) {
    const firstPart = firstName.slice(0, 3);
    const lastPart = lastName.slice(0, 3);
    const totalLength = firstName.length + lastName.length;
    return firstPart + lastPart + totalLength;
}

console.log('Exercise 11 Result:', createUsername("Maha", "Alghuraibi")); 

function numArgs(...args) {
    return args.length;
}

console.log('Exercise 12 Result:', numArgs(1, 2, 3, 4)); 
