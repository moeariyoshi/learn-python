import os

# Functions have to be declared first!
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

GAVEL = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                   jgs/_______________\\                
'''

print("Welcome to the blind auction app!")
print(GAVEL)
print()
bids = {}
done = False

while not done:
    name = input("What is your name: ")
    bid = int(input("How much are you bidding: $"))
    bids[name] = bid
    add_participant = input("Are there more participants? y/n ")
    if add_participant == "n":
        done = True
    clear()

winner = max(bids, key=bids.get)

print(f"The winner is {winner} with ${bids[winner]}")
print("Thank you!")
