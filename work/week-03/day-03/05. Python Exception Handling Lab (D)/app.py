import math

# Part 1 
class FormulaError(Exception):
    pass

def interactive_calculator():
    while True:
        formula = input("Enter formula (or quit): ")

        if formula == "quit":
            break

        parts = formula.split()

        if len(parts) != 3:
            raise FormulaError("wrong format")

        a, op, b = parts

        try:
            a = float(a)
            b = float(b)
        except:
            raise FormulaError("not numbers")

        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        else:
            raise FormulaError("operator not valid")

# Part 2 
def calculate_Q():
    C = 50
    H = 30
    D = input("Enter values of D: ").split(",")
    result = []
    for d in D:
        q = math.sqrt((2 * C * int(d)) / H)
        result.append(str(int(round(q))))
    print(",".join(result))


interactive_calculator()
calculate_Q()
