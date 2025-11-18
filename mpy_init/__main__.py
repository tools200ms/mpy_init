import os
import sys

#import logging
#import traceback

from mpy_init.core.logic.graph_builder import GraphBuilder, GraphBuilderUnitRedefinitionError
from mpy_init.core.node_prototype import NodeSet
from mpy_init.core.unit_errors import UnitExecError
from mpy_init.impl import Impl
from mpy_init.utils.parser import Parser
from mpy_init.core.unit import Unit, MPUnit
from mpy_init.utils.parser_error_list import ConfigErrorList, UnitErrorList

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

py_impl = Impl.get()

#if impl_name == 'micropython':
#    const = getattr(__import__('micropython'), 'const')
#else:
#    def const(x):
#        return x

#impl_name = const(impl_name)

import code
code.interact(local=locals())




if os.getenv('DBG_SERVER'):
    print("Debugging mode is enabled")
    add_remote_dbg__pydevd_pycharm("localhost", 5678)



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
    base_dir = 'targets'
    term_errors = (UnitErrorList, GraphBuilderUnitRedefinitionError)

    Parser.register(NodeSet())

    for target in ('init', 'launch', 'network', 'network_online', 'user'):
        gb.set_target(target)

        target_dir = base_dir + '/' + target
        for file_name in os.listdir(target_dir):

            if not file_name.endswith('.unit'):
                # print warning
                continue

            try:
                parser = Parser.loadFile(target_dir + '/' + file_name)
                unit, node_prototype = parser.parse()
                gb.add(unit, node_prototype)

                # logger.info(f"Loaded unit: {unit_prototype.unitname} ✅")
                print(f"{parser.get_unitproto().unitname:<15} loaded ✅")

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
                print(f"{parser.get_unitproto().unitname:<15} failed ❌")
                error_list.append(err)
                ret_code |= 2**(term_errors.index(type(err)))
            except Exception as e:
                print(f"{file_name} internal failure❗")
                #sys.print_exception(e)
                #import traceback
                #traceback.print_exc()
                return 0xFF
            finally:
                parser = None

    graph = gb.scratch()

    # Iterate through all units in dependency order
    try:
        for unit in graph:
            print(f"{unit.name:<12} {'core' if unit.isBuildIn() else 'ext.'}", end='')
            try:
                unit.start()
                print(" ✅")
            except UnitExecError as exec_err:
                print(f" ❌ {exec_err}")
            except Exception as e:
                print(f"{file_name} internal failure❗")
                sys.print_exception(e)
                #traceback.print_exc()
                return 0xFF

    except Exception as e:
        print(f"Error processing units: {e}")
        return 0xFF

    # except FileNotFoundError as e:
    #     print(f"Config file not found: {e}", file=sys.stderr)
    #     return 1
    # except Exception as e:
    #     print(f"Unexpected error: {e}", file=sys.stderr)
    #     return 1
    if error_list.hasErrors():
        print(error_list)

    os.system('/bin/bash')

    return ret_code

if __name__ == '__main__':
    sys.exit(main())
