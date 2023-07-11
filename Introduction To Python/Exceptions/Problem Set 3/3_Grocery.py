"""
Suppose that you are in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending ones input to a program). Then output the users grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the users input case-insensitively.
"""


def main():
    grocerylist = []
    while True:
        # making list of all the groceries
        try:
            item = input().strip().lower()
            grocerylist.append(item)
        # Using CTRL+D To Stop the output
        # EOFError is raised when one of the built-in functions input() or raw_input() hits an end-of-file condition (EOF) without reading any data.
        except (EOFError, KeyError):
            l = sorted(set(grocerylist))
            for i in l:
                print(f"{grocerylist.count(i)} {i.upper()}")
                quit()


main()
