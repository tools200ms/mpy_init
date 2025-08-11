
class NodeSet:

    def __init__(self):
        self._nodes = {}

    def register(self, name, unit = None):
        pass

    def addWeakDep(self):


class NodePrototype:
    # Unit description:
    _description: str = "",
    # Unit node properties:
    _after: list = None
    _before: list = None
    _wants: list = None
    _requires: list = None
    _provides: list = None
    _defines: str = None



    def __init__(self):
        pass
