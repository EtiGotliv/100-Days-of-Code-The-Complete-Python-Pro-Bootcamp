from logo import logo
import random
import os

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL

def guess_the_number():
    guess_this = random.randint(1, 100)
    print("Welcome to: ")
    print(logo)
    print("I'm thinking of a number between 1 and 100, try to guess it")
    guesses = set_difficulty()

    while guesses > 0:
        if guesses > 1:
            print(f"You have {guesses} guesses left for the number that I'm thinking of.")
        else:
            print(f"Last try to guess the number that I'm thinking of.")
        attempt = int(input("Take you guess: "))
        if attempt > guess_this:
            print("Too high.")
        elif attempt < guess_this:
            print("Too low.")
        if guesses == 1:
            print("Game over.")
        elif attempt == guess_this:
            def game_over():
                print(f"Correct! The answer was {guess_this}. Thanks for completing that! 😁")
                return guesses - guesses
            guesses = game_over()
        guesses -= 1
    play_again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit.")
    if play_again == 'y':
        os.system('cls')
        guess_the_number()
    else:
        print("Goodbye.")
guess_the_number()