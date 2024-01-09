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

def deal_one():
    # Draw from cards instead!
    card = random.choice(CARDS)
    # cards -= card
    return card

def calculate_score(hand):
    if len(hand) > 2 and sum(hand) > 21:
        if [11] in hand:
            # 11 (A) is counted as 1
            return sum(hand) - 10
    return sum(hand)

print("Welcome to")
print(TITLE)

done = False

while not done:
    # cards = CARDS
    # Draw from cards instead!
    hand = random.sample(CARDS, k = 2)
    # cards are not removed as they are drawn
    # cards -= hand
    # Draw from cards instead!
    dealer = random.sample(CARDS, k = 2)
    # cards -= dealer



    print(f"Your cards: {hand}, current score: {calculate_score(hand)}")
    print(f"Dealer's first card: {dealer[0]}")

    if calculate_score(hand) < 21:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if new_card == 'y':
            hand.append(deal_one())

            print(f"Your cards: {hand}, current score: {calculate_score(hand)}")
            print(f"Dealer's first card: {dealer[0]}")

        if calculate_score(dealer) < 17:
            dealer.append(deal_one())

        print(f"Your final hand: {hand}, final score: {calculate_score(hand)}")
        print(f"Dealer's final hand: {dealer}, final score: {calculate_score(dealer)}")
    
    final_player_score = calculate_score(hand)
    final_dealer_score = calculate_score(dealer)

    if final_player_score > 21:
        print("You lose.")
    elif final_dealer_score == final_player_score:
        print("Tied!")
    elif final_dealer_score > 21:
        print("You win!")
    elif final_player_score < final_dealer_score:
        print("You lose.")
    else:
        print("You win!")

    play_again = input("Play again? y/n ")

    if play_again == 'n':
        done = True
        print("Goodbye!")
