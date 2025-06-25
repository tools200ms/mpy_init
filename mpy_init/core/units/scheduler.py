from mpy_init.core.unit import PreDefinedUnit


class Scheduler(PreDefinedUnit):
    """
    Unit responsible for system scheduling and task management.
    Handles initialization and configuration of system scheduler.
    """

    def __init__(self):
        super().__init__(('modules',))
