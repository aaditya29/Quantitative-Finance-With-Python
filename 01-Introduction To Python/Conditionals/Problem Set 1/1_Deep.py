"""
“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You are really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

— The Hitchhiker Guide to the Galaxy, Douglas Adams

In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

meaning = ["forty-two", "forty two", "42"]


def main():
    question = str(input("What is the meaning of life? ").strip().lower())
    """Strip() method in Python removes or truncates the given characters from the beginning and the end of the original string. 
    The lower() method returns a string where all characters are lower case. 
    """
    thinking(question)


def thinking(question):
    if question not in meaning:
        print("No")
    else:
        print("Yes")


main()
