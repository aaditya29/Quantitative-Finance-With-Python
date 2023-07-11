"""
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there is demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, 
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of 
 Bitcoins in USD to four decimal places, using , as a thousands separator.
"""

import sys
import requests

coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    """Let the user ask the price of Bitcoin using sys.argv"""
    print(f"${coindesk(input_logic()):,.4f}")


def input_logic():
    """Check  that the user respects our rules for argv input"""
    try:

        if len(sys.argv) < 2:
            print("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            return float(sys.argv[1])

    # If the argument is anything but a floatable number, let the user know
    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


def coindesk(amount):
    """Sends a get requests to the Coindesk API and return
    the value for the requested amount of Bitcoin"""
    try:
        response = requests.get(coindesk_api)
        data = response.json()
        value = data["bpi"]["USD"]["rate_float"]
        amountvalue = amount * value

    # Let the user know when a request to the API cannot be made
    except requests.RequestException:
        print("Coinbase not available. Please try again in a few minutes.")
        sys.exit()

    return amountvalue


if __name__ == "__main__":
    main()
