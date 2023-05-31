import os, subprocess
from NekoMimi import tools, colourimi

file = "$HOME/.config/variables.ngv"
fullFile = subprocess.getoutput(f"bash -c echo {file}")

contents = nm.read(fullFile)

entries = contents.split("\n")

for line in entries:
    if line.startswith("["):
        vn, vv = line.split("]", 1)
        vnc = vn.split("[", 1)[1]
        pass
