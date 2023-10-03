#!/bin/bash

# configuration
VENV_NAME=ansible2.9
ANSIBLE_VER=2.9
PYTHON_BIN=/usr/bin/python3

# default and derived 
VENV_HOME=~/dev/apps/python-venv
PYTHON_VER=$($PYTHON_BIN -V | awk '{print $2}')

echo "Using Python version $PYTHON_VER ($PYTHON_BIN)"

echo "Create and activate venv '$VENV_NAME' for python $PYTHON_VER and ansible $ANSIBLE_VER"
mkdir -p $VENV_HOME
pushd $VENV_HOME

$PYTHON_BIN -m venv $VENV_NAME
source $VENV_NAME/bin/activate

echo "New python3 default = $(python3 -V)"
python3 -V

echo "upgrade pip"
python3 -m pip install --upgrade pip

echo "Install ansible $ANSIBLE_VER"
python3 -m pip install ansible==$ANSIBLE_VER
python3 -m pip install ansible-core
python3 -m pip install pytest
python3 -m pip install pytest-xdist
python3 -m pip install unittest2
python3 -m pip install ordereddict
python3 -m pip install pytest-forked
python3 -m pip install pytest-coverage
python3 -m pip install pytest-html-reporter
python3 -m pip install selenium
python3 -m pip install python-dotenv

/usr/local/opt/python@3.7/bin/python3.7 -m pip install ansible==2.9 ansible-core pytest pytest-xdist unittest2 ordereddict pytest-forked python-dotenv    
/usr/local/opt/python@3.7/bin/python3.7 -m pip install pytest-xdist
/usr/local/opt/python@3.7/bin/python3.7 -m pip install pytest-forked 

/usr/local/opt/python@3.8/bin/python3.8 -m pip install --upgrade pip
/usr/local/opt/python@3.8/bin/python3.8 -m pip install ansible-core pytest pytest-xdist unittest2 pytest-forked

/usr/local/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip
/usr/local/opt/python@3.9/bin/python3.9 -m pip install ansible-core pytest pytest-xdist unittest2 pytest-forked

/usr/local/opt/python@3.10/bin/python3.10 -m pip install --upgrade pip
/usr/local/opt/python@3.10/bin/python3.10 -m pip install ansible-core pytest pytest-xdist unittest2 pytest-forked

/usr/local/opt/python@3.10/bin/python3.11 -m pip install --upgrade pip
/usr/local/opt/python@3.10/bin/python3.11 -m pip install ansible-core pytest pytest-xdist unittest2 pytest-forked


which ansible 

popd

echo 
echo "activate venv with: "
echo 
echo "   source $VENV_HOME/$VENV_NAME/bin/activate"
echo 




