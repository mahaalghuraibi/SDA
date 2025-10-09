/*-----------------------------------------------------------------
Challenge: 25-getNumForIP
Difficulty:  Intermediate
Prompt:
- Write a function called getNumForIP that accepts a single string as argument.
- The input string is formatted as an IP address, such as '192.156.99.15'.  IP addresses are used in networking and are actually 32-bit integers.  However, those that work with networks find it more convenient to work with these numbers as four 8-bit integers, separated by a 'dot' character.
- The getNumForIP function should return the numeric value of the string IP address being passed in as an argument.
Hints:
- Each 8-bit number can hold a value between 0 and 256.
- An IP's right most 8-bit number represents how many of 256 raised to the power of 0 (equals 1) there are.  The next 8-bit number represents how many of 256 raised to the power of 1 (256) there are, etc.  For example, if you took the right-most two 8-bit numbers of the IP address 192.156.99.15, you would have 15 * (256 ** 0), which equals 15, and 99 * (256**1), which equals 25344.
- To compute the numeric value for an IP address, you first compute the value for each of the four 8-bit chunks (as described in the above hint), and add them together!
Examples:
getNumForIP( '0.0.0.1' ) // => 1
getNumForIP( '0.0.2.0' ) // => 512
getNumForIP( '192.156.99.15' ) // => 3231474447
getNumForIP( '10.0.0.1' ) // => 167772161
-----------------------------------------------------------------*/
// Your solution for 25-getNumForIP here:

export function getNumForIP(ip) {
  let parts = ip.split('.') 
  let total = 0

  for (let i = 0; i < parts.length; i++) {
    let num = Number(parts[i])
    total += num * (256 ** (3 - i))
  }

  return total
}

console.log(getNumForIP('0.0.0.1'))       
console.log(getNumForIP('0.0.2.0'))       
console.log(getNumForIP('192.156.99.15')) 
console.log(getNumForIP('10.0.0.1'))     
