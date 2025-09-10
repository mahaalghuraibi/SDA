// Array
Array.isArray()
const newArr = new Array();
// Object

class Car {
    // name = "name";
    // id = 0

    constructor(make, model, color) {
        this.make = make;
        this.model = model;
        this.color = color;
        this.isRunning = false;
    }

    start() {
        this.isRunning = true;
        console.log("The car started!!")
    }

    static about() {
        console.log("I am the car class!")
    }
}

const myCar = new Car("Ford", "Bronco", "Red");
console.log(Car, myCar)
console.log(typeof myCar)
// myCar.runCar()
myCar.start()

// Create a 'Profile' class that accepts two 
// parameters called "firstName" and "lastName"
// create an instance method called "fullName"
// that will return the 
// full name: this.firstName + this.lastname

class Profile {
    constructor(name1, name2) {
        this.firstName = name1;
        this.lastName = name2
    }
    fullName() {
        console.log(this.firstName + this.lastName, "line 38")
        return `${this.firstName} ${this.lastName}`
    }
}

const devlin = new Profile("Devlin", "Booth");
const fullName = devlin.fullName();
console.log(fullName, "line 45")
Car.about();

class ElectricCar extends Car {
    constructor(make, model, color, batteryCharge) {
        super(make, model, color);
        this.batteryCharge = batteryCharge;
    }

    start() {
        if (this.batteryCharge > 0) {
            this.isRunning = true;
            console.log('Your electric car is running!');
        } else {
            this.isRunning = false;
            console.log('Time to recharge!');
        };
    }
}

const elecCar = new ElectricCar("Tesla", "Model Y", "Electric Blue", 100)
console.log(ElectricCar, elecCar)
elecCar.start()

let randomNumber = Math.random()
console.log(randomNumber)