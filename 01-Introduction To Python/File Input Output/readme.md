# File I/O In Python

## File I/O

- File I/O is the ability of a program to take a file as input or create a file as output.
- Typing in the terminal window `code names.py`:

```Python
name = input("What's your name?" )
print(f"hello, {name}")
```

- Running this code has the desired output. The user can input a name. The output is as expected.
- What if we wanted to allow multiple names to be inputted? To achieve this recall that a list is a data structure that allows us to store multiple values into a single variable.

```Python
names = []

for _ in range(3):
    name = input("What's your name?" )
    names.append(name)

```

- The user will be prompted three times for input. The `append` method is used to add the name to our names list.
- Simplifying above code:

```Python
names = []

for _ in range(3):
    names.append(input("What's your name?" ))
```

- Making list as sorted

```Python
names = []

for _ in range(3):
    names.append(input("What's your name?" ))

for name in sorted(names):
    print(f"hello, {name}")
```

- Once this program is executed, all information is lost. File I/O allows your program to store this information such that it can be used later.

## `open`

- `open` is a functionality built into Python that allows us to open a file and utilize it in our program. The `open` function allows us to open a file such that you can read from it or write to it.
- Enabling file I/O in program:

```Python
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

```

- The `open` function opens a file called `names.txt` with writing enabled, as signified by the `w`. The code above assigns that opened file to a variable called `file`. The line `file.write(name)` writes the name to the text file. The line after that closes the file.
- Ideally, we want to be able to append each of our names to the file. Removing the existing text file by typing `rm names.txt` in the terminal window. Then, modifying our code as follows:

```Python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()
```

- Notice that the only change to our code is that the w has been changed to a for “append”.

## `with`

- The keyword with allows you to automate the closing of a file.
- Modifying above code:

```Python
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    # notice that the line below with is indented.
```

- Up until this point, we have been exclusively writing to a file. Now modifying our code to read from a file:

```Python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)
```

`readlines` has a special ability to read all the lines of a file and store them in a file called lines. Running our program, we will notice that the output is quite ugly. There seem to be multiple line breaks where there should be only one.

- Fixing this error:

```Python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip()) # rstrip has the effect of removing the extraneous line break at the end of each line
```

- Simplifying more the above code:

```Python
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
```

- Improving the code aboveto allow for the sorting of the names:

```Python
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```

- `names` is a blank list where we can collect the names. Each name is appended to the names list in memory. Then, each name in the sorted list in memory is printed.

## `csv`

- CSV stands for “comma separated values”.
- In our terminal window, we type code students.csv which looks like the following:

```
Hermoine,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```

- Typing a new program `code students.py`

```Python
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
```

`rstrip` removes the end of each line in our CSV file. `split` tells the compiler where to find the end of each of our values in our CSV file. row[0] is the first element in each line of our CSV file. row[1] is the second element in each line in our CSV file.

- The above code is effective at dividing each line or “record” of our CSV file. However, it’s a bit cryptic to look at if you are unfamiliar with this type of syntax. Python has built-in ability that could further simplify this code.
- Modifying our code as follows:

```Python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```

- The `split` function actually returns two values: The one before the comma and the one after the comma. Accordingly, we can rely upon that functionality to assign two variables at once instead of one.

- Providing this list as sorted output:

```Python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

```

- We created a list called `students`. We `append` each string to this list. Then, we output a sorted version of our list.
