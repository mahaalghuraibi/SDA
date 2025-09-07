<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Methods</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to create and call methods from objects.

In JavaScript, a _method_ is a function that is a property of an object. When a property holds a function, we commonly refer to it as a method _of_ the object.

Methods are used to define actions or behaviors for an object. They provide a way to interact with the object or to get information about the object.

They can be defined when initializing an object:

```javascript
const music = {
  currentTrack: 'Just Ken',
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70,
  // add the following:
  mute() {
    music.volume = 0;
  },
};
```

You could also use dot notation assignment to define the same method if an object already exists:

```javascript
music.mute = function () {
  music.volume = 0;
};
```

> Why not an arrow function here? Arrow functions are great, but they work a bit differently than regular functions under the hood, especially when dealing with objects. Regular functions are designed to work smoothly with objects when you define methods that need to interact with the object itself.

## Calling object methods

In JavaScript, calling (or invoking) a method is similar to calling a function, but with an important difference: a method is called on an object and it only exists within that object's context.

```javascript
music.mute();
// works!
```

When a function is part of an object (a method), you need to specify the object it belongs to.

```javascript
mute();
// reference error
```

If you try to call a method without referencing its parent object, JavaScript will not know where to find it, leading to a reference error.

> 💡 At this point, you've likely already used methods with arrays and strings in JavaScript - when we use things like `.push()` or `.slice()`, we're invoking an array **method**. If we call `'my-string'.split()`, we're invoking a string **method**. These are built-in methods that provide specific functionalities to array and string objects in JavaScript

If you have been wondering why we use dot notation when we use these methods, now you know!

## Adding a `next()` method to the `music` object

Let’s enhance the `music` object by adding a `next()` method. This method will allow us to move to the next track in our `currentPlaylist`.

One problem - how do we do that? Initially, our object has `currentTrack` and `currentPlaylist` properties, but there's no straightforward way to track our position in the playlist.

To improve this, we'll make a small change. Instead of storing `currentTrack` as a string, we can use an **array index** to keep track of the current song. Let's create a new property called `trackIdx` to store the index of the current track:

```javascript
const music = {
  currentTrack: 'Just Ken',
  trackIdx: 0,
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70,
};
```

With `trackIdx`, we can dynamically find the current track from `currentPlaylist` array using square brackets `[]`:

```javascript
console.log(music.currentPlaylist[music.trackIdx]); // 'Just Ken'
```

Now we can build our `next()` method. This method should simply increment the `trackIdx` by `1`!

```javascript
music.next = function () {
  music.trackIdx += 1;
};
```

```javascript
// invoke the method
music.next();

console.log(music.currentPlaylist[music.trackIdx]); // 'Hey Blondie'
```

## 🎓 You Do

Let's look at our `music` object so far:

```javascript
const music = {
  currentTrack: 'Just Ken',
  trackIdx: 0,
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70,
  mute() {
    music.volume = 0;
  },
  next() {
    music.trackIdx += 1;
  },
};
```

But wait, what about `currentTrack`? Currently, it's just a hard coded string- meaning it wont get updated when we call our `next()` method. How can we change this so that our `currentTrack` property stays up to date?

How could we use other properties in our object to dynamically set the value of `currentTrack`?
