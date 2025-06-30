
import unittest
from unit import MPUnit

class TestMPUnit(unittest.TestCase):
    def test_validate_name(self):
        # Test valid cases
        self.assertTrue(MPUnit.validateName("ValidName"))
        self.assertTrue(MPUnit.validateName("valid123"))
        self.assertTrue(MPUnit.validateName("a"))
        self.assertTrue(MPUnit.validateName("A"))
        
        # Test invalid cases
        self.assertFalse(MPUnit.validateName("123invalid"))  # starts with number
        self.assertFalse(MPUnit.validateName(""))  # empty string
        self.assertFalse(MPUnit.validateName("invalid_name"))  # contains underscore
        self.assertFalse(MPUnit.validateName("invalid-name"))  # contains hyphen
        self.assertFalse(MPUnit.validateName("invalid space"))  # contains space
        self.assertFalse(MPUnit.validateName("#invalid"))  # starts with special character
        self.assertFalse(MPUnit.validateName("invalid!"))  # contains special character

if __name__ == '__main__':
    unittest.main()