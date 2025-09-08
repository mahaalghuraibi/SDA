// NEW ARRAY
const newArr1 = new Array();
const newArr = [];

const nums = [1, 2, 3, 4, 5];
const movies = ['Avatar', 'Formula1', 'Black Swan'];
const booleans = [true, false];
const mixed = [1, "2", true];
const mixed2 = [1, "red", function test() { console.log("test"); }];
console.log(nums[0])
console.log(["red", "test", "white"][0])
function getItems() { return [1, 2, 3, 4] }
console.log(getItems()[1])
console.log(nums.length)
console.log("test".concat("-test2"))
console.log(typeof nums)
console.log(Array.isArray(nums))
for (let i = 0; i < 10; i++) {
    console.log(nums[i])
}

nums.forEach(function (num) {
    console.log(num, 'line 26')
})

for(const item of "testing") {
    console.log(item, "line 35")
}
const newstr = movies.join("-\n");
console.log(newstr)

console.log(movies, "line 41");
const newsetofmovies = movies;
 console.log(newsetofmovies, "line 43");
 newsetofmovies[2] = "back to the future";
movies[3] = "sound of music"
const lastItem = movies.pop();
movies.push = "sound of music"
movies.shift()

 console.log("movies , line 46");
 console.log(newsetofmovies, "line 47");
 console.log(movies [8])

 const nested