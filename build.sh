#!/bin/bash

rm dist/*

bob
pip3 uninstall -y NekoMimi --break-system-packages
pip3 install dist/*.whl --break-system-packages
