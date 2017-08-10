#!/bin/sh

ZILEAN_PATH="$HOME/zilean"
ZILEAN_SQL="$ZILEAN_PATH/zilean/zilean/_sql"
ZILEAN_WORKING_DIR="$HOME/work/zilean"
#XXX: the next line should be already exported at the machine
# creation
#MACHINE_CONFIG = "$HOME/zilean-machine.ini"


function expmk () {
  export ZILEAN_PATH
  export ZILEAN_WORKING_DIR
  export ZILEAN_SQL
  mkdir ZILEAN_WORKING_DIR
  #mv $ZILEAN_PATH/zilean/zilean/zilean-machine.ini $ZILEAN_CONFIG
}

expmk
