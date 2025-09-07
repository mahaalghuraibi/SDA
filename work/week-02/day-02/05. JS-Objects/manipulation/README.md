<h1>
  <span class="headline">Intro to JavaScript Objects</span>
  <span class="subhead">Manipulation</span>
</h1>

**Learning objective:** By the end of this lesson, students will be able to manipulate objects, by changing and deleting properties.

## Changing an object's properties

To update a property in a JavaScript object, you assign a new value to one of its keys (which is like a label or name for that property):

```javascript
const music = {
  currentTrack: 'Just Ken',
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70, 
}

// Let's lower the volume: 
music.volume = 60;

console.log(music.volume) // 60
```

When using the assignment operator, if a property doesn’t exist, it is created; otherwise, it’s updated. In this example, `volume` already exists as a property on `music` so this line of code updates the value.


## Deleting an object's properties

To completely remove a property from an object, we use the delete operator:

```javascript
const music = {
  currentTrack: 'Just Ken',
  currentPlaylist: ['Just Ken', 'Hey Blondie', 'What Was I Made For', 'Dance The Night'],
  volume: 70, 
}

// Let's remove our current playlist: 
delete music.currentPlaylist

console.log(music)
// { currentTrack: 'Just Ken', volume: 70 }
```

## 🎓 You Do 

Let's add and remove a new playlist:

- Create a new playlist array called `myPlaylist` on your music object. Make sure to include a couple of your favorite songs in there. 

- Practice printing `myPlaylist` to the console. 

- Delete `myPlaylist` using the `delete` keyword. 

- Print the `music` object to the console to verify `myPlaylist` has been deleted. 
