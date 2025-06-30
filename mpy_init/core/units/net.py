from mpy_init.core.unit import MPUnit


class net(MPUnit):
    """
    Network configuration unit that handles network interface setup.
    Responsible for DHCP client initialization and static IP configuration.
    """

    def __init__(self):
        super().__init__()
