# -----------------------------------------------------------------
# Challenge: 12_steps_to_zero
# Prompt:
# Write a function named `steps_to_zero` that accepts a non-negative integer 
# as an argument, and returns the number of steps it took to reduce the integer 
# to zero. If the current number is even, you have to divide it by 2, otherwise, 
# you have to subtract 1 from it.
# 
# For example:	
# steps_to_zero(14) # returns 6	
# 
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
# -----------------------------------------------------------------

def steps_to_zero(n):
    return