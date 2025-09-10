// NEW ARRAY
const newArr1 = new Array();
const newArr = [];
const nums = [1, 2, 3, 4, 5];
const movies = ['Avatar', "Formula1", "Black Swan"];
const booleans = [true, false];
const mixed = [1, "2", true] // mix primitive
const mixed2 = [1, "red", function test() { console.log("test")}];

console.log(nums[0])
console.log(["read", "test", "write"][0])

function getItems() { return [1, 2, 3, 4] }
console.log(getItems()[1]);

console.log(nums.length)
console.log("test".concat("-test2"))

console.log(Array.isArray(nums))

for (let i = 0; i < nums.length; i++) {
    console.log(nums[i])
    break;
}

nums.forEach(function(num) {
    console.log(num, "line 26")
})

for (const item of nums) {
    console.log(item, "line 31")
}

for (const item of "testing") {
    console.log(item, "line 35")
}

const newStr = movies.join(" - \n")
console.log(newStr)

console.log(movies, "line 41");
const newSetOfMovies = movies;
console.log(newSetOfMovies, "line 43");
movies[0] = "Avatar: Fire and Ice";
newSetOfMovies[2] = "Back To The Future";
movies[10] = "Sound of Music";
const lastItem = movies.pop();
movies.push("Sounds of Music")
movies.shift()
console.log(lastItem)
console.log(movies, "line 46");
console.log(newSetOfMovies, "line 47");
movies.unshift("Avatar")
console.log(movies, "line 46");
console.log(newSetOfMovies, "line 47");
console.log(movies[8])

const nestedArr = [
    [0, 12, 23, 34, 45, 56],
    [0, 12, [true], 34, 45, 56],
    [0, 12, "test", 34, 45, 56],
    [0, 12, 23, "whatever", 45, 56],
];

console.log(nestedArr[1][2][0])

nestedArr.forEach(function(arr) {
    for (const el of arr) {
        console.log(el)
    }
})

const newNums3 = [...nums];
const nestedCopy = [...nestedArr]
const newArr4 = nums.map(function(ele, ind) {
    return ele * ind;
});
console.log(newArr4, "line 78")

