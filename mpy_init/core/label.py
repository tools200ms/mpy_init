
from mpy_init.utils.parser_errors import LabelEmptyError, LabelTooLongError, LabelDoesNotStartWithLetterError, \
    LabelHasIllegalName


class Label:
    """
    Verify that the label is an alphanumeric string with an allowed '_' character starting with a letter
    """
    @staticmethod
    def pre_check(label: str, value: str):
        if not label:
            raise LabelEmptyError(None)

        if len(label) > 32:
            raise LabelTooLongError(label)

        if not label[0].isalpha():
            raise LabelDoesNotStartWithLetterError(label)

        if not all(c.isalnum() or c == '_' for c in label):
            raise LabelHasIllegalName(label)

        if len(value) > 32:
            raise LabelTooLongError(label)
