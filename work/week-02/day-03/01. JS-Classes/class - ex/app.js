
// Object
class Profile {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  fullName() {
    return this.firstName + " " + this.lastName;
  }
}
const myName = new Profile ("maha" , "alghuraibi");
console.log(myName.fullName());

