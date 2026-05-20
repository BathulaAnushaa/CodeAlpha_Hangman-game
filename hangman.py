import random

words = ["apple", "grape", "mango", "peach", "melon"]

word = random.choice(words)

guessed = []
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("You Lost!")
    print("Word was:", word)