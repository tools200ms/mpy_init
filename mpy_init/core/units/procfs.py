from mpy_init.core.unit import PreDefinedUnit


class procfs(PreDefinedUnit):
    """
    Mounts essential /sys filesystem required for system and device information
    """

    def __init__(self):
        super().__init__(('early',))
