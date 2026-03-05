import sys

class Impl():

    class MICROPYTHON():
        def __init__(self):
            pass

        def __str__(self):
            return "MicroPython"

    class CPYTHON:
        def __init__(self):
            pass

        def __str__(self):
            return "CPython"

    all_supported = (MICROPYTHON, CPYTHON)

    @classmethod
    def chk(cls):
        impl_name = sys.implementation.name.upper()

        if not hasattr(cls, impl_name):
            raise Exception(f"Unsupported Python implementation: {impl_name}")

        impl =  getattr(cls, impl_name)()
        setattr(impl, 'all_supported', cls.all_supported)

        for supported in cls.all_supported:
            setattr(impl, supported.__name__, supported)

        delattr(cls, 'chk') # After that this function should be removed by GC
        return impl

Impl = Impl.chk()
