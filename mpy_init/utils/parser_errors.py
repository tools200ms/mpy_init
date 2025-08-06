from mpy_init.utils.validator_errors import ValidationError


# Value error while parsing the config file
class ConfigError (ValueError):
    _line_no: int

    def __init__(self, line_no: int = -1):
        self._line_no = line_no

    def addLineNo(self, line_no: int):
        self._line_no = line_no

    def __str__(self):
        return f"    at line: '{self._line_no}, "

class MisformattedLineError(ConfigError):
    _line: str

    def __init__(self, line_no, line:str):
        super().__init__(line_no)
        self._line = line
    
    def __str__(self):
        return f"Misformatted line {self._line_no}: \n\t{self._line[0:12]}..."

class LabelError(ConfigError):
    serror: ValidationError

    def __init__(self, name: str):
        self._label_name = name

    # def __init__(self, v_err: ValidationError):
    #     self.serror = v_err

class LabelEmptyError(LabelError):
    def __str__(self):
        return "Label cannot be empty"

class LabelTooLongError(LabelError):
    def __str__(self):
        return f"{super().__str__()} label '{self._label_name[0:36]} ...' exceeds maximum length of 32 characters"

class LabelDoesNotStartWithLetterError(LabelError):
    def __str__(self):
        return f"{super().__str__()} incorrect label name, it must start with a letter, found: '{self._label_name}'"

class LabelHasIllegalName(LabelError):
    def __str__(self):
        return f"{super().__str__()} label '{self._label_name}' contains illegal characters - only alphanumeric characters and underscores are allowed"

class UnknownLabelError(LabelError):
    def __str__(self):
        return f"{super().__str__()} Unknown label '{self._label_name}'"


class LabelValueError(LabelError):
    serror: ValidationError

    def __init__(self, v_err: ValidationError):
        self.serror = v_err

    def addLabel(self, name:str):
        self._label_name = name

