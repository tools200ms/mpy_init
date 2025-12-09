from mpy_init import ABC

class NamingBaseErrorMesg:
    # name is totally missing
    MISSING_NAME = None
    # name has invalid characters
    INVALID_NAME = None
    # name has all valid characters, but there are limitations that are not fulfiled (e.g. first character can't by letter)
    ILLEGAL_NAME = None
    # name is too long
    TOOLONG_NAME = None
    # name is redefined
    REDEFIN_NAME = None

# section

class LineBaseErrorMsg (NamingBaseErrorMesg):
    INVALID = "Misformatted line {self._line_no}: \n\t{self._line[0:12]}..."

# Validators for parameters:
class LabelBaseErrorMsg (NamingBaseErrorMesg):
    MISSING_NAME = "Label cannot be empty"
    INVALID_NAME = "Configuration error, allowed keywords: after, ...."
    ILLEGAL_NAME = None
    TOOLONG_NAME = "{label_name}' exceeds maximum length of {self._limit} characters"
    # Logic
    UNKNOWN_NAME = "Unknown label '{self._label_name}'"

class ValBaseErrorMsg (NamingBaseErrorMesg):
    MISSING_NAME = "No value provided"
    TOOLONG_NAME = "Too long name: '{self._value}'"

# Values for the 'service' section:
class ServiceErrorMsg (NamingBaseErrorMesg):
    MISSING_NAME = None
    TOOLONG_NAME = "{service_name}' exceeds maximum length of {self._limit} characters"
    INVALID_NAME = "Invalid name: {self._val}\nService name must be alpha-numeric with '-' and '_' characters allowed and must start with a letter."
    ILLEGAL_NAME = "Illegal first character: '{self._name}'\nFirst character for service name must be a letter."
    REDEFIN_NAME = "Re-defined service name: {self._name}\nService names must be unique."

# Values for the 'exec' section

# Logic
# Unknown label '{self._label_name}