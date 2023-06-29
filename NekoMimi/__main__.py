class system:
    def __init__(self) -> None:
        self.modules:dict = {}

    class context:
        def __init__(self) -> None:
            self.args:str = ""
            self.name:str = ""
            self.result:str = ""

    def module(self, func) -> None:
        ctx = self.context()
        ctx = func(ctx)
        name = ctx.name
        self.modules[name] = func
        return

#############
#  Modules  #
#############

Factory = system()

@Factory.module
def _pholder(ctx):
    ctx.name = "echo"
    ctx.result = ctx.args
    return ctx

#############
#############


modules = Factory.modules
print(modules)
def _start() -> None:

    com:str = input(">")
    while True:
        name:str = ""
        args:str = ""

        if " " in com:
            name = com.split(" ", 1)[0]
            args = com.split(" ", 1)[1]
        else:
            name = com
            args = ""

        if name in modules:
            ctx = Factory.context()
            ctx.args = args
            ctx = modules[name](ctx)
            print(ctx.result)
        elif com == "exit" or com == "quit":
            exit(0)

        com = input(">")


#run
_start()
