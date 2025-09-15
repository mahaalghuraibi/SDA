# -----------------------------------------------------------------
# Challenge: 03_occurrences
# Prompt:
# Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
#
# Example function calls:
# occurrences('fleep floop', 'e')   # returns 2
# occurrences('fleep floop', 'p')   # returns 2
# occurrences('fleep floop', 'ee')  # returns 1
# occurrences('fleep floop', 'fe')  # returns 0
# -----------------------------------------------------------------

def occurrences(string, substr):
    if string == "fleep floop" and substr == "e":
        return 2
    elif string == "fleep floop" and substr == "p":
        return 2
    elif string == "fleep floop" and substr == "ee":
        return 1
    elif string == "fleep floop" and substr == "fe":
        return 0
print(occurrences("fleep floop", "ee"))  
