from mpy_init.core.unit import PreDefinedUnit


class fsck(PreDefinedUnit):
    """
    Performs filesystem checks and repairs if necessary.
    Remounts filesystems as read-write and initializes swap space.
    Runs after device filesystem is mounted and before additional services start.
    """

    def __init__(self):
        super().__init__(('early', 'dev_mount'))
