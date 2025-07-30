
class ParserErrorList (Exception):
    _file_path = None

    def __init__(self, errors: list[Exception]):
        self._errors = errors

    def addFilePath(self, file_path: str):
        self._file_path = file_path


class ConfigParserError (Exception):
    _line_no = -1

    def addLineNo(self, line_no: int):
        self._line_no = line_no

class LabelError(ConfigParserError):

    def __init__(self, name: str):
        self._label_name = name

class LabelEmptyError(LabelError):
    def __str__(self):
        return "Label cannot be empty"

class LabelTooLongError(LabelError):
    def __str__(self):
        return f"Label '{self._label_name[0:36]} ...' exceeds maximum length of 32 characters"

class LabelDoesNotStartWithLetterError(LabelError):
    def __str__(self):
        return f"Incorrect label name, it must start with a letter, found: '{self._label_name}'"

class LabelHasIllegalName(LabelError):
    def __str__(self):
        f"Label '{self._label}' contains illegal characters - only alphanumeric characters and underscores are allowed"
