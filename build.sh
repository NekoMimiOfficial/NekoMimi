#!/bin/bash

rm -rf ./dist/

pip3 uninstall -y NekoMimi --break-system-packages
bob
pip3 install dist/*.whl --break-system-packages

rm -rf ./build/
rm -rf ./NekoMimi.egg-info/
