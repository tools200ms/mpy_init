
# MicroPython wrappers:
def const(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError("const() accepts only integers")
    return x


from mpy_init.utils import *
