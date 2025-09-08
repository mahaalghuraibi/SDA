const student = {
  name : "maha",
  age : 25,
  grades: [20, 90, 100],

  getAverage: function () {
    let sum = 0;
    for (let i = 0; i < this.grades.length; i++) {
      sum = sum + this.grades[i];
    }
    let average = sum / this.grades.length;
    return average;
  },

  isPassing: function() {
    return this.getAverage() >= 10;
  }
};

console.log(student.name);        
console.log(student.grades[0]);   

student.age = student.age + 1;    
console.log(student.age);         

student.grades.push(100);         
console.log(student.grades);      

console.log(student.getAverage()); 
console.log(student.isPassing());  









