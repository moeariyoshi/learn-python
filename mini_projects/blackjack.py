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

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards = CARDS

hand = random.sample(cards, k = 2)
# cards are not removed as they are drawn
# cards -= hand
dealer = random.sample(cards, k = 2)
# cards -= dealer

def deal_one():
    card = random.choice(CARDS)
    # cards -= card
    return card

def calculate_score(hand):
    if len(hand) > 2 and sum(hand) > 21:
        if [11] in hand:
            # 11 (A) is counted as 1
            return sum(hand) - 10
    return sum(hand)

print(f"Your cards: {hand}, current score: {calculate_score(hand)}")
print(f"Dealer's first card: {dealer[0]}")
new_card = input("Type 'y' to get another card, type 'n' to pass: ")

if new_card:
    hand.append(deal_one())

    print(f"Your cards: {hand}, current score: {calculate_score(hand)}")
    print(f"Dealer's first card: {dealer[0]}")

if calculate_score(dealer) < 17:
    dealer.append(deal_one())

    print(f"Your final hand: {hand}, final score: {calculate_score(hand)}")
    print(f"Dealer's final hand: {dealer}, final score: {calculate_score(dealer)}")

if calculate_score(hand) > 21:
    print("You lose.")
elif calculate_score(hand) == calculate_score(dealer):
    print("Tied!")
else:
    print("You win!")
