# cython: language_level=3


import sys
#import yinit.runenv as runenv

def run():
    if len(sys.argv) < 2:
         print("Usage: app.py <name>")
         return 1

    print(f"Hello, {sys.argv[1]}!")
    #print(runenv.Impl)

    return 0


print(__name__)      # module name
print(__package__)   # package name
print(sys.path)

if __name__ == "__main__":
    run()


