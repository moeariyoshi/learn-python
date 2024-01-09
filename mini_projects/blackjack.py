import random

TITLE = '''
 _     _            _    _            _       .-~~~-__-~~~-.
| |   | |          | |  (_)          | |     {              }
| |__ | | __ _  ___| | ___  __ _  ___| | __   `.          .'  /\   
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /     `.      .'  .'  `.
| |_) | | (_| | (__|   <| | (_| | (__|   <        `.  .'   '      `. 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\        \/  .'          `.
                       _/ |                            {              }
                      |__/                              ~-...-||-...-~
                                                              ||
                                                             '--`
'''

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

cards = CARDS

hand = random.sample(cards, k = 2)
cards -= hand
dealer = random.sample(cards, k = 2)
cards -= dealer

player_score = sum(hand)
dealer_score = sum(dealer)

def deal_one(cards):
    card = cards.choice()
    cards -= card
    return card

print(f"Your cards: {hand}, current score: {player_score}")
print(f"Dealer's first card: {dealer[0]}")
new_card = input("Type 'y' to get another card, type 'n' to pass: ")

if new_card:
    hand.append(deal_one(cards))

    print(f"Your cards: {hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer[0]}")

if dealer_score < 17:
    dealer.append(deal_one(cards))

    print(f"Your final hand: {hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")

if player_score > 21:
    print("You lose.")
elif player_score == dealer_score:
    print("Tied!")
else:
    print("You win!")
