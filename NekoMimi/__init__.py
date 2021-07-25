# __init__.py
from pyfiglet import Figlet
import random


def nekoBanner():
    text = "NekoMimi"
    fonts = ['small' , 'slant' , 'mini' , 'banner' , 'big']
    mode = random.choice(fonts)
    f = Figlet(font=mode)
    render = f.renderText(text)
    return render

def test():
    return "Successful !"