import unittest

from mpy_init.utils.validator import Validators
from mpy_init.utils.messages import ValidatorsNameDoesNotStartWithLetterError, ValidatorsInvalidNameError, \
    ValidatorsEmptyNameError


class TestPreDefinedUnit(unittest.TestCase):
    def test_validate_Validatorsname(self):
        # Test valid cases
        self.assertTrue(Validators.validateName("ValidName"))
        self.assertTrue(Validators.validateName("valid123"))
        self.assertTrue(Validators.validateName("a__d"))
        self.assertTrue(Validators.validateName("A-"))

        # Test invalid cases
        with self.assertRaises(ValidatorsNameDoesNotStartWithLetterError):
            Validators.validateName("123invalid")  # starts with number
        with self.assertRaises(ValidatorsNameDoesNotStartWithLetterError):
            Validators.validateName("_invalid")  # starts with number
        with self.assertRaises(ValidatorsNameDoesNotStartWithLetterError):
            Validators.validateName("-invalid")  # starts with number

        with self.assertRaises(ValidatorsEmptyNameError):
            Validators.validateName(None)
        with self.assertRaises(ValidatorsEmptyNameError):
            Validators.validateName("")  # empty string

        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName("invalid/name")  # contains underscore
        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName("invalid=name")  # contains hyphen
        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName("invalid space")  # contains space
        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName("#invalid")  # starts with special character
        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName("invalid!")  # contains special character

        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName(" spacebefore")
        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName("spaceafter ")
        with self.assertRaises(ValidatorsInvalidNameError):
            Validators.validateName(" spaceinbeatween ")

if __name__ == '__main__':
    unittest.main()
