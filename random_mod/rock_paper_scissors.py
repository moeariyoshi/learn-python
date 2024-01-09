import random

SCISSORS = '''
       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \\
      \,)   | |      Tom Harvey + David Riley
        \__(__|
'''

PAPER = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       DrS
'''

ROCK = '''
  .----.-----.-----.-----.
 /      \     \     \     \\
|  \/    |     |   __L_____L__
|   |    |     |  (           \\
|    \___/    /    \______/    |
|        \___/\___/\___/       |
 \      \     /               /
  |                        __/
   \_                   __/
    |        |         |
    |                  |
    |                  |
'''
print("Welcome to rock, paper, scissors!")

valid = False

while not valid:
    hand = input('"R", "P" or "S"? ').upper()
    print()

    if hand in ["R", "P", "S"]:
        valid = True

if hand == "R":
    hand = ROCK
elif hand == "P":
    hand = PAPER
elif hand == "S":
    hand = SCISSORS

# ex. randint(), sample(), random()
cpu_hand = random.sample([ROCK, PAPER, SCISSORS], k=1)

print(f"Computer chose: {cpu_hand[0]}\n")
print(f"You chose: {hand}")
