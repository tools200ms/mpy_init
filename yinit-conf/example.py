
class data_text:
    def __init__(self, fnc):
        self._fnc = fnc

    def __call__(self):
        print("DECOrator")
        return self._fnc()



@data_text
def key():
    return "TESTING_KEYXXX"

class Config:

    host: str
    port: int
    username: str
    password: str

c = Config()

ret = key()
print(ret)

