/*-----------------------------------------------------------------
Challenge: 11-isPalindrome
Difficulty: Intermediate
Prompt:
- Write a function called isPalindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
- A palindrome is a word or phrase that are the same forward or backward.
- Casing and spaces are not included when considering whether or not a string is a palindrome.
- If the length of the string is 0 or 1, return true.
Examples:
isPalindrome('SEI Rocks'); //=> false
isPalindrome('rotor'); //=> true
isPalindrome('A nut for a jar of tuna'); //=> true
isPalindrome(''); //=> true
-----------------------------------------------------------------*/
// Your solution for 11-isPalindrome here:

// -----------------------------------------------------------------
// Challenge: 11-isPalindrome
// -----------------------------------------------------------------

export function isPalindrome(str) {
  let cleaned = str.toLowerCase();

  cleaned = cleaned.replace(/\s+/g, "");

  if (cleaned.length <= 1) {
    return true;
  }

  let reversed = cleaned.split("").reverse().join("");

  return cleaned === reversed;
}

console.log(isPalindrome("SEI Rocks"));          
console.log(isPalindrome("rotor"));             
console.log(isPalindrome("A nut for a jar of tuna")); 
console.log(isPalindrome(""));                  
