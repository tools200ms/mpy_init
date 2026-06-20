# cython: language_level=3

# __package__ = "yinit"
# __name__ = __package__ + ".__main__"
import sys
import yinit.runenv as runenv

def main():
    if len(sys.argv) < 2:
         print("Usage: app.py <name>")
         return 1

    print(f"Hello, {sys.argv[1]}!")
    print(runenv.Impl)

    return 0


print(__name__)      # module name
print(__package__)   # package name

if __name__ == "__main__":
    main()


