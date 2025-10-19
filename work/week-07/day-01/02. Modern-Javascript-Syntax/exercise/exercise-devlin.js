import returnFirstName, { firstName, testFunc } from "./export-devlin.js";

const flavors = ['vanilla', 'chocolate', 'strawberry'];
console.log(flavors)

const iceCreamFlavors = flavors.map((flavor) => {
  return `${flavor} ice cream`;
});

console.log(iceCreamFlavors); 
// Prints: ['vanilla ice cream', 'chocolate ice cream', 'strawberry ice cream']

const nums = [13, 87, 2, 89, 12, 4, 90, 63];

const numsTimesTwo = nums.map((ele, idx) => {
    return ele *= 2
})

console.log(numsTimesTwo)
const num1 = nums[0]
const num2 = nums[1]
const num3 = nums[2]

const [one, two, three, ...rest] = nums
console.log(one, two, three, rest)

const [flavor1, , flavor3] = flavors
console.log(flavor1, flavor3)

const person = {
  name: 'Alex',
  role: 'Software Engineer',
  address: {
    street: "broadway",
    number: 123,
  }
};

const personName = person.name // person["name"]
const personRole = person.role // person["role"]

const { name, role, address: { number } } = person
console.log(name, role, number)


const newArray = nums.map(ele => ele)

const newNums = [...nums]

// const newPerson = { ...person }
const newPerson = { ...person, address: { ...person.address }}
newPerson.address.number = 38746587364587

console.log(person, newPerson)

console.log([...nums, ...flavors])
// console.log([...nums, ...person]) => cannot spread object into array!


console.log(firstName, "line 60")
testFunc("React Rocks")

const thisValue = nums.length > 3 ? true : false

const newItem = true && person.name

console.log(newItem)

const newItem2 = 0 || 0
console.log(newItem2)

console.log(person.address.street.test)

const adventurer = {
  name: 'Alice',
};

console.log(adventurer.dog?.name); 
// TypeError: Cannot read properties of undefined (reading 'name')