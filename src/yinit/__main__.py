# cython: language_level=3

import sys
from yinit import about

print(__name__)

def main():
    if len(sys.argv) < 2:
        print("Usage: app.py <name>")
        return 1

    print(f"Hello, {sys.argv[1]}!")
    print(about.Impl)

    return 0

if __name__ == "__main__":
    main()
else:
    print("I'm being imported.")
