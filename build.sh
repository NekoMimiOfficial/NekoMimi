#!/bin/bash

version='1.1.0'

rm dist/*
# pip3 uninstall -y NekoMimi

python3 buildTemplates.py $version
#pip3 install build wheel
python3 -m build -n
pip3 uninstall -y NekoMimi
pip3 install dist/*.whl

rm ./setup.py
rm ./NekoMimi/__init__.py
