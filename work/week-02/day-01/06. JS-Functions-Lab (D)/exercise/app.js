// 1 
// Definition of contracts
const name = "maha"
const age = 25 ;

console.log("name")
console.log("age")
//*************************************
// 2
// for 
//Print numbers from 0 to 4
const num = [ 1 , 2 , 3 , 4 ]
for ( let i = 0 ; i <5 ; i++ ){
console.log(i);
}
for (let i = 4; i >= 0; i--) {
  console.log(i);
}


// ex Coal on array elements
const student = ['maha' , 'amwaj' , 'fay']
for (let i=0 ; i< student.length ; i++ ){
    console.log(i)
    console.log(student[i]);
}
for (const name of student){
    console.log(name)
}

//break , continue
for(let i=0 ; i<10 ; i++ )
{
    if( i === 5) break
    console.log (i);
}
for(let i=0 ; i<20 ; i++ ){
    if ( i === 15 )continue;
    console.log(i);
}

//*************************************
//3
//Loops
//while loop
let i=0 ;
while (i < 5){
    console.log(i);
    i++;
}
// do...while loop:
let j=0;
do {
    console.log(j);
    j++;
} while (j < 5);

//*************************************
//4
//Conditions
const grade = 90;
if(grade >= 90){
    console.log("A");
} else if (grade >= 80){
    console.log("B")
}else {
    console.log('C or less')
}

//*************************************
//5
//Functions
function greet (name){
console.log(`Hello ${name}`);
}

greet('maha')

//*************************************
//6 
//Objects
const student1 = {
  name: "maha",
  age: 25
};
console.log(student1.name);
console.log(student1.age);


//*************************************
//7
// array
const numbers1 = [1 , 2 , 3 , 4 , 5]
console.log(numbers1.includes(19));
console.log(numbers1.join("-"));
console.log(numbers1.map( n => n +2 ));
console.log(numbers1.push(6));
console.log(numbers1);
console.log(numbers1.pop());
console.log(numbers1);
console.log(numbers1.shift());
console.log(numbers1);
console.log(numbers1.unshift(0));  
console.log(numbers1);
console.log(numbers1.filter(n => n > 2));
console.log(numbers1);
console.log(numbers1.reduce((sum, n) => sum + n, 0));
console.log(numbers1);




