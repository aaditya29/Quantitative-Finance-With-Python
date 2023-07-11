# Unit Tests In Python

- Up until now, we have been likely testing our own code using print statements. It’s most common in industry to write code to test your own programs.

```Python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
```

- Creating a new test program by typing code `test_calculator.py` and modify our code in the text editor as follows:

```Python
from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
```
