// 3
function sumNumbers(numbers) {
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

// 4
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

