"""
In Massachusetts, home to Harvard University, its possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a 0.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the users input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You are welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

"""


illegal_symbols = [
    " ",
    ".",
    "?",
    "!",
    ",",
    ":",
    ";",
    "(",
    ")",
    "[",
    "]",
    "'",
    "-",
    '"',
    "/",
    "\\",
    "`",
    "@",
    "#",
    "*",
]


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    validated = ""
    numcheck = 0

    # Check the following rules to validate the input
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in illegal_symbols:
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch
                    elif ch.isalpha() and numcheck < 1:
                        validated += ch

    if validated == s:
        return True
    else:
        return False


main()
