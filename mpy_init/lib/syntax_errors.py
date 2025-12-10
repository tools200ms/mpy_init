
"""
# name is totally missing
    MISSING = None
    # name has invalid characters
    INVALID = None
    # name has all valid characters, but there are limitations that are not fulfiled (e.g. first character can't by letter)
    ILLEGAL = None
    # name is too long
    TOOLONG = None
    # name is redefined
    REDEFIN = None

"""
from mpy_init.utils.parser_errors import HyInitSyntaxError, HyLineError, HyLabelError, HyValueError


# syntax level:
#    line interpretation issue
#    label interpretation issue
#    value of label interpretation issue
#    service (value) interpretation issue

class LineSyntaxError (HyLineError):
    def invalid(self): return f"Misformatted line {self._line_no}: \n\t{self._line[0:12]}..."

# Validators for parameters:
class LabelSyntaxError (HyLabelError):
    def missing(self): return "Label cannot be empty"
    def invalid(self): return "Configuration error, allowed keywords: after, ...."
    #ILLEGAL_NAME
    def toolong(self): return f"'{self._label[:8]}...' exceeds maximum length of 32 characters"

    # Logic
    #UNKNOWN_NAME = "Unknown label '{self._label_name}'"

class ValError (HyValueError):
    def missing(self): return "No value provided"
    def toolong(self): return f"Too long name: '{self._val}'"

# Values for the 'service' section:
class ServiceError (HyValueError):
    # MISSING_NAME = None
    def invalid(self): return f"Invalid name: {self._val}\nService name must be alpha-numeric with '-' and '_' characters allowed and must start with a letter."
    def illegal(self): return f"Illegal first character: '{self._val}'\nFirst character for service name must be a letter."
    def toolong(self): return f"{self._val}' exceeds maximum length of 32 characters"
    def redefin(self): return f"Re-defined service name: {self._val}\nService names must be unique."

# Values for the 'exec' section

# Logic
# Unknown label '{self._label_name}