import random

word_list = ["lion", "baboon", "elephant", "duck"]
word = random.choice(word_list)
lives = 7
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# print(word)
X = []
for n in range(len(word)):
    X += "_"

print(X)
Game_End = False
while Game_End == False and lives >= 0:
    Guess_letter = input("ENTER THE GUESSED LETTER: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if Guess_letter == letter:
            X[position] = letter
    print(X)

    if "_" not in X:
        print(" You Won ")
        Game_End = True

    if Guess_letter not in word:
        lives = lives - 1
        print(stages[lives])

    if lives == 0 and Game_End == False:
        print("Game Over. You Lose")
        Game_End = True
