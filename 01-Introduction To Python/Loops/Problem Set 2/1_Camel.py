"""
In some languages, its common to use camel case (otherwise known as “mixed case”) for variables names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a users name might be called name, a variable for a users first name might be called firstName, and a variable for a users preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the users input will indeed be in camel case.
"""


def main():
    case = input("camelCase: ").strip()
    print(f"snake_case: {snekCase(case)}")


def snekCase(input):
    """ "This function converts input to snake_case"""
    snek = ""
    for letter in input:
        if letter.isupper():
            snek += "_"
            snek += letter.lower()
        else:
            snek += letter

    return snek


main()
