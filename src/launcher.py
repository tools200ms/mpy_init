import sys
print(sys.path)

import inspect


from main import run
#from main import run

if __name__ == "__main__":
    print(set(dir()))
    run()

