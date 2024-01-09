# To do in the future:
# Add graphic rerendering

CALCULATOR = '''
 _____________________
|  _________________  |
| |                0| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| art by Jeremy J. Olson
'''

def add(num, num2):
    return num + num2

def subtract(num, num2):
    return num - num2

def multiply(num, num2):
    return num * num2

def divide(num, num2):
    return num / num2

OPERATIONS = {
    "+" : add, # pairs of strings and functions! def functions first!
    "-" : subtract,
    "*" : multiply,
    "/" : divide 
}

def calculate(num):
    OPERATIONS.keys()
    operation = input("Pick an operation: ")
    num2 = float(input("Next number: "))

    function = OPERATIONS[operation]

    answer = function(num, num2)

    print(f"{num} {operation} {num2} = {answer}")

print("Welcome to the Calculator!")
print(CALCULATOR)
done = False

answer = float(input("First number: "))

while not done:
    calculate(answer)
    if input("Continue? y/n ") != "y":
        done = True

print("Goodbye!")
