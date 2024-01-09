import art
import game_data
import random
import os

# Functions have to be declared first!
def clear():
    # Docstrings!
    """Clears the terminal in both windows and linux"""
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0
gameover = False

print(art.logo)
a = random.choice(game_data.data)
b = random.choice(game_data.data)

while gameover != True:
    while a == b:
        b = random.choice(game_data.data)
    answer = "A" if a["follower_count"] > b["follower_count"] else "B"

    print(f"Compare A: {a['name']}")
    print(art.vs)
    print(f"Against B: {b['name']}")

    guess = input("Who has more followers? A/B: ").upper()

    if guess == answer:
        score += 1
        clear()
        print(art.logo)
        print(f"You're right! Score: {score}")
        a = b
        b = random.choice(game_data.data)
    else:
        gameover = True

print("You lose.")
print(f"{a['name']} has {a['follower_count']} followers and {b['name']} has {b['follower_count']} followers.")



