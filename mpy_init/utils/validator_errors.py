

class ValidatorsNameError(ValueError):
    def __init__(self, name: str):
        self._name = name

class ValidatorsEmptyNameError(ValidatorsNameError):
    def __init__(self):
        super().__init__(None)

    def __str__(self):
        return f"No name provided"

class ValidatorsInvalidNameError(ValidatorsNameError):
    def __str__(self):
        return f"Invalid name: {self._name}\nService name must be alpha-numeric with '-' and '_' characters allowed and must start with a letter."

class ValidatorsNameDoesNotStartWithLetterError(ValidatorsNameError):
    def __str__(self):
        return f"Illegal first character: '{self._label_name}'\nFirst character for service name must be a letter."

class ValidatorsNameTooLongError(ValidatorsNameError):
    def __str__(self):
        return f"Too long name: '{self._label_name}'"

class ValidatorsNameReDefinitionError(ValidatorsNameError):
    def __str__(self):
        return f"Re-defined service name: {self._name}\nService names must be unique."
