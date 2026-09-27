#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)
last = abs(number) % 10
digit = 0

if number < 0:
    digit = last * -1
else:
    digit = last

if digit == 0:
    print(f"Last digit of {number} is 0 and is 0")

elif digit <= 5:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")

elif digit >= 6:
    print(f"Last digit of {number} is {digit} and is greater than 5")
