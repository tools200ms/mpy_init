from mpy_init.utils.validator_errors import ValidatorsEmptyNameError, ValidatorsInvalidNameError, \
    ValidatorsNameDoesNotStartWithLetterError


class Validators:
    @staticmethod
    def validateName(name: str) -> True:
        """
        Validates if the given service name follows the required naming rules.

        Args:
            name (str): Service name to validate.

        Returns:
            bool: True if validation passes.

        Raises:
            ServiceEmptyNameError: If name is empty.
            ServiceInvalidNameError: If name contains invalid characters.
            ServiceNameDoesNotStartWithLetterError: If name doesn't start with a letter.
        """
        # ensure that the name is not an empty value
        if not name:
            raise ValidatorsEmptyNameError()

        if not all(c.isalnum() or c == '_' or c == '-' for c in name):
            raise ValidatorsInvalidNameError(name)

        if not name[0].isalpha():
            raise ValidatorsNameDoesNotStartWithLetterError(name)

        return True