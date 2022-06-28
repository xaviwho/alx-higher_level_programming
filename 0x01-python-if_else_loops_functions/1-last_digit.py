#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number >= 0 else ((-number % 10) * -1)
start = f"Last digit of {number} is {last}"

if last == 0:
    print(f"{start} and is 0")
elif last > 5 and last % 10 != 0:
    print(f"{start} and is greater than 5")
else:
    print(f"{start} and is less than 6 and not 0")
