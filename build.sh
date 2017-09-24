#!/bin/bash

ZILEAN_PATH="$PWD"
ZILEAN_SCRIPTS="$ZILEAN_PATH/scripts"
ZILEAN_SQL_SCRIPTS="$ZILEAN_SCRIPTS/SQL"
ZILEAN_API="$ZILEAN_PATH/api"
ZILEAN_ANALYSIS="$ZILEAN_PATH/api"
ZILEAN_OFFICE="$ZILEAN_PATH/office"
ZILEAN_VERSION="0.0.1"
ZILEAN_BUILD_ENV="$ZILEAN_PATH/build_env.py"
ZILEAN_CONFIG="$ZILEAN_PATH/pkg/config"
export ZILEAN_PATH
export ZILEAN_SCRIPTS
export ZILEAN_API
export ZILEAN_VERSION
export ZILEAN_ANALYSIS
export ZILEAN_VERSION
export ZILEAN_OFFICE
export ZILEAN_CONFIG

function make_requirements () {
    python3 $ZILEAN_BUILD_ENV --make $ZILEAN_PATH
}

function make_skmvs_env () {
    python3 $ZILEAN_BUILD_ENV
}

function make_office () {
    mkdir $ZILEAN_OFFICE
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
    build_py_lib
elif [ "$command" = "--build-env" ]; then
    build_env
elif [ "$command" = "--make-req" ]; then
    echo "not implemented"
elif [ "$command" = "--test" ]; then
    #test_py_lib
    echo "not implemented"
elif [ "$command" = "--run-server" ]; then
    echo "not implemented"
elif [ "$command" = "--analyse" ]; then
    echo "not implemented"
fi
