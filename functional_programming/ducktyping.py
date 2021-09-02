#duck typing.....

class Vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("executing using vscode")
    def debug(self):
        print("debuging using vscode")
class Pycharm:
    def compile(self):
        print("compiling using pycharm")
    def execute(self):
        print("executing using pycharm")
    def debug(self):
        print("debuging using pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()

dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)