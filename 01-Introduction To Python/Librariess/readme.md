# Libraries In Python

## Libraries

- Generally, libraries are bits of code written by us or others we can use in our program.
- Python allows us to share functions or features with others as “modules”.
- If we copy and paste code from an old project, chances are we can create such a module or library that we could bring into our new project.

## random In Python

- random is a library that comes with Python that we could import into our own project.
- So, how do we load a module into our own program? We can use the word import in our program.
- Inside the random module, there is a built-in function called random.choice(seq). random is the module we are importing Inside that module, there is the choice function. That function takes into it a seq or sequence that is a list.

```Python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

- We can improve our code. `from` allows us to be very specific about what we’d like to import. Prior, our import line of code is bringing the entire contents of the functions of random. However, what if we want to only load a small part of a module?

- Modifying our code as follows:

```Python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```

- Here, we now can import just the choice function of `random`
- From that point forward, we no longer need to code random.choice. We can now only code choice alone. choice is loaded explicitly into our program. This saves system resources and potentially can make our code run faster!

- Now consider the function random.randint(a, b). This function will generate a random number between a and b.
- Modifying our code as follows:

```Python
import random

number = random.randint(1, 10)
print(number)
```

- We can introduce into our card random.shuffle(x) where it will shuffle a list into a random order.

```Python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
```

## Statistics

- Python comes with a built-in statistics library.

### Using This Module

- `average` is a function of this library that is quite useful.
- Typing code average.py:

```Python
import statistics

print(statistics.mean([100, 90]))
```

Here, we imported a different library called statistics. The mean function takes a list of values. This will print the average of these values. In your terminal window, type python average.py.

## Command-Line Arguments

- What if we wanted to be able to take input from the command-line? For example, rather than typing python average.py in the terminal, what if we wanted to be able to type python average.py 100 90 and be able to get the average between 100 and 90?
- `sys` is a module that allows us to take arguments at the command line.
- `argv` is a function within the sys module that allows us to learn about what the user typed in at the command line.

```Python
import sys

print("hello, my name is", sys.argv[1])
```

- The program is going to look at what the user typed in the command line. Currently, if you type python name.py David into the terminal window, you will see hello, my name is David. Notice that sys.argv[1] is where David is being stored. Why is that? Well, in prior lessons, you might remember that lists start at the 0th element. What do you think is held currently in sys.argv[0]? If you guessed name.py, you would be correct!
- There is a small problem with our program as it stands. What if the user does not type in the name at the command line?
- Typing python `name.py` into the terminal window. An error list index out of range will be presented by the compiler. The reason for this is that there is nothing at sys.argv[1] because nothing was typed.
- Here’s how we can protect our program from this type of error:

```Python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```

- The user will now be prompted with a useful hint about how to make the program work if they forget to type in a name.

- Improving our program

```Python
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
```

- Now if you test our code, we will see how these exceptions are handled, providing the user with more refined advice. Even if the user types in too many or too few arguments, the user is provided clear instructions about how to fix the issue.

## `slices` In Python

- `slice` is a command that allows us to take a list and tell the compiler where we want the compiler to consider the start of the list and the end of the list.
  For example:

```Python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)
```

- If we type `python name.py David Carter Rongxin` into the terminal window, the compiler will output not just the intended output of the names, but also hello, my name is name.py.

- `slice` can be employed in our code to start the list somewhere different.

```Python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```

- Rather than starting the list at 0, we use square brackets to tell the compiler to start at 1 and go to the end using the 1: argument.

## Packages in Python

- One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.
- PyPI is a repository or directory of all available third-party packages currently available.
- `cowsay` is a well-known package that allows a cow to talk to the user.
- Python has a package manager called pip that allows you to install packages quickly onto your system.
  In the terminal window, we can install the cowsay package by typing `pip install cowsay`. After a bit of output, we can now go about using this package in our code.

```Python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

```

## APIs

- APIs or “application program interfaces” allow you to connect to the code of others.
- `requests` is a package that allows your program to behave as a web browser would.
- It turns out that Apple iTunes has its own API that you can access in our programs. In our internet browser, we can visit `https://itunes.apple.com/search?entity=song&limit=1&term=weezer` and a text file will be downloaded.
- The format in the downloaded text file is called <b>JSON</b>, a text-based format that is used to exchange text-based data between applications. Literally, Apple is providing a JSON file that we could interpret in our own Python program.

```Python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
```

- The returned value of `requests.get` will be stored in response.
- Also Python has a built-in JSON library that can help us interpret the data received.
  Modifying our previous code:

```Python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
```

- The `json.dumps` is implemented such that it utilizes indent to make the output more readable.
