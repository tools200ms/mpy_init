import unittest

from mpy_init.core.node_prototype import NodeSet
from mpy_init.utils.parser import Parser
from mpy_init.utils.parser_error_list import UnitErrorList


class TestConfigParser(unittest.TestCase):
    def test_valid_simple_input(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = "exec_start = value"
        expected = {"exec_start": "value", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_multiple_valid_lines(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = """
        after = value1
        before = value2
        exec_start = ...
        """
        expected = {
            "exec_start": "...",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_accept_non_letter_start(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = """
        # relations goes to NodePrototype: 
        after = value1
        before = value4
        requires = value3
        wants = value5
        
        exec_start = value6
        """
        expected_unitdict = {
            "exec_start": "value6",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected_unitdict)

    def test_ignore_labels_prefixed_with_equal_char(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = """
        description = value1
        #=label2 = value2
        #==-label_3 = value3
        exec_start = echo Test
        """
        expected = {'description': 'value1', 'name': 'test', 'exec_start': 'echo Test'}

        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_preserve_value_spaces(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = "exec_start = value with spaces"
        expected = {"exec_start": "value with spaces", "name": "test"}

        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_trim_spaces(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = "exec_start = value with spaces   "
        expected = {"exec_start": "value with spaces", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

        input_text = "   exec_start = value with spaces   "
        expected = {"exec_start": "value with spaces", "name": "test"}

        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_empty_input(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        expected_minimum = {"exec_start": "...", "name": "test"}

        self.assertEqual(Parser.loadConfigTxt("exec_start=...", 'test').parse().to_dict(), expected_minimum)
        self.assertEqual(Parser.loadConfigTxt("exec_start=...\n\n\n", 'test').parse().to_dict(), expected_minimum)

    def test_value_with_equals(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = "exec_start = value = with = equals"
        expected = {"exec_start": "value = with = equals", "name": "test"}

        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_invalid_line_raises_valueerror(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        invalid_inputs = [
            "before",  # no equals sign
            "before value",  # no equals sign
            "before: value"  # no label
            #"label=",  # no value
        ]

        for invalid_input in invalid_inputs:
            with self.assertRaises(UnitErrorList):
                Parser.loadConfigTxt(invalid_input, 'test').parse()


    def test_ignore_empty_lines_and_comments(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = """
        # This is a comment
        after = value1


        # Another comment
        before = value2

        #; Unix-style comment
        exec_start = value3

        #// C-style comment
        """

        expected = {
            "exec_start": "value3",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)


    def test_only_comments_and_empty_lines(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = """
        # Just a comment

        #; Another comment

        #// One more comment

        exec_start = echo hello
        """

        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), {"name": "test", "exec_start": "echo hello"})


    def test_mixed_content_with_comments(self):
        try:
            Parser.register(NodeSet())
        except RuntimeError:
            pass

        input_text = """
        # Configuration section 1
        before = value1

        #; Configuration section 2
        after = value2
        # Ignored line
        #_invalid = value3
        exec_start = value3

        #// End of configuration
        """

        expected = {
            "exec_start": "value3",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

if __name__ == '__main__':
    unittest.main()
