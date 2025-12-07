import sys

_implementation = None

class Implementation:
    @staticmethod
    def micropython():
        global const
        const = getattr(__import__('micropython'), 'const')

    @staticmethod
    def cpython():
        global const
        const = lambda x: x

class Environment:
    # Prevent the class from being instantiated (optional)
    def __init__(self):
        raise TypeError("Status is not instantiable.")

    @staticmethod
    def init():
        global _implementation
        if _implementation is None:
            impl_name = sys.implementation.name

            if not hasattr(Implementation, impl_name):
                raise Exception(f"Unsupported Python implementation: {impl_name}")

            _implementation = getattr(Implementation, impl_name)
            _implementation()

    @staticmethod
    def info():
        global _implementation
        if _implementation is not None:
            return _implementation.__name__

        return None