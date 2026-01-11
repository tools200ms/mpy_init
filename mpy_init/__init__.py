from .sys import about
from .sys import *

from .utils import *
from .abc import *


__version__ = "0.1.0"


if about.Impl == about.Impl.MICROPYTHON:
    const = getattr(__import__('micropython'), 'const')
else:
    const = lambda x: x

print(about.Impl)
