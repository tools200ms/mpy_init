import os
import sys
import logging

from mpy_init.utils.parser import Parser
from mpy_init.core.unit import Unit, MPUnit
from mpy_init.utils.parser_errors import ParserErrorList

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> int:
    """
    Main entry point for the mpy_init module.

    Args:
        argv: List of command line arguments. If None, sys.argv[1:] will be used.

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    argv = sys.argv

    # if len(argv) < 2:
    #     print("Usage: mpy_init <directory>", file=sys.stderr)
    #     return 1

    ret_code = 0x0
    directory = '/home/barney/devel.200ms/mpy_init/targets'
    print(os.curdir)

    # dirname, dir. list, file list
    for base_dir, _, file_list in os.walk(directory):
        for file_name in file_list:
            if not file_name.endswith('.unit'):
                # print warning
                continue

            try:
                file_path = os.path.join(base_dir, file_name)
                logger.info(f"Processing unit file: {file_path}")
                Parser.loadFile(file_path).parse()

                # if 'mpy_package' in unit_conf:
                #     buildin_unit_name = unit_conf['mpy_package']
                #
                #     try:
                #         import mpy_init.core.units
                #
                #         cls = getattr(mpy_init.core.units, buildin_unit_name)
                #         unit = cls()
                #     except AttributeError:
                #         print(f"Package '{buildin_unit_name}' not found in predefined units", file=sys.stderr)
                #         return 1
                # else:
                #     try:
                #         unit = Unit.factory(**unit_conf)
                #     except TypeError as e:
                #         if "unexpected keyword argument" in str(e):
                #             print(f"Invalid configuration key in {file_path}: {str(e)}", file=sys.stderr)
                #             return 1
                #         raise
            except ParserErrorList as e:
                print(f"Error parsing configuration: {e}", file=sys.stderr)
                ret_code |= 0x1

    # except FileNotFoundError as e:
    #     print(f"Config file not found: {e}", file=sys.stderr)
    #     return 1
    # except Exception as e:
    #     print(f"Unexpected error: {e}", file=sys.stderr)
    #     return 1
    return ret_code

if __name__ == '__main__':
    sys.exit(main())
