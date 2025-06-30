from mpy_init.core.unit import MPUnit


class procfs(MPUnit):
    """
    Mounts essential /sys filesystem required for system and device information
    """

    def __init__(self):
        super().__init__()
