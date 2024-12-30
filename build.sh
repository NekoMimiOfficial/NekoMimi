#!/bin/bash

version='1.1.1'

rm dist/*
# pip3 uninstall -y NekoMimi

python3 buildTemplates.py $version
#pip3 install build wheel
python3 setup.py bdist_wheel
pip3 uninstall -y NekoMimi --break-system-packages
pip3 install dist/*.whl --break-system-packages

rm ./setup.py
rm ./NekoMimi/__init__.py
