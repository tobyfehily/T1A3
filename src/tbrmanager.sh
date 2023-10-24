#!/bin/bash

if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 -m venv .venv
        source .venv/bin/activate
        python3 -m pip install -r requirements.txt
        python3 main.py
        deactivate
    else
        echo 'You need to upgrade Python to Python 3 to run this program. To upgrade to Python 3, visit https://www.python.org/downloads/' >&2
        exit 1
        fi
else
    echo 'You need to install Python 3 to run this program. To download Python 3, visit https://www.python.org/downloads/' >&2
    exit 1
fi