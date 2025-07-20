class ParserError:
    def __init__(self, label: str):
        self._label = label

    def format_err_msg(message: str, line_no: int, file_path: str) -> str:
        pass


class ParserEmptyError (ParserError):
    def format_err_msg(self, line_no: int, file_path: str) -> str:
        return "Label cannot be empty"

class ParserTooLongError (ParserError):
    def format_err_msg(self, line_no: int, file_path: str) -> str:
        return f"Label '{self._label[0:36]} ...' exceeds maximum length of 32 characters"

class ParserStartWithLetterError (ParserError):
    def format_err_msg(self, line_no: int, file_path: str) -> str:
        pass

class ParserHasIllegalName (ParserError):
    def format_err_msg(self, line_no: int, file_path: str) -> str:
        f"Label '{self._label}' contains illegal characters - only alphanumeric characters and underscores are allowed"


class Parser:
    _config: str
    _file_path: str
    _unit_name: str

    def __init__(self, config: str, file_path: str = None):
        self._config = config
        self._file_path = file_path

        #ExecUnit
        self._serch_key = self._node_keys

        # Extract and validate base name
        base_name = file_path.rsplit('/', 1)[-1]

        # Validate file extension
        if not base_name.endswith('.unit'):
            raise ValueError(f"Invalid file extension - must be '.unit': {file_path}")

        self._unit_name = base_name.rsplit('.', 1)[0]
        if not self._unit_name[0].isalpha():
            raise ValueError(f"File name must start with a letter: {base_name}")

        if not self._unit_name.isalnum():
            raise ValueError(f"File name must be alphanumeric: {base_name}")

    """
    Verify that the label is an alphanumeric string with an allowed '_' character starting with a letter
    """
    @staticmethod
    def check_label(label: str):
        if not label:
            raise ParserEmptyError(label)

        if len(label) > 32:
            raise ParserTooLongError(label)

        if not label[0].isalpha():
            raise ParserStartWithLetterError(label)
        
        if not all(c.isalnum() or c == '_' for c in label):
            raise ParserHasIllegalName(label)

    def find(self, name: str):

        if name in self._serch_key:


    @classmethod
    def load(cls, file_path: str) -> 'Parser':
        """
        Create a Parser instance by reading configuration from a file.

        Args:
            file_path (str): Path to the configuration file

        Returns:
            Parser: New Parser instance with loaded configuration

        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the configuration format is invalid or file name format is incorrect
        """

        with open(file_path, 'r') as f:
            return cls(f.read(), file_path)

        # End of function

    
    def parse(self) -> dict:
        """
        Parse configuration text in 'label = value' format.
        Only lines where label starts with a letter are processed.
    

        Returns:
            dict: Dictionary containing parsed label-value pairs
        
        Raises:
            ValueError: If a non-ignored line doesn't contain exactly one '=' character
        """
        
        result: dict = {}

        for line_no, line in enumerate(self._config.splitlines(), 1):
        
            # Skip empty lines
            line = line.strip()

            # Ignore empty lines, or comment lines
            if not line or line[0] == '#':
                continue

            # Split by = and let ValueError propagate up
            label, value = line.split('=', 1)
            # 'label' is striped with 'line.strip()'
            value = value.strip()

            Parser.check_label(label)
            
            if value == '':
                raise ValueError(ParserError.print_error(f"Invalid line: '{line}'", line_no, self._file_path))

            if len(value) > 1024:
                raise ValueError(
                    ParserError.print_error(f"Value for label '{label}' exceeds maximum length of 1024 characters",
                                            line_no, self._file_path))

            result[label] = value


        return UnitPrototype(result)
