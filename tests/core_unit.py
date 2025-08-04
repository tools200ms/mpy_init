import unittest

from mpy_init.core.service import Service
from mpy_init.utils.parser_errors import ServiceNameDoesNotStartWithLetterError, ServiceEmptyNameError, \
    ServiceInvalidNameError


class TestPreDefinedUnit(unittest.TestCase):
    def test_validate_servicename(self):
        # Test valid cases
        self.assertTrue(Service.validateName("ValidName"))
        self.assertTrue(Service.validateName("valid123"))
        self.assertTrue(Service.validateName("a__d"))
        self.assertTrue(Service.validateName("A-"))

        # Test invalid cases
        with self.assertRaises(ServiceNameDoesNotStartWithLetterError):
            Service.validateName("123invalid")  # starts with number
        with self.assertRaises(ServiceNameDoesNotStartWithLetterError):
            Service.validateName("_invalid")  # starts with number
        with self.assertRaises(ServiceNameDoesNotStartWithLetterError):
            Service.validateName("-invalid")  # starts with number

        with self.assertRaises(ServiceEmptyNameError):
            Service.validateName(None)
        with self.assertRaises(ServiceEmptyNameError):
            Service.validateName("")  # empty string

        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName("invalid/name")  # contains underscore
        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName("invalid=name")  # contains hyphen
        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName("invalid space")  # contains space
        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName("#invalid")  # starts with special character
        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName("invalid!")  # contains special character

        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName(" spacebefore")
        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName("spaceafter ")
        with self.assertRaises(ServiceInvalidNameError):
            Service.validateName(" spaceinbeatween ")

if __name__ == '__main__':
    unittest.main()
