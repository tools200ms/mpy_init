import unittest
from mpy_init.utils.parser import Parser


class TestConfigParser(unittest.TestCase):
    def test_valid_simple_input(self):
        input_text = "label = value"
        expected = {"label": "value"}
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_multiple_valid_lines(self):
        input_text = """
        label1 = value1
        label2 = value2
        """
        expected = {
            "label1": "value1",
            "label2": "value2"
        }
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_ignore_non_letter_start(self):
        input_text = """
        label1 = value1
        _label = value2
        123label = value3
        label2 = value4
        """
        expected = {
            "label1": "value1",
            "label2": "value4"
        }
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_ignore_non_alphanumeric_labels(self):
        input_text = """
        label1 = value1
        label-2 = value2
        label_3 = value3
        """
        expected = {
            "label1": "value1"
        }
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_preserve_value_spaces(self):
        input_text = "label = value with spaces"
        expected = {"label": "value with spaces"}
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_trim_spaces(self):
        input_text = "label = value with spaces   "
        expected = {"label": "value with spaces"}
        self.assertEqual(Parser(input_text).parse(), expected)

        input_text = "   label = value with spaces   "
        expected = {"label": "value with spaces"}
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_empty_input(self):
        self.assertEqual(Parser("").parse(), {})
        self.assertEqual(Parser("\n\n\n").parse(), {})

    def test_value_with_equals(self):
        input_text = "label = value = with = equals"
        expected = {"label": "value = with = equals"}
        self.assertEqual(Parser(input_text).parse(), expected)

    def test_invalid_line_raises_valueerror(self):
        invalid_inputs = [
            "label",  # no equals sign
            "label value",  # no equals sign
            "label: value",  # no label
            "label=",  # no value
        ]

        for invalid_input in invalid_inputs:
            with self.assertRaises(ValueError):
                Parser(invalid_input).parse()


if __name__ == '__main__':
    unittest.main()


    def test_ignore_empty_lines_and_comments(self):
        input_text = """
        # This is a comment
        label1 = value1
        = This should be ignorred

        # Another comment
        label2 = value2

        ; Unix-style comment
        label3 = value3

        // C-style comment
        """

        expected = {
            "label1": "value1",
            "label2": "value2",
            "label3": "value3"
        }
        self.assertEqual(Parser(input_text).parse(), expected)


    def test_only_comments_and_empty_lines(self):
        input_text = """
        # Just a comment

        ; Another comment

        // One more comment

        """

        self.assertEqual(Parser(input_text).parse(), {})


    def test_mixed_content_with_comments(self):
        input_text = """
        # Configuration section 1
        key1 = value1

        ; Configuration section 2
        key2 = value2
        # Ignored line
        _invalid = value3
        key3 = value3

        // End of configuration
        """

        expected = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
        self.assertEqual(Parser(input_text).parse(), expected)
