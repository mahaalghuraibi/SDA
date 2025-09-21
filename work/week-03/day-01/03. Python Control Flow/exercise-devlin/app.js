console.log(Boolean([]));

const test = null;
if (!test) console.log("test is working");

const res = test ? "this is true" : "this is false";
console.log(res)

for (let i = 0; i < 10; i++) {
    console.log(i)
}

for (let i = 10; i > 0; i--) {
    console.log(i)
}