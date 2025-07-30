
from mpy_init.utils.parser_errors import LabelEmptyError, LabelTooLongError, LabelDoesNotStartWithLetterError, \
    LabelHasIllegalName


class Label:

    """
    Verify that the label is an alphanumeric string with an allowed '_' character starting with a letter
    """
    @staticmethod
    def check_label(label: str):
        if not label:
            raise LabelEmptyError(None)

        if len(label) > 32:
            raise LabelTooLongError(label)

        if not label[0].isalpha():
            raise LabelDoesNotStartWithLetterError(label)

        if not all(c.isalnum() or c == '_' for c in label):
            raise LabelHasIllegalName(label)
