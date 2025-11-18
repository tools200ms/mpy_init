from mpy_init.impl._base import Implementation


class MicroPython(Implementation):

    def __init__(self):
        global const
        const = getattr(__import__('micropython'), 'const')
