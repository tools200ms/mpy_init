

"""
Unit prototype class providing base functionality for unit configuration and validation.
"""
from mpy_init.core.node_prototype import NodeSet
from mpy_init.core.param import Param
from mpy_init.core.unit import ExecUnit, MPUnit
from mpy_init.utils.parser_common import ParserCommon
from mpy_init.utils.validator import Validators
from mpy_init.utils.parser_errors import UnknownLabelError, LabelValueError, MissConfigurationError
from mpy_init.utils.validator_errors import ValidationError


class UnitNameError(Exception):
    """Raised when unit name validation fails"""
    pass


class SyntaxException(Exception):
    """Raised when unit configuration syntax is invalid"""
    pass

class UnitPrototype:
    # Unit description:
    _description: str = "",
    # Unit node properties:
    _after: list = None
    _before: list = None
    _wants: list = None
    _requires: list = None
    _provides: list = None
    _defines: str = None

    # Unit exec parameters:
    _exec_start: str = None
    _exec_stop: str = None
    _exec_reload: str = None
    _pid_file: str = None

    # MPY pre-defined unit name
    _mpy_package: str = None

    def __init__(self, name):
        Validators.validateName(name)
        self._name = name.lower()

    def registerNodeSet(self, node_set: NodeSet):
        self._node_set = node_set

    def get_unitname(self):
        return self._name
    
    def get_description(self):
        return self._description
    def set_description(self, value):
        self._description = value

    def get_after(self):
        if self._after is None:
            return None
        return ' '.join(self._after)
    def set_after(self, value):
        self._after = ParserCommon.split_servicenames_to_list(value)

    def get_before(self):
        if self._before is None:
            return None
        return ' '.join(self._before)
    def set_before(self, value):
        self._before = ParserCommon.split_servicenames_to_list(value)

    def get_wants(self):
        if self._wants is None:
            return None
        return ' '.join(self._wants)
    def set_wants(self, value):
        self._wants = ParserCommon.split_servicenames_to_list(value)

    def get_requires(self):
        if self._requires is None:
            return None
        return ' '.join(self._requires)
    def set_requires(self, value):
        self._requires = ParserCommon.split_servicenames_to_list(value)

    def get_provides(self):
        if self._provides is None:
            return None
        return ' '.join(self._provides)
    def set_provides(self, value):
        self._provides = ParserCommon.split_servicenames_to_list(value)

    def get_defines(self):
        return self._defines
    def set_defines(self, srv_name):
        try:
            Validators.validateName(srv_name)
            self._defines = srv_name.lower()
        except ValidationError as v_err:
            raise LabelValueError(v_err)

    unitname = property(get_unitname)
    description = property(get_description, set_description)
    
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
        Param.pre_check(label_name, value)

        if not hasattr(self, '_' + label_name):
            raise UnknownLabelError(label_name)

        setattr(self, f"_{label_name}", value)

    def to_dict(self) -> dict:
        """Return dictionary containing all set properties"""
        properties = {}

        for attr_name, attr_value in vars(self).items():
            if attr_name.startswith('_') and attr_value is not None:
                properties[attr_name[1:]] = attr_value

        return properties


    def update(self):

        # check if ExecUnit or MPY pre-defined unit is declared
        if self._mpy_package is None and self._exec_start is None:
            raise MissConfigurationError("Missing 'mpy_package' or 'exec_start' definitions.")

        if self._mpy_package is not None and self._exec_start is not None:
            raise MissConfigurationError("Conflicting 'mpy_package' and 'exec_start' definitions.")

        if self._mpy_package is not None and (self._exec_stop is not None or self._exec_reload is not None or self._pid_file is not None):
            raise MissConfigurationError("Conflicting 'mpy_package' and exec unit (exec_*, pid_file) definitions.")

        if self._exec_start:
            unit = ExecUnit(self._exec_start, self._exec_stop, self._exec_reload, self._pid_file, self._description)
        else: # elif self._mpy_package:
            unit = MPUnit.load(self._mpy_package, self.description)

        return unit
