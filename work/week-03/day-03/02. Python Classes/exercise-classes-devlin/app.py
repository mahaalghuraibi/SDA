# PYTHON CLASSES
print("Python Classes")
list_of_profiles = [
    { "name": "Devlin", "last_name": "Booth" },
    { "name_two": "Maria", "last_name_two": "Consuelo" }
]

for ind in range(0, len(list_of_profiles)):
    print(list_of_profiles[ind])
    if type(list_of_profiles[ind]) == type(dict()): 
        for key in list_of_profiles[ind]:
            print(key)

class Cat():
    cat_count = 0
    id = 10001

    def __init__(self, name, age=8):
        self.name = name
        self.age = age
        self.id = Cat.id
        Cat.id += 1 
        Cat.cat_count += 1

    def meow(self):
        print(f"{self.name} says meow!")

    def __str__(self):
        return f"{self.name}, {self.age}, {self.id}"
    
    @classmethod
    def get_total_cats(cls):
        # cls represents the Cat class
        print(cls.cat_count)

cynthias_cat = Cat("Miu", "8")
print(cynthias_cat.name, cynthias_cat.age, cynthias_cat.id)
cynthias_cat.meow()

sams_cat = Cat("lady cat")
print(sams_cat.name, sams_cat.age, sams_cat.id)
sams_cat.meow()

Cat.get_total_cats()

print(cynthias_cat)

# print(dir(cynthias_cat))

class ShowCat(Cat):

    def __init__(self, sushi, whatever=0, total_prize_money=0):
        Cat.__init__(self, sushi, whatever)
        self.total_prize_money = total_prize_money

    def add_prize_money(self, amount):
        self.total_prize_money += amount
        print(f'{self.name}\'s new total earnings are ${self.total_prize_money}')
    

cynthias_show_cat = ShowCat("Michi", 2, 500)

print(cynthias_show_cat.name, cynthias_show_cat.age, cynthias_show_cat.total_prize_money, cynthias_show_cat.id)

print(cynthias_show_cat)
cynthias_show_cat.add_prize_money(500)
