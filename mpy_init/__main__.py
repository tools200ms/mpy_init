import os
import sys
import logging
import traceback

from mpy_init.core.logic.graph_builder import GraphBuilder, GraphBuilderUnitRedefinitionError
from mpy_init.core.node_prototype import NodeSet
from mpy_init.utils.parser import Parser
from mpy_init.core.unit import Unit, MPUnit
from mpy_init.utils.parser_error_list import ConfigErrorList, UnitErrorList

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

    error_list = ConfigErrorList()
    gb = GraphBuilder()
    ret_code = 0x0
    directory = 'targets'
    term_errors = (UnitErrorList, GraphBuilderUnitRedefinitionError)
    node_set = NodeSet()

    # dirname, dir. list, file list
    for base_dir, _, file_list in os.walk(directory):
        for file_name in file_list:

            if not file_name.endswith('.unit'):
                # print warning
                continue

            try:
                file_path = os.path.join(base_dir, file_name)

                parser = Parser.loadFile(file_path)
                unit_prototype = parser.parse(node_set)

                gb.add(unit_prototype)

                # logger.info(f"Loaded unit: {unit_prototype.unitname} ✅")
                print(f"{parser.unitname:<15} loaded ✅")

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
            except term_errors as err:
                print(f"{parser.unitname:<15} failed ❌")
                error_list.append(err)
                ret_code |= 2**(term_errors.index(type(err)))
            except Exception as e:
                print(f"{parser.unitname} internal failure❗")
                traceback.print_exc()
                return 0xFF
            finally:
                parser = None


# except FileNotFoundError as e:
    #     print(f"Config file not found: {e}", file=sys.stderr)
    #     return 1
    # except Exception as e:
    #     print(f"Unexpected error: {e}", file=sys.stderr)
    #     return 1
    if error_list.hasErrors():
        print(error_list)

    return ret_code

if __name__ == '__main__':
    sys.exit(main())
