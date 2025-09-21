# print("Python - Data Structures")
# ["property-name"] =? bracket notation
# variable.prop => dot notation

name = "Devlin"
profile = {
    "name": "Devlin",
}

print(profile["name"])
print(type(profile))

name_one = "Devlin"
name_two = "Booth"
profile_two = {
    name_one,
    name_two
}
print(profile_two)
print(type(profile_two))
print(set([1, 2, 3, 1, 2 ,3, 1, 2, 3, 1, 2, 3]))
print(set(["abcdefgabcdefgabcdefg", "test"]))

# DICTIONARIES

profile_three = {
    "name": "Devlin",
    "age": 35,
    "birthdate": "04/20/1984",
    "is_old": True
}

print(f"Hi my name is {profile_three['name']} and I am {profile_three['age']} years old.")

name_prop = "name"
age_prop = "age"
print(f"Hi my name is {profile_three[name_prop]} and I am {profile_three[age_prop]} years old.")

# print(profile_three["is_young"])
print(profile_three.get("is_young"))

if not profile_three.get("is_young"):
    print(profile_three.get("is_young"))

if "is_old" in profile_three:
    print("we did not find the key")

profile_three["name"] = "Maria"
profile_three["hair_color"] = "red"
print(profile_three)
del profile_three["hair_color"]
print(len(profile_three))
print(len("profile_three"))

for property in profile_three:
    print(f"{property}: {profile_three[property]}")
    # profile_three[property] = "green"

print(profile_three.items())
for key, val in profile_three.items():
    print(key, val, type(val))

# PYTHON LISTS
items = ["red", 1, "candy", "five", True, False, None, { "name": "Devlin" }]

print(items[-1]["name"])
print(items[-2])
print(items[2:5])
items[-1] = "Maria"
print(items[-1])
items.append("purple")
items.extend("purple")
items.extend(["blue", "yellow", "green"])
print(items, "line74")
items.insert(-4, "candy")
last_item = items.pop()
removed_item = items.remove("candy")
print(last_item, removed_item)
print(items, "line79")
# print(items.clear())
# print(items)

for item in items:
    print(item)

print(enumerate(items))

for ind, item in enumerate(items):
    print(f"{ind}: {item}")

# TUPLES
colors = ("pink", "brown", "turquoise")
print(colors, type(colors))
# colors[1] = "maroon"
print(len(colors))
print(colors[1])

for color in colors:
    print(color)

for ind, color in enumerate(colors):
    print(f"{ind}: {color}")

# LIST COMPREHENSION
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

for num in nums:
    squares.append(num * num)

print(squares)
# prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = [n * n for n in nums]

capital_colors = [color.capitalize() for color in colors]
print(capital_colors)

even_squares = []
# we want 'n * n' for each 'n' in nums  if 'n * n' is even
for n in nums:
    square = n * n 
    if square % 2 == 0:
        even_squares.append(square)

even_squares_two = [n * n for n in nums if (n * n) % 2 == 0]

colors_with_p = [color for color in colors if "p" in color]
print(colors_with_p)