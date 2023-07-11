"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isnt an accepted denomination.

"""


def main():
    valid_coins = [25, 10, 5]
    cost = 50
    tendered = 0
    # This is a fancy loop, this is a fancy loop, this is a...
    while tendered < cost:
        print(f"Amount Due: {cost - tendered}")
        money = int(input(f"Insert Coin: ").strip())
        if money in valid_coins:
            tendered += money
        else:
            continue
    print(f"Change Owed: {tendered - cost}")


main()
