<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">How Variables Reference Objects</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to explain how variables reference objects in JavaScript, distinguish between primitive and reference types, and understand the difference when comparing objects and arrays.

As you know, variables are slots in memory that hold a value. All non-object data types are known as primitive or value types because they hold a single value. Picture a table in memory like this:

```markdown
SCOPE TABLE            var | value/ref
                      -----------------
let x = 25        -->   x  |  25
var msg = 'hello' -->  msg | 'hello'
const y = x       -->   y  |  25
```

But objects are complex/reference types because they can hold multiple pieces of data…

Objects, including Arrays, Functions, etc., are stored in a separate part of memory known as the *heap*. A variable for an object has as its value a “reference” (think pointer):

```markdown
SCOPE TABLE             var | value/ref
                       -----------------
let x = 25         -->   x  |  25
var msg = 'hello'  -->  msg | 'hello'        HEAP 
const obj = {a: 1} -->  obj |  ref1   --->  {a: 1} <--|
let arr = [1,2]    -->  arr |  ref2   --->  [1,2]     |
let obj2 = obj     -->  obj2|  ref1   -----------------
```

Similarly, the elements of an array and the properties of an object hold their values in the same way.

Now this makes sense:

```javascript
const arr1 = []
const arr2 = []
const arr3 = arr1
arr1 === arr2  // false!
arr3 === arr1 // true!
```