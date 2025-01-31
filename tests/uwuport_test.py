from NekoMimi import utils as nm
from NekoMimi import consoleToys

#import os using uwuport
os= nm.load_mod("os");
if os == False:
    consoleToys.kprint("Error loading module", "#ff2288");
    exit(1);

consoleToys.kprint("Module loaded successfully.", "#66ff22");
consoleToys.kprint("Listing current directory using the loaded os module:", "#8888bb");
consoleToys.kprint(os.listdir("./"), "#ddddff");
