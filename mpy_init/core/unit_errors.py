

class UnitExecError(RuntimeError):
    """Runtime exception for execution errors."""

    def __init__(self, return_code: int = None):
        super().__init__()
        self.__return_code = return_code

    def __str__(self) -> str:
        return f"Execution error occurred with return code: {self.__return_code}"
