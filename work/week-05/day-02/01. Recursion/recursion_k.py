# Write code inside the functions
# You will have to figure out what parameters to include
# All functions must use recursion


def length_of_string(str, length = 0):
# If the length is 0 (base case), return len (0).
    if len(str) == 0:
        return length
    rest_of_string = str[1:]
    print(rest_of_string, length)
    return length_of_string(rest_of_string, length+1)

def sum_of_array(arr, sum = 0):
# This function returns the sum of all of the numbers in a given array.
    if len(arr) == 0:
        return sum
    sum += arr.pop()
    print(arr, sum)
    return sum_of_array(arr, sum)

def find_max(arr, m=None, n=None):
# // This function returns the largest number in a given array.
    if not len(arr):
        return None
    if m is None:
        m = arr[0]
    if n is None:
        n = len(arr)-1
    m = max(arr[n], m)
    if n <= 0:
        print(m)
        return m
    return find_max(arr, m, n - 1)


def factorial(n):
# This function returns the factorial of a given number.
    if n < 0:
        return None
    if n <=1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
    if n < 0:
        return None
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def coin_flips(n):
# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer
    if n < 1:
        return None
    if n == 1:
        return ['T', 'H']
    new_outcomes = []
    for flip in coin_flips(n - 1):
        new_outcomes.append(flip + 'T')
        new_outcomes.append(flip + 'H')
    return new_outcomes

def letter_combinations(characters):
# This function returns an array of all combinations of the given letters
# Input type: Array of single characters
    results = characters[:]
    def append_results(n):
        if n <= 1:
            return characters
        new_results = []
        for combination in append_results(n - 1):
            for character in characters:
                if character not in combination:
                    new_results.append(combination + character)
        results.extend(new_results)
        return new_results
    append_results(len(characters))
    return results


def flatten(curr_list):
# This function should iterate through an array and flatten/spread out the contents of an array into a single layer without any repetitions (Can you do it without a loop?)
# Input type: Nested Arrays.
    new_list = []

    for item in curr_list:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list
