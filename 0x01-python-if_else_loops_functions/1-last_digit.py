#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 0
if number < 0:
    sign = 1
    number *= -1
lastDigit = number % 10
if sign == 1:
    lastDigit *= -1
    number *= -1
print("Last digit of {:d} is ".format(number), end="")
if lastDigit > 5:
    print("{:d} and is greater than 5".format(lastDigit))
elif lastDigit == 0:
    print("{:d} and is 0".format(lastDigit))
else:
    print("{:d} and is less than 6 and not 0".format(lastDigit))
