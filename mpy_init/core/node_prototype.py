
class NodeSet:

    def __init__(self):
        self._nodes = {}

    def register(self, name, unit = None):
        pass

    def addWeakDep(self):
        pass

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

    def __init__(self, name):
        self._deps = []

    def prepare(self, nmark, ndeps):
        mark = None
        for v in self._deps:
            if v in self._deps:
                return True

        self._deps.append(ndeps)


    def get_description(self):
        return self._description
    def set_description(self, value):
        self._description = value

    def get_after(self):
        return self._after
    def set_after(self, lst):
        self._after = self.prepare(lst)

    def get_before(self):
        return self._before
    def set_before(self, lst):
        self._before = self.prepare(lst)

    def get_wants(self):
        return self._wants
    def set_wants(self, lst):
        self._wants = self.prepare(lst)

    def get_requires(self):
        return self._requires
    def set_requires(self, lst):
        self._requires = self.prepare(lst)

    def get_provides(self):
        return self._provides
    def set_provides(self, lst):
        self._provides = self.prepare(lst)

    def get_defines(self):
        return self._defines
    def set_defines(self, name):
        self._defines = name

    description = property(get_description, set_description)
    after = property(get_after, set_after)
    before = property(get_before, set_before)
    wants = property(get_wants, set_wants)
    requires = property(get_requires, set_requires)
    provides = property(get_provides, set_provides)
    defines = property(get_defines, set_defines)

