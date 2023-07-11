"""
In The Sound of Music, there is a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isnt grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isnt even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:
 def main():
    p = inflect.engine()
    mylist = []

    while True:

        # Get input from the user
        try:
            user_input = str(input("Name: ")).strip()
            mylist.append(user_input)
        # Catch CTRL+D to end the session
        except (EOFError, KeyError):
            print(f"Adieu, adieu, to {p.join(mylist)}", end="\n")
            quit()


if __name__ == "__main__":
    main()
"""
import inflect  # The Inflect module in Python is used to create plural nouns, singular nouns, ordinals, and indefinite articles, as well as to convert numbers into words.


def main():
    p = inflect.engine()
    mylist = []

    while True:
        # Getting input from the user
        try:
            user_input = str(input("Name: ")).strip()
            mylist.append(user_input)
        except (EOFError, KeyError):
            print(f"Adieu, adieu, to {p.join(mylist)}", end="\n")
            quit()


if __name__ == "__main__":
    main()
