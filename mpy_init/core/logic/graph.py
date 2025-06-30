
class Node:
    def __init__(self, name: str, after: list[str], requires: list[str],
                 wants: list[str], provides: str, defines: str):
        self.name = name

        self.after = after
        self.requires = requires
        self.wants = wants
        self.provides = provides
        self.defines = defines
