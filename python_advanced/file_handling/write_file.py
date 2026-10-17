#!/usr/bin/env python3

"""Read and display contents of UTF-8 textfiles"""


def write_file(filename="", text=""):
    """Read and display contents of UTF-8 textfiles"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
