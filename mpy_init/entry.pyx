# cython: language_level=3
from .sys import about

print(__name__)

if __name__ == "__main__":
    print("Hi, I'm embedded.")

    print(about.Impl)

else:
    print("I'm being imported.")
