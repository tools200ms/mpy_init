from mpy_init import const
from mpy_init.lib.messages import LabelBaseErrorMsg, ValBaseErrorMsg, ServiceErrorMsg
from mpy_init.utils.parser_errors import LabelError, ValError


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
            raise LabelError(LabelBaseErrorMsg.MISSING_NAME, None)

        if len(label) > PreCheck.MAX_LABEL_LEN:
            raise LabelError(LabelBaseErrorMsg.TOOLONG_NAME, label[:6] + '...')

        if not all(c.isalpha() or c.isdigit() or c == '_' for c in label):
            raise LabelError(LabelBaseErrorMsg.ILLEGAL_NAME, label)

        if not label[0].isalpha():
            raise LabelError(LabelBaseErrorMsg.INVALID_NAME, label)

        # prevalidate value
        # raise ParamEmptyError(label)

        if not value:
            raise ValError(ValBaseErrorMsg.MISSING_NAME, value)

        if len(value) > PreCheck.MAX_VALUE_LEN:
            raise ValError(ValBaseErrorMsg.TOOLONG_NAME, value)

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
            raise ValError(ServiceErrorMsg.MISSING_NAME, None)

        if len(name) > 32:
            raise ValError(ServiceErrorMsg.TOOLONG_NAME, name[:6] + '...')

        if not all(c.isalpha() or c.isdigit() or c == '_' or c == '-' for c in name):
            raise ValError(ServiceErrorMsg.INVALID_NAME, name)

        if not name[0].isalpha():
            raise ValError(ServiceErrorMsg.ILLEGAL_NAME, name)

        # End of def

