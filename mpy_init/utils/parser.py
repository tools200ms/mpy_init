import os

from mpy_init.core.node_prototype import NodeSet
from mpy_init.core.unit import Unit
from mpy_init.core.unit_prototype import UnitPrototype
from mpy_init.utils.parser_error_list import UnitErrorList, LabelValueErrorList
from mpy_init.utils.parser_errors import MisformattedLineError, LabelValueError, ConfigError, MissConfigurationError
from mpy_init.utils.py_compatibility import const


class Parser:
    MAX_FILE_SIZE = const(1024 * 1024)  # 1 MB

    _origin_file_path: str = None
    _config_txt: str
    _node_set: NodeSet = None

    @staticmethod
    def register(node_set: NodeSet):
        if Parser._node_set is not None:
            raise RuntimeError("NodeSet has already been registered")
        Parser._node_set = node_set

    def __init__(self, config_txt: str, unit_name: str, origin_file_path: str = None):
        if self._node_set is None:
            raise RuntimeError("NodeSet is not registered")
        self._config_txt = config_txt

        self._unit_proto = UnitPrototype(unit_name, self._node_set)
        self._origin_file_path = origin_file_path
        

    def get_unitproto(self):
        return self._unit_proto


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

        if not file_path.startswith("/"):
            # make correction to get an absolute path
            file_path = '/'.join((os.getcwd(), file_path))

        if os.stat(file_path)[6] > cls.MAX_FILE_SIZE:
            raise ValueError(f"File size exceeds the maximum limit of {cls.MAX_FILE_SIZE} bytes.")

        with open(file_path, 'r') as f:
            return cls( f.read(),
                        base_name.rsplit('.', 1)[0],
                        file_path )

        # End of function

    
    def parse(self):
        """
        Parse configuration text in 'label = value' format.
        Only lines where label starts with a letter are processed.
    

        Returns:
            dict: Dictionary containing parsed label-value pairs
        
        Raises:
            ValueError: If a non-ignored line doesn't contain exactly one '=' character
        """
        if self._node_set is None:
            raise RuntimeError("NodeSet is not registered")
        error_list = UnitErrorList(self._origin_file_path)

        
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

                self._unit_proto.setLabel(label, value)

            except (LabelValueError, ConfigError) as parser_err:
                # Errors encountered while parsing value:
                # add line no. that has been not available in validator:
                parser_err.addLineNo(line_no)
                # Add a label name that has been not available in validator:
                if isinstance(parser_err, LabelValueError):
                    parser_err.addLabel(label)
                # add errors to the list and continue parsing so all syntax errors
                # are cached
                error_list.append(parser_err)
            except ValueError as v_err:
                error_list.append(MisformattedLineError(line_no, line))

            # if value == '':
            #     raise ValueError(ParserError.print_error(f"Invalid line: '{line}'", line_no, self._file_path))
            #
            # if len(value) > 1024:
            #     raise ValueError(
            #         ParserError.print_error(f"Value for label '{label}' exceeds maximum length of 1024 characters",
            #                                 line_no, self._file_path))

        try:
            unit, node_proto = self._unit_proto.update()
        except MissConfigurationError as err:
            error_list.append(err)

        if error_list.hasErrors():
            raise error_list

        return unit, node_proto
