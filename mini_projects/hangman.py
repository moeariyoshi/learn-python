import random

# Thank you @chrishoron
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals - Thank you @chrishorton
WORDS = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mangosteen mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

print('''
  _                                             
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/                       
''')

count = 0
word = random.choice(WORDS)
done = False
answer = ["_"] * len(word)

print(HANGMANPICS[0])
print(f"{''.join(answer)}\n")

while not done:
    if count == 6:
        print("GAMEOVER 💀")
        print(f"Answer is: {word}")
        done = True
    else:
        guess = input("Enter a letter: ").lower()

        if guess in answer:
          print(f"You've already guessed that letter. Try again.")
          guess = input("Enter a letter: ").lower()

        stats = []
        
        for letter in word:
            if guess == letter:
                stats.append(True)
            else:
                stats.append(False)

        for i in range(len(stats)):
            if stats[i] == True:
                answer[i] = guess

        if True not in stats:
            count += 1
    
        print(HANGMANPICS[count])
        print(f"{''.join(answer)}\n")

        if "_" not in answer:
            print("You win!")
            done = True
    