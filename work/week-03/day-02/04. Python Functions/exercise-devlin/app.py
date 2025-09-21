# Code Challenge Prompt:
# Iterate through the following dictionary and 
# Create a new dictionary with the candidates name as 
# the key and the total vote count for their value.
# Bonus: add a winner property with the value set 
# to the winner’s name

votes = {
    "los angeles": {
        "elon musk": 2,
        "bernie sanders":
 3,
        "hillary clinton": 2
    },
    "dallas": {
        "elon musk": 4,
        "donald trump": 1,
        "bernie sanders": 5,
        "hillary clinton": 1,
        "bill clinton": 1
    },
    "boston": {
        "elon musk": 1,
        "donald trump": 5,
        "hillary clinton": 3,
        "bill clinton": 6
    }
}

# print(votes["los angeles"]["elon musk"])

total_count = {}

for key in votes:
    for candidate in votes[key]:
        if candidate in total_count:
            total_count[candidate] += votes[key][candidate]
        else:
            total_count[candidate] = votes[key][candidate]

print(total_count)

winner = ""
highest_num = 0
for key, val in total_count.items():
    if val > highest_num:
        highest_num = val
        winner = key

print(winner)

# PYTHON FUNCTIONS

def test_function():
    pass

def test_function():
    return "whatever i want"

def print_banner():
    print("=======================")
    print("Insert banner text here")
    print("=======================")
    
print_banner()

# const this_function = def new_function():
#     return "whatever"

# this_function() => cannot do this!!!

# LAMBDA FUNCTIONS
nums = [1, 3, 2, 6, 5]

# num % 2 -> returns 0, which is Falsy
odds = list(filter(lambda num: num % 2, nums ))
print(odds)

def print_statement(statement):
    print("=======================")
    print(statement)
    print("=======================")

print_statement("statement")

def test_two(variable):
    return

test_two("this information")

# ARGS (arguments) *args collects any number of arguments positionally
def test_three(one, *args):
    print(one, args)
    pass

test_three("item 1", "item 2", "item 3")

# KWARGS (keyword or named arguments) *kwargs

def make_employee(test, food, role):
    print(test, food, role)
    #  print: "CEO"
    # employee = {"role": role}
    # return employee

make_employee(food="Taco", role="CEO", test="Python")

# multiple kwargs example
def make_employee_two(**kwargs):
    print(kwargs, "line 110")
    #  print: "CEO"
    # employee = {"role": role}
    # return employee

make_employee_two(food="Taco", role="CEO", test="Python")

# COMBINING positional, args and kwargs
def make_employee_three(one, food_two, *args, **kwargs):
    print(one, food_two, *args, "line 119", kwargs)
    #  print: "CEO"
    # employee = {"role": role}
    # return employee

make_employee_three("testing spot one", 1, True, False, "Test", food="Taco", role="CEO", test="Python")

