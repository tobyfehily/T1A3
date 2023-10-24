#!/bin/bash

if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python example.py
    else
        echo "You need Python3 to run this program, but you have an older release. To update your version of Python, visit https://www.python.org/downloads/" >&2
    fi 
else
    echo "You need to install Python3 to run this program. To download Python3, visit https://www.python.org/downloads/" >&2
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
deactivate