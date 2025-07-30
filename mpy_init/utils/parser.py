import os

from mpy_init.core.label import Label
from mpy_init.core.unit import Unit
from mpy_init.utils.parser_errors import ConfigParserError, ParserErrorList


class Parser:
    MAX_FILE_SIZE = 1024 * 1024  # 1 MB

    _config_txt: str
    _unit_name: str

    def __init__(self, config_txt: str, unit_name: str):
        self._config_txt = config_txt

        if not Unit.validateName(unit_name):
            raise ValueError(f"Invalid unit name: {unit_name}\nUnit name must be alpha-numeric.")

        self._unit_name = unit_name


    @classmethod
    def loadConfigTxt(cls, config_txt: str, unit_name: str) -> 'Parser':
        return cls(config_txt, unit_name)

    @classmethod
    def loadFile(cls, file_path: str) -> 'Parser':
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

        # Extract and validate base name
        base_name = file_path.rsplit('/', 1)[-1]

        # Validate file extension
        if not base_name.endswith('.unit'):
            raise ValueError(f"Invalid file extension - must be '.unit': {file_path}")

        if os.path.getsize(file_path) > cls.MAX_FILE_SIZE:
            raise ValueError(f"File size exceeds the maximum limit of {cls.MAX_FILE_SIZE} bytes.")

        with open(file_path, 'r') as f:
            return cls(f.read(), base_name.rsplit('.', 1)[0], file_path)

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
        errors = []
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

            try:
                Label.check_label(label)
            except ConfigParserError as cp_err:
                cp_err.addLineNo(line_no)
                errors.append(cp_err)

            # if value == '':
            #     raise ValueError(ParserError.print_error(f"Invalid line: '{line}'", line_no, self._file_path))
            #
            # if len(value) > 1024:
            #     raise ValueError(
            #         ParserError.print_error(f"Value for label '{label}' exceeds maximum length of 1024 characters",
            #                                 line_no, self._file_path))

            if len(errors) > 0:
                raise ParserErrorList(errors)

            result[label] = value

        return result
        #UnitPrototype(result)
