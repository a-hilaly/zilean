#!/bin/bash

ZILEAN_PATH="$PWD"
ZILEAN_SCRIPTS="$ZILEAN_PATH/zilean/_sql"
ZILEAN_VERSION="0.0.1"
ZILEAN_WORKING_DIR="$ZILEAN_PATH/work/zilean"

#MACHINE_CONFIG = "$HOME/zilean-machine.ini"

function expmk () {
  export ZILEAN_PATH
  export ZILEAN_WORKING_DIR
  export ZILEAN_SCRIPTS
  export ZILEAN_VERSION
  mkdir ZILEAN_WORKING_DIR
}

expmk
