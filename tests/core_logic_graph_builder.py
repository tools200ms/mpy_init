import unittest

from mpy_init.core.logic.graph_builder import GraphBuilder
from mpy_init.core.node_prototype import NodeSet
from mpy_init.utils.parser import Parser

class ExtGraphBuilder (GraphBuilder):
    def getTopNode(self):
        return self._nodes[-1]

class TestGraphBuilder(unittest.TestCase):
    def test_order(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        conf_a = "exec_start = echo TestA"
        conf_b = "after=a\nexec_start = echo TestB"
        conf_c = "after=b\nexec_start = echo TestC"

        gb = ExtGraphBuilder()
        gb.set_target('init')

        unit_prototype = Parser.loadConfigTxt(conf_a, 'a').parse()
        gb.add(*unit_prototype.update())
        node_a = gb.getTopNode()

        unit_prototype = Parser.loadConfigTxt(conf_c, 'c').parse()
        gb.add(*unit_prototype.update())
        node_c = gb.getTopNode()

        unit_prototype = Parser.loadConfigTxt(conf_b, 'b').parse()
        node_b = gb.getTopNode()

        gb.add(*unit_prototype.update())

        self.assertTrue(node_a < node_b)
        self.assertFalse(node_a > node_b)
        self.assertTrue(node_b > node_c)
        self.assertFalse(node_b > node_c)

        graph = gb.scratch()

        expected_order = ['a', 'b', 'c']
        tested_order = []

        for unit in graph:
            print(unit.name)
            tested_order.append(unit.name)

        self.assertEqual(tested_order, expected_order)

if __name__ == '__main__':
    unittest.main()
