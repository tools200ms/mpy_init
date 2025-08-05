import unittest

from mpy_init.utils.parser import Parser
from mpy_init.utils.parser_errors import ParserErrorList


class TestConfigParser(unittest.TestCase):
    def test_valid_simple_input(self):
        input_text = "wants = value"
        expected = {"wants": "value", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_multiple_valid_lines(self):
        input_text = """
        after = value1
        before = value2
        """
        expected = {
            "after": "value1",
            "before": "value2",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_accept_non_letter_start(self):
        input_text = """
        after = value1
        before = value4
        requires = value3
        wants = value5
        defines = value6
        """
        expected = {
            "after": "value1",
            "before": "value4",
            "requires": "value3",
            "wants": "value5",
            "defines": "value6",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_ignore_labels_prefixed_with_equal_char(self):
        input_text = """
        description = value1
        #=label2 = value2
        #==-label_3 = value3
        """
        expected = {
            "description": "value1",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_preserve_value_spaces(self):
        input_text = "wants = value with spaces"
        expected = {"wants": "value with spaces", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_trim_spaces(self):
        input_text = "requires = value with spaces   "
        expected = {"requires": "value with spaces", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

        input_text = "   requires = value with spaces   "
        expected = {"requires": "value with spaces", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_empty_input(self):
        self.assertEqual(Parser.loadConfigTxt("", 'test').parse().to_dict(), {"name": "test"})
        self.assertEqual(Parser.loadConfigTxt("\n\n\n", 'test').parse().to_dict(), {"name": "test"})

    def test_value_with_equals(self):
        input_text = "description = value = with = equals"
        expected = {"description": "value = with = equals", "name": "test"}
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)

    def test_invalid_line_raises_valueerror(self):
        invalid_inputs = [
            "before",  # no equals sign
            "before value",  # no equals sign
            "before: value"  # no label
            #"label=",  # no value
        ]

        for invalid_input in invalid_inputs:
            with self.assertRaises(ParserErrorList):
                Parser.loadConfigTxt(invalid_input, 'test').parse()

#if __name__ == '__main__':
 #   unittest.main()

    def test_ignore_empty_lines_and_comments(self):
        input_text = """
        # This is a comment
        after = value1


        # Another comment
        before = value2

        #; Unix-style comment
        wants = value3

        #// C-style comment
        """

        expected = {
            "after": "value1",
            "before": "value2",
            "wants": "value3",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)


    def test_only_comments_and_empty_lines(self):
        input_text = """
        # Just a comment

        #; Another comment

        #// One more comment

        """

        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), {"name": "test"})


    def test_mixed_content_with_comments(self):
        input_text = """
        # Configuration section 1
        before = value1

        #; Configuration section 2
        after = value2
        # Ignored line
        #_invalid = value3
        wants = value3

        #// End of configuration
        """

        expected = {
            "before": "value1",
            "after": "value2",
            "wants": "value3",
            "name": "test"
        }
        self.assertEqual(Parser.loadConfigTxt(input_text, 'test').parse().to_dict(), expected)
