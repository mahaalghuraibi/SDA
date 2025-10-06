/*-----------------------------------------------------------------
Challenge: 21-primeFactors
Difficulty: Intermediate
Prompt:
Now that you have solved the last challenge of determining if a whole number is prime, let's expand upon that concept to...
- Write a function named primeFactors that accepts a whole number greater than one (1) as an argument and returns an array of that argument's prime factors.
- The prime factors of a whole number are the prime numbers that, when multiplied together, equals the whole number.
- If the argument provided is not greater than 1, or not a whole number, then primeFactors should return an empty array.
Examples:
primeFactors(2) //=> [2]
primeFactors(3) //=> [3]
primeFactors(4) //=> [2, 2]
primeFactors(18) //=> [2, 3, 3]
primeFactors(29) //=> [29]
primeFactors(105) //=> [3, 5, 7]
primeFactors(200) //=> [2, 2, 2, 5, 5]
Hint: Code a nested isPrime(n) helper function that returns true if n is prime, otherwise it returns false
-----------------------------------------------------------------*/
// Your solution for 21-primeFactors here:

export function primeFactors(num) {
  if (!Number.isInteger(num) || num <= 1) {
    return [];
  }

  let factors = [];   
  let divisor = 2;   

  while (num > 1) {
    if (num % divisor === 0) {
      factors.push(divisor); 
      num = num / divisor;  
    } else {
      divisor++; 
    }
  }

  return factors;
}

console.log(primeFactors(2));   
console.log(primeFactors(3));   
console.log(primeFactors(4));    
console.log(primeFactors(18));   
console.log(primeFactors(29));  
console.log(primeFactors(105));   
console.log(primeFactors(200));  
