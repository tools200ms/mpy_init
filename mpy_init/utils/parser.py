import os

from mpy_init.core.label import Label
from mpy_init.core.unit import Unit
from mpy_init.core.unit_prototype import UnitPrototype
from mpy_init.utils.parser_errors import ConfigParserError, LabelSrvNameError, ParserErrorList, MisformattedLineError


class Parser:
    MAX_FILE_SIZE = 1024 * 1024  # 1 MB
    MAX_LABEL_LEN = 32
    MAX_VALUE_LEN = 2048

    _config_txt: str

    def __init__(self, config_txt: str, unit_name: str):
        self._config_txt = config_txt

        self._unit_prototype = UnitPrototype(unit_name)


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

    
    def parse(self, execept=None) -> dict:
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

        for line_no, line in enumerate(self._config_txt.splitlines(), 1):
        
            # Skip empty lines
            line = line.strip()

            # Ignore empty lines, or comment lines
            if not line or line[0] == '#':
                continue

            try:
                # Split by = and let ValueError propagate up
                # Can throw: ValueError: not enough values to unpack (expected 2, got 1)
                label, value = line.split('=', 1)
                label, value = label.rstrip(), value.lstrip()

                self._unit_prototype.setLabel(label, value)

            except (LabelSrvNameError, ConfigParserError) as parser_err:
                # Errors encountered while parsing value:
                # add line no. that has been not available in validator:
                parser_err.addLineNo(line_no)
                # Add a label name that has been not available in validator:
                if isinstance(parser_err, LabelSrvNameError):
                    parser_err.addLabel(label)
                # add errors to the list and continue parsing so all syntax errors
                # are cached
                errors.append(parser_err)
            except ValueError:
                errors.append(MisformattedLineError(line_no))

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
