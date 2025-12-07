import sys

from mpy_init.dbg.cpython import CPython
from mpy_init.dbg.micropython import MicroPython
from mpy_init.dbg.pypy import PyPy


class Impl:
    # Prevent the class from being instantiated (optional)
    def __init__(self):
        raise TypeError("Status is not instantiable.")

    class micropython(MicroPython): pass
    class cpython(CPython): pass
    class pypy(PyPy): pass

    @staticmethod
    def get():
        impl_name = sys.implementation.name

        if hasattr(Impl, impl_name):
            return getattr(Impl, impl_name)()

        raise Exception(f"Unsupported Python implementation: {impl_name}")
