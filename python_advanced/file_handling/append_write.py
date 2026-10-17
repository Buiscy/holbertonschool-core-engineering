#!/usr/bin/env python3

"""Read and display contents of UTF-8 textfiles"""


def append_write(filename="", text=""):
    """Read and display contents of UTF-8 textfiles"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
