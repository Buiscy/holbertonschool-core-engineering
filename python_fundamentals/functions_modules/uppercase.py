#!/usr/bin/env python3

def uppercase(str):

    for c in str:
        if 97 <= ord(c) <= 122:
            i = ord(c) - 32
        else:
            i = ord(c)
        
        print("{}".format(chr(i)), end="")

    print('')

