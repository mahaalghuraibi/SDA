<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Data Structures</span>
</h1>

**Learning objective:** By the end of this lesson, students will understand how objects and arrays combine to form common data structures in JavaScript.

For reference, here is our current `music` object: 

```javascript
const music = {
  currentTrack: 'Just Ken',
  trackIdx: 0,
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70,
  mute(){
    music.volume = 0
  },
  next(){
    music.trackIdx += 1
    music.currentTrack = music.currentPlaylist[music.trackIdx]
  },
}
```

## Using objects and arrays together

Objects and arrays each have their specialty as a type of data storage: 

**Objects for Grouping Data**: Objects, like our `music` object, are great for grouping *related* data. They store data in key-value pairs.

**Arrays for Ordered Data**: Arrays are used to store multiple items in an *ordered* manner. Our `currentPlaylist` is an array inside the music object. 

As a result, data is often structured using a combination of both! 

Let's examine our current `music.currentPlaylist`: 

```javascript
['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night']
```

In a real world application, each song would likely have more associated data - an artist, album, song length, etc. This is a great use case for an object, something like: 

```javascript
{ 
  title: 'Just Ken',
  artist: 'Ryan Gosling',
  album: 'Barbie The Album',
  length: '3:43',
};
```

If we adopted that structure for each song, then our `currentPlaylist` array would resemble something like this, an array of objects: 

```javascript
music.currentPlaylist = [
  {
    title: 'Just Ken',
    artist: 'Ryan Gosling',
    album: 'Barbie The Album',
    length: '3:43',
  }, {
    title: 'Hey Blondie',
    artist: 'Dominic Fike',
    album: 'Barbie The Album',
    length: '2:21',
  }, {
    title: 'What Was I Made For',
    artist: 'Billie Eilish',
    album: 'Barbie The Album',
    length: '3:42',
  }, {
    title: 'Dance The Night',
    artist: 'Dua Lipa',
    album: 'Barbie The Album',
    length: '2:56',
  }
];
```

We can still access each element the same way as before, but now they are objects rather than strings: 

```javascript
console.log(music.currentPlaylist[music.trackIdx]);

// { title: 'Just Ken', artist: 'Ryan Gosling', album: 'Barbie The Album',length: '3:43' }
```

That means we can now use dot notation to return specific properties on that element! 

```javascript
console.log(music.currentPlaylist[music.trackIdx].title); // 'Just Ken'
console.log(music.currentPlaylist[music.trackIdx].artist); // 'Ryan Gosling'
```

## 🎓 You Do 

Using dot notation, practice updating a value from one of the objects in the new `currentPlaylist` array. 

Can you change the track length for the song `'What was I Made For'`?

```JS
{
  title: 'What Was I Made For',
  artist: 'Billie Eilish',
  album: 'Barbie The Album',
  length: '3:42', // <----  lets update this to 3:54
}
```

> Think about the structure of the data as you attempt to access each level:
>>  `music object > playlist array > song object`
