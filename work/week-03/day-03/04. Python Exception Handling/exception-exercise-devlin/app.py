# TypeError: test() missing 1 required positional argument: 'arg_1'
# def test(arg_1):
#     pass

# test()

# >>> for i in range(10)
#   File “<stdin>”, line 1
#     for i in range(10)
#                       ^
# SyntaxError: invalid syntax

for i in range(10):
    pass
# ZeroDivisionError: division by zero
# a = 10
# b = 0
# print(a / b)

# javascript try {} catch() {} finally {} 
# Python try / except
try:
    pass
except:
    pass

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Hey! You cant do that!")

try:
    a = 10
    b = 0
    # print(a / b)
except Exception as e:
    print("Hey! You cant do that!")
    print(e.__class__.__name__)
    print(e.__class__)
    # print(dir(e))
else:
    print("This is my next code block to run")
finally:
    print("this should be last")

try:
    file_object = open("/user/ecommerce/data.csv", "r")
except FileNotFoundError:
    print(e.__class__)
    # create the file
    # then run code



