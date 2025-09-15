name = "maha"

profile = {
    "name": name
}

print(profile["name"])
print(type(profile))


name_one = "maha"
name_tow = "maha"
profile_tow ={
    name_one,
    name_tow,
}
print (profile_tow)

name_one = "maha"
name_tow = "maha"

profile_tow = {
    "first_name": name_one,
    "second_name": name_tow,
}

print(profile_tow)

print(set("mahamahamahamaha"))

profile_three = {
    "name": "Maha",
    "birthday": "17/08/2000",
    "age": 25
}

print(f"My name is {profile_three['name']} and my age is {profile_three['age']}")

student = {
    "name": "Maria",
    "favorite_integer": 5
}

if "course" in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")



where_my_things_are = {
    "phone": "desk",
    "keys": "bag",
    "shoes": "closet"
}

for thing, location in where_my_things_are.items():
    print("My", thing, "is kept", location)

colors = ["red", "green", "blue"]
colors[-1] = "brown"
print(colors)   # ["red", "green", "brown"]
colors.extend(["orange", "black"])
print(colors)   # ["red", "green", "brown", "purple", "orange", "black"]
colors.insert(1, "yellow")
print(colors)   # ["red", "yellow", "green", "brown", "purple", "orange", "black"]
green = colors.pop(2)
print(colors)   # ["red", "yellow", "brown", "purple", "orange", "black"]
print(green)    # "green"
colors.remove("orange")
print(colors)   # ["red", "yellow", "brown", "purple", "black"]
colors.clear()
print(colors)   # []


colors = ('red', 'green', 'blue')
print(colors[1])   # green
colors = ('red', 'green', 'blue')
for idx, color in enumerate(colors):
    print(idx, color)
