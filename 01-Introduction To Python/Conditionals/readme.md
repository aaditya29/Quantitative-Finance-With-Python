# Conditionals In Python

- Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.

## Creating Parity Function

```Python
def main():
    x = int(input("What's x? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
```

## Pythonic

- In the programming world, there are types of programming that are called “Pythonic” in nature. That is, there are ways to program that are sometimes only seen in Python programming. Consider the following revision to our program:

```Python
def main():
    x = int(input("What's x? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False # Feels more like english language


main()
```

We can further revise our code and make it more and more readable:

```Python
def main():
    x = int(input("What's x? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
```

## match In Python

- Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.

```Python
name = input("What's your name? ")

  if name == "Harry":
      print("Gryffindor")
  elif name == "Hermione":
      print("Gryffindor")
  elif name == "Ron":
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
```

- We can improve this code slightly with the use of the or keyword:

```Python
name = input("What's your name? ")

  if name == "Harry" or name == "Hermione" or name == "Ron":
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
```

- Alternatively, we can use match statements to map names to houses. Consider the following code:

```Python
name = input("What's your name? ")

  match name:
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _: #  _ symbol  will match with any input, resulting in similar behavior as an else statement.
          print("Who?")
```

- We can improve the code:

```Python
name = input("What's your name? ")

  match name:
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
```
