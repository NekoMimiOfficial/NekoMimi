#!/bin/bash
python3 -m build
pip3 uninstall -y NekoMimi
pip3 install dist/*.whl
