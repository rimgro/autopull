#!/bin/bash

PWD=`pwd`
/usr/local/bin/virtualenv --python=python3 venv
echo $PWD
activate () {
    . $PWD/venv/bin/activate
}
activate
echo running
./venv/bin/python ./main.py

