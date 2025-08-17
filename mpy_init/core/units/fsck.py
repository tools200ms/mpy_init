from mpy_init.core.unit import MPUnit


class fsck(MPUnit):
    """
    Performs filesystem checks and repairs if necessary.
    Remounts filesystems as read-write and initializes swap space.
    Runs after device filesystem is mounted and before additional services start.
    """

    def __init__(self, description: str):
        super().__init__(description)

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def reload(self):
        pass
