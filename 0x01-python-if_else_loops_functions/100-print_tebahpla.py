#!/usr/bin/python3
for i in range(122, 96, -1):
    oddPosition = 0
    if i % 2 != 0:
        oddPosition = 1
        i = i - 32
    print("{:s}".format(chr(i)), end="")
    if oddPosition == 1:
        i = i + 32
