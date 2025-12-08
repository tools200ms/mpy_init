
class Implementation:
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


def check_implementation():
    import sys
    impl_name = sys.implementation.name.upper()

    if not hasattr(Implementation, impl_name):
        raise Exception(f"Unsupported Python implementation: {impl_name}")

    return getattr(Implementation, impl_name)()

IMPLEMENTATION = check_implementation()

if IMPLEMENTATION == Implementation.MICROPYTHON:
    const = getattr(__import__('micropython'), 'const')
else:
    const = lambda x: x
