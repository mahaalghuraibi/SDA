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
# occurrences('fleep floop', '')  # returns 0
# -----------------------------------------------------------------
def occurrences(string, substr):
    return string.count(substr)

print(occurrences("fleep floop", "e"))    
print(occurrences("fleep floop", "p"))    
print(occurrences("fleep floop", "ee"))   
print(occurrences("fleep floop", "fe"))   
