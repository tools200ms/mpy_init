from mpy_init.core.unit import MPUnit


class modules(MPUnit):
    """
    Manages kernel module loading during system initialization.
    Loads additional kernel modules needed for hardware support
    like network devices, power management, GPU etc that were
    not loaded by initramfs.
    """

    def __init__(self):
        super().__init__()
