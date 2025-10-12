/*-----------------------------------------------------------------
Challenge: 26-toCamelCase
Difficulty:  Intermediate
Prompt:
- Write a function called toCamelCase that accepts a single string as argument.
- The toCamelCase function should return the string as camel-cased, removing each _ or - characters and capitalizing the character following the _ or -.
Hints:
- This is a great challenge for using regular expressions combined with the String.replace method.
Examples:
toCamelCase( 'wdi-rocks' ) // => 'wdiRocks'
toCamelCase( 'banana_Turkey_potato' ) // => 'bananaTurkeyPotato'
toCamelCase( 'Mama-mia' ) // => 'MamaMia'
toCamelCase( 'A_b_c' ) // => 'ABC'
-----------------------------------------------------------------*/
// Your solution for 26-toCamelCase here:

export function toCamelCase(str) {
  let result = ''
  for (let i = 0; i < str.length; i++) {
    if (str[i] === '-' || str[i] === '_') {
      result += str[i + 1].toUpperCase()
      i++
    } else {
      result += str[i]
    }
  }
  return result
}

console.log(toCamelCase('wdi-rocks'))
console.log(toCamelCase('banana_Turkey_potato'))
console.log(toCamelCase('Mama-mia'))
console.log(toCamelCase('A_b_c'))

