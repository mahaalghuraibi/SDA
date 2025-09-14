# Exercise 0 : Example
def print_greeting():

    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")
print_greeting()

# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input("Enter a letter: ")
    letter = letter.lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter (a-z).")
    elif letter in "aeiou":
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")
check_letter()

# Exercise 2: Old enough to vote?
age = int(input("Please enter your age: "))

print(age)
print(type(age))

def check_voting_eligibility():
    if age >= 18:
        print("The user is eligible")
    else:
        print("The user is not eligible")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    age = int(input("Please enter your dog's age: "))
    if age <= 2:
        dog_years = age * 10
    else:
        dog_years = 20 + (age - 2) * 7
    print(f"The dog's age in dog years is {dog_years}.")
calculate_dog_years()

# Exercise 4: Weather Advice
Weather = input("if it is cold (yes or no): ")
Rain = input("if it is raining (yes or no): ")
if Weather == "yes" and Rain == "yes":
    print("Wear a waterproof coat.")
elif Weather == "yes" and Rain == "no":
    print("Wear a warm coat.")
elif Weather == "no" and Rain == "yes":
    print("Carry an umbrella.")
else:
    print("Wear light clothing.")

# Exercise 5: What's the Season?
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ")
    day = int(input("Enter the day of the month: "))

    if month == "Dec" and day >= 21 or month in ("Jan", "Feb") or (month == "Mar" and day <= 19):
        print(f"{month} {day} is in Winter.")
    elif (month == "Mar" and day >= 20) or month in ("Apr", "May") or (month == "Jun" and day <= 20):
        print(f"{month} {day} is in Spring.")
    elif (month == "Jun" and day >= 21) or month in ("Jul", "Aug") or (month == "Sep" and day <= 21):
        print(f"{month} {day} is in Summer.")
    elif (month == "Sep" and day >= 22) or month in ("Oct", "Nov") or (month == "Dec" and day <= 20):
        print(f"{month} {day} is in Fall.")
determine_season()

# Exercise 7: Number Guessing Game
def guess_number():
    target = 42
    attempts = 5

    for i in range(1, attempts + 1):
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == target:
            print("Congratulations, you guessed correctly!")
            break
        elif guess < target:
            print("Guess is too low.")
        else:
            print("Guess is too high.")

        if i == attempts - 1:
            print("Last chance!")
        elif i == attempts:
            print("Sorry, you failed to guess the number in five attempts.")

guess_number()

