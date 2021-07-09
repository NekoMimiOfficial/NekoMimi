from pyfiglet import Figlet

def figlet(text, mode="small"):
    f = Figlet(font=mode)
    render = f.renderText(text)
    return render