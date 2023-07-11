# Exceptions In Python

- Exceptions are things that go wrong within our coding.

## Runtime Errors

Runtime errors refer to those created by unexpected behavior within your code.
For example, perhaps you intended for a user to input a number, but they input a character instead. Our program may throw an error because of this unexpected input from the user.

If we run run code `number.py`

```Python
x = int(input("What's x? "))
print(f"x is {x}")
```

Notice that by including the f, we tell Python to interpolate what is in the curly braces as the value of x. Further, testing out our code, we can imagine how one could easily type in a string or a character instead of a number. Even still, a user could type nothing at all – simply hitting the enter key.
As programmers, we should be defensive to ensure that our users are entering what we expected. We might consider “corner cases” such as `-1, 0` or `cat`
If we run this program and type in “cat”, we’ll suddenly see `ValueError: invalid literal for int() with base 10: cat`

Essentially, the Python interpreter does not like that we passed “cat” to the print function.
An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.

## try

- In Python `try` and `except` are ways of testing out user input before something goes wrong.<br>
  For Example:

```Python
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

When we run this code, inputting 50 will be accepted. However, typing in cat will produce an error visible to the user, instructing them why their input was not accepted.

- This is still not the best way to implement this code. Notice that we are trying to do two lines of code.<br>
  For best practice, we should only try the fewest lines of code possible that we are concerned could fail.

  Editing our code as:

```Python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```

## else

- It turns out that there is another way to implement `try` that could catch errors of this nature. <br>
  Editing our code as:

```Python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

If no exception occurs, it will then run the block of code within `else`.

- Notice that we are being a bit rude to our user. If our user does not cooperate, we currently simply end our program. Consider how we can use a loop to prompt the user for x and if they don’t prompt again.<br>
  Improving our code as follows:

```Python
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```

Notice that `while True` will loop forever. If the user succeeds in supplying the correct input, we can break from the loop and then print the output. Now, a user that inputs something incorrectly will be asked for input again.

## Creating a Function to Get an Integer

- If we want to get an integer from our user we can modify our code as follows:

```Python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
```

Here we are manifesting many great properties. First, we have abstracted away the ability to get an integer. Now, this whole program boils down to the first three lines of the program.

- Somehow we can still improve this program. Consider what else we could do to improve this program.
- Modifying our code as follows:

```Python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
```

That return will not only `break` us out of a loop, but it will also return a value.

## pass

- We can make it such that our code does not warn our user, but simply re-asks them our prompting question by modifying our code as follows:

```Python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass


main()
```

- Our code will still function but will not repeatedly inform the user of their error. In some cases, you’ll want to be very clear to the user what error is being produced. Other times, you might decide that you simply want to ask them for input again.

## Function Arguments

- Final refinement that could improve the implementation of this get_int function. Right now, notice that we are relying currently upon the honor system that the x is in both the main and get_int functions. We probably want to pass in a prompt that the user sees when asked for input.
- Modifying our code as follows:

```Pythondef main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
```
