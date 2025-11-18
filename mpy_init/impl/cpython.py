from mpy_init.impl._base import Implementation


class CPython(Implementation):
    def __init__(self):
        global const
        const = lambda x: x

    def setrdbg(self, host: str, port: int):
        import pydevd_pycharm

        try:
            pydevd_pycharm.settrace(
                host=host, port=port,
                stdout_to_server=True,
                stderr_to_server=True)
        except ConnectionRefusedError:
            print("Failed to connect to debug server: Connection refused")
        except OSError as e:
            print(f"Failed to connect to debug server: {str(e)}")

