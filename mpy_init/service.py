from mpy_init.target import Target
from mpy_init.unit import Unit


class Service (Unit):
    __description: str

    # Start service after "__after" but does not imply a dependency.
    __after: tuple(Unit)
    # Start service before "__before".
    __before: tuple(Unit)

    # Weak dependency, if "__wants" service is missing, starts anyway.
    __wants: tuple(Unit)
    # Strong dependency, "__requires" is requied to start service.
    __requires: tuple(Unit)

    __provides: tuple(Target)

    __exec_start: str
    __exec_stop: str
    __exec_reload: str

    __pid_file: str

    def __init__(self,  description:str,
                        after: tuple(Unit),
                        before: tuple(Unit),
                        wants: tuple(Unit),
                        requires: tuple(Unit),
                        provides: Target,
                        exec_start: str,
                        exec_stop: str,
                        exec_reload: str,
                        pid_file: str ):
        pass
