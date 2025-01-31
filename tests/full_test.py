from NekoMimi import utils as nm
from NekoMimi import consoleToys as ct

#the windows logo
info_c= "#ffca00";
false_c= "#ff0066";
true_c= "#88ff22";
fact_c= "#2288ff";

#Figlet test also tests the banner and colors
ct.kprint(nm.figlet("NekoMimi","larry3d"), "#ffca00")

#isUP test
state= nm.isUp("http://nekomimi.tilde.team");
ct.kprint("http://nekomimi.tilde.team", fact_c, False);
ct.kprint(" is currently ", "#fcfcff", False);
ct.kprint("[  UP  ]", true_c) if state else ct.kprint("[ DOWN ]", false_c);

#done
ct.kprint("Unit test completed");
