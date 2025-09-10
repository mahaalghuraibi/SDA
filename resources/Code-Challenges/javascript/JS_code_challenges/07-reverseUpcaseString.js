/*-----------------------------------------------------------------
Challenge: 07-reverseUpcaseString
Difficulty: Basic
Prompt:
- Write a function called reverseUpcaseString that accepts a single string argument, then returns the string with its characters in reverse order and converts all characters to uppercase.
Examples:
reverseUpcaseString("SEI Rocks!"); //=> "!SKCOR IES"
-----------------------------------------------------------------*/
// Your solution for 07-reverseUpcaseString here:

export function reverseUpcaseString(string) {
  let arr = string.split("");   
  arr = arr.reverse();          

  let reversed = arr.join("");
  let result = reversed.toUpperCase();

  return result;
}
console.log(reverseUpcaseString("SEI Rocks!"));
