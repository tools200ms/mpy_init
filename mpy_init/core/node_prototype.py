from mpy_init.core.unit import Unit
from mpy_init.utils.parser_common import ParserCommon
from mpy_init.utils.parser_errors import LabelValueError
from mpy_init.utils.validator import Validators
from mpy_init.utils.validator_errors import ValidationError, ValidatorsNameReDefinitionError


class NodeSet:
    def __init__(self):
        self._nodesp = {}

    def add(self, node_name: str):
        if node_name in self._nodesp:
            nodep = self._nodesp[node_name]
        else:
            nodep = NodePrototype(self)
            self._nodesp[node_name] = nodep

        return nodep
    
    def add_list(self, node_name_list: [str]):
        nodep_list = []

        for name in node_name_list:
            nodep_list.append(self.add(name))

        return nodep_list

    def register(self, name: str, unit: Unit):
        self._nodesp[name] = unit

    def addWeakDep(self):
        pass


    # def prepare(self, nmark, ndeps):
    #     mark = None
    #     for v in self._deps:
    #         if v in self._deps:
    #             return True
    #
    #     self._deps.append(ndeps)


class NodePrototype:
    # Unit node properties:
    _after: list = None
    _before: list = None
    _wants: list = None
    _requires: list = None
    _provides: list = None
    _defines: str = None

    def __init__(self, node_set: NodeSet):
        self._node_set = node_set

    def get_after(self):
        if self._after is None:
            return None
        return ' '.join(self._after)

    def set_after(self, value):
        self._after = \
            self._node_set.add_list(ParserCommon.split_servicenames_to_list(value))

    def get_before(self):
        if self._before is None:
            return None
        return ' '.join(self._before)

    def set_before(self, value):
        self._before = \
            self._node_set.add_list(ParserCommon.split_servicenames_to_list(value))

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

