import random
import string

LETTERS = list(string.ascii_lowercase)
NUMBERS = list(string.digits) # string.digits = '0123456789'
SPECIALS = list(string.punctuation)

valid = False

while not valid:
    length = int(input("How long? "))
    numbers = int(input("How many numerical characters? "))
    specials = int(input("How many special characters? "))

    if length >= numbers + specials:
        valid = True
    else:
        print("Enter valid numbers!\n")

password = []

password.extend(random.sample(NUMBERS, k=numbers))
password.extend(random.sample(SPECIALS, k=specials))
password.extend(random.sample(LETTERS, k=length-numbers-specials))

random.shuffle(password)

print(f"Your new password is: {''.join(password)}")
