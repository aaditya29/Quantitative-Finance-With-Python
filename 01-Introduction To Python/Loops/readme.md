# Loops In Python

<b>Loops are a way to do something over and over again.</b>

## While-Loop

- The `while` loop is nearly universal throughout all coding languages.
- Such a loop will repeat a block of code over and over again.

```Python
i = 3
while i != 0:
    print("meow")
```

This code will execute print("meow") multiple times, it will never stop! It will loop forever. `while` loops work by repeatedly asking if the condition of the loop has been fulfilled. In this case, the compiler is asking “does i not equal zero?” When you get stuck in a loop that executes forever, you can press `control-c` on your keyboard to break out of the loop.

- To fix this loop that lasts forever, we can edit our code as follows:

```Python
i = 3
while i != 0:
  print("meow")
  i = i - 1
```

Now our code executes properly, reducing `i` by `1` for each “iteration” through the loop. This term iteration has special significance within coding. By iteration, we mean one cycle through the loop. The first iteration is the “0th” iteration through the loop. The second is the “1st” iteration. In programming we count starting with 0, then 1, then 2.

- We can further improve our code as follows:

```Python
i = 1
  while i <= 3:
      print("meow")
      i = i + 1
```

## For Loop

- A for loop is a different type of loop which iterates through a list of items.

## Lists

- Consider the world of Hogwarts from the famed Harry Potter universe. In the text editor, code as follows:

```Python
students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
```

Notice how we have a list of students with their names as above. We then print the student who is at the 0th location, “Hermoine”. Each of the other students are printed as well.

- We can use a loop to iterate over the list as follows:

```Python
students = ["Hermoine", "Harry", "Ron"]

for student in students:
    print(student)
```

## Length

- We can utilize `len` as a way of checking the length of the list called students.

```Python
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```

- Executing this code results in not only getting the position of each student plus one using i + 1, but also prints the name of each student. len allow you to dynamically see how long the list of the students is regardless how much it grows.

## Dictionaries

- `dicts` or dictionaries is a data structure that allows you to associate keys with values where a list is a list of multiple values, a dict associates a key with a value.
- We could use lists alone to accomplish this:

```Python
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]
```

- We can better our code using a dict as follows:

```Python
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
```

- Improving it further

```Python
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student)
```

- Notice how executing this code, the for loop will only iterate through all the keys, resulting in a list of the names of the students.

- To print both values and keys:

```Python
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student]) # students[student] will go to each student’s key and find the value of the their house.
```

- We can clean up the print function by improving our code as follows:

```Python
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")
```
