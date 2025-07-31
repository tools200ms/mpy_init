

"""
Unit prototype class providing base functionality for unit configuration and validation.
"""
from mpy_init.core.label import Label
from mpy_init.utils.parser_errors import UnknownLabelError


class SyntaxException(Exception):
    """Raised when unit configuration syntax is invalid"""
    pass

class UnitPrototype:
    # Unit description:
    _description: str = "",
    # Unit node properties:
    _after: str = None
    _before: str = None
    _wants: str = None
    _requires: str = None
    _defines: str = None

    # Unit exec parameters:
    _exec_start: str = None,
    _exec_stop: str = None,
    _exec_reload: str = None,
    _pid_file: str = None,

    # MPY pre-defined unit name
    _mpy_package: str = None

    def get_description(self):
        return self._description
    def set_description(self, value):
        self._description = value

    def get_after(self):
        return self._after
    def set_after(self, value):
        self._after = value

    def get_before(self):
        return self._before
    def set_before(self, value):
        self._before = value

    def get_wants(self):
        return self._wants
    def set_wants(self, value):
        self._wants = value

    def get_requires(self):
        return self._requires
    def set_requires(self, value):
        self._requires = value

    def get_defines(self):
        return self._defines
    def set_defines(self, value):
        self._defines = value

    after = property(get_after, set_after)
    before = property(get_before, set_before)
    wants = property(get_wants, set_wants)
    requires = property(get_requires, set_requires)
    defines = property(get_defines, set_defines)

    def get_exec_start(self):
        return self._exec_start
    def set_exec_start(self, value):
        self._exec_start = value

    def get_exec_stop(self):
        return self._exec_stop
    def set_exec_stop(self, value):
        self._exec_stop = value

    def get_exec_reload(self):
        return self._exec_reload
    def set_exec_reload(self, value):
        self._exec_reload = value

    def get_pid_file(self):
        return self._pid_file
    def set_pid_file(self, value):
        self._pid_file = value

    exec_start = property(get_exec_start, set_exec_start)
    exec_stop = property(get_exec_stop, set_exec_stop)
    exec_reload = property(get_exec_reload, set_exec_reload)
    pid_file = property(get_pid_file, set_pid_file)

    def get_mpy_package(self):
        return self._mpy_package
    def set_mpy_package(self, value):
        self._mpy_package = value
    
    mpy_package = property(get_mpy_package, set_mpy_package)

    def setLabel(self, label_name:str, value:str):
        # Can throwException LabelError
        Label.pre_check(label_name, value)

        if not hasattr(self, f"_{label_name}"):
            raise UnknownLabelError(label_name)

        setattr(self, f"_{label_name}", value)

    def update(self):
        # check if ExecUnit or MPY pre-defined unit is declared
        # if self._mpy_package is None and self._exec_start is None:
        #     if not ( and self._exec_stop is None and
        #             self._exec_reload is None and self._pid_file is None):
        #         raise SyntaxException("Predefined-unit declared conflicts with 'exec unit' definitions")
        pass
            #self._unit_type =
