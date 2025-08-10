from mpy_init.core.unit_prototype import UnitPrototype


class GraphBuilder:
    def __init__(self):
        self._units = {}

    def add(self, up: UnitPrototype):
        if up.unitname in self._units:
            raise GraphBuilderUnitRedefinitionError(up.unitname)

        self._units[up.unitname] = up


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
