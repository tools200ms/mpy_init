
class Unit:
    description: str
    before: str
    after: str
    requires: str
    wants: str
    defines: str
    provides: str
    exec_start: str
    exec_stop: str
    pid_file: str
    mpy_package: str

    @staticmethod
    def factory(description: str = "", before: str = "", after: str = "",
                requires: str = "", wants: str = '', defines: str = "", provides: str = "",
                exec_start: str = "", exec_stop: str = "",
                pid_file: str = "", mpy_package: str = "") -> 'PreDefinedUnit':

        unit = PreDefinedUnit()

        unit.description = description
        unit.before = before
        unit.after = after
        unit.requires = requires
        unit.wants = wants
        unit.defines = defines
        unit.provides = provides
        unit.exec_start = exec_start
        unit.exec_stop = exec_stop
        unit.pid_file = pid_file
        unit.mpy_package = mpy_package
        

        return unit


class PreDefinedUnit(Unit):
    pass

