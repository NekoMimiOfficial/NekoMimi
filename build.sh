#!/bin/bash
pip3 install build wheel
python3 -m build -n
pip3 uninstall -y NekoMimi
pip3 install dist/*.whl
