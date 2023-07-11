"""
FIGlet, named after Frank, Ian, and Glens letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""
import sys
from random import choice
from pyfiglet import Figlet


def main():
    f = Figlet()
    available_fonts = f.getFonts()

    # When there are no arguments passed to argv
    if len(sys.argv) == 1:
        s = input("Input: ").strip()
        f.setFont(font=choice(available_fonts))
        print(f.renderText(s))

    # When parameters are according to correct conditions
    elif len(sys.argv) == 3:
        if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in available_fonts:
            s = input("Input: ").strip()
            f.setFont(font=str(sys.argv[2]))
            print(f.renderText(s))
        else:
            sys.exit("Invalid usage")

    # If incorrect
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
