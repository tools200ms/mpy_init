from mpy_init.core.unit import PreDefinedUnit


class devmount(PreDefinedUnit):
    """
    Mounts essential /dev filesystem and its special files
    """

    def __init__(self):
        super().__init__(('early',))
