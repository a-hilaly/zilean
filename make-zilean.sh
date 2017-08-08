#!/bin/sh

ZILEAN_PATH = "$HOME/zilean"
ZILEAN_WORKING_DIR = "$HOME/zileanwork"
ZILEAN_MACHINE_CONFIG = "$HOME/zilean-machine.ini"


function expmk () {
  export ZILEAN_PATH
  export ZILEAN_WORKING_DIR
  export ZILEAN_CONFIG
  mkdir ZILEAN_WORKING_DIR
  mv $ZILEAN_PATH/zilean/zilean/zilean-machine.ini $ZILEAN_CONFIG
}

expmk
