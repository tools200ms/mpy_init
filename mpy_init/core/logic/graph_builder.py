from mpy_init.core.logic.Node import Node
from mpy_init.core.node_prototype import NodePrototype
from mpy_init.core.unit import Unit


class GraphBuilder:
    def __init__(self):
        self._nodes = []


    def set_target(self, target_name: str):
        self._target_name = target_name

    def add(self, u: Unit, nodep: NodePrototype):

        if self._target_name is None:
            raise RuntimeError("Target name must be set before adding units")

        node = Node(nodep, u);
        #for n in set(node.back_refs) & set(self._nodes):


        self._nodes.append(node)

    
    def scratch(self):
        scratched = []
        self._nodes.sort()

        for node in self._nodes:
            scratched.append(node.unit)

        return tuple(scratched)


class GraphBuilderError(Exception):
    pass

class GraphBuilderUnitRedefinitionError(GraphBuilderError):
    def __init__(self, unit_name: str):
        self._unitname = unit_name

    def __str__(self):
        return f"Re-definition of unit: {self._unitname}"
