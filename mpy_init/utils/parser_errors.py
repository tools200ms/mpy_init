from mpy_init.utils.parser_error_list import ErrorList


# Value error while parsing the config file
class ConfigError (Exception):
    _line_no: int
    _msg: str

    def __init__(self, msg:str, line_no:int = -1):
        super().__init__(msg)
        self._line_no = line_no

    # def __init__(self, line_no: int = -1):
    #     self._line_no = line_no

    def suplLineNo(self, line_no: int):
        self._line_no = line_no

    def getPosition(self):
        return self._line_no

    def getMesgPos(self):
        if self._line_no == -1:
            return ""

        return f"""at line: {self._line_no}"""

    def getMesg(self):
        # '.format' is not implemented in MicroPython

        return self.args[0].format(self=self)

    def __str__(self):
        return self.getMesg()

class MissConfigurationError(ConfigError):
    def __init__(self, msg: str):
        super().__init__(msg)


class LineError(ConfigError):
    _line: str

    def __init__(self, line_no, line:str):
        super().__init__(line_no)
        self._line = line
    
    def __str__(self):
        return f""

class LabelError(ConfigError):
    def __init__(self, templ, label):
        super().__init__(templ)
        self._label = label

    def suplLabel(self, label: str):
        self._label = label


class ValError(LabelError):
    def __init__(self, templ, val):
        super().__init__(templ, None)
        self._val = val

    #def __str__(self):
    #    return self.args[0]

# Errors found for a single label
class ValListError(ValError, ErrorList):
# accept class LabelValueError
    def __init__(self):
        ErrorList.__init__(self)

    def strip(self):
        if len(self._error_list) == 1:
            return self._error_list[0]
        return self

