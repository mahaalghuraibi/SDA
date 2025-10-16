/*-----------------------------------------------------------------
Challenge: 29-addChecker
Difficulty:  Intermediate
Prompt:
- Write a function called addChecker that accepts two arguments.
- The first argument is an array containing at least two integers.  The integers in the array are sorted in ascending order.
- The second argument is an integer.
- The addChecker function should return true if there are two integers in the array of integers (first argument) that when added together, equals the integer passed in as the second argument.
- If there are no two integers in the array that sum up to equal the second argument, addChecker should return false.
Hint:
- An efficient solution can leverage the the fact that the integers in the array are sorted.
Examples:
addChecker( [1, 2], 3 ) // => true
addChecker( [-3, 2], 9 ) // => false
addChecker( [10, 15, 16, 22], 32 ) // => true
addChecker( [10, 15, 16, 22], 19 ) // => false
-----------------------------------------------------------------*/
// Your solution for 29-addChecker here:

export function addChecker(arr, num) {
  let left = 0
  let right = arr.length - 1

  while (left < right) {
    let sum = arr[left] + arr[right]
    if (sum === num) return true
    if (sum < num) left++
    else right--
  }
  return false
}

console.log(addChecker([1, 2], 3))      
console.log(addChecker([-3, 2], 9))      
console.log(addChecker([10, 15, 16, 22], 32)) 
console.log(addChecker([10, 15, 16, 22], 19)) 
