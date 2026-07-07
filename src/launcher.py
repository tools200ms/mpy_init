import sys
print(sys.path)

from yinit import *
from main import run

if __name__ == "__main__":
    print(set(dir()))
    run()
