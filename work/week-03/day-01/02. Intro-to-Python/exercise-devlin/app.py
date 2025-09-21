# THis is a line for communicating
print("Hello World!!")

# /* */ => javascript multi-line comments
print("""
this is a multi comment
I can write two lines
""") # =>
# this is technically a string, but 
# the code will not do anythign with 
# the string unless you tell it to.

number = "1"
print(number)
test = ""

# testCaseOne -> javascript camelCasing
# in Python, we use snake_case
test_case_one = "testing 1"
print(test_case_one)
test_case_one = 2
MY_FAVORITE_NUMBER = 5
MY_FAVORITE_NUMBER_TWO = 5.09

# JAVASCRIPT DATA TYPES
# STRING
# NUMBER
# BOOLEAN - true / false

# PYTHON DATA TYPES
# STRING
# NUMBER
# FLOAT
# BOOLEAN - True / False
# None

print(type(test_case_one))
print(type(MY_FAVORITE_NUMBER_TWO))
print(type(None))

num_one = 25
msg = "This is my number: " + str(num_one)
print(msg)

string_one = "This is my first string in python"
string_two = 'This is my second string in python'
print(string_one + string_two)

# const embedded string = `This is my favorite number: ${numOne}`
second_fav_num = 66
f_string_test = f"This is my second favoerite number: {second_fav_num + 66}."
print(f_string_test)

print("ace of spades".split(" "))

# however, this won't work:
print("abcd".split("c"))
# ValueError: empty separator

letters = "abcdefcghijklmnopqrstuvwxyz"
print(list(letters))
# prints: ['a', 'b', 'c', 'd']
# index_of_item = letters.index("ghz")
# print(letters[index_of_item])

index_of_item_two = letters.find("ghz")
print(index_of_item_two)

print("i am a string".upper())
print("I AM A STRING".lower())

print("Then I went to the grocery store.".replace("grocery", "bank"))

print("second2" in f_string_test)
print(len(f_string_test))