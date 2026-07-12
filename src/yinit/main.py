# cython: language_level=3

import sys


def main():
    if len(sys.argv) < 2:
         print("Usage: app.py <name>")
         return 1

    print(f"Hello, {sys.argv[1]}!")

    return 0



