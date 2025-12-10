from mpy_init import const
from mpy_init.lib.syntax_errors import LabelSyntaxError, ValError, ServiceError


class PreCheck:
    PARAM_LABEL = const(0x1)
    PARAM_VALUE = const(0x2)

    MAX_LABEL_LEN = const(32)
    MAX_VALUE_LEN = const(1024)

    """
    Verify that the label is an alphanumeric string with an allowed '_' character starting with a letter
    """
    @staticmethod
    def LabelAndValue(label: str, value: str):
        if not label:
            raise LabelSyntaxError(LabelSyntaxError.missing, None)

        if len(label) > PreCheck.MAX_LABEL_LEN:
            raise LabelSyntaxError(LabelSyntaxError.toolong, label[:6] + '...')

        if not all(c.isalpha() or c.isdigit() or c == '_' for c in label):
            raise LabelSyntaxError(LabelSyntaxError.illegal, label)

        if not label[0].isalpha():
            raise LabelSyntaxError(LabelSyntaxError.invalid, label)

        # prevalidate value
        # raise ParamEmptyError(label)

        if not value:
            raise ValError(ValError.missing, value)

        if len(value) > PreCheck.MAX_VALUE_LEN:
            raise ValError(ValError.toolong, value)

        return True

    @staticmethod
    def serviceName(name: str):
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
            raise ServiceError(ServiceError.missing, None)

        if len(name) > 32:
            raise ServiceError(ServiceError.toolong, name[:6] + '...')

        if not all(c.isalpha() or c.isdigit() or c == '_' or c == '-' for c in name):
            raise ServiceError(ServiceError.invalid, name)

        if not name[0].isalpha():
            raise ServiceError(ServiceError.illegal, name)

        # End of def

