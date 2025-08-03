from abc import ABC, abstractmethod


"""
    Defines unit file parameters: 
        'description'
"""

class Unit(ABC):
    _description: str

    # Start service after "__after" but does not imply a dependency.
    __after: tuple() # Unit
    # Start service before "__before".
    __before: tuple() # Unit

    # Weak dependency, if "__wants" service is missing, starts anyway.
    __wants: tuple() # Unit
    # Strong dependency, "__requires" is requied to start service.
    __requires: tuple() # Unit

    __provides: tuple() # Target

    def __init__(self, description: str = ""):
        self._description = description

    @abstractmethod
    def run(self) -> None:
        """Execute unit action"""
        pass

class ExecUnit(Unit):
   
    _exec_start: str
    _exec_stop: str
    _exec_reload: str
    _pid_file: str

    def __init__(self, exec_start: str, exec_stop: str = "", exec_reload: str = "",
                 pid_file: str = "", description: str = ""):
        self._description = description
        self._exec_start = exec_start
        self._exec_stop = exec_stop
        self._exec_reload = exec_reload
        self._pid_file = pid_file

    def run(self) -> None:
        pass

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def exec_start(self) -> str:
        return self._exec_start

    @exec_start.setter
    def exec_start(self, value: str):
        self._exec_start = value

    @property
    def exec_stop(self) -> str:
        return self._exec_stop

    @exec_stop.setter
    def exec_stop(self, value: str):
        self._exec_stop = value

    @property
    def pid_file(self) -> str:
        return self._pid_file

    @pid_file.setter
    def pid_file(self, value: str):
        self._pid_file = value



class MPUnit(Unit):
    @staticmethod
    def find(name, value):
        try:
            import mpy_init.core.units
            return getattr(mpy_init.core.units, name)
        except AttributeError:
            return None

    def run(self) -> None:
        pass

