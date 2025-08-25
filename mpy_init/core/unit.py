import os

from mpy_init import ABC, abstractmethod
from mpy_init.core.unit_errors import UnitExecError

"""
    Defines unit file parameters: 
        'description'
"""

class Unit(ABC):

    def __init__(self, name: str, description: str = None):
        self._name = name
        self._description = description if description is not None else ""

    def get_name(self):
        return self._name
    def set_name(self, name: str):
        self._name = name

    def get_description(self):
        return self._description
    def set_description(self, description: str):
        self._description = description

    name = property(get_name, set_name)
    description = property(get_description, set_description)

    def isBuildIn(self):
        return isinstance(self, MPUnit)

    @abstractmethod
    def start(self) -> None:
        """Execute unit action"""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Execute unit action"""
        pass

    @abstractmethod
    def reload(self):
        pass
    
    

class ExecUnit(Unit):
   
    _exec_start: str
    _exec_stop: str
    _exec_reload: str
    _pid_file: str

    def __init__(self, exec_start: str, exec_stop: str,
                 exec_reload: str,
                 pid_file: str, 
                 name: str, 
                 description: str = None):

        super().__init__(name, description)
        self._exec_start = exec_start
        self._exec_stop = exec_stop
        self._exec_reload = exec_reload
        self._pid_file = pid_file

    def start(self) -> None:
        res = os.system(self._exec_start)
        if res != 0:
            raise UnitExecError(res)

    def stop(self) -> None:
        res = os.system(self._exec_stop)
        if res != 0:
            raise UnitExecError(res)

    def reload(self):
        res = os.system(self._exec_reload)
        if res != 0:
            raise UnitExecError(res)


class MPUnit(Unit, ABC):
    
    def __init__(self, description: str = None):
        super().__init__(type(self).__name__, description)
