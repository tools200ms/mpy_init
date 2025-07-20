from abc import ABC, abstractmethod


"""
    Defines unit file parameters: 
        'description'
"""
class Unit(ABC):
    _description: str

    def __init__(self, description: str = ""):
        self._description = description

    @abstractmethod
    def run(self) -> None:
        """Execute unit action"""
        pass

    @staticmethod
    def validateName(str: str):
        if not str or not str[0].isalpha():
            return False
        return str.isalnum()



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
    def __init__(self):
        pass

    def run(self) -> None:
        pass

