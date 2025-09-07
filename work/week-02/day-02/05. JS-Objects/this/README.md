<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead"><code>this</code></span>
</h1>

**Learning objective:** By the end of this lesson, learners will be able to understand the basic concept of `this` in JavaScript and how it can be used within object methods.

## What is `this`?

In JavaScript, `this` is a special keyword that refers to the object that is currently executing the code. When you use `this` inside a method, it allows you to access other properties and methods of the same object.

## Why use `this`?

Using `this` can make your code more flexible and easier to maintain. It helps avoid hardcoding the object name inside its methods, which can be especially useful when you have multiple similar objects or if the object's name changes.

### Example: Using `this` in methods

Let's revisit the `music` object example and see how we can use `this` to make it more dynamic.

#### Without `this`

```javascript
const music = {
  currentTrack: 'Just Ken',
  trackIdx: 0,
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70,
  mute() {
    music.volume = 0; // we must reference the object by name
  },
  next() {
    music.trackIdx += 1; // we must reference the object by name
  },
};

// Calling methods
music.mute();
console.log(music.volume);  // Output: 0

music.next();
console.log(music.currentPlaylist[music.trackIdx]);  // Output: 'Hey Blondie'
```

#### With `this`

Now, let's update the `music` object to use `this` inside its methods:

```javascript
const music = {
  currentTrack: 'Just Ken',
  trackIdx: 0,
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70,
  mute() {
    this.volume = 0;  // 'this' is referring to the music obj
  },
  next() {
    this.trackIdx += 1; 
    this.currentTrack = this.currentPlaylist[this.trackIdx];
  },
};

// Calling methods
music.mute();
console.log(music.volume);  // Output: 0

music.next();
console.log(music.currentTrack);  // Output: 'Hey Blondie'
```

What is happening:

  - Inside the `mute` method, `this.volume` refers to the `volume` property of the `music` object. Similarly, inside the `next` method, `this.trackIdx` and `this.currentTrack` refer to the properties of the `music` object.

  - Using `this`, the methods can dynamically access and update the properties of the object they belong to, making the code more flexible.

By using `this`, we avoid hardcoding the object name within its methods, making the code easier to maintain and reuse. As you continue learning about JavaScript, understanding `this` will be essential, especially when you start working with classes and more complex objects.

## 🎓 You Do: Update your music object to use `this`

Update the `music` object to use `this` in all its methods. Try adding a new method that uses `this` to interact with the object's properties and see how it works. For example, create a method called `previous` that moves to the previous track in the playlist.
