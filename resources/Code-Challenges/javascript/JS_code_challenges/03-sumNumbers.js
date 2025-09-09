/*-----------------------------------------------------------------
Challenge: 03-sumNumbers
Difficulty: Basic
Prompt:
- Write a function called sumNumbers that accepts a single array of numbers and returns the sum of the numbers in the array.
- If the array is empty, return 0 (zero).
Examples:
sumNumbers([10]) //=> 10
sumNumbers([5, 10]) //=> 15
sumNumbers([2, 10, -5]) //=> 7
sumNumbers([]) //=> 0
-----------------------------------------------------------------*/
// Your solution for 03-sumNumbers here:

export function sumNumbers(numbers) {
    // مجموع الصفر
    let sum = 0;
    
    // المرور على كل عنصر 
    for (let i = 0; i < numbers.length; i++) {
        // كل الارقام نضضيف sum
        sum = sum + numbers[i];
    }
    
    // نرجع المجموع
    return sum;
}
console.log(sumNumbers([10]));        
console.log(sumNumbers([5, 10]));    
console.log(sumNumbers([2, 10, -5])); 
console.log(sumNumbers([]));          
