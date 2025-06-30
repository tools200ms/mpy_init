from mpy_init.core.unit import MPUnit


class sysfs(MPUnit):


    """
    Mounts essential /sys filesystem providing kernel and hardware information
    """

    def __init__(self):
        super().__init__()
