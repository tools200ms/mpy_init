from mpy_init.utils.messages import ValidationError


# Value error while parsing the config file
class ConfigError (ValueError):
    _line_no: int
    _msg: str

    def __init__(self, msg:str):
        super().__init__(msg)
        self._line_no = -1

    # def __init__(self, line_no: int = -1):
    #     self._line_no = line_no

    def addLineNo(self, line_no: int):
        self._line_no = line_no

    def __str__(self):
        if self._line_no == -1:
            return f"   {self.args[0]}"

        return f"""    at line: {self._line_no}: {type(self)}"""

class MissConfigurationError(ConfigError):
    def __init__(self, msg: str):
        super().__init__(msg)


class MisformattedLineError(ConfigError):
    _line: str

    def __init__(self, line_no, line:str):
        super().__init__(line_no)
        self._line = line
    
    def __str__(self):
        return f"Misformatted line {self._line_no}: \n\t{self._line[0:12]}..."


class NamingError(Exception):
    def __init__(self, msg_templ: str):
        self._msg_templ = msg_templ

    def setProperty(self, arg_name: str, value):
        setattr(self, arg_name, value)

    def __str__(self):
        return self._msg_templ.format(self=self)


class LabelError(ConfigError):
    def __init__(self, name: str):
        self._label_name = name


class ValueError(LabelError):
    serror: ValidationError

    def __init__(self, v_err: ValidationError):
        self.serror = v_err

    def addLabel(self, name:str):
        self._label_name = name

# Errors found for a single label
class MultipleValueError(ValueError):
# accept class LabelValueError
    def __init__(self):
        self.__errors = []

    def addError(self, value: str):
        self.__errors.append(value)

    # TODO add __str__ for printing cumulated messages

