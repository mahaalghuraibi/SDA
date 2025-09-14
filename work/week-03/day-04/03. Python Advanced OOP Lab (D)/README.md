<div style=" display:flex; align-items:center;">

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) <h1>Python Advanced OOP Lab</h1>

</div>



Let's explore _inheritance_ in Python classes by creating a whole farm full of `Animal`s. Create a new file in this
repository called `animals.py` and follow the directions below.

## The `Animal` parent class

First, we'll set up a parent class for _all_ animals. Here's some starter code:

```python
class Animal:
    pass
```

Set up some characteristics that all `Animal`s will have by creating an `__init__` method to establish the following
instance variables:

* `name`
* `color`
* `stuff_in_belly` (default = [])
* `position` (default = 0)

Test your class by creating a new variable called `sparky` that will be an instance of the `Animal` class, then make
sure you can access `sparky`'s attributes:

```python
sparky = Animal('Sparky', 'brown', ["dog food", "McDonald's wrapper"])
print(sparky.stuff_in_belly)
print(sparky.name)
```

Animals don't just sit there, right? Give your class some methods:

* `talk(sound=None)` : If a sound is specified, print "{ animal's name } says { sound }". If no sound is specified,
  print "{ animal's name } has nothing to say right now.".
* `walk(walk_increment)` : Change the `Animal`'s position by the `walk_increment`, then print "{ animal's name } walked
  { walk_increment } steps and is now at position { animal's position }."
* `run(run_increment)` : Change the `Animal`'s position by the `run_increment`, then print "{ animal's name } ran {
  run_increment } steps and is now at position { animal's position }!"
* `is_hungry()` : Returns `True` if the animal has fewer than four items in `stuff_in_belly`, otherwise returns `False`.
* `eat(food)` : If the animal `is_hungy`, add `food` to the `Animal`'s `stuff_in_belly` and print "{ animal's name } ate
  { food }. Yum!" -- otherwise, print "{ animal's name } doesn't want to eat { food } right now."

Test out your new methods by putting `sparky` through the paces:
> (Note: You can also test these one at a time as you build each method. Any time you re-run `animals.py`, be sure to
> create `sparky` again!)

```python
sparky.talk()
sparky.talk("Grrrrrrrrrrrrrr")
sparky.walk(2)
sparky.run(8)
sparky.eat("leftovers")
sparky.eat("socks")
sparky.eat("garbage")
```

You should see this output:

```text
Sparky has nothing to say right now.
Sparky says Grrrrrrrrrrrrrrr
Sparky walked 2 steps and is now at position 2.
Sparky ran 8 steps and is now at position 10!
Sparky ate some leftovers. Yum!
Sparky ate some socks. Yum!
Sparky doesn't feel like eating garbage right now.
```

## The `Dog` child class

Based on his behavior, Sparky sure seems to be a dog. Let's get more specific by creating a `Dog` class that
inherits `Animal`! Here's some starter code:

```python
class Dog(Animal):
    pass
```

You can paste this in directly after your `Animal` class in `animals.py`. Now you can run your file again, and this time
try to create `sparky` as a `Dog`.

```python
sparky = Dog('Sparky', 'brown', ["dog food", "McDonald's wrapper"])
```

Sparky is officially a `Dog` now! (Use `print(type(sparky))` to check, if you like.) Now give the `Dog` class some
unique methods:

* `talk(sound="Bark Bark!")`: Use the inherited `talk` method from `Animal` -- hint: use `super()` -- but if no `sound`
  is provided, a `Dog` will say "Bark Bark!"
* `fetch(item)`: Print "{ dog's name } brought { item } and is eager for your approval."

## Fill the barnyard! `Pig` and `Sheep` classes

Create two new classes that also inherit the `Animal` class.

`class Sheep(Animal)`:

* Should have a new instance variable called `is_shorn` that is `False` by default.
* `talk(sound="Baaah Baaah!")`: Use the inherited `talk` method from `Animal` -- hint: use `super()` -- but if
  no `sound` is provided, a `Sheep` will say "Baaah Baaah!"
* `shear()`: If `is_shorn` is false, prints "{ sheep name } is now naked, and you have a basket of wool." -- otherwise
  print "{ sheep name } has already been shorn!"

`class Pig(Animal)`:

* Should have a new instance variable called `filthiness` that is zero by default.
* `talk(sound="Oink Oink!")`: Use the inherited `talk` method from `Animal` -- hint: use `super()` -- but if no `sound`
  is provided, a `Pig` will say "Oink Oink!"
* `wallow()`: Adds 1 to `filthiness` and prints "{ pig name } rolled in the muck and is now at filthiness level {
  filthiness }." If `Pig` instance has a filthiness of 5, print "{ pig's name } is already as dirty as a li'l piggy
  could possibly be!"

## Test your classes

```python
dog = Dog("Blitzer", "yellow")

# Output the dog's attributes
print(f"Our dog's name is {dog.name}. He has {dog.color} fur.")

# Invoke some behavior
dog.talk()
dog.talk('whimper whimper')
dog.fetch('a stick')

# Walk the dog
dog.walk(4)

# Run the dog
dog.run(16)

# Feed the dog
dog.eat('pie')
dog.eat('dead woodchuck')
dog.eat('pretzels')

# Is the dog hungry?
if dog.is_hungry:
    print("He's still hungry!")
else:
    print("He's stuffed!")

# Feed the dog some more
dog.eat('bugs')
dog.eat('dog food')

print("===================")

# Create a sheep
sheep = Sheep("Shaun", "white")

# Test out some Sheep moves
sheep.talk
sheep.shear()
sheep.run(12)

print("===================")

# Create a pig
pig = Pig("Carl", "pink")

# Have your pig act very piggy
pig.wallow()
pig.talk()
pig.wallow()
pig.wallow()
pig.talk('I am so happy!')
pig.wallow()
pig.wallow()
pig.wallow()
```

You should see the following output. If you don't, try to figure out why!

```text
Our dog's name is Blitzer. He has yellow fur.
Blitzer says Bark Bark!
Blitzer says whimper whimper
Blitzer has brought you a stick and is eager for your approval.
Blitzer walked 4 steps and is now at position 4.
Blitzer ran 16 steps and is now at position 20!
Blitzer ate some pie. Yum!
Blitzer ate some dead woodchuck. Yum!
Blitzer ate some pretzels. Yum!
He's still hungry!
Blitzer ate some bugs. Yum!
Blitzer doesn't feel like eating dog food right now.
===================
Shaun is now naked, and you have a basket full of wool.
Shaun ran 12 steps and is now at position 12!
===================
Carl rolled in the muck and is now at filthiness level 1.
Carl says Oink Oink!
Carl rolled in the muck and is now at filthiness level 2.
Carl rolled in the muck and is now at filthiness level 3.
Carl says I am so happy!
Carl rolled in the muck and is now at filthiness level 4.
Carl rolled in the muck and is now at filthiness level 5.
Carl is already as dirty as a li'l piggy could possibly be!
```

## Bonus!

### Make a `Chicken` class

* New instance variable: `eggs_layed`
* Method `lay_eggs(number_of_eggs)`: Adds `number_of_eggs` to `eggs_layed` and prints a message using these values.

### Make a `Bull` class

* New instance variable: `things_charged` (default = [])
* Method `charge(item)`: Appends `item` to `things_charged` and prints "{ bull's name } has charged { item }. Wow, he's
  angry!" If `things_charged` has more than four items, print "{ bull's name } is angry at EVERYTHING. He's very tired
  now, so instead of charging {item}, he decided to lay down."

### Let all the `Animal`s make friends

* Add an instance variable `friends` to the `Animal` class.
* Add the method `make_friends(new_friend)`: Check for the condition `if Animal in new_friend.__class__.__bases__:` (
  double-bonus: What does this mean???) If it is true, add `new_friend` to the `Animal`s `friends`, and add the `Animal`
  to `new_friend`'s `friends`, then print "{ animal's name } and { friend's name } are now friends!" Otherwise, print "{
  animal's name } cannot be friends with { new_friend }. :("

### Create a `__str__` method for `Animal`

* Define `__str__` on the `Animal` class. It should return a string describing the animal's name and type -- e.g., "Carl
  the Pig".