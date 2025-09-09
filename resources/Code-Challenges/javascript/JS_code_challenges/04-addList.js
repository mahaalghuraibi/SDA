/*-----------------------------------------------------------------
Challenge: 04-addList
Difficulty: Basic
Prompt:
- Write a function called addList that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
- Assume all parameters will be numbers.
- If called with no arguments, return 0 (zero).
Examples:
add(1) //=> 1
add(1, 50, 1.23) //=> 52.23
add(7, -12) //=> -5
Hint:  Check out the Further Study section of the JS Functions lesson regarding "rest parameters"
-----------------------------------------------------------------*/
// Your solution for 04-addList here:


export function addList(...numbers) {
  // مجموع الصفر كبداية
  let sum = 0;

  // المرور على كل رقم من الأرقام المدخلة
  for (let i = 0; i < numbers.length; i++) {
    // نضيف الرقم الحالي للمجموع
    sum = sum + numbers[i];
  }

  // نرجع المجموع (إذا ما فيه أرقام يرجع 0)
  return sum;
}
console.log(addList(1));            
console.log(addList(1, 50, 1.23));  
console.log(addList(7, -12));       
console.log(addList());             
