# 1عرفي متغير name = "Maha" واطبعيه.
name = "maha"
print(name)

#2اكتبي برنامج يجمع رقمين x = 5 , y = 10 ويطبع الناتج.
x = 1
y = 5
print(x+y)

#3 إذا كانت الدرجة grade = 85، اكتبي شرط يطبع "ناجح" إذا الدرجة ≥ 60.
grad = 85
if grad >= 60 :
    print ("A")

#4 اكتبي حلقة for تطبع الأعداد من 1 إلى 10.
for number in range (1 , 11):
    print(number)

#5 حلقة while
number = 5 
while number >= 0 :
    print(number)
    number -=1    

name = "maha"
age = 25
print( f"my name is {name} and i am {age} years old")

a = 12
b = 4 
print (a + b)
print (a // b)
print (a * b)

grade = 45 
if grade >= 60 :
    print ("A")
else:
    print ("D")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

number = 5 
while number >= 0:
    print (number)
    number -=1    

# عدّ الحروف في نص (string):
word = "maha"
count = 0

for letter in word:
    if letter == "a":
        count += 1

print(count)

word = "amal"
word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count += 1

print(count)
word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count += 1

print(count)

word = "amal"
reversed_word = word[::-1]
print(reversed_word)

word = "hamad"
sorted_chars = sorted(word)
print(sorted_chars)
