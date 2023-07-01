import sys
from NekoMimi import utils as nm

__version__ = sys.argv[1]

print(f"building templates for v{__version__}")

setup_tmp = nm.read("./templates/setup.py")
init_tmp = nm.read("./templates/__init__.py")

setup = setup_tmp.replace("<PLACEHOLDER>", __version__)
init = init_tmp.replace("<PLACEHOLDER>", __version__)

nm.write(init, "./NekoMimi/__init__.py")
nm.write(setup, "./setup.py")

print("done! proceeding...")
