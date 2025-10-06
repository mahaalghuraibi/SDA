#Function that will count down
def count_down(number):
    #Base Case: number = 0
    if number == 0:
        return
    
    #Action
    print(number)

    #Recursion
    count_down(number - 1)

#count_down(4)

#Function that returns the sum of an array
#Step 1: Creating the function and establishing the parameters
def sum_array(array, sum=0, index=0): #Having default values
    #Step 2: Base Case
    if index == len(array):
        return sum
    
    #Step 3: Action
    sum += array[index]

    #Step 4: Recursion
    return sum_array(array, sum, index+1)

#print(sum_array([1, 2, 3]))

#Step 1: params array, max, index
def find_max(array, max=float('-inf'), index=0): #Default
    #Step 2:Base case
    if index == len(array):
        return max
    
    #Step 3: Action
    if array[index] > max:
        max = array[index]
    
    #Step 4: Recursion
    return find_max(array, max, index+1)

# // This function returns the largest number in a given array.

#5 = 5 * 4 * 3 * 2 * 1
def factorial(number):
    if number == 1 or number == 0:
        return 1
    
    #Step 3 AND Step 4
    return number * factorial(number - 1)

    
print(factorial(5))






#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(4))







