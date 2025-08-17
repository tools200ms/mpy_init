from mpy_init.core.unit import MPUnit


class devmount(MPUnit):
    """
    Mounts essential /dev filesystem and its special files
    """

    def __init__(self, description: str):
        super().__init__(description)
