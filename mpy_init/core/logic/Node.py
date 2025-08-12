

class Node:

    _description: str

    # Start service after "__after" but does not imply a dependency.
    __after = None  # Unit
    # Start service before "__before".
    __before = None  # Unit

    # Weak dependency, if "__wants" service is missing, starts anyway.
    __wants = None # Unit
    # Strong dependency, "__requires" is requied to start service.
    __requires = None  # Unit

    __provides = None  # Target
    __defines = None


    def __init__(self, name: str, after: list[str], requires: list[str],
                 wants: list[str], provides: str, defines: str):
        self.name = name

        self.after = after
        self.requires = requires
        self.wants = wants
        self.provides = provides
        self.defines = defines

