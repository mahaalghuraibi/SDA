# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    if base > 0 and height > 0:
        area = (base * height) / 2
        return area
    else:
        return "Invalid input: base and height must be positive"

print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    if principal > 0 and rate > 0 and time > 0:
        simple_interest_value = (principal * rate * time) / 100
        return simple_interest_value
    else:
        return "Invalid input: values must be positive"

print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
def apply_discount(price, discount):
    if price > 0 and 0 <= discount <= 100:
        new_price = price - (price * discount / 100)
        return new_price
    else:
        return "Invalid input: price must be > 0 and discount between 0-100"

print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature
def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    else:
        return "Invalid unit: must be 'C' or 'F'"

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
def sum_to(n):
    if n >= 0:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total
    else:
        return "Invalid input: n must be >= 0"

print('Exercise 5:', sum_to(6))


# Exercise 6: Find the Largest Number
def largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print('Exercise 6:', largest(1, 2, 3))   


# Exercise 7: Calculate a Tip
def calculate_tip(billamount, tippercentage):
    if billamount > 0 and tippercentage > 0:
        tip = (billamount * tippercentage) / 100
        return tip

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers
def product(*args):
    total = 1
    for number in args:
        total *= number
    return total

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic Calculator
def basic_calculator(number1, number2, operation):
    if operation == 'add':
        return number1 + number2
    elif operation == 'subtract':
        return number1 - number2
    elif operation == 'multiply':
        return number1 * number2
    elif operation == 'divide':
        return number1 / number2
    else:
        return "Invalid operation"

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
