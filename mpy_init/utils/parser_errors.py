
class ParserErrorList (Exception):
    _file_path = None

    def __init__(self, errors: list[Exception]):
        self._errors = errors

    def addFilePath(self, file_path: str):
        self._file_path = file_path


class ServiceNameError(ValueError):
    def __init__(self, name: str):
        self._name = name

class ServiceEmptyNameError(ServiceNameError):
    def __init__(self):
        super().__init__(None)

    def __str__(self):
        return f"No service name provided"

class ServiceInvalidNameError(ServiceNameError):
    def __str__(self):
        return f"Invalid service name: {self._name}\nService name must be alpha-numeric with '-' and '_' characters allowed and must start with a letter."

class ServiceNameDoesNotStartWithLetterError(ServiceNameError):
    def __str__(self):
        return f"Illegal first character for value: '{self._label_name}'\nFirst character must be a letter."

class ServiceNameTooLongError(ServiceNameError):
    def __str__(self):
        return f"Too long value for label: '{self._label_name}'"

class ServiceNameReDefinitionError(ServiceNameError):
    def __str__(self):
        return f"Re-defined service name: {self._name}\nService names must be unique."


# Value error while parsing the config file
class ConfigParserError (ValueError):
    _line_no = -1

    def addLineNo(self, line_no: int):
        self._line_no = line_no

class MisformattedLineError(ConfigParserError):
    def __init__(self, line_no):
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

class UnknownLabelError(LabelError):
    def __str__(self):
        return f"Unknown label '{self._label_name}'"

class LabelValueError(LabelError):
    def __init__(self):
        super().__init__(None)

    def addLabel(self, name:str):
        self._label_name = name

class LabelSrvNameError(LabelValueError):
    def __init__(self, srv_name_err: ServiceNameError):
        self._srv_name_err = srv_name_err

class LabelSrvNameErrorList(LabelSrvNameError):
    def __init__(self, errors: list[ServiceNameError]):
        self._errors = errors
    # TODO add __str__ for printing cumulated messages

