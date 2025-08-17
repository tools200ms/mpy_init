from mpy_init.core.node_prototype import NodePrototype
from mpy_init.core.unit import Unit


class GraphBuilder:
    def __init__(self):
        self._units = {}
        self._all_units = set()
        self._target_name = None

    def set_target(self, target_name: str):
        self._target_name = target_name

    def add(self, u: Unit, nodep: NodePrototype):
        uname = u.name
        if uname in self._all_units:
            raise GraphBuilderUnitRedefinitionError(uname)

        self._all_units.add(uname)

        if self._target_name is None:
            raise RuntimeError("Target name must be set before adding units")


        self._units[uname] = u
    
    
    def compile(self):
        nodes = []
        for unit_name, unit in self._units.items():
            node = Node(
                name=unit_name,
                after=unit.after,
                requires=unit.requires,
                wants=unit.wants,
                provides=unit.provides,
                defines=unit.defines
            )
            nodes.append(node)
        return nodes


class GraphBuilderError(Exception):
    pass

class GraphBuilderUnitRedefinitionError(GraphBuilderError):
    def __init__(self, unit_name: str):
        self._unitname = unit_name

    def __str__(self):
        return f"Re-definition of unit: {self._unitname}"
