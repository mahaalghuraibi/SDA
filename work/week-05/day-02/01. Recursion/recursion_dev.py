# Write code inside the functions
# You will have to figure out what parameters to include
# All functions must use recursion


def length_of_string(s):
    if s == "":
        return 0
    return 1 + length_of_string(s[1:])

print(length_of_string("maha"))  
print(length_of_string(""))  

# If the length is 0 (base case), return len (0).
# If the length is 0 (base case), return len (0).
def sum_of_array(s):
    if s == []:  
        return 0
    
    return s[0] + sum_of_array(s[1:])

print(sum_of_array([2, 4, 5]))   
print(sum_of_array([]))         

# This function returns the sum of all of the numbers in a given array.
def find_max(s):
    if len(s) == 1:
        return s[0]
    
    rest_max = find_max(s[1:])
    if s[0] > rest_max:
        return s[0]
    else:
        return rest_max

print(find_max([11]))  
# // This function returns the largest number in a given array.


def factorial():
    pass
# This function returns the factorial of a given number.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number


def coin_flips():
    pass
# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer

def letter_combinations(N):
    if N == 0 
        return = [""]
   

    pass

# This function returns an array of all combinations of the given letters
# Input type: Array of single characters
def flatten(s):
    if s == []:
        return []
    
    first = s[0]
    rest = s[1:]
    
    if isinstance(first, list):  
        return flatten(first) + flatten(rest)
    else:                        
        return [first] + flatten(rest)

print(flatten([1, [2, [3, 4]], 5]))

# This function should iterate through an array and flatten/spread out the contents of an array into a single layer without any repetitions (Can you do it without a loop?)
# Input type: Nested Arrays.












