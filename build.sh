#!/bin/bash

ZILEAN_PATH="$PWD"
ZILEAN_SCRIPTS="$ZILEAN_PATH/zilean/_sql"
ZILEAN_VERSION="0.0.1"
ZILEAN_CACHE="$ZILEAN_PATH/cache"
export ZILEAN_PATH
export ZILEAN_CACHE
export ZILEAN_SCRIPTS
export ZILEAN_VERSION
#MACHINE_CONFIG = "$HOME/zilean-machine.ini"

function expmk () {
    mkdir ZILEAN_CACHE
}

function build_env () {
    f="$ZILEAN_PATH/build_env.py"
    python3 $f
}

function build_py_lib () {
    s="$ZILEAN_PATH/setup.py"
    sudo python3 $s install
}

function test_py_lib () {
    s="$ZILEAN_PATH/setup.py"
    python3 $s test
}

expmk
