

"""
Unit prototype class providing base functionality for unit configuration and validation.
"""
from mpy_init.core.node_prototype import NodeSet, NodePrototype
from mpy_init.core.param import Param
from mpy_init.core.unit import ExecUnit, MPUnit
from mpy_init.utils.validator import Validators
from mpy_init.utils.parser_errors import UnknownLabelError, LabelValueError, MissConfigurationError


class UnitNameError(Exception):
    """Raised when unit name validation fails"""
    pass


class SyntaxException(Exception):
    """Raised when unit configuration syntax is invalid"""
    pass

class UnitPrototype:
    _name: str = None
    # Unit description:
    _description: str = None

    # Unit exec parameters:
    _exec_start: str = None
    _exec_stop: str = None
    _exec_reload: str = None
    _pid_file: str = None

    # MPY pre-defined unit name
    _mpy_package: str = None

    def __init__(self, name, node_set: NodeSet):
        Validators.validateName(name)
        self._name = name.lower()

        self._node_proto = node_set.add(name)

    def getNodeProto(self):
        return self._node_proto

    def get_unitname(self):
        return self._name
    
    def get_description(self):
        return self._description
    def set_description(self, value):
        self._description = value

    
    unitname = property(get_unitname)
    description = property(get_description, set_description)


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

    set_after = lambda self, value: self._node_proto.set_after(value)
    set_before = lambda self, value: self._node_proto.set_before(value)
    set_wants = lambda self, value: self._node_proto.set_wants(value)
    set_requires = lambda self, value: self._node_proto.set_requires(value)
    set_provides = lambda self, value: self._node_proto.set_provides(value)
    set_defines = lambda self, value: self._node_proto.set_defines(value)

    def get_mpy_package(self):
        return self._mpy_package
    def set_mpy_package(self, value):
        self._mpy_package = value
    
    mpy_package = property(get_mpy_package, set_mpy_package)

    def setLabel(self, label_name:str, value:str):
        # Can throwException LabelError
        Param.pre_check(label_name, value)
        set_fun = 'set_' + label_name

        if not hasattr(self, set_fun):
            raise UnknownLabelError(label_name)

        getattr(self, set_fun)(value)
        #setattr(self, label_name, value)

    def to_dict(self) -> dict:
        """Return dictionary containing all set properties"""
        properties = {}

        for attr_name, attr_value in vars(self).items():
            if  attr_name.startswith('_') and \
                attr_value is not None and \
                isinstance(attr_value, (str, int, float) ):
                properties[attr_name[1:]] = attr_value

        return properties

    @staticmethod
    def loadMPUnit(name, description, values=()):
        try:
            import mpy_init.core.units
            cls = getattr(mpy_init.core.units, name)

            return cls(description, *values)
        except AttributeError:
            raise MissConfigurationError(f"Package '{name}' not found in predefined units")

    def update(self):

        # check if ExecUnit or MPY pre-defined unit is declared
        if self._mpy_package is None and self._exec_start is None:
            raise MissConfigurationError("Missing 'mpy_package' or 'exec_start' definitions.")

        if self._mpy_package is not None and self._exec_start is not None:
            raise MissConfigurationError("Conflicting 'mpy_package' and 'exec_start' definitions.")

        if self._mpy_package is not None and (self._exec_stop is not None or self._exec_reload is not None or self._pid_file is not None):
            raise MissConfigurationError("Conflicting 'mpy_package' and exec unit (exec_*, pid_file) definitions.")

        if self._exec_start:
            unit = ExecUnit(self._exec_start, self._exec_stop, self._exec_reload, self._pid_file,
                            self._name, self._description)
        else: # elif self._mpy_package:
            unit = UnitPrototype.loadMPUnit(self._mpy_package, self.description)

        return unit, self._node_proto

    def isConflicting(self):
        self._node_proto