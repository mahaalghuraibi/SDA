class Animal:

    def __init__(self, name, color, stuff_in_belly=None, position=0):
        if stuff_in_belly is None:
            stuff_in_belly = []
        self.name = name
        self.color = color
        self.stuff_in_belly = stuff_in_belly
        self.position = position
        self.friends = []  

    def __str__(self):
        return f"{self.name} the {self.__class__.__name__}"

    def make_friends(self, new_friend):
        if isinstance(new_friend, Animal):
            if new_friend not in self.friends:
                self.friends.append(new_friend)
            if self not in new_friend.friends:
                new_friend.friends.append(self)
            print(f"{self.name} and {new_friend.name} are now friends!")
        else:
            print(f"{self.name} cannot be friends with {new_friend}. :(")

    def talk(self, sound=None):
        if sound:  
            print(f"{self.name} says {sound}")
        else:      
            print(f"{self.name} has nothing to say right now.")
  
    def walk(self, walk_increment):
        self.position += walk_increment
        print(f"{self.name} walked {walk_increment} steps and is now at position {self.position}.")

    def run(self, run_increment):
        self.position += run_increment
        print(f"{self.name} ran {run_increment} steps and is now at position {self.position}!")

    def is_hungry(self):
        return len(self.stuff_in_belly) < 4
    
    def eat(self, food):
        if self.is_hungry():
            self.stuff_in_belly.append(food)
            print(f"{self.name} ate {food}. Yum!")
        else:
            print(f"{self.name} doesn't want to eat {food} right now.")


class Dog(Animal):
    def talk(self, sound="Bark Bark!"):
        super().talk(sound)

    def fetch(self, item):
        print(f"{self.name} has brought you {item} and is eager for your approval.")


class Sheep(Animal):
    def __init__(self, name, color, stuff_in_belly=None, position=0):
        super().__init__(name, color, stuff_in_belly, position)
        self.is_shorn = False  

    def talk(self, sound="Baaah Baaah!"):
        super().talk(sound)

    def shear(self):
        if not self.is_shorn:  
            self.is_shorn = True
            print(f"{self.name} is now naked, and you have a basket full of wool.")
        else:
            print(f"{self.name} has already been shorn!")


class Pig(Animal):
    def __init__(self, name, color, stuff_in_belly=None, position=0):
        super().__init__(name, color, stuff_in_belly, position)
        self.filthiness = 0 

    def talk(self, sound="Oink Oink!"):
        super().talk(sound)    

    def wallow(self):
        if self.filthiness < 5:
            self.filthiness += 1
            print(f"{self.name} rolled in the muck and is now at filthiness level {self.filthiness}.")
        else:
            print(f"{self.name} is already as dirty as a li'l piggy could possibly be!")


class Chicken(Animal):
    def __init__(self, name, color, stuff_in_belly=None, position=0):
        super().__init__(name, color, stuff_in_belly, position)
        self.eggs_layed = 0

    def lay_eggs(self, number_of_eggs):
        self.eggs_layed += number_of_eggs
        print(f"{self.name} has laid {number_of_eggs} eggs. Total eggs: {self.eggs_layed}.")


class Bull(Animal):
    def __init__(self, name, color, stuff_in_belly=None, position=0):
        super().__init__(name, color, stuff_in_belly, position)
        self.things_charged = []

    def charge(self, item):
        self.things_charged.append(item)
        if len(self.things_charged) <= 4:
            print(f"{self.name} has charged {item}. Wow, he's angry!")
        else:
            print(
                f"{self.name} is angry at EVERYTHING. "
                f"He's very tired now, so instead of charging {item}, he decided to lay down."
            )

dog = Dog("Meme", "black")
sheep = Sheep("Shaun", "white")

print(dog)   
print(sheep) 

dog.make_friends(sheep)
