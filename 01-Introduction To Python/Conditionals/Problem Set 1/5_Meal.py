"""
Suppose that youare in a country where it is customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldnt it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether its breakfast time, lunch time, or dinner time. If its not time for a meal, dont output anything at all. Assume that the users input will be formatted in 24-hour time as #:## or ##:##. And assume that each meals time range is inclusive. For instance, whether its 7:00, 7:01, 7:59, or 8:00, or anytime in between, its time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
"""

meal_time = [
    {"meal": "breakfast time", "start hour": 7, "end hour": 8},
    {"meal": "lunch time", "start hour": 12, "end hour": 13},
    {"meal": "dinner time", "start hour": 18, "end hour": 19},
]


def main():
    time = input("Enter current time.")
    time = float(convert(time))

    for dict in meal_time:
        if time >= float(dict["start hour"]) and time <= float(dict["end hour"]):
            print(dict["meal"])
        else:
            continue


def convert(time):
    h, m = time.strip().split(":")
    t = float(h) + (float(m) / 60)
    return f"{t:.2f}"


if __name__ == "__main__":
    main()
