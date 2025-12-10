from mpy_init.utils.parser_error_list import ErrorList


# Value error while parsing the config file
class HyInitSyntaxError (Exception):
    _line_no: int
    _msg: str

    def __init__(self, msg, line_no: int = -1):
        self.getMesg = msg
        self._line_no = line_no

    # def __init__(self, line_no: int = -1):
    #     self._line_no = line_no

    def suplLine(self, line: str):
        self._line = line

    def suplLineNo(self, line_no: int):
        self._line_no = line_no

    def getPosition(self):
        return self._line_no

    def getMesgPos(self):
        if self._line_no == -1:
            return ""

        return f"""at line: {self._line_no}"""

    def __str__(self):
        return self.getMesg(self)

#class LogicError(ConfigError):
 #   def __init__(self, msg: str, file_path: str):
  #      super().__init__(msg)


class HyLineError(HyInitSyntaxError):
    _line: str

    def __init__(self, msg, line_no: int, line: str):
        super().__init__(msg, line_no)
        self._line = line
    
    def __str__(self):
        return f""

class HyLabelError(HyInitSyntaxError):
    def __init__(self, msg, label):
        super().__init__(msg)
        self._label = label

    def suplLabel(self, label: str):
        self._label = label


class HyValueError(HyLabelError):
    def __init__(self, msg, val):
        super().__init__(msg, None)
        self._val = val

    #def __str__(self):
    #    return self.args[0]

# Errors found for a single label
class ValListError(HyValueError, ErrorList):
# accept class LabelValueError
    def __init__(self):
        ErrorList.__init__(self)

    def strip(self):
        if len(self._error_list) == 1:
            return self._error_list[0]
        return self

