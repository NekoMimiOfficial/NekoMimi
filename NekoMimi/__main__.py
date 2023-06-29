from NekoMimi import tools, colourimi
import sys

factory = colourimi.colourFactory()
factory.colour = "ffaa00"

def _start():
    factory.text = tools.figlet("NekoMimi")
    factory.cinit()
    factory.cprint()
    factory.text = "Python preprocessor"
    factory.cinit()
    factory.cprint()

    file = sys.argv[1]

if __name__ == "__main__":
    _start()
