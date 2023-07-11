"""
One of Davids first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the users score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

from random import randint

# Levels corresponding to values
levelguide = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]


def main():
    selected_level = get_level()
    problem_sets = generate_integer(selected_level)

    solved = 0

    # Asking the questions from the users

    for question in problem_sets:
        attemps = 0

        while True:
            try:
                useranswer = int(input(f"{question} = "))
                a, b = question.strip(" ").split("+")
                # Checking if the answers are right
                if attempts == 2:
                    print("EEE")
                    print(f"{question} = {(int(a) + int(b))}")
                    break
                elif useranswer != (int(a) + int(b)):
                    attempts += 1
                    print("EEE")
                else:
                    solved += 1
                    attempts = 0
                    break
            # Catching any kind of valye error
            except ValueError:
                print("EEE")
                attempts += 1
                continue
    print(f"Score: {solved}")


def get_level():
    # User choosing the difficulty level
    while True:
        try:
            level = int(input("Level: "))
            # If the level is between 1 to 3 then accept the input else user will re-enter
            if level <= 3 and level > 0:
                return level

        except ValueError:
            continue


def generate_integer(level):
    # Generating 10 random number as puzzle
    problem_set = []

    # getting the appropriate difficulty from the level
    rint_lo = levelguide[level - 1][level][0]
    rint_hi = levelguide[level - 1][level][1]

    # build a list of problem sets based off of the user's input
    for _ in range(0, 10):
        problem_set.append(
            f"{randint(rint_lo, rint_hi)} + {randint(rint_lo, rint_hi)}")

    return problem_set


if __name__ == "__main__":
    main()
