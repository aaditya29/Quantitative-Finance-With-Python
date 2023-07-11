"""
Problem:
One of the most popular places to eat in Harvard Square is Felipes Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:
{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending ones input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the users input case insensitively. Ignore any input that isnt an item. Assume that every item on the menu will be titlecased.

"""
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    orders = 0
    while True:
        """Making user inputt case insensitive and printing total of the items"""
        try:
            item = input("Item: ").strip().title()
            if item in menu:
                orders += menu[item]
                print(f"${orders:.2f}")
        # Using CATCH ctrl+D to end the session of ordering food
        except (EOFError, KeyError):
            print("", end="\n")
            quit()


main()
