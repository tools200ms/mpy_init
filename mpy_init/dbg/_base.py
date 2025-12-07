
class Implementation:

    def setrdbg(self, host: str, port: int):
        print('Function not supported')

    def setRemoteDebugger(self, url: str):
        # Split URL into host and port parts
        if ':' in url:
            host, port = url.split(':')
            port = int(port)
        else:
            host = url
            port = 5678

        self.setrdbg(host, port)
