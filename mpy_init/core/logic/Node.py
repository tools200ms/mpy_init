
from mpy_init.core.node_prototype import NodePrototype
from mpy_init.core.unit import Unit


class Node:

    def __init__(self, node_proto: NodePrototype, unit:Unit):
        back_refs = []
        next_refs = []

        if node_proto.after is not None:
            back_refs.extend(node_proto.after)

        if node_proto.before is not None:
            next_refs.extend(node_proto.before)

        if node_proto.wants is not None:
            back_refs.extend(node_proto.wants)

        if node_proto.requires is not None:
            back_refs.extend(node_proto.requires)

        #self.provides: list = None
        #self.defines: str = None

        self.__unit = unit
        self.__back_refs = set(tuple(back_refs))
        self.__next_refs = set(tuple(next_refs))

    @property
    def unit(self):
        return self.__unit

    @property
    def back_refs(self):
        return self.__back_refs

    @property
    def next_refs(self):
        return self.__next_refs

    # def __eq__(self, other):
    # compare with Python references

    def __lt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented

        other_has_after = self.next_refs.intersection(other.back_refs)
        other_has_before = self.back_refs.intersection(other.next_refs)

        o_after_cnt = len(other_has_after)
        o_before_cnt = len(other_has_before)

        if o_after_cnt != 0 and o_before_cnt != 0:
            raise SyntaxError('f"Direct circular dependency detected"')

        return o_after_cnt == 0

    def __gt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented

        other_has_before = self.back_refs.intersection(other.next_refs)
        other_has_after = self.next_refs.intersection(other.back_refs)

        o_before_cnt = len(other_has_before)
        o_after_cnt = len(other_has_after)

        if o_before_cnt != 0 and o_after_cnt != 0:
            raise SyntaxError('f"Direct circular dependency detected"')

        return o_before_cnt == 0

