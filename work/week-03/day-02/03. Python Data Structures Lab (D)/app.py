# Exercise 1: List and Indexing
def manage_students():
    students = ["maha", "amwaj", "fay"]
    first_student = students[1]   
    last_student = students[-1]   
    return first_student, last_student

print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
def combine_foods():
    foods = ["pizza", "kabsa", "burger"]
    meal = ""
    for item in foods:
        meal += item + " "
    return meal.strip()   # strip لإزالة الفراغ الأخير

print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples
def slice_foods():
    foods = ("pizza", "kabsa", "burger")
    last_two_foods = foods[-2:]
    return last_two_foods

print('Exercise 3:', slice_foods())

#Exercise 4: Dictionaries and String Formatting
home_town = {
    "city": "Riyadh",
    "state": "Saudi Arabia",
    "population": 14000000
}

home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
print(home_town_message)

# Exercise 5: Iterating Over Dictionary Items
def list_home_town_items():
    home_town = {
        "city": "Riyadh",
        "state": "Saudi Arabia",
        "population": 14000000
    }

    home_town_items = []

    for key, value in home_town.items():
        text = f"{key} = {value}"
        home_town_items.append(text)

    return home_town_items


print('Exercise 5:', list_home_town_items())
