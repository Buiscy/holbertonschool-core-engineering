#!/usr/bin/env python3

def pow(a, b):

    i = 0
    j = 1

    while i < abs(b):
        j = j * a
        i += 1
    if b < 0:
        j = 1 / j

    return (j)
