from mpy_init.core.unit import PreDefinedUnit


class SysFS(PreDefinedUnit):
    """
    Mounts essential /sys filesystem providing kernel and hardware information
    """

    def __init__(self):
        super().__init__(('early',))
