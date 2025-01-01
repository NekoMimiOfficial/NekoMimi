from NekoMimi import colourimi

"""
Simple tools and wrappers for CLI tools
mostly neko-fied :3
"""

Factory = colourimi.colourFactory()

def kprint(text: str, colour: str= "fcfcff", newline: bool= True)-> None:
    Factory.text= text
    Factory.colour= colour
    Factory.newline= newline
    Factory.cinit()
    Factory.cprint()
    return
