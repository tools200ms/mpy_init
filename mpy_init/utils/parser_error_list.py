import sys
from abc import ABC, abstractmethod

from mpy_init.utils.parser_errors import LabelValueError

class ErrorList:
    def __init__(self):
        self._error_list = []

    def __len__(self):
        return len(self._error_list)

    def __iter__(self):
        return iter(self._error_list)

    def append(self, error: Exception):
        self._error_list.append(error)

    def cntErrors(self):
        total = 0
        for error in self._error_list:
            if isinstance(error, ErrorList):
                total += error.cntErrors()
            else:
                total += 1
        return total

    def hasErrors(self):
        return len(self._error_list) > 0


class ConfigErrorList(Exception, ErrorList):
    def __init__(self):
        ErrorList.__init__(self)

    def __str__(self):
        msg = f"Found {self.cntErrors()} error(s): \n"
        for err in self._error_list:
            msg += f"{err}"

        return msg

# List of errors found in unit configuration (file)
class UnitErrorList(Exception, ErrorList):

    def __init__(self, file_path: str):
        ErrorList.__init__(self)
        self._file_path = file_path

    def __str__(self):
        error_messages = []
        for error in self._error_list:
            error_messages.append(str(error))
        return f"File '{self._file_path}':\n" + "\n".join(error_messages) + "\n"

# Errors found for a single label
class LabelValueErrorList(LabelValueError, ErrorList):
    pass
    # TODO add __str__ for printing cumulated messages
