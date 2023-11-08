from NekoMimi import utils as nm
from NekoMimi import colourimi as cimi
from NekoMimi.legacy import consoleToys as cty

cty._defColour = "FFCA00"

#Figlet test also tests the banner and colors
cty.kprint(nm.figlet("NekoMimi","larry3d"))

#binary
print(nm.nekoBinConverter(511))

#urban test which also tests jsonAPI
print(nm.urban('NekoMimi'))

#isUP test
print(f"{nm.isUp('https://google.com')} is the status of google.com")

#debug
#add -v for debug
nm.debug("Debug message")

factory = cimi.colourFactory()
def nyaPrint(text, colour="00FF44"):
    factory.colour = colour
    factory.text = text
    factory.cinit()
    factory.cprint()

#done
nyaPrint("Unit test completed")
