from subprocess import getoutput
from os.path import exists
import pickle

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
def __CMD_echo(ctx: system.context):
    ctx.name = "echo"
    ctx.result = ctx.args
    return ctx

@Factory.module
def __CMD_regTools(ctx: system.context):
    ctx.name = "reg"
    args = ctx.args

    _home = getoutput("echo $HOME")
    regFile = f"{_home}/.config/NekoPyReg/db.pkl"

    if not exists(regFile):
        getoutput("mkdir ~/.config/NekoPyReg/")
        regBuff = open(regFile, 'wb')
        reg = {}
        pickle.dump(reg, regBuff)
        regBuff.close()

    if " " in args:
        argvr = args.split(" ")
        if len(argvr) == 3:
            if argvr[0] == "r":
                regBuff = open(regFile, "rb")
                getReg = pickle.load(regBuff)
                if argvr[1] in getReg:
                    ctx.result = getReg[argvr[1]]
                    regBuff.close()
                    return ctx
                else:
                    ctx.result = "No cell found with name: "+argvr[1]
                    regBuff.close()
                    return ctx
            if argvr[0] == "w":
                regBuff = open(regFile, "rb")
                getReg = pickle.load(regBuff)
                regBuff.close()
                regBuff = open(regFile, "wb")
                getReg[argvr[1]] = argvr[2]
                pickle.dump(getReg, regBuff)
                regBuff.close()
                ctx.result = "Operation completed."
                return ctx
            if argvr[0] == "d":
                regBuff = open(regFile, "rb")
                getReg: dict = pickle.load(regBuff)
                regBuff.close()
                regBuff = open(regFile, "wb")
                if not argvr[2] == "conFirm":
                    ctx.result = "Please make sure your 3rd argument is conFirm case sensitive to confirm the deletion"
                    return ctx
                del getReg[argvr[1]]
                pickle.dump(getReg, regBuff)
                regBuff.close()
                ctx.result = "Operation completed."
                return ctx

    ctx.result = "Wrong formatting [reg {r/w/d} {cell} {data+w/confirm+r/conFirm+d}]"
    return ctx

#############
#############


modules = Factory.modules
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
