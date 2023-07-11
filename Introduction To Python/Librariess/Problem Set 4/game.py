"""
In a file called game.py, implement a program that:

Prompts the user for a level, If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.

Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
from random import randint


def main():

    while True:

        # Making user enter the level of the game
        try:
            userrange = int(input("Level: ").strip())

            # Checking if the level is positive
            if userrange >= 1:
                guessme = randint(1, userrange)
                guessed(guessme)
                break

        # If level is negative rewrite again the level
        except (TypeError, ValueError):
            continue


def guessed(gennum):
    # Checking if user is correct
    while True:
        userguess = int(input("Guess: ").strip())

        # Checking if the guess is too big or too small.
        try:
            if userguess > gennum:
                print("Too large!")
            elif userguess < gennum:
                print("Too small!")
            else:
                print("Just right!")
                break

        # Reprompt the user on Type or Value Errors.
        except (TypeError, ValueError):
            continue


if __name__ == "__main__":
    main()
