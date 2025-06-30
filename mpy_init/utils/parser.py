
class Parser:
    _config: str
    _file_path: str
    _node_keys: dict = {'after': None,
                        'before': None,
                        'wants': None,
                        'requires': None,
                        'defines': None}
    _ex_keys: dict = {'exec_start': None,
                      'exec_stop': None,
                      'exec_reload': None,
                      'pid_file': None}
    _mp_keys: dict = {'mpy_package': None}
    _set_keys: dict = {'description': None}

    def __init__(self, config: str, file_path: str = None):
        self._config = config
        self._file_path = file_path

        ExecUnit
        self._serch_key = self._node_keys

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
            ValueError: If the configuration format is invalid
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

            # Skip lines not starting with a letter
            if not line[0].isalpha():
                continue
            
            # Split by = and let ValueError propagate up
            label, value = line.split('=', 1)
            label, value = label.strip(), value.strip()
            
            if label == '' or value == '':
                raise ValueError(f"Invalid line {line_no} in {self._file_path}: '{line}'")

            if len(label) > 32:
                raise ValueError(
                    f"Label '{label}' on line {line_no} in {self._file_path} exceeds maximum length of 32 characters")

            if len(value) > 1024:
                raise ValueError(
                    f"Value for label '{label}' on line {line_no} in {self._file_path} exceeds maximum length of 1024 characters")

            # Verify the label is alphanumeric
            if not all(c.isalnum() or c == '_' for c in label):
                raise ValueError(
                f"Label '{label}' on line {line_no} in {self._file_path} contains illegal characters - only alphanumeric characters and underscores are allowed")

            result[label] = value

        return result
