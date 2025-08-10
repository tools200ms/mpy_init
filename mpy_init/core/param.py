
from mpy_init.utils.parser_errors import LabelDoesNotStartWithLetterError, \
    LabelHasIllegalName, ParamTooLongError, ParamEmptyError
from mpy_init.utils.py_compatibility import const


class Param:
    PARAM_LABEL = const(0x1)
    PARAM_VALUE = const(0x2)

    MAX_LABEL_LEN = const(32)
    MAX_VALUE_LEN = const(1024)

    """
    Verify that the label is an alphanumeric string with an allowed '_' character starting with a letter
    """
    @staticmethod
    def pre_check(label: str, value: str):
        if not label:
            raise ParamEmptyError(None)

        if len(label) > Param.MAX_LABEL_LEN:
            raise ParamTooLongError(label, Param.MAX_LABEL_LEN)

        if not label[0].isalpha():
            raise LabelDoesNotStartWithLetterError(label)

        if not all(c.isalnum() or c == '_' for c in label):
            raise LabelHasIllegalName(label)

        # prevalidate value
        # raise ParamEmptyError(label)

        if len(value) > Param.MAX_VALUE_LEN:
            raise ParamTooLongError(label, Param.MAX_VALUE_LEN, value)

        return True
