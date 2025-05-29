
class service:
    __description: str

    # start service after "__after" but does not imply a dependency.
    __after: []
    # start service before "__before"
    __before: []

    # week dependency, if "__wants" service is missing, start any way
    __wants: []
    # strong dependency, "__requires" is requied to start service.
    __requires: []

    __provides: str
    __exec_start: str
    __exec_stop: str
    __exec_restart: str
    __exec_reload: str
