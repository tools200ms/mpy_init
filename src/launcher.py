import sys
print(sys.path)

import inspect


import main
#from main import run

if __name__ == "__main__":
    print(set(dir()))

    print(f"Module: {main.__name__}\n")

    for name, obj in inspect.getmembers(main):
        if inspect.isfunction(obj):
            print(f"Function : {name}{inspect.signature(obj)}")
        elif inspect.isclass(obj):
            print(f"Class    : {name}")
        elif inspect.ismodule(obj):
            print(f"Module    : {name}")
        else:
            print(f"Variable  : {name} = {obj!r}")

    #run()

