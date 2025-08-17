from mpy_init.core.unit import MPUnit


class sysfs(MPUnit):


    """
    Mounts essential /sys filesystem providing kernel and hardware information
    """

    def __init__(self, description: str):
        super().__init__(description)

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def reload(self):
        pass
