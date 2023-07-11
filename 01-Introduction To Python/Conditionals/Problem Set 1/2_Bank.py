"""
In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isnt greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isnt a “hello,” and so he asks for $100. The banks manager proposes a compromise: “You got a greeting that starts with an h, how does $20 sound?” Kramer accepts.

In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the users greeting, and treat the users greeting case-insensitively.
"""


def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${penalty(greeting)}")


def penalty(greeting):
    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


main()
