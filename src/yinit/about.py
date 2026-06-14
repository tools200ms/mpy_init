import sys

class Impl():

    class MICROPYTHON:
        def __init__(self):
            pass

        def __str__(self):
            return "MicroPython"

    class CPYTHON:
        def __init__(self):
            pass

        def __str__(self):
            return "CPython"

    supported = (MICROPYTHON, CPYTHON)

    @classmethod
    def chk(cls):
        impl_name = sys.implementation.name.upper()

        impl_cls = next(
            (impl for impl in cls.supported if impl.__name__ == impl_name),
            None,
        )

        if impl_cls is None:
            raise Exception(f"Unsupported Python implementation: {sys.implementation.name}")

        impl = impl_cls()
        setattr(impl, "supported", cls.supported)

        delattr(cls, 'chk') # After that this function should be removed by GC
        return impl

Impl = Impl.chk()
