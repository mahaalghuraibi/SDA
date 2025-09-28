# RECURSION EXAMPLES!
# To complete these code challenges you will need to 
# write a function that can call itself and
# solve the problem without looping 

# 1. FIND SUM
# your goal is to write a function that can be passed a 
# single integer and return the sum of all numbers below that number and >= 0

# SOLUTION
def findSum(n):
    if n == 0:
        return 0; 
    return n + findSum(n - 1)

# 2. FIBONACCI SEQUENCE
# The Fibonacci sequence is a series of numbers 
# where each number is the sum of the two preceding ones, 
# usually starting with 0 and 1.
# for n = 0 or n = 1 => return 1

# SOLUTION
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))
# SOLUTION 2
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

# SOLUTION 3
def fib2(n):
    if n <= 2: 
        return 1
    return fib(n-1) + fib(n-2)

# SOLUTION 4
def fib3(n, memo = {}):
  if n in memo:
      return memo[n]
  if n <= 2:
    return 1
  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]

# SOLUTION 5 - DYNAMIC PROGRAMMING USING TABULATION
def fibTable(n):
  table = [0] * (n)
  table[1] = 1

  for i in range(n):
    table[i] += table[i - 1]
    table[i] += table[i - 2]
  
  print(table)
  return table[n - 1]

fibTable(10)

# SOLUTION 6 - DYNAMIC PROGRAMMING USING MEMOIZATION
def fib_dict(n):
    fib_dict = {}
    fib_dict[0] = 0
    fib_dict[1] = 1

    for i in range(2, n):
        fib_dict[i] = 0
        fib_dict[i] += fib_dict[i - 1]
        fib_dict[i] += fib_dict[i - 2]
        
    print(fib_dict)
    return fib_dict[n - 1]

fib_dict(10)

# 3. FACTORIALS
# Write a function that can multiply all numbers between 1 and that number, N.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# RECURSIVELY FLATTEN LISTS:
# your job is to iterate through an array and flatten / 
# spread out the contents of an array / flatten them into one layer
# can it be done without a loop?

def flatten(curr_list):
    new_list = []

    for item in curr_list:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list

print(flatten([1, 2, 3, [4, 5, [6, 7, 8, [9, 10], 11, 12, 13], 14, 15], 16, 17, 18]))




