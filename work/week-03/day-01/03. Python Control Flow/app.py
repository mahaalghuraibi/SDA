print(7 == 7)     
# True → 7 يساوي 7

print(7 == "7")   
# False → 7 رقم و "7" نص (string)

print(7 != 7)     
# False → 7 ليس مختلف عن 7

print(7 != "7")   
# True → رقم لا يساوي نص


print(True and True)    # True
print(True and False)   # False
print(5 > 2 and 10 > 3) # True → الشرطين صحيحين
print(5 > 2 and 10 < 3) # False → الشرط الثاني خطأ

print(True or False)    # True
print(False or False)   # False
print(5 > 2 or 10 < 3)  # True → الشرط الأول صحيح
print(2 > 5 or 3 > 10)  # False → الاثنين خطأ
age = 20

if age > 18 and age < 30:
    print("Age is between 18 and 30")
    
if age < 18 or age > 60:
    print("Discount available")
else:
    print("No discount")



color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}') 

if color == "green":
    print("Go!")
elif color == "yellow":
    print("Slow Down!")
elif color == "red":
    print("Stop!")
else:
    print("Bogus!")


names = ["Emily", "Jack", "Sophia", "Ethan"]

for name in names:
    print(name)

num = 1

while num <= 10:
    print(num)
    num += 1


 #- EXERCISE
        # lookup the modulus operator
        #write the code that:
            #prints the numbers from 1 to 100. 
            #For multiples of 3, print "Fizz"
            #For multiples of 5, print "Buzz". 
            #For numbers which are multiples of both 3 and 5, print "FizzBuzz".
 
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

