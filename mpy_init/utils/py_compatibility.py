# MicroPython wrappers:
import sys

if sys.implementation.name == 'micropython':
    from micropython import const
else:
    def const(x: int) -> int:
        if not isinstance(x, int):
            raise TypeError("const() accepts only integers")
        return x


