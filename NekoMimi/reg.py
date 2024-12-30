import pickle
from subprocess import getoutput
from os.path import exists

"""
registry reading tools for the reg module in __main__
good for saving single line strings and tokens (unencrypted)
"""

def readCell(cell: str)->str:
    """
    retrieve data from cells in the neko py registry
    @arg cell: the cell of which data will be returned
    >>> NekoMimi.reg.readCell("cellname")
    REG UNINIT ERR "or" CELL NOT FOUND ERR "or" DATA
    """
    _home = getoutput("echo $HOME")
    if not exists(f"{_home}/.config/NekoPyReg/db.pkl"):
        return "Registry uninitialized, please use the neko shell to initialize it"
    buffer = open(f"{_home}/.config/NekoPyReg/db.pkl", "rb")
    db = pickle.load(buffer)
    if not cell in db:
        return f"cell: {cell} is not in database"
    return db[cell]
