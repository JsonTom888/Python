class DiyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise DiyError("my diy exception") #触发异常
except DiyError as e:
    print(e)