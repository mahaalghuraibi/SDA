const newArr = [1, 2, 3, 4]
console.log(newArr[1]);

// OBJECTS
const newObj = {}
const newObj2 = {
    "firstName": "Devlin",
    secondName: "Booth",
    1: 23,
    text: "This is text",
    age: 41,
    isOld: true,
    newArr: [{ firstName: "Devlin"}]
}

console.log(newObj2.secondName)
console.log(newObj2[1])

const arrTest = {
    1: "test",
    2: 34,
    3: true
}

newObj2.secondName = "Devlin";
const text = "text";
newObj2["text"] = newObj2.firstName + "add more text";
console.log(newObj2);
delete newObj2.firstName;
console.log(newObj2.newArr[0].firstName);


const myObject = { a: 1, b: 2 };
for (const key in myObject) {
    if (myObject.hasOwnProperty(key)) {
        console.log(key, myObject[key]);
    }
}
console.log(Object.keys(myObject))
console.log(Object.values(myObject))
console.log(Object.entries(myObject))

const profile = {
    firstName: "Devlin",
    sirName: "Booth",
    age: 41,
    isOld: true,
    fullName: "no",
    createFullName() {
        return `${profile.firstName} ${profile.sirName}`
    },
    myBirthday() {
        this.age += 1;
    },
    get fullName() {
        return `${this.firstName} ${this.sirName}`;
    },
    set fullName(test) {
        return `${this.firstName} ${this.sirName}`;
    },
    // set fullName(test) {
    //     this.fullName = test;
    // },
}

console.log(profile.createFullName())
profile.myBirthday()
console.log(profile.fullName)
profile.fullName = "changing the name"
console.log(profile.fullName);

// - EXERCISE
// • build an object that can:
// •• Add a `name` property with your own name as a string.  
// •• Add an `age` property with a number.  
// •• Add a `grades` property with an array of numbers (at least 3 values).  
// •• Print the student’s name.  
// •• Print the student’s first grade from the array.  
// •• Increase the student’s age by 1.  
// •• Add a new grade to the `grades` array.  
// •• Add a method called `getAverage` that returns the average of the student’s grades.  			•• Call the method and print the result.  
// •• Add a property `isPassing` that is `true` if the student’s average grade is **10 or higher**
