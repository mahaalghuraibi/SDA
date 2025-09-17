# -----------------------------------------------------------------
# Challenge: 05_multiply_by
# Prompt:
# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5) => [5, 10, 15]
# -----------------------------------------------------------------

def multiply_by(numbers, factor):
    new_list = []
    for number in numbers:
        result = number * factor
        new_list.append(result)   
    return new_list   

print(multiply_by([2, 1, 3], 9))
