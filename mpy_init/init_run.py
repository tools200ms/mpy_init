
from mpy_init.sys import about

def main() -> int:
    # System checks first:
    print(about.Impl)
    if about.Impl == about.Impl.MICROPYTHON:
        const = getattr(__import__('micropython'), 'const')
    else:
        const = lambda x: x

