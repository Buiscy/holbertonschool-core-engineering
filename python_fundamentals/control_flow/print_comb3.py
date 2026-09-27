#!/usr/bin/env python3

for i in range(100):
    a = i % 10
    b = i // 10
    if a > b:
        print("{:02d}".format(i), end=", " if i != 89 else "\n")
