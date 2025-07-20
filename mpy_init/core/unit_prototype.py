

"""
Unit prototype class providing base functionality for unit configuration and validation.
"""


class SyntaxException(Exception):
    """Raised when unit configuration syntax is invalid"""
    pass


class UnitPrototype:
    # node properties
    _after: str
    _before: str
    _wants: str
    _requires: str
    _defines: str

    _unit_type: None

    def __init__(self,
                 # Unit description:
                 description: str = "",
                 # Unit node properties:
                 after: str = None,
                 before: str = None,
                 wants: str = None,
                 requires: str = None,
                 defines: str = None,

                 # Unit exec parameters:
                 exec_start: str = None,
                 exec_stop: str = None,
                 exec_reload: str = None,
                 pid_file: str = None,

                 # MPY pre-defined unit name
                 mpy_package: str = None
                 ):
        self._after = after
        self._before = before
        self._wants = wants
        self._requires = requires
        self._defines = defines

        # check if ExecUnit or MPY pre-defined unit is declared

        if mpy_package is not None:
            if not (exec_start is None and exec_stop is None and
                    exec_reload is None and pid_file is None):
                raise SyntaxException("Predefined-unit declared conflicts with 'exec unit' definitions")


            #self._unit_type =
