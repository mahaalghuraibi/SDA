<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Fundamentals</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to apply the basics of object creation, access, and assignment.

## Object literal notation

Let’s create an object by using **Object Literal** notation, also known as an [Object Initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer):

```javascript
const music = {};
console.log(typeof music); // 'object'
```

As you can see, Object Literal notation consists of a set of opening and closing curly braces, `{}`. We just used curly braces to create an empty `music` object.

Let’s change the code so that `music` has a property:

```javascript
const music = { currentTrack: 'Just Ken' };
console.log(music);
```

Properties are separated by commas:

```javascript
const music = {
  currentTrack: 'Just Ken',
  volume: 70
};
```

Syntactically, [trailing commas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Trailing_commas) are permitted and encouraged:

```javascript
const music = {
  currentTrack: 'Just Ken',
  volume: 70, // <-----
};
```

Why? Check out [this commit](https://github.com/DavidStinson/objects-are-a-thing/commit/b1bb58d364975e3dbed12f4c9726720ded2a3cfd) for a look into how this looks to version control software when modified. It’s also just less work later!

## Dot notation

The primary way to access, add, or modify an existing object’s properties is __dot notation__. 

Let’s use dot notation to add another property to the music object:

```javascript
music.currentPlaylist = ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'];
```

We can then access the value using the same dot notation syntax:
```javascript
console.log(music.currentPlaylist)  // ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'] 
```

## 🎓 You Do 

Using dot notation: 

- Whats playing? Can you print the property `currentTrack` to the console? 
