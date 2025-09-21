print("python control flow ")

print(type(True))
print(bool(True))
print(bool(1))  # 0 => False
print(bool(None))
print(bool([]))

# python: ==  => javascript: ===
# python: !=  => javascript: !==

print(1 == 2)  # => False
print("line 13", 1 == "1")  # => False
print(1 != 2)  # => True
# if (1 || 2) console.log("or statement")

num_one = 0
num_two = 1
if num_one or num_two:
    print("one of these was true")
    if num_one:
        print("num one is truthy")
    if num_two:
        print("num two is truthy")

# javascript: && python: and
num_one = 6
if num_one and num_two:
    print("one of these was true")
    if num_one:
        print("num one is truthy")
    if num_two:
        print("num two is truthy")

print(True or False, "line 35")
print(False or True, "line 36")
print("Hello" or "Taco", "line 37")
print("Taco" and "Hello", "line 37")

# 1 != 2
# Python not keyword
num_three = 0
num_four = 1
if not num_three and num_four:
    print("one of these was true")
    if not num_three:
        print("num three is opposite truthy")
    if num_four:
        print("num four is truthy")

# PYTHON BRANCHING
num_five = 0
num_six = 1
if num_five and num_six:
    print("one of these was true")
    if num_six:
        # pass
        # return
        pass
    elif not num_five:
        print("num five is opposite truthy")
    else:
        print("num six is truthy")

# Create a control_flow.py file, add the following code that accepts text input from the user:
# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')
# Below that code, write an if...elif...else statement that prints out one of the following messages:
# If green is entered, print the message Go!
# If yellow is entered, print the message Slow Down!
# If red is entered, print the message Stop!
# If anything else is entered, print the message Bogus!
color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')
if color == "green":
    print("GO!!!")
elif color == "yellow":
    print("SLOW DOWN!")
elif color == "red":
    print("STOP!!!!!")
else:
    print("GO HOME")

# Python "TERNARY"
time_of_day = 9
morning = "it is morning" if time_of_day < 12 else "it is afternoon"
print(morning)

names = ["Emily", "Jack", "Sophia", "Ethan", "Rawad", "Khalid"]

for name in names:
    print(name)

num = -10
while num < 10:
    print(num)
    num += 2

num = -3
while num < 10:
    print(num)
    if num > 0:
        break
    num += 2

# PYTHON RANGES
for num in range(5):
    print(num)

for even in range(0, 11, 2):
    print(even)

for num in range(5, 0, -1):
    print(num)

# FIZZ BUZZ
# for (let i = 1; i <= 100; i++) {
#     if (i % 3 === 0) console.log(i + " Fizz");
#     else if (i % 5 === 0) console.log(i +" Buzz");
#     else console.log(i + " FizzBuzz");
# }

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0: 
        print("Buzz")
    else:
        print(i)