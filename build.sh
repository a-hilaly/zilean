#!/bin/bash

ZILEAN_PATH="$PWD"
ZILEAN_SCRIPTS="$ZILEAN_PATH/scripts"
ZILEAN_SQL_SCRIPTS="$ZILEAN_SCRIPTS/SQL"
ZILEAN_API="$ZILEAN_PATH/api"
ZILEAN_ANALYSIS="$ZILEAN_PATH/api"
ZILEAN_OFFICE="$ZILEAN_PATH/office"
ZILEAN_VERSION="0.0.1"
ZILEAN_BUILD_ENV="$ZILEAN_PATH/build_env.py"
export ZILEAN_PATH
export ZILEAN_SCRIPTS
export ZILEAN_API
export ZILEAN_ANALYSIS
export ZILEAN_VERSION
export ZILEAN_OFFICE

function make_skmvs_env () {
    python3 $ZILEAN_BUILD_ENV
}

function make_office () {
    mkdir ZILEAN_OFFICE
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

command=$1
option=$2

if [ "$command" = "--build" ]; then

elif [ "$command" = "--test" ]; then

elif [ "$command" = "--run-server" ]; then

elif [ "$command" = "--analyse" ]; then

fi
