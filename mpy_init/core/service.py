from mpy_init.utils.parser_errors import ServiceEmptyNameError, ServiceNameDoesNotStartWithLetterError, \
    ServiceInvalidNameError


class Service:
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
            raise ServiceEmptyNameError()

        if not all(c.isalnum() or c == '_' or c == '-' for c in name):
            raise ServiceInvalidNameError(name)

        if not name[0].isalpha():
            raise ServiceNameDoesNotStartWithLetterError(name)

        return True
