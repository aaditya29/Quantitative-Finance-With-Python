# Regular Expressions In Python

- Regular expressions or “regexes” will enable us to examine patterns within our code. For example, we might want to validate that an email address is formatted correctly. Regular expressions will enable us to examine expressions in this fashion.
- For example `code validate.py`:

```Python
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
```

- `strip` will remove whitespace at the beginning or end of the input. Running this program, we will see that as long as an @ symbol is inputted, the program will regard the input as valid.
- However, one could input @@ alone and the input could be regarded as valid. We could regard an email address as having at least one @ and a . somewhere within it.
- Modifying your code as follows:

```Python
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

```

- Notice that while this works as expected, our user could be adversarial, typing simply `@.` would result in the program returning valid.
- Modifying the code as follows:

```Python
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
```

- The `strip` method is used to determine if username exists and if . is inside the domain variable. Running this program, a standard email address typed in by us could be considered valid. Typing in abc@harvard alone, we’ll find that the program regards this input as invalid.
  Modifying further:

```Python
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

```

- The endswith method will check to see if domain contains .edu. However, a nefarious user could still break our code. For example, a user could type in abc@.edu and it would be considered valid.

- We could keep iterating upon this code ourselves. However, it turns out that Python has an existing library called `re` that has a number of built-in functions that can validate user inputs against patterns.
- One of the most versatile functions within the library `re` is `search`. The `search` library follows the signature `re.search(pattern, string, flags=0)`
- Following this signature, we can modify our code as follows:

```Python
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
```

- This does not increase the functionality of our program at all. In fact, it is somewhat a step back.
- We can further our program’s functionality. However, we need to advance our vocabulary around validation. It turns out that in the world of regular expressions there are certain symbols that allow us to identify patterns. At this point, we have only been checking for specific pieces of text like @. It so happens that many special symbols can be passed to the compiler for the purpose of engaging in validation. A non-exhaustive list of those patterns is as follows:

```
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
```

- Implementing this inside our code:

```Python
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
```

- Notice that we don’t care what the username or domain is. What we care about is the pattern. .+ is used to determine if anything is to the left of the email address and if anything is to the right of the email address. Running our code, typing in abc@, we’ll notice that the input is regarded as invalid as we would hope.
