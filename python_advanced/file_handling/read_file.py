#!/usr/bin/env python3

"""Read and display contents of UTF-8 textfiles"""


def read_file(filename=""):
    """Prints contents of textfile"""
    with open(filename, 'r', encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
