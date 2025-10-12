

console.log ("my test")

const flavors = ['vanilla', 'chocolate', 'strawberry'];

const iceCreamFlavors = flavors.map((flavor) => {
  return `${flavor} ice cream`;
});

console.log(iceCreamFlavors); 



const nums = [13, 87, 2, 89, 12, 4, 90, 63];

const numsTimesTwo = nums.map((ele, idx) => {
  return ele * 2;
});

console.log(numsTimesTwo);


const person = {
  name: 'Maha',
  role: 'Software Engineer',
  address: {
    street: 'Taif',
    number: 123
  }
};

console.log(`Name: ${person.name}, Role: ${person.role}, Street: ${person.address.street}, Number: ${person.address.number}`);


console.log (FirsName)