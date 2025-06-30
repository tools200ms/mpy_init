import os
import logging
import re
import mpy_init.core.units
from mpy_init.utils.parser import Parser
from mpy_init.core.unit import Unit

logger = logging.getLogger(__name__)


class Loader:
    """
    Loader class that handles loading all available units from unit files.
    """

    @staticmethod
    def split_deps(input_str: str) -> list:
        """
        Split string by space or comma separators.

        Args:
            input_str (str): Input string to split

        Returns:
            list: List of substrings
        """
        if not input_str:
            return []
        return [x.strip() for x in re.split(r'[,\s]+', input_str) if x.strip()]

    def loadUnits(self, path: str):
        """
        Load and process unit files from specified directory path.

        Args:
            path (str): Directory path containing .unit files

        Returns:
            list: List of instantiated unit objects
        """
        units = []
        worker = None

        for base_dir, _, file_list in os.walk(path):
            for file_name in file_list:
                if not file_name.endswith('.unit'):
                    continue

                file_path = os.path.join(base_dir, file_name)
                logger.info(f"Processing unit file: {file_path}")

                try:
                    unit_conf = Parser.load(file_path).parse()

                    if 'mpy_package' in unit_conf:
                        worker = unit_conf['mpy_package']
                        del unit_conf['mpy_package']

                        try:
                            cls = getattr(mpy_init.core.units, worker)
                            unit = cls()
                            
                        except AttributeError:
                            logger.error(f"Package '{worker}' not found in predefined units")
                    else:

                        if 'exec_start' not in unit_conf:
                            raise ValueError("exec_start is requied parameter")

                        worker = unit_conf['exec_start']
                        del unit_conf['exec_start']

                        unit = Unit(**unit_conf)

                    units.append(unit)

                except Exception as e:
                    logger.error(f"Error processing {file_path}: {str(e)}")

        return units

    