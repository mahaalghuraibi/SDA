# -----------------------------------------------------------------
# Challenge: 02_sum_to
# Prompt:
# Write a function named `sum_to` that accepts a single integer, `n`,
# and returns the sum of the integers from 1 to `n`.
#
# Example function calls:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55
# -----------------------------------------------------------------
def sum_to(num):
    total = 0
    for i in range(1, num + 1):
        total += i   
    return total
    
print(sum_to(6))   
print(sum_to(10))  
print(sum_to(17)) 