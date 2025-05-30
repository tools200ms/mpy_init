

from mpy_init.unit import Unit


class Target(Unit):
    def __init__(self, requires: tuple(str), wants: tuple(str) = None):
        pass

class Sysinit(Target):
    def __init__(self):
        self.__init__(('dev',))

class Basic(Target):
    pass

class Natwork(Target):
    def __init__(self):
        self.__init__(('network',))

class Online(Target):
    def __init__(self):
        self.__init__(('online',))

class Multiuser(Target):
    pass

class Shutdown(Target):
    pass

class Reboot(Target):
    pass

class Rescue(Target):
    pass

