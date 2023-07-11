# Functions And Variables In Python

## Strings And Parameters

- A string, known as a `str` in Python, is a sequence of text.

```Python
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```

### Formatting Strings

Probably the most elegant way to use strings would be as follows:

```Python
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
```

Notice the f in print(f"hello, {name}"). This f is a special indicator to Python to treat this string a special way, different than previous approaches.

### More On Strings

By utilizing the method strip on name as name = name.strip(), it will strip all the whitespaces on the left and right of the users input. You can modify your code to be:

```Python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")
```

## Functions In Python

In any programming language, functions facilitate code reusability. In simple terms, when you want to do something repeatedly, you can define that something as a function and call that function whenever you need to.

### Python Function Syntax

The following snippet shows the general syntax to define a function in Python:

```Python
def function_name(parameters):
    # What the function does goes here
    return result
```

### Creating Our Own Hello Function

```Python
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
```

### Improving Above Code

```Python
# Create our own function
def hello(to):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)
```

Here, in the first line, you are creating your hello function. This time, however, you are telling the compiler that this function takes a single parameter: a variable called to. Therefore, when you call hello(name) the computer passes name into the hello function as to. This is how we pass values into functions.<br>

### Changing Default To Hello World!

```Python
# Create our own function
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()
```

## Returning Values In Functions

We an imagine many scenarios where you don’t just want a function to perform an action, but also to return a value back to the main function. For example, rather than simply printing the calculation of `x + y`, you may want a function to return the value of this calculation back to another part of your program. This “passing back” of a value we call a `return` value.

```Python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```
