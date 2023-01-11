#!/bin/bash
pip3 install build
python3 -m build
pip3 uninstall -y NekoMimi
pip3 install dist/*.whl
