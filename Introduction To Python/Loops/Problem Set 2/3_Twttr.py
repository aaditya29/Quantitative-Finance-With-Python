"""
When texting or tweeting, its not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

vowels = ["a", "e", "i", "o", "u"]


def main():
    
    full_text = input("Input: ").strip()
    print(f"Output: {vwlrmvr(full_text)}")


def vwlrmvr(input):
  
    new_string = ""
    for letter in input:
        if letter.lower() not in vowels:
            new_string += letter

    return new_string


main()
"""

vowels = ["a", "e", "i", "o", "u"]


def main():
    original_text = input("Input: ").strip()
    print(f"Output: {vowel_removed(original_text)}")


def vowel_removed(input):
    removed_string = ""
    for letter in input:
        if letter.lower() not in vowels:
            removed_string += letter
    return removed_string


main()
