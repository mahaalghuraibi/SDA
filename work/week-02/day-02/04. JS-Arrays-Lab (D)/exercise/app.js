// مصفوفة فاضية
const foods = [];
console.log('Exercise 1 result:', foods);

//  أضيفي pizza و cheeseburger
foods.push('pizza');
foods.push('cheeseburger');
console.log('Exercise 2 result:', foods);

//  أضيفي taco في البداية
foods.unshift('taco');
console.log('Exercise 3 result:', foods);

//تخزين "pizza" في متغير favFood
const favFood = foods[1];
console.log('Exercise 4 result:', favFood);

//إدخال "tofu" بين "pizza" و "cheeseburger"
foods.splice(2, 0, 'tofu');
console.log('Exercise 5 result:', foods);

//استبدال "pizza" بـ "sushi" و "cupcake"
foods.splice(1, 1, 'sushi', 'cupcake')
console.log('Exercise 6 result:', foods);

//(استخدام slice() لإنشاء مصفوفة جديدة فيها 'sushi' و 'cupcake'
const yummy = foods.slice(0, 2)
console.log('Exercise 7 result:', yummy);

//البحث عن مكان "tofu" باستخدام indexOf
const soyIdx = foods.indexOf('tofu');
console.log('Exercise 8 result:', soyIdx);

//join()
const allFoods = foods.join("->")
console.log('Exercise 9 result:', allFoods);

// التحقق من وجود عناصر
const hasSoup = foods.includes("soup");
console.log('Exercise 10 result:', hasSoup);

// مصفوفة جديدة 
const nums = [100, 5, 23, 15, 21, 72, 9, 45, 66, 7, 81, 90];
const odds = [];
for (let n of nums) {
    if (n % 2 !== 0) {
        odds.push(n);
    }
}

console.log('Exercise 11 result:', odds);

// اضافة مصفوفات + وقسمة
const fizz = [];
const buzz = [];
const fizzbuzz = [];

for (let n of nums) {
    if (n % 3 === 0) {
        fizz.push(n);
    }
    if (n % 5 === 0) {
        buzz.push(n);
    }
    if (n % 3 === 0 && n % 5 === 0) {
        fizzbuzz.push(n);
    }
}

console.log('Exercise 12 Results:');
console.log('  fizz:', fizz);
console.log('  buzz:', buzz);
console.log('  fizzbuzz:', fizzbuzz);

// اخزن اخر مصفوفة في متغير جديد 
const numArrays = [
  [100, 5, 23],
  [15, 21, 72, 9],
  [45, 66],
  [7, 81, 90]
];

const numList = numArrays[numArrays.length - 1];

console.log('Exercise 13 result:', numList);

// نجيب رقم ٦٦ من المصفوفه

const num = numArrays [2][1];
console.log('Exercise 14 result:', num);

let total = 0;
for (let row of numArrays) {
  for (let n of row) {
    total += n;  
  }
}

console.log('Exercise 15 result:\n', total);
