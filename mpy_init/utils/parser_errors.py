from mpy_init.utils.validator_errors import ValidatorsNameError


class ParserErrorList (Exception):
    _file_path = None

    def __init__(self, errors: list[Exception], file_path: str):
        self._errors = errors
        self._file_path = file_path

    def __str__(self):
        error_messages = []
        for error in self._errors:
            error_messages.append(str(error))
        return f"Errors in file '{self._file_path}':\n" + "\n".join(error_messages)

# Value error while parsing the config file
class ConfigParserError (ValueError):
    _line_no: int

    def __init__(self, line_no: int = -1):
        self._line_no = line_no

    def addLineNo(self, line_no: int):
        self._line_no = line_no

class MisformattedLineError(ConfigParserError):
    _line: str

    def __init__(self, line_no, line:str):
        super().__init__(line_no)
        self._line = line
    
    def __str__(self):
        return f"Misformatted line {self._line_no}: \n\t{self._line[0:12]}..."

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
        return f"Label '{self._label_name}' contains illegal characters - only alphanumeric characters and underscores are allowed"


class UnknownLabelError(LabelError):
    def __str__(self):
        return f"Unknown label '{self._label_name}'"

class LabelValueError(LabelError):
    def __init__(self):
        super().__init__(None)

    def addLabel(self, name:str):
        self._label_name = name

class LabelSrvNameError(LabelValueError):
    def __init__(self, srv_name_err: ValidatorsNameError):
        self._srv_name_err = srv_name_err

class LabelSrvNameErrorList(LabelSrvNameError):
    def __init__(self, errors: list[ValidatorsNameError]):
        self._errors = errors
    # TODO add __str__ for printing cumulated messages

